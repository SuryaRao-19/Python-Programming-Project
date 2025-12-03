"""
Weather Data Visualizer - Final Complete Mini Project (OOP Version)
Fulfills ALL tasks in Lab Assignment 4  (:contentReference[oaicite:0]{index=0})

This script:
1. Creates a sample weather CSV (data acquisition)
2. Loads the CSV and displays head, info, describe
3. Cleans missing values, converts date
4. Computes statistics with NumPy (daily, monthly, yearly)
5. Generates all required plots:
   - Daily temperature line chart
   - Monthly rainfall bar chart
   - Humidity vs temperature scatter
   - Combined subplot figure
6. Groups data by month and season
7. Exports cleaned CSV + PNG files
8. Generates a Markdown report
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class WeatherDataVisualizer:

    def __init__(self):
        self.raw_csv = "weather_data.csv"
        self.cleaned_csv = "weather_data_cleaned.csv"
        self.output_dir = "outputs"
        os.makedirs(self.output_dir, exist_ok=True)
        self.df = None

    # ---------------------------------------------------------
    # Task 1: Data Acquisition – Create & Load CSV
    # ---------------------------------------------------------
    def create_sample_csv(self):
        data = {
            "Date": [
                "2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05",
                "2024-02-01","2024-02-02","2024-02-03","2024-02-04","2024-02-05"
            ],
            "Temperature": [26, 27, np.nan, 29, 30, 31, 32, 33, np.nan, 34],
            "Rainfall": [0, 5, 2, np.nan, 10, 0, 0, np.nan, 4, 1],
            "Humidity": [70, 72, 68, 75, np.nan, 80, 82, 78, 77, 79]
        }
        df_sample = pd.DataFrame(data)
        df_sample.to_csv(self.raw_csv, index=False)
        print(f"[+] Sample CSV created: {self.raw_csv}")

    def load_data(self):
        self.df = pd.read_csv(self.raw_csv)
        print("\n----- DATA LOADED -----")
        print(self.df.head())
        print("\nINFO:\n", self.df.info())
        print("\nDESCRIBE:\n", self.df.describe())

    # ---------------------------------------------------------
    # Task 2: Data Cleaning
    # ---------------------------------------------------------
    def clean_data(self):
        self.df["Date"] = pd.to_datetime(self.df["Date"])
        self.df["Temperature"] = self.df["Temperature"].fillna(self.df["Temperature"].mean())
        self.df["Rainfall"] = self.df["Rainfall"].fillna(0)
        self.df["Humidity"] = self.df["Humidity"].fillna(self.df["Humidity"].mean())

        self.df = self.df.set_index("Date")
        print("\n----- CLEANED DATA -----")
        print(self.df.head())

    # ---------------------------------------------------------
    # Task 3: Statistical Analysis (NumPy)
    # ---------------------------------------------------------
    def compute_statistics(self):
        print("\n----- NUMPY STATISTICS -----")
        temp = self.df["Temperature"].values
        rain = self.df["Rainfall"].values
        hum = self.df["Humidity"].values

        print("Mean Temp:", np.mean(temp))
        print("Min Temp:", np.min(temp))
        print("Max Temp:", np.max(temp))
        print("Std Temp:", np.std(temp))
        print("Total Rainfall:", np.sum(rain))
        print("Mean Humidity:", np.mean(hum))

        # Monthly and yearly statistics using resample
        self.monthly_stats = self.df.resample("M").mean()
        self.yearly_stats = self.df.resample("Y").mean()

    # ---------------------------------------------------------
    # Task 4: Required Plots
    # ---------------------------------------------------------
    def generate_plots(self):

        # 1. Line chart – Daily temperature
        plt.figure(figsize=(8,4))
        plt.plot(self.df.index, self.df["Temperature"], marker="o")
        plt.title("Daily Temperature Trend")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/temperature_line.png")
        plt.close()

        # 2. Bar chart – Monthly rainfall
        monthly_rain = self.df["Rainfall"].resample("M").sum()
        plt.figure(figsize=(8,4))
        plt.bar(monthly_rain.index.strftime("%Y-%m"), monthly_rain.values)
        plt.title("Monthly Rainfall Totals")
        plt.xlabel("Month")
        plt.ylabel("Rainfall (mm)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/rainfall_bar.png")
        plt.close()

        # 3. Scatter plot – Humidity vs Temperature
        plt.figure(figsize=(6,4))
        plt.scatter(self.df["Temperature"], self.df["Humidity"])
        plt.title("Humidity vs Temperature")
        plt.xlabel("Temperature")
        plt.ylabel("Humidity")
        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/humidity_temperature_scatter.png")
        plt.close()

        # 4. Combined Plot – Temp + Rainfall
        fig, axes = plt.subplots(2, 1, figsize=(8,6))

        axes[0].plot(self.df.index, self.df["Temperature"])
        axes[0].set_title("Daily Temperature Trend")

        axes[1].bar(self.df.index, self.df["Rainfall"])
        axes[1].set_title("Daily Rainfall")

        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/combined_plot.png")
        plt.close()

        print("[+] All required plots generated & saved!")

    # ---------------------------------------------------------
    # Task 5: Grouping & Aggregation
    # ---------------------------------------------------------
    def grouping(self):
        self.df["Month"] = self.df.index.month_name()

        # Season mapping
        def find_season(m):
            return ("Winter" if m in ["December","January","February"]
                    else "Summer" if m in ["March","April","May"]
                    else "Monsoon" if m in ["June","July","August","September"]
                    else "Post-Monsoon")

        self.df["Season"] = self.df.index.month_name().map(find_season)

        print("\n----- GROUP BY MONTH -----")
        print(self.df.groupby("Month")[["Temperature","Rainfall","Humidity"]].mean())

        print("\n----- GROUP BY SEASON -----")
        print(self.df.groupby("Season")[["Temperature","Rainfall","Humidity"]].mean())

    # ---------------------------------------------------------
    # Task 6: Exporting & Storytelling (Markdown Report)
    # ---------------------------------------------------------
    def export_cleaned_csv(self):
        self.df.to_csv(self.cleaned_csv)
        print(f"[+] Cleaned CSV saved as: {self.cleaned_csv}")

    def generate_report(self):
        report_path = f"{self.output_dir}/weather_report.md"

        hottest_season = self.df.groupby("Season")["Temperature"].mean().idxmax()
        wettest_month = self.df.groupby("Month")["Rainfall"].sum().idxmax()

        content = f"""
