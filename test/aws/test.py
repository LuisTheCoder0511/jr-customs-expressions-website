from api.bucket.aws import aws
import time


print(aws.s3.list_buckets())
filename = "static/assets/images/Image_Test_Template.png"
timestamp = int(time.time())
if aws.__upload__(filename, timestamp):
    url = aws.__get_url__(timestamp)
    print(url)

    time.sleep(60)

    aws.__delete__(timestamp)

