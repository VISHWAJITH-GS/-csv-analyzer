import streamlit as st
from utils import (
    load_csv,
    show_basic_info,
    show_missing_values,
    show_statistics,
    clean_data,
    plot_correlation_heatmap,
    plot_column_distributions
)

# 🧠 App Title & Description
st.set_page_config(page_title="Smart CSV Analyzer", layout="wide")
st.title("📊 Smart CSV Analyzer")
st.markdown("""
Upload any CSV file and this app will automatically:
- Show the data preview
- Analyze missing values
- Clean the data
- Generate summary statistics
- Plot a correlation heatmap
- Plot individual column distributions
""")

# 📤 File Uploader
uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])

if uploaded_file is not None:
    # 📥 Load the dataset
    df = load_csv(uploaded_file)
    if df is not None:
        st.success("✅ File uploaded and read successfully!")

        # 🔍 Show basic info
        show_basic_info(df)

        # 🚨 Show missing values
        show_missing_values(df)

        # 📉 Summary statistics
        show_statistics(df)

        # 🧹 Clean the data
        df_cleaned = clean_data(df)
        st.success("✅ Missing values handled (median/mode).")

        # 🔥 Correlation heatmap
        st.write("### 🔥 Correlation Heatmap (Numerical Columns Only)")
        fig_corr = plot_correlation_heatmap(df_cleaned)
        if fig_corr:
            st.pyplot(fig_corr)

        # 📈 Column distributions
        plot_column_distributions(df_cleaned)

else:
    st.info("⬆️ Upload a CSV file to start analyzing.")
