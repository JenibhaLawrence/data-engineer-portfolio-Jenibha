from flask import Flask, request, jsonify
from google.cloud import storage
from bq_load import load_to_bigquery
import os
import uuid

app = Flask(__name__)

BUCKET_NAME = os.environ.get("BUCKET_NAME")

@app.route("/")
def home():
    return "CSV Upload API is running"

@app.route("/upload", methods=["POST"])
def upload_csv():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        filename = file.filename

        if not filename.endswith(".csv"):
            return jsonify({"error": "Only CSV files allowed"}), 400

        storage_client = storage.Client()
        bucket = storage_client.bucket(BUCKET_NAME)

        unique_name = f"{uuid.uuid4()}_{filename}"
        blob = bucket.blob(unique_name)
        blob.upload_from_file(file)

        # Trigger BigQuery Load
        load_to_bigquery(unique_name)

        return jsonify({
            "message": "File uploaded successfully",
            "gcs_path": f"gs://{BUCKET_NAME}/{unique_name}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
