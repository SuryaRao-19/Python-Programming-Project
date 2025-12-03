# CAPSTONE PROJECT REPORT
## Campus Energy-Use Dashboard

### Student Name: Surya Rao  
### Course: B.Tech CSE – AIML  
### Lab Assignment 5 – Final Submission

---

# 1. Objective
The goal of this project is to analyze campus energy consumption data using:
- Python programming
- Data ingestion and cleaning
- OOP concepts
- Aggregation (daily & weekly)
- Visualization using Matplotlib
- File exports and summary reporting

---

# 2. Dataset Description
The dataset contains:
- Timestamp (date/time of the reading)
- kWh (energy consumed)
- Building name (Library, Admin)

Sample CSV data is auto-generated inside the `data/` folder.

---

# 3. Methodology

### Step 1 – CSV Ingestion  
The program reads all CSV files inside `data/` and validates timestamp format.

### Step 2 – OOP Model  
The system uses two classes:
- **Building** – stores readings
- **BuildingManager** – manages all buildings and generates a report

### Step 3 – Aggregation  
Using pandas:
- Daily totals  
- Weekly totals  
- Building summary (min, max, avg, total)

### Step 4 – Visualization  
A simple line graph compares buildings' consumption over time.

### Step 5 – Export  
The system exports:
- Cleaned data  
- Daily totals  
- Weekly totals  
- Summary text report  
- Dashboard plot  

---

# 4. Results

### • Total Campus Consumption  
Combined kWh of Library + Admin buildings.

### • Highest Consuming Building  
Displayed in summary.txt.

### • Peak Usage  
Highest single energy reading with timestamp.

### • Dashboard  
A PNG image under `output/dashboard.png`.

---

# 5. Conclusion
This project successfully demonstrates:
- Python data processing
- Use of OOP
- Data visualization
- Aggregation and reporting
- File handling in real-world scenarios

The Campus Energy Dashboard can help institutions monitor energy trends efficiently.

---

# END OF REPORT
