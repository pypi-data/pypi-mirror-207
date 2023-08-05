import kfp.components as comp
import logging
import re
import csv
import requests
import pandas as pd
from minio import Minio
from minio.select import (CSVInputSerialization, CSVOutputSerialization,
                          SelectRequest)
from minio.error import S3Error
from datahub.metadata.schema_classes import (
    SchemaFieldClass,
    AuditStampClass,
    SchemaFieldDataTypeClass,
    BooleanTypeClass,
    FixedTypeClass,
    StringTypeClass,
    BytesTypeClass,
    NumberTypeClass,
    DateTypeClass,
    TimeTypeClass,
    EnumTypeClass,
    NullTypeClass,
    MapTypeClass,
    ArrayTypeClass,
    UnionTypeClass,
    RecordTypeClass
)

# Configure logger
log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s" 
logging.basicConfig(format = log_format, level = logging.INFO)
logger = logging.getLogger()

def get_minio_auth_session(endpoint: str):
    # Strip http/s:// from endpoint
    endpoint = endpoint.replace("http://","")
    endpoint = endpoint.replace("https://","")
    # Create minio client
    return Minio(
        endpoint,
        access_key="minio",
        secret_key="minio123",
        secure=False
    )

def download_from_public_api(url: str, 
                             name: str) -> None:
  r = requests.get(url, allow_redirects=True)
  open(name, 'wb+').write(r.content)

def check_source_exists(s3_uri: str,
                        endpoint: str) -> bool:
    client = get_minio_auth_session(endpoint)
    s3_uri_split = re.split('/', s3_uri)
    print("Splitting S3_uri into tuple => %s" % s3_uri_split)
    print("bucket name -> %s" % s3_uri_split[0])
    print("object name -> %s" % '/'.join(s3_uri_split[1:]))
    try:
        with client.select_object_content(
                bucket_name=s3_uri_split[0], 
                object_name='/'.join(s3_uri_split[1:]), # rejoin remaining into the object.
                request=SelectRequest(
                "select * from S3Object limit 5",
                    CSVInputSerialization(),
                    CSVOutputSerialization(),
                    request_progress=True,
                ),
        ) as result:
            for data in result.stream():
                print(data.decode())
        logger.info("%s exists" % s3_uri)
        return True
    except S3Error:
        logger.info("%s doesn't exist" % s3_uri)
        return False
    
    
def get_source_schema(s3_uri: str,
                      endpoint: str,
                      row_offset: int=0) -> list[SchemaFieldClass]:
    # Get some data to infer the schema from
    client = get_minio_auth_session(endpoint)
    s3_uri_split = re.split('/', s3_uri)
    schema_to_return = []
    try:
        with client.select_object_content(
                bucket_name=s3_uri_split[0], 
                object_name='/'.join(s3_uri_split[1:]), # rejoin remaining into the object.
                request=SelectRequest(
                "select * from S3Object limit 500",
                    CSVInputSerialization(),
                    CSVOutputSerialization(),
                    request_progress=True,
                ),
        ) as result:
            # Output results into some we can read into the infer
            pathfile = "results.csv"
            f = open(pathfile, "w")
            f.truncate(0)
            for r in result.stream():
                f.writelines(r.decode())
            f.close()
            df = pd.read_csv('results.csv').infer_objects()
            logger.info(df.dtypes)
            for col in df: 
                df_col_type = get_datahub_col_type_from_df_col_type(dtype=df[col].dtype)
                schema_to_return.append(
                    SchemaFieldClass(
                        fieldPath=col,
                        type=SchemaFieldDataTypeClass(type=df_col_type), 
                        nativeDataType=str(df[col].dtype),  
                        description="%s" % df.loc[:5, col], # <-- PUT SOME EXAMPLE VALUES HERE? 
                        lastModified=AuditStampClass(
                            time=1640692800000, actor="urn:li:corpuser:ingestion"
                        )
                    )
                )
        logger.info("%s exists" % s3_uri)
    except S3Error:
        logger.info("%s doesn't exist" % s3_uri)
    return schema_to_return

def get_datahub_col_type_from_df_col_type(dtype: str) -> SchemaFieldDataTypeClass:
    print("******* mapping col_type -> %s" % dtype)
    match dtype: 
        case 'boolean':
            return BooleanTypeClass()
        case 'string':
            return StringTypeClass()
        case 'int' | 'float32' | 'float64' | 'int8' | 'int16' | 'int32' | 'int64' | 'uint8' | 'uint16' | 'uint32' | 'uint64':
            return NumberTypeClass()
        case 'datetime64[ns, <tz>]' | 'datetime':
            return DateTypeClass()
        #case pattern-1:
        #    return FixedTypeClass()
        #case pattern-1:
        #    return BytesTypeClass()
        #case pattern-1:
        #    return TimeTypeClass()
        #case pattern-1:
        #    return EnumTypeClass()
        #case pattern-1:
        #    return NullTypeClass()
        #case pattern-1:
        #    return MapTypeClass()
        #case pattern-1:
        #    return ArrayTypeClass()
        #case pattern-1:
        #    return UnionTypeClass()
        #case pattern-1:
        #    return RecordTypeClass()
        case _:
            return UnionTypeClass()

def add_to_minio(
        dataset_name: str,
        source_spec: dict,
        object_key: str,
        endpoint: str) -> str:
    
    # Get the Minio client session
    client = get_minio_auth_session(endpoint)

    # Download file from URL
    match source_spec['type']:
        case "public_api":
            logger.info("Downloading %s from %s" % (dataset_name, source_spec['url']))
            download_from_public_api(url=source_spec['url'], 
                                     name=dataset_name)
        case _:
            logger.info("Type not supported, skipping '%s'" % dataset_name)
    
    # Unpack object_key into the bucket and remaining object_key
    object_key_split = re.split('/', object_key)
    bucket_name=object_key_split[0]
    object_name="%s/%s" % ('/'.join(object_key_split[1:]), dataset_name)

    # Make a bucket for sources, if does not exist...
    found = client.bucket_exists(bucket_name)
    if not found:
        logger.info("Bucket %s does not exist, creating." % bucket_name)
        client.make_bucket(bucket_name)
    else:
        logger.info("Bucket %s already exists" % bucket_name)

    # Put each of the datasets into sources, keyed to this pipeline
    s3_uri = "%s/%s" % (bucket_name, object_name)
    client.fput_object(bucket_name, object_name, dataset_name)
    logger.info("Created new Minio source %s -> %s" % (object_name, s3_uri))
    return s3_uri