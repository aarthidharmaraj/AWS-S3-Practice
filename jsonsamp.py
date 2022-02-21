book={}
book['list1']={
    'name':'tom',
    'address':'xyz',
    'mobile':'787568384',
    'edition':'6th'
}
book['list2']={
    'name':'jerry',
    'address':'abc',
    'mobile':'987568384',
    'edition':'5th'
}
import json
print(type(book))
res=json.dumps(book,indent=2)#takes the dictionary object book and dumps as a string
#print(res)#will be in json format
# write this in a file
with open("C://Users//aarthi.dharmaraj//Documents//AWSs3_boto3//samp1json.txt",'w')as f:
    f.write(res)
#for reading the file
f=open("C://Users//aarthi.dharmaraj//Documents//AWSs3_boto3//samp1json.txt",'r')
res1=f.read()
print(res1)
print(type(res1))
#for getting particular details of specific item ,
# load as a string and converted to dictionary

res2=json.loads(res1)
print(res2)
print(type(res2))

print("The list1 details",res2['list1'])
print("list1's mobile number",res2['list1']['mobile'])
