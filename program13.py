import pandas as pd
import numpy as np

print(f"---1.Series and Dataframe---")
s=pd.Series([10,20,30,40,50],name="Numbers")
print(f"simple series:\n{s}\n")

data={
	'City' : ['Mumbai','Delhi','Chennai','Kolkata'],
	'Population' : [20,10,11,15],
	'Area_sq_kmkm' : [603,1484,400,105]
	}
df=pd.DataFrame(data)
print(f"Data frame created from a dictionary: \n{df}")
print(f"---Multilevel index series---")
index_tuples=[
				('GroupA','item1'),('GroupA','item2'),
				('GroupB','item1'),('GroupB','item2'),
			]
multi_index=pd.MultiIndex.from_tuples(index_tuples,name=['Group','item'])
multilevel_s=pd.Series([100,200,300,400],index=multi_index)
print(f"Multi level index series: \n{multilevel_s}\n")
print("Accessing data for 'Group A':")
print(multilevel_s.loc['GroupA'])