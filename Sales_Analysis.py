import pandas as pd
#Load CSV  file
df = pd.read_csv("sales_data.csv")
print(df.columns)
#Display first 5 rows
print(df.head())
#Calculate total sales
total_sales=df["Total_Sales"].sum()
print("Total sales:",total_sales)
#Best selling product by revenue
sales_by_product=df.groupby("Product")["Total_Sales"].sum()
best_product_revenue=sales_by_product.idxmax()
best_product_revenue_value=sales_by_product.max()
print("Best selling product by revenue:",best_product_revenue)
print("Revenue:",best_product_revenue_value)
#Best selling product by quantity
quantity_by_product=df.groupby("Product")["Total_Sales"].sum()
best_product_quantity=quantity_by_product.idxmax()
best_product_quantity_value=quantity_by_product.max()
print("Best selling product by quantity:",best_product_quantity)
print("Units sold:",best_product_quantity_value)
#sales report
sales_report=pd.DataFrame({
    "Total Revenue":sales_by_product,
    "Total units sold":quantity_by_product
})
print("\nsales_report:")
print(sales_report)