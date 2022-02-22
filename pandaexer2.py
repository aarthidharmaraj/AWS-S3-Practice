from random import random
from sre_parse import CATEGORIES
from unicodedata import category

import pandas as pd
import numpy as np
##Time series
dates=pd.date_range("12/02/2022",periods=20,freq='N')
ts=pd.Series(np.random.randint(0,50,len(dates)),dates)
ts1=ts.resample('5min').sum()
print(ts1)

dates=pd.date_range("12/03/2022",periods=10,freq='N')
ts=pd.Series(np.random.randn(len(dates)),dates)
ts1=ts.resample('5min').sum()
print(ts)

#time zone representation
ts_utc=ts.tz_localize('UTC')
print(ts_utc)
ts_utc1=ts_utc.tz_convert('US/Eastern')
print(ts_utc1)

dates=pd.date_range("12/03/2022",periods=10,freq='M')
ts=pd.Series(np.random.randn(len(dates)),dates)
ps=ts.to_period()
print(ps)
print(ps.to_timestamp())

df=pd.DataFrame({'id':[1,2,3,4,5,6],
                 'grade':['a','b','c','a','e','f']
                 })
df["Grade"]=df['grade'].astype("category")
# print(df["Grade"])
df["Grade"].cat.categories=['Very Good','Good','Bad','Verybad','Fails']
df["Grade"]=df['Grade'].cat.set_categories(['Very Good','Excellent','Verybad','Good','Average','Bad'])
print(df["Grade"])

##Dataframe to json file
import json
df = pd.DataFrame(
    [["a", "b"], ["c", "d"]],
    index=["row 1", "row 2"],
    columns=["col 1", "col 2"],
)
result = df.to_json(orient="records")#orient=index,columns,values,split,table,
parsed = json.loads(result)
pr=json.dumps(parsed, indent=4) 
print(pr)
##reading json files
df1=pd.read_json('loadfile1.json')
print(df1)

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":50,
    "3":45,
    "4":45,
    "5":60
  },
  "Values":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

df2 = pd.DataFrame(data)

print(df2) 
##working with csv files
df=pd.read_csv('details.csv')

print(df.to_string())#to print entire dataframe
print(pd.options.display.max_rows)#dipaly maximum of rows
#to remove duplicte entries
print(df.duplicated())
d=df.drop_duplicates(inplace = True)
print(df.to_string())
print(df.corr())#correlation method removes non-numeric values
#plotting
import sys
import matplotlib.pyplot as plt
plt.close('all')
ts=pd.Series(np.random.randn(50),index=pd.date_range('10/02/2022',periods=50))
print(ts)
ts.plot()
plt.show()
# #converting to csv
ts.to_csv('plottedfile.csv')#dataframe to csv file

##reading csv file
df = pd.read_csv('details.csv')

df.plot()

plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()