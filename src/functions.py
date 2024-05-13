import pandas as pd
from helpers.config import get_settings

app_settings = get_settings()
postings_path = app_settings.POSTINGS_PATH
skills_path = app_settings.SKILLS_PATH

postings = pd.read_csv(postings_path)
skills = pd.read_csv(skills_path)


def get_jobs(query: str) -> tuple[pd.DataFrame, pd.Series]:
    query = query.lower()

    postings['job_title'] = postings['job_title'].str.lower()
    matched_jobs = postings.loc[postings['job_title'].str.contains(query)]

    print(f"Matched Jobs: {len(matched_jobs)}")
    return matched_jobs, matched_jobs['job_link']


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


def extract_graph_elements(links: pd.Series) -> tuple[list, list, list]:
    edges = []
    skills_nodes = []
    titles_nodes = []

    jobs_count = app_settings.RESULT_JOBS_COUNT
    for i in range(jobs_count):
        link = links.iloc[i]
        title = get_job_title(link)
        job_skills = get_skills(link)

        edges += [(title, skill.title()) for skill in job_skills]
        skills_nodes += [skill.title() for skill in job_skills]
        titles_nodes += [title]

    return titles_nodes, skills_nodes, edges


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
