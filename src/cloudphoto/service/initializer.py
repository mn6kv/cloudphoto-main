from botocore.exceptions import ClientError

from .aws_helper import create_s3_session
from .config import create_config

default_bucket_name = "no-name-bucket"
region = "ru-central1"
endpoint_url = "https://storage.yandexcloud.net"


def initialize():
    bucket_name = default_bucket_name
    aws_access_key_id = input("input key id: ")
    aws_secret_access_key = input("input secret key: ")
    bucket_name = input("bucket name: ")

    try:
        s3 = create_s3_session(aws_access_key_id, aws_secret_access_key, endpoint_url, region)
        s3.create_bucket(Bucket=bucket_name, ACL='public-read-write')
    except ClientError as clientError:
        if clientError.response["Error"]["Code"] != "BucketAlreadyOwnedByYou":
            raise clientError

    create_config(access_key=aws_access_key_id, secret_key=aws_secret_access_key, bucket_name=bucket_name)