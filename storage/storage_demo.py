# =========================================================
# IMPORTS
# =========================================================

# argparse permite recibir parámetros desde la terminal
import argparse

# SDKs oficiales de Google Cloud
from google.cloud import storage, bigquery, spanner


# =========================================================
# FUNCION PARA CREAR UN BUCKET EN CLOUD STORAGE
# =========================================================

def create_bucket(bucket_name, location="US"):

    # Cliente autenticado contra Google Cloud
    client = storage.Client()

    # Referencia lógica al bucket
    bucket = client.bucket(bucket_name)

    # Crear bucket físicamente en GCP
    client.create_bucket(bucket, location=location)

    # Mensaje de éxito
    print(f"✅ Bucket creado: {bucket.name}")


# =========================================================
# FUNCION PARA CREAR UN DATASET EN BIGQUERY
# =========================================================

def create_bigquery_dataset(dataset_id, location="US"):

    # Cliente BigQuery
    client = bigquery.Client()

    # Construcción del dataset:
    # proyecto.dataset
    dataset = bigquery.Dataset(
        f"{client.project}.{dataset_id}"
    )

    # Región donde vivirá el dataset
    dataset.location = location

    # Crear dataset si no existe
    client.create_dataset(dataset, exists_ok=True)

    # Mensaje de éxito
    print(f"✅ Dataset creado: {dataset.dataset_id}")


# =========================================================
# FUNCION PARA CREAR UNA INSTANCIA DE SPANNER
# =========================================================

def create_spanner_instance(
    instance_id,
    config="regional-us-central1",
    display_name=None
):

    # Cliente Spanner
    client = spanner.Client()

    # Definición de la instancia
    instance = client.instance(

        # ID técnico de la instancia
        instance_id,

        # Configuración regional
        configuration_name=
        f"projects/{client.project}/instanceConfigs/{config}",

        # Nombre visible
        display_name=display_name or instance_id,

        # Proyecto GCP
        project="gcp-data-engineer-curso-06"
    )

    # Crear instancia (operación async)
    operation = instance.create()

    # Esperar hasta que termine
    operation.result()

    # Mensaje de éxito
    print(f"✅ Instancia Spanner creada: {instance_id}")


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    # Parser para leer argumentos desde terminal
    parser = argparse.ArgumentParser(
        description="Crear recursos en Google Cloud."
    )

    # Tipo de recurso a crear
    parser.add_argument(
        "resource",
        choices=["bucket", "dataset", "spanner"],
        help="Recurso a crear"
    )

    # Nombre del recurso
    parser.add_argument(
        "--name",
        required=True,
        help="Nombre del recurso"
    )

    # Región para bucket/dataset
    parser.add_argument(
        "--location",
        default="US",
        help="Ubicación para bucket/dataset"
    )

    # Configuración Spanner
    parser.add_argument(
        "--config",
        default="regional-us-central1",
        help="Configuración de Spanner"
    )

    # Nombre visible Spanner
    parser.add_argument(
        "--display_name",
        help="Nombre visible de la instancia"
    )

    # Leer argumentos ingresados en consola
    args = parser.parse_args()

    # =====================================================
    # LOGICA PRINCIPAL
    # =====================================================

    # Si el recurso es bucket
    if args.resource == "bucket":

        create_bucket(
            args.name,
            args.location
        )

    # Si el recurso es dataset
    elif args.resource == "dataset":

        create_bigquery_dataset(
            args.name,
            args.location
        )

    # Si el recurso es spanner
    elif args.resource == "spanner":

        create_spanner_instance(
            args.name,
            args.config,
            args.display_name
        )