# Number of employees
# Industry
# What's your average churn rate?
# Are there any rewwards program in place?

notes = """
Assumptions that we need to answer:

- What is the cost of churn per employee (i.e as a percentage of salary)?
- What percentage of the company revenue is spent on employee churn?

- What is a reduction in churn that you can expect from Visix?
"""

assumptions_explanation = """
1. According to https://www.peoplekeep.com/blog/employee-retention-the-real-cost-of-losing-an-employee, the average cost to replace an employee is 50pct of their salary, this is reflected as the\
default value in the first slider
2. According to various sites, there is a proportion of revenue that is spent on employee churn, this is reflected as the default value in the second slider
3. According to various sites, there is a reduction in churn that you can expect from Visix (comparable to other wellbeing platforms), this is reflected as the default value in the third slider
"""



import streamlit as st
import numpy as np

st.title('Visix ROI Calculator')

st.warning('You can adjust the assumptions below to see how they impact the ROI')
with st.expander('See assumptions'):
    st.write(assumptions_explanation)
    st.write("")
    st.write("")
    # Cost of churn as a percentage of salary
    churn_multiplier = st.slider('What is the cost of churn per employee (i.e as a percentage of salary) in %?', 0, 200, 50) / 100
    # Percentage of revenue spent on employee churn
    churn_revenue = st.slider('What percentage of the company revenue is spent on employee churn in %?', 0, 100, 2) / 100
    # Percentage reduction in churn rate
    churn_reduction = st.slider('What is a reduction in churn that you can expect from Visix in %?', 0, 20, 5) / 100


# -----------------------------------------------------

st.header('Employee Churn Calculator')

# Number of employees
employees = st.slider('Number of employees', 1, 100000, 10)

# What's your average churn rate?
churn_rate = st.slider('What is your average churn rate?', 0.0, 1.0, 0.1)

# Average salary per employee
salary = st.slider('What is the average salary per employee?', 0, 100000, 10000)

# Company revenue
revenue = st.slider('What is the company revenue?', 0, 100000000, 1000000)

# Annual cost of employee churn assuming the cost of churn is 1.5 times the salary and 2% of revenue
churn_cost = (employees * churn_rate) * salary * churn_multiplier + (revenue * churn_revenue)

# Estimate savings from a reduction in turnover (assuming 5% reduction in churn rate)
total_savings = churn_cost * 0.01

# Total savings for year 1
total_savings_y1 = int(total_savings)

# Total savings for year 2
total_savings_y2 = int(total_savings * 1.1)

# Total savings for year 3
total_savings_y3 = int(total_savings_y2 * 1.1)

st.text('Total Savings for implementing Visix')

# Display the total savings as streamlit metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.text('Year 1')
    # Display the number with commas
    st.header(f'${total_savings_y1:,}')

with col2:
    st.text('Year 2')
    st.header(f'${total_savings_y2:,}')

with col3:
    st.text('Year 3')
    st.header(f'${total_savings_y3:,}')

st.header('Visix Costing Calculator')

# Cost per user for Visix (the cost of the software)
cost_per_user = st.slider('What is the cost per user per month for Visix?', 0, 20, 1)

# Total cost of Visix for the company
total_cost = cost_per_user * employees * 12

col1, col2, col3 = st.columns(3)

# Total cost for year 1
with col1:
    st.text('Year 1 Cost')
    # Display the number with commas
    st.header(f'${total_cost:,}')
    ROI_y1 = total_savings_y1 / total_cost
    st.text(f'ROI = {ROI_y1 * 100:.2f}%')

with col2:
    st.text('Year 2 Cost')
    st.header(f'${int(total_cost * 1.1):,}')
    ROI_y2 = total_savings_y2 / (total_cost * 1.1)
    st.text(f'ROI = {ROI_y2 * 100:.2f}%')

with col3:
    st.text('Year 3 Cost')
    st.header(f'${int(total_cost * 1.1 * 1.1):,}')
    ROI_y3 = total_savings_y3 / (total_cost * 1.1 * 1.1)
    st.text(f'ROI = {ROI_y3 * 100:.2f}%')


        

