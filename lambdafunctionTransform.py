import os
from dotenv import load_dotenv
import polars as pl

load_dotenv()

s3_path = "s3://capstone-techcatalyst-raw/yellow_taxi/yellow_tripdata_2023-09.parquet"
df = pl.read_parquet(s3_path)
print(df)