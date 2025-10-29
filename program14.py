import pandas as pd
import numpy as np
print("....2. Grouping ......")
sales_data = {
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse', 'Keyboard'],
    'region': ['North', 'North', 'South', 'South', 'North', 'South'],
    'sales': [1200, 25, 75, 1500, 30, 80]
}
sales_df = pd.DataFrame(sales_data)
print(f"Original Sales Data Frame : \n{sales_df}\n")
product_groups = sales_df.groupby('product')
print("Grouped by 'Product' (not yet aggregated) :")
print(product_groups.first())
print(".....3. Aggregating....")
total_sales = sales_df.groupby('product')['sales'].sum()
print(f"Total sales per product : \n{total_sales}\n")
average_sales = sales_df.groupby('region')['sales'].mean()
print(f"average sales per product : \n{average_sales}\n")
aggregated_df = sales_df.groupby('product').agg({'sales': ['sum', 'mean', 'count']})
print(f"Multiple aggregations :\n{aggregated_df}\n")