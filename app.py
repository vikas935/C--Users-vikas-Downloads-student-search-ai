import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Load Excel data
df = pd.read_excel("students.xlsx")

st.title("AI Student Search")

query = st.text_input("🔍 Search student by name, roll number, or department:")

if query:
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    if not results.empty:
        st.write(results)
    else:
        st.warning("No results found.")
