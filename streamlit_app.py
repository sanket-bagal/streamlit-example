import streamlit as st
import pandas as pd

# Available datasets
available_datasets = {
    "Dataset 1": pd.DataFrame({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6], "Column 3": [7, 8, 9]}),
    "Dataset 2": pd.DataFrame({"Column A": ['a', 'b', 'c'], "Column B": ['d', 'e', 'f'], "Column C": ['g', 'h', 'i']}),
}

# Select dataset
selected_dataset = st.sidebar.selectbox("Select Dataset", list(available_datasets.keys()))

# Select columns from the selected dataset
selected_columns = st.multiselect("Select Columns", list(available_datasets[selected_dataset].columns), default=list(available_datasets[selected_dataset].columns))

# Deselect all columns if user clicks a button
if st.button("Deselect All Columns"):
    selected_columns = []

# Display selected columns
st.write("Selected Columns:", selected_columns)

# Display the selected dataset with selected columns
st.write("Selected Dataset:")
st.write(available_datasets[selected_dataset][selected_columns])
