import argparse
from google.cloud import storage

def main():
    parser = argparse.ArgumentParser(description="Create a GCP bucket.")

    parser.add_argument(
        "bucket_name",
        type=str,
        help="Name of the bucket to create"
    )

    args = parser.parse_args()

    bucket_name = args.bucket_name

    print(f"Bucket name received: {bucket_name}")

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Clase de almacenamiento
    bucket.storage_class = "STANDARD"

    # Crear bucket en la región indicada
    new_bucket = storage_client.create_bucket(
        bucket,
        location="US-CENTRAL1"
    )

    print(
        f"Bucket {new_bucket.name} created in "
        f"{new_bucket.location} with class "
        f"{new_bucket.storage_class}"
    )

if __name__ == "__main__":
    main()