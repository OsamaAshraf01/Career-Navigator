import pandas as pd
from helpers.config import get_settings

app_settings = get_settings()
postings_path = app_settings.POSTINGS_PATH
skills_path = app_settings.SKILLS_PATH

postings = pd.read_csv(postings_path)
skills = pd.read_csv(skills_path)


def get_jobs(query: str) -> pd.DataFrame:
    query = query.lower()

    postings['job_title'] = postings['job_title'].str.lower()
    matched_jobs = postings.loc[postings['job_title'].str.contains(query)]

    return matched_jobs


def get_skills(link: str) -> list[str]:  # -> tuple[np.ndarray, set]
    skills_list = []
    try:
        skills_list = skills.loc[skills["job_link"] == link, "job_skills"].iloc[0].split(", ")
    except:
        pass

    return skills_list


def get_job_title(link: str) -> str:
    title = ""
    try:
        title = postings.loc[postings["job_link"] == link, "job_title"].iloc[0]
    except:
        pass

    return title


def get_job_loction(link: str) -> str:
    location = ""
    try:
        location = postings.loc[postings["job_link"] == link, "job_location"].iloc[0]
    except:
        pass

    return location



if __name__ == "__main__":
    print(postings)
    print("==============")
    print(skills)
    print("==============")
    # print(summary)

# job_type = {
#     "Working From Home" : "1",
#     "On Sight" : None
# }

# def GET_jobs(query:str) -> pd.DataFrame:
#     params = {
#         "engine" : "google_jobs",
#         "q" : query,
#         "hl" : "en",
#         "no_cache" : True,
#         "api_key" : ""
#     }


#     results = pd.DataFrame(GoogleSearch(params).get_dict()["jobs_results"])

#     return pd.DataFrame(results)