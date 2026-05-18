import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    # Configuración del pipeline
    options = PipelineOptions(
        runner="DataflowRunner",  # Cambiar a DataflowRunner para GCP. DataflowRunner es para que se corra en Cloud y DirectRunner es para que corra local
        project="gcp-data-engineer-curso-05", 
        region="us-central1",
        temp_location="gs://gcp-bucket-curso-05/temp"
    )

    with beam.Pipeline(options=options) as p:

        (
            p
            | "Leer archivo" >> beam.io.ReadFromText(
                "gs://dataflow-samples/shakespeare/kinglear.txt"
            )
            | "Separar palabras" >> beam.FlatMap(
                lambda line: line.split()
            )
            | "Contar palabras" >> beam.combiners.Count.PerElement()
            | "Guardar resultados" >> beam.io.WriteToText(
                "gs://gcp-bucket-curso-05/output/wordcount"
            )
        )

if __name__ == "__main__":
    run()