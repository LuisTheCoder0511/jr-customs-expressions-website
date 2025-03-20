import boto3

class AWS:

    def __init__(self):
        self.bucket_name = "luisthecoder-images-bucket"
        print("Connecting to AWS")
        self.s3 = boto3.client('s3',
                               aws_access_key_id='AKIA5H5LK4SRTSS5KTO7',
                               aws_secret_access_key='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',
                               region_name='us-east-1')
        print("Connected to AWS")


    def __upload__(self, img):
        self.s3.upload_file(img, self.bucket_name, f"uploads/{img}")

aws = AWS()
