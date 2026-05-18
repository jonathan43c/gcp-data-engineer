python3 wordcount.py \
  --runner DataflowRunner \
  --project gcp-data-engineer-curso-05 \
  --region us-central1 \
  --staging_location gs://gcp-bucket-curso-05/staging/ \
  --temp_location gs://gcp-bucket-curso-05/temp/ \
  --template_location gs://gcp-bucket-curso-05/templates/wordcount_template