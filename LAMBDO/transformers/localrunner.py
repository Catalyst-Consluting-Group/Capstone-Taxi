# Run your Lambda handler locally with a fake event

from app import handler

if __name__ == "__main__":
    event = {"bucket": "capstone-techcatalyst-raw", 
             "key": "yellow_taxi/yellow_tripdata_2023-09.parquet"}
    result = handler(event, context=None)
    print(result)
