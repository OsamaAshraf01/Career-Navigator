from dash import Dash, Input, Output, State, callback
from helpers.variables import APP_LAYOUT
from functions import get_jobs, get_job_title, get_skills
from graph import make_bar_graph
from insights import conclude_insights
from network import generate_network
from maps import generate_heatmap
from plot_3d import make_3D_plot


# TODO: Filter graph from zero Centrality edges
# TODO: Add conclusions from Betweenness (Bar Graph and text)
# TODO: More Betweennees --> more near to center
# TODO: Scale Bars to be more visible


app = Dash(__name__)

app.layout = APP_LAYOUT

@callback(
    [Output('skills-network', 'elements'),  # What will be changed
     Output('skills-graph', 'figure'),
     Output('next-skill', 'children'),
     Output('related-courses', 'children'),
     Output('heatmap', 'figure'),
     Output('3D-graph', 'figure'),
     Output('anaysis-div', 'style'),],
    Input('submit-value', 'n_clicks'),
    State('entered-job-title', 'value'),
    prevent_initial_call=True
)
def update_graphs(n_clicks, job_title: str):
    matched_jobs = get_jobs(job_title)
    print(f"Matched Jobs: {len(matched_jobs)}")
    links = matched_jobs['job_link']
    edges = []
    skills_nodes = []
    titles_nodes = []

    for i in range(100):
        link = links.iloc[i]
        title = get_job_title(link)
        job_skills = get_skills(link)

        edges += [(title, skill.title()) for skill in job_skills]
        skills_nodes += [skill.title() for skill in job_skills]
        titles_nodes += [title]



    #! Network Section
    Graph_elements = generate_network(titles_nodes, skills_nodes, edges)
    
    #! Bar Graph Section
    skills_bar, betweenness = make_bar_graph(titles_nodes, edges)
    
    #! Insights Secion
    related_courses, highest_skill = conclude_insights(betweenness)
    
    #! Jobs Destribution Section
    heatmap = generate_heatmap(matched_jobs)
    
    #! 3D Plotting Section
    plot_3d = make_3D_plot()


    return Graph_elements, skills_bar, highest_skill, related_courses, heatmap, plot_3d, {'display' : 'block'} # 

if __name__ == '__main__':
    app.run(debug=True)
