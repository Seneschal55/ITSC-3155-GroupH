import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../Datasets/Weather2014-15.csv')


df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

df['Average Max Temperature'] = df['average_max_temp']

new_df = df.groupby(['date']).agg({'actual_mean_temp': 'sum', 'average_min_temp': 'sum', 'average_max_temp': 'sum'}).reset_index()

# Preparing data
data = [ go.Scatter(x=new_df['average_min_temp'], y=new_df['average_max_temp'], text=new_df['date'], mode='markers',
marker=dict(size=new_df['actual_mean_temp'],color=new_df['actual_mean_temp'], showscale=True))]

# Preparing layout
layout = go.Layout(title='Average Monthly Temperature',
xaxis_title="Average Minimum Temperature",
yaxis_title="Average Maximum Temperature", hovermode='closest')

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubblechartWeather.html')
