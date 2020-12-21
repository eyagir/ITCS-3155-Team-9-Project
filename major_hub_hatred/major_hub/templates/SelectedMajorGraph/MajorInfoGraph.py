import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/MajorData.csv', index_col="Major")

rank = df["Rank"]

np_df = df.to_numpy()

career = "ZOOLOGY"
careerRank = rank.loc[career]
careerIndex = careerRank - 1

xLabels = ['Employed', 'Full Time', 'Part Time', 'Full Time (Year Round)', 'Unemployed']

employed = np_df[careerIndex][9]
fullTime = np_df[careerIndex][10]
partTime = np_df[careerIndex][11]
fullTimeYR = np_df[careerIndex][12]
unemployed = np_df[careerIndex][13]

yValues = [employed, fullTime, partTime, fullTimeYR, unemployed]

layout = go.Layout(title=career,
                   xaxis_title="Data", yaxis_title="", barmode='stack')

fig = go.Figure([go.Bar(x=xLabels, y=yValues)], layout=layout)
pyo.plot(fig, filename="MajorInfoGraph.html")