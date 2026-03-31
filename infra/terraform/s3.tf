resource "aws_s3_bucket" "raw_bucket" {
  bucket = var.raw_bucket_name

  tags = {
    Name        = "raw-data-bucket"
    Environment = "dev"
    Project     = "aws-data-engineering-project"
    Layer       = "raw"
  }
}

resource "aws_s3_bucket" "processed_bucket" {
  bucket = var.processed_bucket_name

  tags = {
    Name        = "processed-data-bucket"
    Environment = "dev"
    Project     = "aws-data-engineering-project"
    Layer       = "processed"
  }
}