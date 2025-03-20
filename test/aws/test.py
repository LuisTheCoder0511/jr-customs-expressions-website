from api.bucket.aws import AWS

aws = AWS()
print(aws.s3.list_buckets())