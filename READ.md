#  Sales Analysis Report

## 1. Introduction
This report presents an analysis of the sales dataset using Python and the Pandas library.  
The objective is to calculate total sales, identify the best-selling product, and summarize product-wise performance.

---

## 2. Dataset Overview
The dataset contains the following columns:

- **Date** – Date of transaction  
- **Product** – Product name  
- **Quantity** – Number of units sold  
- **Price** – Price per unit  
- **Customer_ID** – Unique customer identifier  
- **Region** – Sales region  
- **Total_Sales** – Total sales amount for each transaction  

---

## 3. Tools & Technologies Used
- **Programming Language:** Python  
- **Library:** Pandas  
- **IDE:** VSCode
- **File Format:** CSV  

---

## 4. Total Sales Analysis
The total sales were calculated by summing the `Total_Sales` column.

**Result:**
- **Total Revenue:** ₹12,365,048

---

## 5. Best Selling Product Analysis

### 5.1 Best Selling Product by Revenue
- **Product:** Laptop  
- **Total Revenue:** ₹3,889,210  

### 5.2 Best Selling Product by Quantity
- **Product:** Laptop  
- **Units Sold:** 136  

 *Laptop is the best-selling product in terms of both revenue and quantity.*

---

## 6. Product-wise Sales Summary

| Product      | Total Revenue (₹) | Units Sold |
|--------------|------------------|------------|
| Laptop       | 3,889,210        | 136        |
| Tablet       | 2,884,340        | 127        |
| Phone        | 2,859,394        | 101        |
| Headphones   | 1,384,033        | 48         |
| Monitor      | 1,348,071        | 66         |

---

## 7. Conclusion
The analysis shows strong overall sales performance with total revenue exceeding ₹12 million.  
Among all products, **Laptops** emerged as the top-performing product, contributing the highest revenue and the highest number of units sold. Tablets and Phones also showed significant sales, while Headphones and Monitors had comparatively lower performance.

---

## 8. Future Enhancements
- Region-wise sales analysis  
- Monthly and yearly trend analysis  
- Data visualization using charts  
- Integration with Django for web-based reporting  

---

## 9. References
- Pandas Documentation: https://pandas.pydata.org/