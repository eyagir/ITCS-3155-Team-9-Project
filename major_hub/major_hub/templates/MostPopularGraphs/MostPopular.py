import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/MajorData.csv')

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

new_df = df.groupby(['Major']).agg(
    {'Total': 'sum', 'Men': 'sum', 'Women': 'sum'}).reset_index()

new_df = new_df.sort_values(by=['Total'], ascending=[False]).reset_index()

trace1 = go.Bar(x=new_df['Major'], y=new_df['Men'], name='Men', marker={'color': '#47FCFF'})
trace2 = go.Bar(x=new_df['Major'], y=new_df['Women'], name='Women', marker={'color': '#FF78F8'})
data = [trace1, trace2]

layout = go.Layout(title='Most Popular Majors',
                   xaxis_title=" ", yaxis_title="Total", barmode='stack')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='MostPopular.html')
