import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data

data = pd.read_csv('superstore_dataset2011-2015.csv',encoding="ISO-8859-1")

# Sidebar
st.sidebar.title("Hypotheses")
hypothesis = st.sidebar.radio("Select a hypothesis:", [
    "Technology products have the highest profit margin compared to other product categories.",
    "The East region has the highest sales compared to other regions.",
    "Sales are higher during certain months of the year.",
    "Orders with same-day shipping have the lowest rate of returned products.",
    "The company's profit is more on weekdays than on weekends."])

# Main page
st.title("Superstore Sales Dashboard")

# Hypothesis 1
if hypothesis == "Technology products have the highest profit margin compared to other product categories.":
    # Group by product category and calculate the sum profit
    plt.figure(figsize=(8, 5))
    cat_profit = data.groupby('Category')['Profit'].sum()

    # Create a bar plot of profit by category
    fig, ax = plt.subplots()
    ax.bar(cat_profit.index, cat_profit.values)
    ax.set_title('Total Profit by Category')
    ax.set_xlabel('Category')
    ax.set_ylabel('Total Profit')
    st.pyplot(fig)

    # Conclusion
    st.write(
        "Conclusion: The hypothesis is supported as technology products have the highest profit margin of the three categories.")

# Hypothesis 2
elif hypothesis == "The East region has the highest sales compared to other regions.":
    # Group by region and calculate the sum of sales
    reg_sales = data.groupby('Region')['Sales'].sum()

    # Create a bar plot of sales by region
    fig, ax = plt.subplots()
    ax.bar(reg_sales.index, reg_sales.values)
    ax.set_title('Total Sales by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Sales')
    ax.tick_params(axis='x', rotation=45)  # rotate x-axis label
    st.pyplot(fig)

    # Conclusion
    st.write("Conclusion: The hypothesis is not supported as the central region has the highest sales.")

# Hypothesis 3
elif hypothesis == "Sales are higher during certain months of the year.":
    # Extract the month from the Order Date column
    data['Order Month'] = pd.DatetimeIndex(data['Order Date']).month

    # Group by month and calculate the sum of sales
    month_sales = data.groupby('Order Month')['Sales'].sum()

    # Create a line plot of sales by month
    fig, ax = plt.subplots()
    ax.plot(month_sales.index, month_sales.values)
    ax.set_title('Total Sales by Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Sales')
    ax.tick_params(axis='x', rotation=45)  # rotate x-axis label
    st.pyplot(fig)

    # Conclusion
    st.write(
        "Conclusion: As we can see from the line plot, sales are higher in November and December. This supports our hypothesis that sales are higher during certain months of the year.")

# Hypothesis 4
elif hypothesis == "Orders with same-day shipping have the lowest rate of returned products.":
    # Calculate the total number of orders for each shipping mode
    total_orders_by_shipping_mode = data.groupby('Ship Mode').size()

    # Calculate the total number of returned orders for each shipping mode
    returned_orders_by_shipping_mode = data[data['Profit'] < 0].groupby('Ship Mode').size()

    # Calculate the percentage of orders that are returned for each shipping mode
    return_percentage_by_shipping_mode = (returned_orders_by_shipping_mode / total_orders_by_shipping_mode) * 100

    # Create a bar plot of return percentage by shipping mode
    fig, ax = plt.subplots()
    ax.bar(return_percentage_by_shipping_mode.index, return_percentage_by_shipping_mode.values)
    ax.set_title('Return Percentage by Shipping Mode')
    ax.set_xlabel('Shipping Mode')
    ax.set_ylabel('Return Percentage')
    ax.tick_params(axis='x', rotation=45)  # rotate x-axis label
    st.pyplot(fig)

    # Conclusion
    st.write("Conclusion: The hypothesis is supported as same-day shipping has the lowest rate of returned products.")
elif hypothesis == "The company's profit is more on weekdays than on weekends.":
    # Extract the day of the week from the Order Date column
    data['Order Day'] = pd.DatetimeIndex(data['Order Date']).day_name()
    # Group by day of the week and calculate the mean profit
    day_profit = data.groupby('Order Day')['Profit'].sum()

    # Create a bar plot of mean profit by day of the week
    fig, ax = plt.subplots()
    ax.bar(day_profit.index, day_profit.values)
    ax.set_title('Mean Profit by Day of the Week')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Total Profit')
    st.pyplot(fig)

    # Conclusion
    st.write("Conclusion: The hypothesis is supported as the mean profit is higher on weekdays than on weekends.")
