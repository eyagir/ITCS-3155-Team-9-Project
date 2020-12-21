import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/MajorData.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum
new_df = df.groupby(['Major'])['P75th'].sum().reset_index()

# Sorting values
new_df = new_df.sort_values(by=['P75th'], ascending=[False])

# Preparing data
data = [go.Bar(x=new_df['Major'], y=new_df['P75th'])]

# Preparing layout
layout = go.Layout(title='Highest Pay by 75th Percentile', xaxis_title="",
                   yaxis_title="P75th")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='HighestPay75.html')
