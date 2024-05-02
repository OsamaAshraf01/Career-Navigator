import pandas as pd
from decorators import *
from serpapi import GoogleSearch        # To search for jobs
from llama_3 import prompt_llama        # To chat with LLAMA 3 Model

job_type = {
    "Working From Home" : "1",
    "On Sight" : None
}

def GET_jobs(query:str, type:str = "On Sight") -> pd.DataFrame:
    params = {
        "engine" : "google_jobs",
        "q" : query,
        "ltype" : job_type[type],
        "api_key" : "c46787c1fe731e96ceb2cabf7362fd857ed16a820c03d9e85d698541014835f6"
    }


    results = pd.DataFrame(GoogleSearch(params).get_dict()["jobs_results"])
    
    return pd.DataFrame(results)