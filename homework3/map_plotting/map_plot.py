import plotly.express as px
import pandas as pd

def display_on_map(file_name):
    # df = px.data.gapminder()

    # read the csv file into a dataframe for display on the map
    df = pd.read_csv(file_name)
    df = df.sort_values(by=['Date'], ascending=True, na_position='first')

    #  display the data on the map
    fig = px.scatter_geo(df, lat=df["Latitude"], lon=df["Longitude"], color=df["Country"],
                        hover_name=df["Label"], size=df["Count"],
                        animation_frame=df["Date"],
                        projection="natural earth",
                        fitbounds=False)

    fig.show()