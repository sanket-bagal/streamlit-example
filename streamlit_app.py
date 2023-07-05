import streamlit as st
import pandas as pd
import numpy as np

csv_file = st.sidebar.file_uploader("Upload CSV", type="csv")

# Load dataset from CSV file
if csv_file is not None:
    df = pd.read_csv(payments_churn_data)
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


