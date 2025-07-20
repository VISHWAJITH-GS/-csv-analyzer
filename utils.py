import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 📥 Load CSV
def read_csv(file) -> pd.DataFrame:
    return pd.read_csv(file)

# 👀 Preview
def preview_data(df):
    return df.head()

# 🧠 Column types
def get_column_types(df):
    return df.dtypes.reset_index().rename(columns={'index': 'Column', 0: 'Type'})

# ❓ Missing values %
def get_missing_info(df):
    missing = df.isnull().mean() * 100
    return missing[missing > 0].sort_values(ascending=False)

# 🛠️ Imputation Logic
def impute_data(df, strategy='mean'):
    df_cleaned = df.copy()
    for col in df_cleaned.select_dtypes(include=np.number).columns:
        if df_cleaned[col].isnull().sum() > 0:
            if strategy == 'mean':
                df_cleaned[col].fillna(df_cleaned[col].mean(), inplace=True)
            elif strategy == 'median':
                df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
            elif strategy == 'mode':
                df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
    return df_cleaned

# 📊 Summary Stats
def get_descriptive_stats(df):
    return df.describe().T

# 📈 Histograms
def plot_histograms(df):
    numeric_cols = df.select_dtypes(include='number').columns
    plots = []
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), ax=ax, kde=True)
        ax.set_title(f'Histogram: {col}')
        plots.append(fig)
    return plots

# 📉 Boxplots
def plot_boxplots(df):
    numeric_cols = df.select_dtypes(include='number').columns
    plots = []
    for col in numeric_cols:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax)
        ax.set_title(f'Boxplot: {col}')
        plots.append(fig)
    return plots

# 🔗 Correlation Matrix
def plot_correlation_heatmap(df):
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Matrix")
    return fig
