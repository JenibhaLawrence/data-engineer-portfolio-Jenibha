from google.cloud import bigquery
import os

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET = os.getenv("DATASET")
TABLE = os.getenv("TABLE")
BUCKET_NAME = os.getenv("BUCKET_NAME")

def load_to_bigquery(file_name):
    client = bigquery.Client()

    uri = f"gs://{BUCKET_NAME}/{file_name}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
        skip_leading_rows=1,
        write_disposition="WRITE_APPEND"
    )

    load_job = client.load_table_from_uri(
        uri,
        f"{PROJECT_ID}.{DATASET}.{TABLE}",
        job_config=job_config,
    )

    load_job.result()  # Waits for job to finish

    print(f"Loaded file {file_name} into BigQuery.")
