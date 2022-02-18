from os import access
import boto3
#creating an object for s3 service, IAM user details are taken directly from the .aws folder
client=boto3.client('s3')

#for creating bucket
client.create_bucket(Bucket='boto3samp1')

# for listing buckets names in S3
response=client.list_buckets()
print(response['Buckets'])

# for listing buckets details in S3
response=client.list_buckets()
print(response)
#for listing objects in buckets
response=client.list_objects(Bucket="boto3samp1")
objects=response.get("Contents")
print(f"Total Objects: {len(objects)}")
print(objects)

#for deleting a object
response = client.delete_object(
    Bucket='boto3samp1',
    Key='B3upload2.py',#file in s3 to be deleted
)
print(response)

#Giving IAM user details directly
client1=boto3.client('s3',
                     aws_access_key_id = "AKIA4B5VXORR5R576YVF",aws_secret_access_key = "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",
                     region_name="us-east-1")
response=client1.create_bucket(Bucket="boto3samp3")
print(response)

 #for uploading a file in bucket
response = client.put_object(
    Body=open('S3Boto3.py','r').read(),#object data with open and read module of the uploading file
    Bucket='boto3samp1',
    Key='data/image1.jpg',#file name to be in s3
)
print(response)

#for downloading a file to local machine
response = client.get_object(
    Bucket='boto3samp1',
   
    Key='B3upload2.py',#file name in s3 to be downloaded
)
data=response.get("Body").read().decode()
file=open('B3upload2.py','w')
file.writelines(data)
file.close()

#for deleting bucket
response=client.delete_bucket(
    Bucket="boto3samp2"
)
print(response)