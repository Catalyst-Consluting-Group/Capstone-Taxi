import os
import json
import polars as pl
import boto3
from dotenv import load_dotenv
load_dotenv()

s3 = boto3.client('s3')

def handler(event, context):
    bucket = event.get("bucket")
    key    = event.get("key")

    if not bucket or not key:
        return {"statusCode" : 400, "body" : "NO BUCKET OR NO KEY"}


    obj    = s3.get_object(Bucket=bucket, Key=key)
    df     = pl.read_parquet(obj["Body"].read())

    summary = (
        df.head(1000).select(df.columns).to_dicts()[:10]
    )

    print(summary)
    print(type(summary))

    return {"statusCode" : 400, "body" : json.dumps({"rows" : summary, "columns" : df.columns})}