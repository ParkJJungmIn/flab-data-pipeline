output "s3_bucket_name" {
  value = aws_s3_bucket.datalake.bucket
}

resource "local_file" "bucket_config" {
  content  = "S3_BUCKET_NAME=${aws_s3_bucket.datalake.bucket}"
  filename = "${path.module}/bucket_config.txt"
}