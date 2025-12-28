# 不安全的 S3 配置（Checkov 会报警！）
resource "aws_s3_bucket" "example" {
  bucket = "my-devsecops-bucket"
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.example.id
  acl    = "public-read"  # ← 这是高危配置！Checkov 会报错
}
