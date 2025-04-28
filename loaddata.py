import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    # Read from a CSV file (first 20 rows only)
    df = pd.read_csv('sales_data_sample.csv', encoding='latin1', nrows=20)
    print("✅ Data loaded successfully!\n")

    # Display the first five rows
    print("📄 First 5 rows:")
    print(df.head(), "\n")

    # Get the datatypes of each column
    print("ℹ️ Data Types Info:")
    print(df.info(), "\n")

    # Print null values
    print("🧹 Missing Values Per Column:")
    print(df.isnull().sum(), "\n")

    # Fill null values with 'Unknown'
    df_cleaned = df.fillna('Unknown')
    print("✅ Null values filled. Here's the updated data:")
    print(df_cleaned.head(), "\n")

    # Compute basic statistics
    print("📊 Basic Statistics:")
    print(df.describe(), "\n")

    # Group sales per country and get the mean
    grouped_country = df_cleaned.groupby('COUNTRY')['SALES'].mean().sort_values(ascending=False)
    print("🌎 Average Sales per Country:")
    print(grouped_country, "\n")

    # Group sales per dealsize and get the mean
    grouped_dealsize = df_cleaned.groupby('DEALSIZE')['SALES'].mean().sort_values(ascending=False)
    print("🤝 Average Sales per Deal Size:")
    print(grouped_dealsize, "\n")

    # ======================= Plotting ========================

    sns.set_style('darkgrid')

    # Line Plot: SALES vs COUNTRY
    plt.figure(figsize=(10,6))
    plt.plot(df_cleaned['COUNTRY'], df_cleaned['SALES'], marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Country')
    plt.ylabel('Sales')
    plt.title('Sales by Country (Line Plot)')
    plt.tight_layout()
    plt.show()

    # Bar Plot: Average Sales by Country
    plt.figure(figsize=(10,6))
    grouped_country.plot(kind='bar', color='skyblue')
    plt.xlabel('Country')
    plt.ylabel('Average Sales')
    plt.title('Average Sales by Country (Bar Chart)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Histogram: Distribution of Sales
    plt.figure(figsize=(8,5))
    df_cleaned['SALES'].plot(kind='hist', bins=10, color='lightgreen', edgecolor='black')
    plt.xlabel('Sales Amount')
    plt.title('Distribution of Sales')
    plt.tight_layout()
    plt.show()

    # Scatter Plot: ORDERLINENUMBER vs SALES
    plt.figure(figsize=(8,5))
    sns.scatterplot(x='ORDERLINENUMBER', y='SALES', data=df_cleaned, hue='DEALSIZE', palette='muted')
    plt.title('Order Line Number vs Sales')
    plt.xlabel('Order Line Number')
    plt.ylabel('Sales')
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("❌ File not found. Please check the file path and name.")
except pd.errors.EmptyDataError:
    print("❌ The file is empty. Please provide a valid CSV file.")
except pd.errors.ParserError:
    print("❌ Error parsing file. Please ensure it's a properly formatted CSV.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
