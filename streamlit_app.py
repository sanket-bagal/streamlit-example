import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

csv_file = st.sidebar.file_uploader("Upload CSV", type="csv")

# Load dataset from CSV file
if csv_file is not None:
    df = pd.read_csv(csv_file)
else:
    df = pd.DataFrame()


selected_columns = st.multiselect("Select Columns", list(df.columns), default=list(df.columns))

# Deselect all columns if user clicks a button
if st.button("Deselect All Columns"):
    selected_columns = []

# Display selected columns
st.write("Selected Columns:", selected_columns)

# Display the loaded dataset with selected columns
selected_data = df[selected_columns]
st.write("Loaded Dataset:")
st.write(selected_data)

# Display descriptive statistics
if len(selected_columns) > 0:
    st.write("Descriptive Statistics:")
    st.write(selected_data.describe())



# for column in selected_columns:
#     st.subheader(f"Column: {column}")
    
#     # Check if variable is continuous or categorical
#     if selected_data[column].dtype == 'object' or len(selected_data[column].unique()) <= 10:
#         # Categorical variable
#         st.write("Variable Type: Categorical")
        
#         # Univariate analysis
#         st.write("Value Counts:")
#         st.write(selected_data[column].value_counts())
        
#         # Bivariate analysis
#         bivariate_columns = st.multiselect("Select Columns for Bivariate Analysis", selected_columns)
#         if len(bivariate_columns) > 0:
#             st.write("Bivariate Analysis:")
#             for bivariate_column in bivariate_columns:
#                 if bivariate_column != column:
#                     st.subheader(f"Bivariate Analysis with {bivariate_column}")
#                     cross_tab = pd.crosstab(selected_data[column], selected_data[bivariate_column])
#                     st.write(cross_tab)
#     else:
#         # Continuous variable
#         st.write("Variable Type: Continuous")
        
#         # Univariate analysis
#         st.write("Histogram:")
#         plt.figure(figsize=(8, 6))
#         sns.histplot(data=selected_data, x=column, kde=True)
#         st.pyplot(plt)
        
#         # Bivariate analysis
#         bivariate_columns = st.multiselect("Select Columns for Bivariate Analysis", selected_columns)
#         if len(bivariate_columns) > 0:
#             st.write("Bivariate Analysis:")
#             for bivariate_column in bivariate_columns:
#                 if bivariate_column != column:
#                     st.subheader(f"Bivariate Analysis with {bivariate_column}")
#                     plt.figure(figsize=(8, 6))
#                     sns.boxplot(data=selected_data, x=bivariate_column, y=column)
#                     st.pyplot(plt)



univariate_columns = st.multiselect("Select Columns for Univariate Analysis", selected_columns)

if len(univariate_columns) > 0:
    st.write("Univariate Analysis:")
    for column in univariate_columns:
        st.subheader(f"Column: {column}")
        st.write("Value Counts:")
        st.write(selected_data[column].value_counts())

        st.write("Histogram:")
        plt.figure(figsize=(8, 6))
        sns.histplot(data=selected_data, x=column, kde=True)
        st.pyplot(plt)

bivariate_columns = st.multiselect("Select Columns for Bivariate Analysis", selected_columns)

# Perform bivariate analysis
if len(bivariate_columns) > 1:
    st.write("Bivariate Analysis:")
    st.write("Pairplot:")
    pairplot_data = selected_data[bivariate_columns]
    plt.figure(figsize=(10, 8))
    sns.pairplot(data=pairplot_data)
    st.pyplot(plt)
    
    st.write("Correlation Heatmap:")
    plt.figure(figsize=(10, 8))
    sns.heatmap(pairplot_data.corr(), annot=True, cmap="coolwarm", square=True)
    st.pyplot(plt)

# Available datasets
# available_datasets = available_datasets = {
#     "Dataset 1": pd.DataFrame({
#     'Column 1': [1, 2, np.nan, 4, 5, 6, 7, 8, np.nan, 10],
#     'Column 2': ['a', 'b', 'c', 'd', np.nan, 'f', 'g', np.nan, 'i', 'j'],
#     'Column 3': [True, False, True, np.nan, True, False, np.nan, True, False, True],
#     'Column 4': [0.1, 0.2, 0.3, np.nan, 0.5, np.nan, 0.7, 0.8, 0.9, 1.0],
#     'Column 5': ['text', 'data', 'science', 'with', 'null', 'values', 'in', 'some', 'entries', 'too']
# }),
#     "Dataset 2": pd.DataFrame({"Column A": ['a', 'b', 'c'], "Column B": ['d', 'e', 'f'], "Column C": ['g', 'h', 'i']}),
# }

# available_datasets = df

# # Select dataset
# selected_dataset = st.sidebar.selectbox("Select Dataset", list(available_datasets.keys()))

# # Select columns from the selected dataset
# selected_columns = st.multiselect("Select Columns", list(available_datasets[selected_dataset].columns), default=list(available_datasets[selected_dataset].columns))

# # Deselect all columns if user clicks a button
# if st.button("Deselect All Columns"):
#     selected_columns = []

# # Display selected columns
# st.write("Selected Columns:", selected_columns)

# # Display the selected dataset with selected columns
# st.write("Selected Dataset:")
# st.write(available_datasets[selected_dataset][selected_columns])

# if len(selected_columns) > 0:
#     st.write("Descriptive Statistics:")
#     st.write(selected_data.describe())


