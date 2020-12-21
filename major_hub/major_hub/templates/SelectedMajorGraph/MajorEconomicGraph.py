import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


def major_economic_change(major):
    # Load CSV file from Datasets folder
    df = pd.read_csv('major_hub/templates/Datasets/MajorData.csv', index_col="Major")

    rank = df["Rank"]

    np_df = df.to_numpy()

    career = major
    careerRank = rank.loc[career]
    careerIndex = careerRank - 1

    xLabels = ['P25th', 'Median', 'P75th']

    P25th = np_df[careerIndex][15]
    Median = np_df[careerIndex][14]
    P75th = np_df[careerIndex][16]

    yValues = [P25th, Median, P75th]

    layout = go.Layout(title="",
                       xaxis_title="Economic Data", yaxis_title="", barmode='stack')

    fig = go.Figure([go.Bar(x=xLabels, y=yValues)], layout=layout)
    pyo.plot(fig, filename="major_hub/templates/SelectedMajorGraph/MajorEconomicGraph.html")
