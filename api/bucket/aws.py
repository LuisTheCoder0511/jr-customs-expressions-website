import boto3
from botocore.exceptions import ClientError


class AWS:

    def __init__(self):
        self.bucket_name = "luisthecoder-images-bucket"
        print("Connecting to AWS")
        self.s3 = boto3.client('s3',
                               aws_access_key_id='AKIA5H5LK4SRTSS5KTO7',
                               aws_secret_access_key='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',
                               region_name='us-east-1')
        print("Connected to AWS")


    def __upload__(self, filename, timestamp):
        try:
            self.s3.upload_file(filename, self.bucket_name, f"uploads/{timestamp}.png", ExtraArgs={'ACL': 'public-read'})
            self.s3.head_object(Bucket=self.bucket_name, Key=f"uploads/{timestamp}.png")
        except ClientError as e:
            print("Upload failed:", e)
            return False
        return True

    def __delete__(self, timestamp: int):
        try:
            self.s3.delete_object(Bucket=self.bucket_name, Key=f"uploads/{timestamp}.png")
            self.s3.head_object(Bucket=self.bucket_name, Key=f"uploads/{timestamp}.png")
            print("Delete failed!")
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                print("File successfully deleted!")
                return True
            else:
                print("Error during deletion:", e)
        return False

    def __get_url__(self, timestamp: int):
        return f"https://{self.bucket_name}.s3.amazonaws.com/uploads/{timestamp}.png"

aws = AWS()
