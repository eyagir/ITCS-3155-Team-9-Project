import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


def major_work_change(major):
    # Load CSV file from Datasets folder
    df = pd.read_csv('major_hub/templates/Datasets/MajorData.csv', index_col="Major")

    rank = df["Rank"]

    np_df = df.to_numpy()

    career = major
    careerRank = rank.loc[career]
    careerIndex = careerRank - 1

    xLabels = ['Employed', 'Full Time', 'Part Time', 'Full Time (Year Round)', 'Unemployed']

    employed = np_df[careerIndex][8]
    fullTime = np_df[careerIndex][9]
    partTime = np_df[careerIndex][10]
    fullTimeYR = np_df[careerIndex][11]
    unemployed = np_df[careerIndex][12]

    yValues = [employed, fullTime, partTime, fullTimeYR, unemployed]

    layout = go.Layout(title=career,
                       xaxis_title="Workforce Data", yaxis_title="", barmode='stack')

    fig = go.Figure([go.Bar(x=xLabels, y=yValues)], layout=layout)
    pyo.plot(fig, filename="major_hub/templates/SelectedMajorGraph/MajorWorkGraph.html")
