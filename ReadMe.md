# 🦠 COVID-19 ETL Pipeline with Airflow, S3, Snowflake & Power BI

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Repo](https://img.shields.io/badge/GitHub-Bilal-2099-orange)

## 🚀 Project Overview
A complete data engineering pipeline that extracts live COVID-19 data through an API, processes and stores it on AWS, and prepares it for analytics in Power BI. The goal was to practice building real-world data pipelines using industry tools like Airflow, S3, and Snowflake.

---

## 📊 Architecture
```
[COVID-19 API]
      ↓
[Airflow DAG] 
      ↓
[S3 Bucket → redfin-airflow-bilal]
      ↓
[Snowflake Data Warehouse]
      ↓
[Power BI Dashboard]
```

---

## 🧰 Tools & Technologies
- **Apache Airflow** – Workflow orchestration and scheduling  
- **AWS S3** – Cloud storage for raw and processed data  
- **Snowflake** – Data warehouse for analytical workloads  
- **Power BI** – Dashboard and visualization  
- **Python** – For extraction, transformation, and automation scripts  

---

## ⚡ How It Works
1. **Extract:** Airflow DAG calls the COVID-19 API to fetch daily data.  
2. **Transform:** The data is cleaned and formatted into a structured CSV.  
3. **Load:** The processed CSV is uploaded to the S3 bucket.  
4. **Visualize:** Data is loaded from S3 into Snowflake and visualized in Power BI.  

---

## 🧑‍💻 Steps to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/Bilal-2099/COVID-19-ETL-Pipeline-Airflow-S3-Snowflake-PowerBI.git
   cd COVID-19-ETL-Pipeline-Airflow-S3-Snowflake-PowerBI
   ```
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
3. Set up AWS and Snowflake credentials in Airflow Connections.  
4. Start Airflow webserver and scheduler.  
5. Trigger the DAG manually or schedule it automatically.  
6. Verify output in your S3 bucket and Snowflake tables.  

---

## 🎯 Project Highlights
- Built a **fully automated ETL pipeline** using modern cloud tools.  
- Applied **best practices in workflow management** with Airflow DAGs.  
- Created a **real dashboard** in Power BI from live COVID-19 data.  
- Designed to simulate **real-world data engineering tasks**.  

---

## 📌 Future Improvements
- Add automated data validation & alerting in Airflow.  
- Include vaccination and regional trend datasets.  
- Implement incremental data loading (delta updates).  
- Automate Power BI dataset refresh.  

---

## 👤 Author
**Bilal Raza**  
Python Developer & Data Engineering Student at **S.M.I.T** under **Sir Qasim Hassan**  
GitHub: [Bilal-2099](https://github.com/Bilal-2099)

---

## 📄 License
MIT License
