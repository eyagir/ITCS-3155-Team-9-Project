import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/MajorData.csv')

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

new_df = df.groupby(['Major'])['Rank'].sum().reset_index()

new_df = new_df.sort_values(by=['Rank'], ascending=[True])

data = [go.Bar(x=new_df['Major'], y=new_df['Rank'])]

layout = go.Layout(title='Majors ordered through Rank', xaxis_title="",
                   yaxis_title="Rankings")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='MajorIndex.html')
