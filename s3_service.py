import boto3
from io import BytesIO


class S3Service:

    AWS_ACCESS_KEY = "XXX"
    AWS_SECRET_KEY = "XXX"

    def __init__(self):
        """ Initialises the S3 Service (low-level client and higher-level resource objects) """
        self.s3_client = boto3.client('s3',
                                      aws_access_key_id=self.AWS_ACCESS_KEY,
                                      aws_secret_access_key=self.AWS_SECRET_KEY)

    def upload_binary_file(self, bucket_name, s3_key, bytes_io):
        """ Upload a binary file to S3 """
        try:
            self.s3_client.upload_fileobj(bytes_io, bucket_name, s3_key)
        except Exception as e:
            print('Error putting S3 file: {}'.format(e))

    def download_binary_file(self, bucket_name, s3_key):
        """ Upload a binary file to S3 """
        try:
            bytes_io = BytesIO()
            self.s3_client.download_fileobj(Bucket=bucket_name, Key=s3_key, Fileobj=bytes_io)
            bytes_io.seek(0)
            return bytes_io
        except Exception as e:
            print('Error getting S3 file: {}'.format(e))
