import streamlit as st
from utils import *

st.set_page_config(page_title="Smart CSV Analyzer", layout="wide")

st.title("📊 Smart CSV Analyzer - Auto EDA Engine")

# Upload CSV
file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if file:
    st.success("✅ File uploaded successfully!")
    
    # Read and preview
    df = read_csv(file)
    st.subheader("🔍 Data Preview (First 5 Rows)")
    st.write(preview_data(df))

    # Data Types
    st.subheader("🔢 Column Data Types")
    st.dataframe(get_column_types(df))

    # Missing Values
    st.subheader("❓ Missing Value Summary")
    missing_info = get_missing_info(df)
    if missing_info.empty:
        st.info("✅ No missing values detected.")
    else:
        st.dataframe(missing_info)

    # Imputation
    st.subheader("🛠️ Missing Value Imputation")
    impute_option = st.radio("Choose strategy:", ['mean', 'median', 'mode'], horizontal=True)
    df_cleaned = impute_data(df, strategy=impute_option)
    st.write(f"Imputation using: {impute_option.upper()}")
    st.write(df_cleaned.head())

    # Descriptive Statistics
    st.subheader("📊 Descriptive Statistics")
    st.dataframe(get_descriptive_stats(df_cleaned))

    # Histograms
    st.subheader("📈 Histograms")
    for fig in plot_histograms(df_cleaned):
        st.pyplot(fig)

    # Boxplots
    st.subheader("📉 Boxplots")
    for fig in plot_boxplots(df_cleaned):
        st.pyplot(fig)

    # Correlation Heatmap
    st.subheader("🔗 Correlation Matrix")
    st.pyplot(plot_correlation_heatmap(df_cleaned))

    # Download Report (Text)
    import io
    if st.button("📄 Generate Text Summary Report"):
        buffer = io.StringIO()
        df_cleaned.info(buf=buffer)
        info_str = buffer.getvalue()
        stats = get_descriptive_stats(df_cleaned).to_string()
        report = f"""
Smart CSV Analyzer Report
=========================

DATA INFO:
----------
{info_str}

DESCRIPTIVE STATISTICS:
-----------------------
{stats}
"""
        st.download_button(
            label="📥 Download Report as TXT",
            data=report,
            file_name="eda_summary.txt",
            mime="text/plain"
        )
