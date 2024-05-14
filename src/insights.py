import requests
from bs4 import BeautifulSoup
from dash import html


def get_related_courses(query: str) -> list[str]:
    query = query.split()
    query = '+'.join(query)
    try:
        response = requests.get(f'https://www.coursera.org/search?query={query}')
    except:
        print("Couldn't access Coursera")
        return []
    soup = BeautifulSoup(response.text, 'html5lib')
    a_tags = soup.find_all('a')
    links = []

    for tag in a_tags:
        if tag['href'].startswith('/learn'):
            links.append('https://coursera.org' + tag['href'])

    return links


def conclude_insights(betweenness):
    highest_skill_name = str(betweenness.index[-1])
    
    courses_links = get_related_courses(highest_skill_name)  # TODO! Make sure that it is working properly
    
    highest_skill = html.Div([
        html.H3([
            'Next Skill to Learn: ',
            html.Span(highest_skill_name),
        ]),
    ], className='next-skill')
    related_courses = html.Div([
        html.H3('Related Courses: '),
        html.Ul([
            html.Li(html.A(link_text, href=link_text, target='_blank')) for link_text in courses_links
        ], className='courses-list')
    ], className='related-courses')

    print("Making insights has finished !")

    return related_courses, highest_skill
