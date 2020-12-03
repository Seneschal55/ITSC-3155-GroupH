import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Preparing data
data = [go.Heatmap(x=df['date'],
                y=df['record_max_temp'],
                z=df['record_max_temp_year'].values.tolist(),
                colorscale='Jet')]
# Preparing layout
layout = go.Layout(title='Record maximum temperature', xaxis_title="Year",
yaxis_title="Record Max Temperature")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename="heatmap.html")