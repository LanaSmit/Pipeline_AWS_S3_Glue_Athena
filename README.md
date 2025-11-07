# AWS ETL Pipeline: Spotify Dataset

An **ETL pipeline** built on **AWS** that ingests, transforms, and analyzes Spotify streaming data.  

The project utilizes:  
- **Amazon S3** for centralized data storage  
- **AWS Glue** for automated ETL orchestration and transformation  
- **Amazon Athena** for querying and analytics  

---

## Pipeline Workflow

1. **Data Ingestion:**  
   Raw Spotify data is extracted from the Spotify API and stored in an Amazon S3 bucket.  

2. **ETL Automation:**  
   AWS Glue automatically extracts, transforms, and loads the data into a structured format suitable for analysis.  

3. **Data Analysis:**  
   Amazon Athena queries the transformed dataset to explore artist popularity, track performance, and streaming trends.  
