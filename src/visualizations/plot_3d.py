import pandas as pd
import plotly.express as px


def make_3D_plot(jobs: pd.DataFrame):
    jobs.loc[:, 'first_seen'] = pd.to_datetime(jobs['first_seen'])
    aggregated_df = jobs.groupby(['first_seen', 'search_city']).size().reset_index(name='post_count')
    plot_3d = px.scatter_3d(aggregated_df, x='first_seen', y='search_city', z='post_count', labels={'post_count': 'Postings Count', 'first_seen': 'Date', 'search_city':'City'})
    # plot_3d.update_traces(mode='lines+markers')
    # plot_3d.update_layout(hovermode='x unified')  
    # plot_3d = go.Figure(data=[go.scatter3d(z=aggregated_df.values)])
    # plot_3d.update_layout(title='', autosize=True)
    return plot_3d
