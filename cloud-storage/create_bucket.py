from google.cloud import storage

def main():
    bucket_name = input("Ingresa el nombre del bucket: ").strip()

    if not bucket_name:
        print("Error: el nombre del bucket no puede estar vacío.")
        return

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