import pandas as pd
df=pd.read_csv('filter1.csv')
print(df)
##to check the datatypes
print("The datatypes present in file",df.dtypes)
print(df.info())

##make a copy of data
dfcpy=df.copy()

##Handling missing values
print(df.dropna())
print(df.dropna(axis='index',how='any'))#axis='columns and how='all'

##datatype conversion
df['Age']=df.Age.astype(float)
print(df.dtypes)
# print(df)

df['SerialNumber']=df['SerialNumber'].astype(str)
print(df.dtypes)

df['Age']=df.Age.astype(int)
print(df.dtypes)

##Apply function to return to the original dtype
df['Age']=df['Age'].apply(pd.to_numeric)
print(df.dtypes)

#infer method
df['Age']=df['Age'].infer_objects()
print(df.dtypes)
