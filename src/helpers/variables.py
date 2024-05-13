import dash_cytoscape as cyto
from dash import dcc, html
from graph import default_graph
from helpers.config import get_settings
app_settings = get_settings()

network_stylesheet = [
    {
        'selector': '.parent',
        'style': {
            'background-color': '#1e293b',
        }
    },
    {
        'selector': 'node',
        'style': {
            'content': 'data(label)',
            'text-halign': 'center',
            'text-valign': 'center',
            "text-wrap": "wrap",
            "text-max-width": 80
        }
    },
    {
        'selector': 'edge',
        'style': {
            'background-color': '#CC1684'
        }
    },
    {
        'selector': '.title',
        'style': {
            'background-color': '#84CC16',
            'width': '200px',
            'height': '200px'
        }
    },
    {
        'selector': '.skill',
        'style': {
            'background-color': '#CC1684',
            'width': '100px',
            'height': '100px'
        }
    }
]

APP_LAYOUT = html.Div([
    html.H1(app_settings.APP_NAME),
    html.P("Get Ready for Your Next Job"),
    html.Div([
        dcc.Input(id='entered-job-title', type='text', placeholder='Enter a job title'),
        html.Button('Search', id='search-button', n_clicks=0, className='main-button'),
    ], className="inputs"),
    html.Div([
        html.H2("Check Known Skills:"), # should be added after clicking search
        html.Div(
            dcc.Checklist(
                id='skills-checklist',
                options = [],
                value = []  # Selected Items
            )
        ),
        html.Button('Continue', id='continue-button', n_clicks=0, className='main-button'),
    ], id='options-div', style={'display':'none'}),
    html.Div([
        html.Section([
            html.H2("Jobs-Skills Network"),
            cyto.Cytoscape(
                id='skills-network',
                elements=[],
                stylesheet=network_stylesheet,
                style={
                    'width': '100%',
                    'height': '1000px', },
                layout={
                    'name': 'concentric',
                    'fit' : True
                },
            ),
        ], className="section-1"),

        html.Section([
            html.H2("Highly Demanded Skills"),
            html.Div([
                dcc.Graph(
                    id='skills-graph',
                    className='skills-graph',
                    style={'width': '80%'},
                    figure=default_graph
                )
            ], style={'display': 'flex', 'justifyContent': 'center'})
        ], className="section-2"),

        html.Section([
            html.H2("Insights"),
            html.Div(id='next-skill'),
            html.Div(id='related-courses'),
        ], className="section-1"),

        html.Section([
            html.H2("Jobs Distribution"),
            html.Div([
                dcc.Graph(
                    id='heatmap',
                    style={'width': '80%'},
                )
            ], style={'display': 'flex', 'justifyContent': 'center'}),
        ], className="section-2"),

        html.Section([
            html.H2("Salary Distribution"),
            html.Div([
                dcc.Graph(
                    id='3D-graph',
                    style={'width': '50%'},
                ),
            ], style={'display': 'flex', 'justifyContent': 'center'}),
        ], className="section-1"),

        # html.Section([
        #     html.H2("Getting Hired"),
        #     html.P("Matched Jobs"),
        #     html.P("Automatic Apply"),
        # ], className="section-2"),
    ], id='anaysis-div', style={'display': 'none'})
], className='main-div')
