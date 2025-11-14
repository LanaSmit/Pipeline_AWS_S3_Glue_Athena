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
   
# Setup Instructions

## 1. Clone the Repository

Paste this in your terminal:
```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

## 2. Create a Virtual Environment (Optional)

Paste this in your terminal:
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

Paste this in your terminal:
```bash
pip install -r requirements.txt
```

## 4. Set Your Environment Variables

Create a .env file in the project root with:
```bash
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
S3_BUCKET_NAME=your_bucket_name
```

## 5. Run the ETL Script

Paste this into a new file named .env in the project root:
Paste this in your terminal:
```bash
python spotify_etl.py \
  --SPOTIPY_CLIENT_ID $SPOTIPY_CLIENT_ID \
  --SPOTIPY_CLIENT_SECRET $SPOTIPY_CLIENT_SECRET \
  --S3_BUCKET_NAME $S3_BUCKET_NAME
```

## 6. Query Data in Amazon Athena

Create a table pointing to your S3 path, then run:
Paste this in your Athena query editor:
```bash
SELECT track_name, album, popularity
FROM spotify_database.spotify
WHERE popularity > 80
ORDER BY popularity DESC;
```