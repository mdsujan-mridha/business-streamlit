import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="Brand Owner", page_icon=":shark:", layout="wide")
st.sidebar.header("🔰Dashboard")


page=st.sidebar.radio("Select a page",["Home","Sales Analysis","Revenue Comparison","Inventory Managment","Predict Data","Profit Calculator","Product Suggestions"])
# st.page_link("pages/sales.py", label="Sales Analysis", icon="📉")
# st.page_link("pages/sales.py", label="Revenue Comparison", icon="📉")
# st.page_link("pages/sales.py", label="Inventory Managment", icon="📉")
# st.page_link("pages/sales.py", label="Predict Data", icon="📉")
# st.page_link("pages/sales.py", label="Profit Calculator", icon="📉")
# st.page_link("pages/sales.py", label="Product Suggestions", icon="📉")

if page=="Home":
    st.write("Home")
elif page=="Sales Analysis":
    st.write("Sales Analysis")
    # Create columns for the pie chart and filter
    col1, col2 = st.columns([2, 1])
    with col1:
    # Sample data for pie chart
            data = {
                  'Category': ['Electronics', 'Clothing', 'Home', 'Books'],'Sales': [35, 25, 20, 20]}
            fig = px.pie(data, values='Sales', names='Category', 
             color_discrete_sequence=['#FF6B6B', '#4ECDC4'])
            st.plotly_chart(fig, use_container_width=True)
    with col2:
         category = st.selectbox(
        'Filter by category:',
        ('Apparel', 'Electronics', 'Home', 'Books'))
    # Regional Performance Section
    st.header("Regional Performance")
    # Create columns for map and metrics
    col1, col2 = st.columns([2, 1])
    with col1:
    # Sample data for US map
        # states = px.utils.us_states()
        fig = px.choropleth(
        locations=['CA', 'NY', 'TX'],
        locationmode="USA-states",
        scope="usa",
        color=[1, 2, 3],
        color_continuous_scale=["#4ECDC4", "#FF6B6B"], )
        fig.update_layout(geo_scope='usa')
        st.plotly_chart(fig, use_container_width=True)
    with col2:
    # Profit Margins & Opportunity Costs
        st.subheader("Profit Margins & Opportunity Costs")
    
    # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Sales Data", "$120K")
        with col2:
            st.metric("Profit Margins", "35%")
        with col3:
            st.metric("Opportunity Costs", "$15K")
    # Seasonal Trends Section
    st.header("Seasonal Trends")

# Sample data for seasonal trends
    seasons_data = {
    'Season': ['Spring', 'Summer', 'Fall', 'Winter'],
    'Sales 2023': [65, 80, 95, 70],
    'Sales 2022': [60, 75, 85, 65]}
    df = pd.DataFrame(seasons_data)

    fig = px.bar(df, x='Season', y=['Sales 2023', 'Sales 2022'],
             barmode='group',
             color_discrete_sequence=['#4ECDC4', '#FF6B6B'])
    st.plotly_chart(fig, use_container_width=True)

# Navigation buttons
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
       st.button('Back')
    with col3:
        st.button('Next')     
        # revenue page =======================================================   
elif page=="Revenue Comparison":
    # Set page configst.set_page_config(page_title="Revenue Comparison", layout="wide")

# Generate mock data
        np.random.seed(42)
        months = pd.date_range(start='2023-01-01', end='2023-12-31', freq='M')
        current_year = 70 + np.random.rand(12) * 3
        previous_year = 40 + np.random.rand(12) * 30

        data = pd.DataFrame({
                'Month': months,
                'Current Year': current_year,
                'Previous Year': previous_year})

       # Title
        st.title('📈 Revenue Comparison')

# Date range selector
        date_range = st.selectbox(
             'Select Date Range:',
                ['Year-over-Year', 'Quarter-over-Quarter', 'Month-over-Month'])

# Main chart
        st.subheader('Comparative Analysis')
        chart_data = pd.DataFrame({'Month': months,'Current Year': current_year,'Previous Year': previous_year})

        st.line_chart(
        chart_data.set_index('Month')[['Current Year', 'Previous Year']],height=400)

# Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
            label="Revenue Growth",
            value="12%",
            delta="2.5%")

        with col2:
            st.metric(label="Revenue Decline",value="5%",delta="-1.2%")

        with col3:
            st.metric(label="Net Profit Margin",value="8%",delta="0.8%"
    )

# Navigation buttons
        col1, col2 = st.columns([1, 1])

        with col1:
           if st.button('⬅️ Back'):
            pass  # Add navigation logic here
        with col2:
         if st.button('Next ➡️'):
          pass  # Add navigation logic here
elif page=="Inventory Managment":
    # inventory page ====================================
    col1, col2, col3 = st.columns(3)

    with col1:
            st.write('Wireless Headphones')
            st.write('Category: Electronics')
            st.write('StockLevel: 100')

    with col2:
            st.write('T-shirt')
            st.write('Category: Apparel')
            st.write('StockLevel: 100')

    with col3:
            st.write('Ceramic')
            st.write('Category: home Goods')
            st.write('StockLevel: 100')
    

# Navigation buttons
    col1, col2 = st.columns([1, 1])

    with col1:
           if st.button('⬅️ Back'):
            pass  # Add navigation logic here
    with col2:
         if st.button('Next ➡️'):
          pass  # Add navigation logic here
    st.write("Inventory Managment")
elif page=="Predict Data":
    st.write("Predict Data")
elif page=="Profit Calculator":
    st.write("Profit Calculator")
elif page=="Product Suggestions":
    st.write("Product Suggestions")
    




