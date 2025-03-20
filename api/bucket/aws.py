import boto3

class AWS:

    def __init__(self):
        self.s3 = boto3.client('s3')

