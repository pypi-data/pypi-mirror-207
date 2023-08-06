import boto3
import os

class s3_wrapper:
    def __init__(self):
        self.s3 = boto3.client('s3')
        self.s3_resource = boto3.resource('s3')
        self.bucket_name ='vijaysagemakerbucket'
    
    def get_object(self, key):
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=key)
        return obj['Body'].read().decode('utf-8')

    def put_object(self, key, body):
        self.s3.put_object(Bucket=self.bucket_name, Key=key, Body=body)
    
    def delete_object(self, key):
        self.s3.delete_object(Bucket=self.bucket_name, Key=key)
        
    def list_objects(self, prefix=''):
        print('custom access invoked')
        objects = []
        resp = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=prefix)
        for obj in resp['Contents']:
            objects.append(obj['Key'])
        return objects
    
    def copy_object(self, source_key, dest_key):
        copy_source = {'Bucket': self.bucket_name, 'Key': source_key}
        self.s3_resource.Object(self.bucket_name, dest_key).copy_from(CopySource=copy_source)
    
    def move_object(self, source_key, dest_key):
        self.copy_object(source_key, dest_key)
        self.delete_object(source_key)
