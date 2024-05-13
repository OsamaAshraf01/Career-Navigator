import pandas as pd
import plotly.express as px
from network import calc_betweenness
from helpers.config import get_settings
app_settings = get_settings()

background_rectangles = [
    dict(
        type="rect",
        xref="x",
        yref="paper",
        x0=0,
        y0=0,
        x1=25,
        y1=1,
        fillcolor="#1d2839",
        opacity=0.3,
        line_width=0,
    ),
    dict(
        type="rect",
        xref="x",
        yref="paper",
        x0=25,
        y0=0,
        x1=50,
        y1=1,
        fillcolor="#1c2636",
        opacity=0.3,
        line_width=0,
    ),
    dict(
        type="rect",
        xref="x",
        yref="paper",
        x0=50,
        y0=0,
        x1=75,
        y1=1,
        fillcolor="#1c2435",
        opacity=0.3,
        line_width=0,
    ),
    dict(
        type="rect",
        xref="x",
        yref="paper",
        x0=75,
        y0=0,
        x1=100,
        y1=1,
        fillcolor="#1a2332",
        opacity=0.3,
        line_width=0,
    ),
]

default_graph = px.bar(pd.DataFrame({'Skill': [], 'Demand': []}), y='Skill', x='Demand', orientation='h',
                       height=500).update_layout(
    xaxis=dict(
        range=[0, 100],  # Rearrange X-axis
        title="",
        tickfont=dict(color='#e2e8f0'),
        showgrid=False,  # Hide x-axis gridlines
        zeroline=True,
    ),
    yaxis=dict(
        # tickmode='array',
        title="",
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        tickfont=dict(color='#e2e8f0')  # Color for the y-axis labels
    ),

    uniformtext_minsize=8,  # Minimum text size
    uniformtext_mode='hide',  # Hide text if it doesn't fit
    paper_bgcolor='rgba(255, 255, 255, 0)',
    plot_bgcolor='rgba(255, 255, 255, 0)',

    # shapes=background_rectangles,
).update_traces(
    marker_color='#9fff0e',
    texttemplate='%{text}%',
    selector=dict(type='bar'),
)

def make_bar_graph(nodes, edges):
    betweenness = calc_betweenness(edges, main_nodes=nodes)  # , exclude=['Data Analysis'])
    df = pd.DataFrame(betweenness).reset_index()
    df.columns = ['Skill', 'Demand']
    graph_height = app_settings.SKILLS_COUNT * 40 # Making a relation between graph size and skills count
    skills_bar = px.bar(df, y='Skill', x='Demand', orientation='h', height=graph_height)  # Creat Bar Graph
    skills_bar.update_layout(
        xaxis=dict(
            range=[0, 100],  # Rearrange X-axis
            title="",
            title_font_color="#e2e8f0",
            tickfont=dict(color='#e2e8f0'),
            showgrid=False,  # Hide x-axis gridlines
            zeroline=True,
        ),
        yaxis=dict(
            tickmode='array',
            tickvals=df['Skill'],
            ticktext=df['Skill'],
            # automargin=True,
            title="",
            title_font_color='#e2e8f0',  # Color for the y-axis title
            tickfont=dict(color='#e2e8f0')  # Color for the y-axis labels
        ),

        uniformtext_minsize=8,  # Minimum text size
        uniformtext_mode='hide',  # Hide text if it doesn't fit
        paper_bgcolor='rgba(255, 255, 255, 0)',
        plot_bgcolor='rgba(255, 255, 255, 0)',

        shapes=background_rectangles,
    )
    # Ensure that the text property is properly assigned
    skills_bar.update_traces(text=df['Demand'], textposition='inside')
    # Use texttemplate to format the text display
    skills_bar.update_traces(
        marker_color='#9fff0e',
        texttemplate='%{text}%',
        selector=dict(type='bar'),
    )

    print("Rendering Skills bar graph  has finished !")


    return skills_bar, betweenness