variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "raw_bucket_name" {
  description = "Raw S3 bucket name"
  type        = string
}

variable "processed_bucket_name" {
  description = "Processed S3 bucket name"
  type        = string
}