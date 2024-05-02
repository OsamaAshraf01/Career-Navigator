from classes import *


#while True:
#    prompt = input("Enter Your Prompt ")
#    answer = prompt_llama(prompt)
#    print(f"LLAMA 3 Answer: {answer}")


jobs = GET_jobs("Senior Data Scientis")

skills = []


for i in range(len(jobs)):
    job = Job(jobs.iloc[i])

    skills += job.key_skills
    print("--->", job.key_skills)
    
print(len(skills))
print(len(set(skills)))
print(set(skills))


# TODO: extract salary
# TODO: skills network graph --> start plotly
# TODO: Graphs Ideas to add to our dashboard
# TODO: How to involve 3D Modeling?
# TODO: What about storing results for more indights?
# TODO: Using other APIs
# TODO: Heat Map