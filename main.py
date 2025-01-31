from google.cloud import bigquery
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
#update for Banorte
app = FastAPI()
big_query_client = bigquery.Client()

@app.get("/")
def insert_bigquery():
    table_id = "gsd-ai-mx-ulises.test_schema.us_states"
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
    )
    uri = "gs://your-bucket-name-gsd-ai-mx-ulises-unique/us-states.csv"
    load_job = big_query_client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )

    load_job.result()

    destination_table = big_query_client.get_table(table_id)
    return JSONResponse({"data": destination_table.num_rows})