# Weather Data Storytelling Report  
(Generated Automatically)

## Overview
This report describes key insights from the weather dataset, including temperature, rainfall, and humidity patterns.

## Key Findings
- **Hottest Season:** {hottest_season}
- **Wettest Month:** {wettest_month}
- **Average Temperature:** {self.df['Temperature'].mean():.2f}
- **Total Rainfall:** {self.df['Rainfall'].sum():.2f} mm
- **Average Humidity:** {self.df['Humidity'].mean():.2f}%

## Visualizations
Generated PNG files:
- temperature_line.png  
- rainfall_bar.png  
- humidity_temperature_scatter.png  
- combined_plot.png  

## Conclusion
Weather shows clear seasonal trends. Understanding these trends helps in planning activities, agriculture, and sustainability efforts.
"""

        with open(report_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"[+] Report generated: {report_path}")

    # ---------------------------------------------------------
    # Run All Tasks
    # ---------------------------------------------------------
    def run_all(self):
        print("\n=== Weather Data Visualizer (FULL PROJECT) ===\n")
        self.create_sample_csv()
        self.load_data()
        self.clean_data()
        self.compute_statistics()
        self.generate_plots()
        self.grouping()
        self.export_cleaned_csv()
        self.generate_report()
        print("\n=== ALL TASKS COMPLETED SUCCESSFULLY ===")


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    app = WeatherDataVisualizer()
    app.run_all()
