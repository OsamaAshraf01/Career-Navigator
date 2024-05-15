from dash import Dash, Input, Output, State, callback
from helpers.variables import APP_LAYOUT
from functions import get_jobs, extract_graph_elements
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
# matched_jobs=[];titles_nodes=[];skills_nodes=[];edges=[]



# First Callback: When click submit button ---> Show opotions div
@callback(
    [Output('skills-checklist', 'options'),
     Output('options-div', 'style')],
    Input('search-button', 'n_clicks'),
    State('entered-job-title', 'value'),
    prevent_initial_call=True
)
def show_options_div(n_clicks, job_title:str):
    global matched_jobs, titles_nodes, skills_nodes, edges, betweenness, bar_graph
    # ? Get Matched Jobs
    matched_jobs, links = get_jobs(job_title)

    # ? Extract Graph Elements
    titles_nodes, skills_nodes, edges = extract_graph_elements(links)

    bar_graph, betweenness = make_bar_graph(titles_nodes, edges)
    skills = list(betweenness.keys())[::-1]
    return skills, {'display':'flex'}

# Second Callback: When options div is visible ---> Navigate to it
# @callback(
#     Output('url', 'pathname'),
#     Input('options-div', 'style'),
#     State('search-button', 'n_clicks'),
#     prevent_inital_call = True
# )
# def navigate_to_options_section(style, n_clicks):
#     if n_clicks == 0:
#         return '/'
#     return '/#options-div'


# Third Callback: When click continue button  ---> Generate all required graphs
@callback(
     Output('skills-network', 'elements'),  # What will be changed
     Output('skills-graph', 'figure'),
     Output('next-skill', 'children'),
     Output('related-courses', 'children'),
     Output('heatmap', 'figure'),
     Output('3D-graph', 'figure'),
     Output('anaysis-div', 'style'),
     Input('continue-button', 'n_clicks'),
     State('skills-checklist', 'value'),
     State('entered-job-title', 'value'),
    prevent_initial_call=True
)
def update_graphs(n_clicks, excluded_skills, job_title: str):
    # ! Network Section
    Graph_elements = generate_network(titles_nodes, skills_nodes, edges)

    # ! Bar Graph Section
    skills_bar = bar_graph

    # ! Insights Secion
    global betweenness
    betweenness_copy = betweenness.copy()  # TO save the original betweennesss
    for skill in excluded_skills:
        betweenness_copy = betweenness_copy.drop(skill) # Remove known skills

    related_courses, highest_skill = conclude_insights(betweenness_copy)

    # ! Jobs Destribution Section
    heatmap = generate_heatmap(matched_jobs)

    # ! 3D Plotting Section
    plot_3d = make_3D_plot(matched_jobs)

    return Graph_elements, skills_bar, highest_skill, related_courses, heatmap, plot_3d, {'display': 'flex', 'flex-direction':'column'}  #


# Fourth Callback: When graphs div is visible navigate to it

if __name__ == '__main__':
    app.run(debug=True)
