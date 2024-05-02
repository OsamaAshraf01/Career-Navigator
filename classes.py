from functions import *

class Job:
    title:int
    salary:int
    description:str
    key_skills:list
    company:str
    website:str
    qualifications:str
    responsibilities:str
    benefits:str
    location:str
    extensions:str


    def __init__(self, details:pd.Series):
        self.title = details['title']
        self.description = details['description']
        self.compnay = details['company_name']
        self.extensions = details['extensions']
        self.location = details['location']
        self.website = details['via']

        #highlights = details['job_highlights']
        #self.qualifications = highlights[0]['items']
        #self.responsibilities = highlights[1]['items']
        #self.benefits = highlights[2]['items']



        self.salary = self.extract_salary()
        self.key_skills = self.extract_key_skills()





    # Methods
    def extract_salary(self) -> tuple[int,str]:
        return None

    
    @clean
    def extract_key_skills(self) -> list[str]:
        skills = prompt_llama(
            f"""
            This is a job description for a {self.title} position. 

            {self.description}

            What are the 5 to 10 most important skills listed in this job description?
            (respond with key words only separated by commas). each skill should be one or two words, no parantheses, no explanations, no examples.
            replace any abbreviation or ambigious skill name with the standard and famous name of it.
            """
        )

        return skills



    
