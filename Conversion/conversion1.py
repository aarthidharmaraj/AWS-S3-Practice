from os import access
import boto3
##creating an object for s3 service, IAM user details are taken directly from the .aws folder
client=boto3.client('s3')

##for creating bucket
client.create_bucket(Bucket='convertcsvtojsoninpandas')
response = client.put_object(
    Body=open('convert1.csv','r').read(),#object data with open and read module of the uploading file
    Bucket='convertcsvtojsoninpandas',
    Key='CSVtoPandas.csv',#file name to be in s3
)
# print(response)

##download the csv file uploaded and convert it to json 
response = client.get_object(
    Bucket='convertcsvtojsoninpandas',
   
    Key='CSVtoPandas.csv',#file name in s3 to be downloaded
)
data=response.get("Body").read().decode()
file=open('downloadedcsv.csv','w')
file.writelines(data)
file.close()

##converting the downloaded csv file to json using pandas

import pandas as pd

pdObj = pd.read_csv('downloadedcsv.csv')#read as a pandas object

jsonData = pdObj.to_json('convertedjson.json',indent=2)#pandas object to json
print(jsonData)

##upload that to s3
response = client.put_object(
    Body=open('convertedjson.json','r').read(),#object data with open and read module of the uploading file
    Bucket='convertcsvtojsoninpandas',
    Key='ConvertedJSON.json',#file name to be in s3
)

##download the json and convert to csv

response = client.get_object(
    Bucket='convertcsvtojsoninpandas',
   
    Key='ConvertedJSON.json',#file name in s3 to be downloaded
)
data=response.get("Body").read().decode()
file=open('downloadedjson.json','w')
file.writelines(data)
file.close()

##Conversion to csv
pdObj1 = pd.read_json('downloadedjson.json', orient='index')
pdObj1.to_csv('convertedcsv.csv', index=False)

##upload to s3
response = client.put_object(
    Body=open('convertedcsv.csv','r').read(),#object data with open and read module of the uploading file
    Bucket='convertcsvtojsoninpandas',
    Key='ConvertedCSV.json',#file name to be in s3
)
