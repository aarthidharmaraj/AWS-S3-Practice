from sqlite3 import Timestamp
import pandas as pd
import numpy as np

# #creating pandas series with null value
se=[1,2,3,4,5,6,7,np.nan,9,10]
ser=pd.Series(se)
print(ser)

# #creating dataframe using numpy array ,daytime index and label
da=pd.date_range("20220110",periods=20)
print(da)

df=pd.DataFrame(np.random.randn(20,5),index=da,columns=['A','B','C','D','E'])
print(df)
print(df.head())#displays first five rows
print(df.tail())#displays last five rows
print(df.index) #displays index datas
print(df.columns) #dispalys columns datas
print(df.to_numpy()) #create numpy arrays
print(df.describe()) #gives descrition
print(df.sort_index(axis=1,ascending=False))#sort of values,index
print(df.sort_values(by='C'))
print(df['C'])
print(df[0:3])

print(df.loc[:,['A','B']])##selecting multi-axis by label

print(df.loc['20220110':'20220120',['A','B']])##label slicing

print(df.at[da[0],'C'])#scalar value
print(df.iloc[4])#displays data from position
print(df[df['A']>2])#boolean indexing

#reindexing
df2=df.reindex(index=da[0:4],columns=list(df.columns)+['E'])
df2.loc[da[0]:da[1],'E']=np.nan
print(df2)

#Handling missing data
print(df2.isnull())#pd.isna(df2)
print(df2.dropna())#drop null values
print(df2.fillna(value=3))#fill null values
print(df2.mean())

#Descriptive statistic operations
da1=pd.date_range("20220110",periods=10)
df3=pd.Series([1,2,3,4,np.nan,6,4,3,6,2],index=da1).shift(1)
print(df3)

#applying functions
print(df.apply(np.cumsum))
s=pd.Series(['Python','Sample','Programming',np.nan,'Boto','Dictionary'])
print(s.str.upper())

#for concatenation process
df4=[df[:3],df[3:7],df[7:12]]#breaking
print(pd.concat(df4))

#grouping
print(df.groupby(['C','D']).sum())

#reshaping
tup=list(zip(*[[1,2,3,4,5,6,7,8,12,23],[11,12,13,14,15,17,18,19]]))
index=pd.MultiIndex.from_tuples(tup,names=['First','Second'])
dataf=pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
dataf2=dataf[:7]
print(dataf2)

#compress using stack
print(dataf2.stack())#a.unstack() to unstack 

##creating pivot table
df=pd.DataFrame({'A':['a','b','c','d']*3,
                 'B':['A','B','C']*4,
                 'C':['P','P','P','Q','Q','Q']*2,
                 'D':np.random.randn(12),
                 'E':np.random.randn(12)
                 })
print(df)
df6=pd.pivot_table(df,values='D',index=['A','B'],columns=['C'])
print(df6)

#creating dataframe from 2 series
data={
    "column1":[123,234,134,23],
    "column2":[23,45,67,89]
}
datafr = pd.DataFrame(data)
print(datafr)

#naming indexes
datafr = pd.DataFrame(data, index = ["row1", "row2", "row3","row4"])
print(datafr)

#locate row with index
print(datafr.loc[0])

#locating row with list of index
print(datafr.loc[[0,3]])

df=pd.DataFrame({'A':[1,2,3,4],
                 'B':pd.Timestamp('20220110'),
                 'C':pd.Series(1,index=list(range(4))),
                 'D':np.array([5]*4),
                 'E':pd.Categorical(['True','False','true','false']),
                 'F':'Pandas'
                 })
print(df)#df.dtypes displays the datatypes of the columns
