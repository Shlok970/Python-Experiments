import pandas as pd
import numpy as np
print("\n---3.Merging DataFrames---")
df1=pd.DataFrame({
			'ID' : [1,2,3,4],
			'Name' : ['Jeet','Aastha','Swayam','Sankhya']
			})
df2=pd.DataFrame({
			'ID' : [1,2,5,4],
			'Score' : [95,88,75,92]
			})
print(f"DataFrame 1 : \n{df1}\n")
print(f"DataFrame 2 : \n{df2}\n")
merged_df = pd.merge(df1,df2,on='ID')
print(f"Merged DataFrame (Inner join,only common ID's): \n{merged_df}")
merged_on = pd.merge(df1,df2,on='ID',how = 'outer')
print(f"Merged DataFrame (Outer join,only common ID's): \n{merged_on}")