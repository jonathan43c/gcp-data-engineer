import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run():
    # Configuración del pipeline
    options = PipelineOptions(
        runner="DataflowRunner",  # Cambiar a DataflowRunner para GCP. DataflowRunner es para que se corra en Cloud y DirectRunner es para que corra local
        project="beaming-mode-496723-c0", #Esto es el PROJECT_ID
        region="us-central1",
        temp_location="gs://gcp-data-engineer-curso-04b/temp"
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
                "gs://gcp-data-engineer-curso-04b/output/wordcount"
            )
        )

if __name__ == "__main__":
    run()