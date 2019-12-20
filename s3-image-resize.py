import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image
import random

bucket = 'snabarparking-files'
s3_client = boto3.client('s3', region_name='us-east-1')
keys = [x['Key'] for x in s3_client.list_objects(Bucket=bucket)['Contents'] if x['Size'] > 250000]

def resize_image(image_path):
    with Image.open(image_path) as image:
        print(image.size)
        if image.size[0] > 1000:
            new_size = [int(x/2) for x in image.size]
            image_resize = image.resize(new_size)
            image_resize.save(image_path)

for key in keys:
    ran_dig = random.randint(10000,99999)
    download_path = f'c:\\temp\\images\\img-tmp-{ran_dig}.jpg'

    s3_client.download_file(bucket, key, download_path)
    resize_image(download_path)
    s3_client.upload_file(download_path, bucket, key)
