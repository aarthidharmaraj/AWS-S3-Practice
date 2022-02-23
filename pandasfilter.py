import pandas as pd
# df=pd.read_excel('excelfile1.xls')
# dfcsv=df.to_csv('filter1.csv')
# print(dfcsv)

recsv=pd.read_csv('filter1.csv')
# print(df.shape) #gives number of rows and columns
print(recsv.head(10))
print(recsv['Age']<25) #gives boolean values
print(recsv[recsv['Age']<25])#gives the records
print(recsv[(recsv['Age']>25) & (recsv['Age']<30)])#filtering in between values
print(recsv[recsv['First Name'].str.len()>6])#filtering based on string length
 
re1=(recsv['Country']=='United States')|(recsv['Country']=='France') #filtering with or condition
print(recsv[re1])
re2=(((recsv['Country']=='United States')|(recsv['Country']=='France')) & ((recsv['Age']>25) & (recsv['Age']<30)))
print(recsv[re2])
re3=(recsv['Country']!='United States') & (recsv['Country']!='France')
print(recsv[re3])

##to exclude the contents
re4=(recsv['Country']=='France')
print(recsv[~re4])
re4=recsv[~(recsv['Country']=='France') & ~(recsv['Country']=='Great Britain')]['Country'].unique()
print(re4)

##using query method to filter by columns
print(recsv.query("Country!=['France','Great Britain']"))

print(recsv.query('Age>=20 & Age<35 & Country.str.startswith("F").values'))

#Arranging as per preference
re5=recsv[recsv['Country'].str.startswith("F")][['Id','First Name','Last Name','Country']]
print(re5)

##Arranging as per preference using for 
re6=recsv[[x.startswith("F")for x in recsv['Country']]][['Id','First Name','Last Name','Country']]
print(re6)

re7=recsv[recsv['First Name'].str.contains("vo")].head()
print(re7)

print(recsv[~recsv['First Name'].str.startswith("A")].sort_values(by="First Name"))

##filtering a set of values based on column
Ages=[37,28,32,26]
print(recsv[recsv.Age.isin(Ages)])

#for giving unique values , avoiding repition
print(sorted(list(recsv[~recsv.Age.isin(Ages)]['Age'].unique())))

#filtering using loc
print(recsv.loc[(recsv['Gender']=='Male') & (recsv['Age']<25),] [['Id','First Name','Last Name','Gender']])

##to display top items
print(recsv.nlargest(10,'Age'))
print(recsv.nsmallest(10,'Age'))

##filtering using lambda
print(recsv[recsv.apply(lambda x:x['Country']=="France" and x["Gender"]=="Male",axis=1)])
