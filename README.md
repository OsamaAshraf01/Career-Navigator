# Career Navigator
Career Navigator is a user-friendly application designed to empower individuals in their career exploration. It acts as a comprehensive guide, leveraging data analysis and visualization techniques to provide valuable insights into the job market.

## Installation

### Install the required packages
```bash
pip install -r requirements.txt
```

### Setup the environment variables
```bash
cp .env.example .env
```
Then, set your environment variables in the `.env` file. like `MAPBOX_ACCESS_TOKEN` and `LOCATIONIQ_API_KEY` values.

### Install Datasets
Download the required datasets from this [direct link](https://www.kaggle.com/datasets/asaniczka/1-3m-linkedin-jobs-and-skills-2024/download?datasetVersionNumber=2)

After downloading the zip file, exctract `job_skills.csv` and `linkedin_job_postings.csv` files and put them in `src/data`directory.
