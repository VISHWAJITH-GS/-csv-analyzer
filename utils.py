import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# 📌 1. Load the CSV file
def load_csv(file):
    try:
        return pd.read_csv(file)
    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
        return None

# 📌 2. Show basic metadata
def show_basic_info(df):
    st.write("### 📄 Dataset Preview")
    st.dataframe(df.head())

    st.write("### 📏 Dataset Shape")
    st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    st.write("### 🧬 Column Data Types")
    st.write(df.dtypes)

# 📌 3. Check for missing values
def show_missing_values(df):
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if not missing.empty:
        st.write("### ⚠️ Missing Values")
        st.write(missing)
    else:
        st.success("✅ No missing values detected!")

# 📌 4. Basic statistical summary
def show_statistics(df):
    st.write("### 📊 Summary Statistics")
    st.write(df.describe())

# 📌 5. Clean data (simple fill strategy)
def clean_data(df):
    df_cleaned = df.copy()
    for col in df_cleaned.columns:
        if df_cleaned[col].dtype in ['int64', 'float64']:
            df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
        else:
            df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mode()[0] if not df_cleaned[col].mode().empty else "Unknown")
    return df_cleaned

# 📌 6. Plot correlation heatmap
def plot_correlation_heatmap(df):
    corr = df.corr(numeric_only=True)

    if corr.empty or corr.shape[0] < 2:
        st.warning("⚠️ Not enough numeric data for correlation heatmap.")
        return None

    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    return fig

# 📌 7. Plot column-wise distribution
def plot_column_distributions(df):
    numeric_cols = df.select_dtypes(include='number').columns
    if numeric_cols.empty:
        st.warning("⚠️ No numeric columns to plot.")
        return

    st.write("### 📈 Column Distributions")
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        ax.set_title(f"Distribution: {col}")
        st.pyplot(fig)
