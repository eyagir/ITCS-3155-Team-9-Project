import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo


def related_majors(major):
    # Load CSV file from Datasets folder
    df = pd.read_csv('major_hub/templates/Datasets/MajorData.csv', index_col="Major")
    df2 = pd.read_csv('major_hub/templates/Datasets/MajorData.csv')

    rank = df["Rank"]

    np_df = df.to_numpy()

    career = major
    careerRank = rank.loc[career]
    careerIndex = careerRank - 1


    category = np_df[careerIndex][5]

    print(category)
    related_majors_index= []

    for arr in np_df:
        if arr[5] == category:
            related_majors_index.append(arr[0])


    related_majors_list = []
    names = df.index.values

    for ind in related_majors_index:
        related_majors_list.append(names[ind])


    return related_majors_list


    