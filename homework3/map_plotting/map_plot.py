import plotly.express as px
import pandas as pd

def display_on_map(file_name):
    # df = px.data.gapminder()

    df = pd.read_csv (file_name)
    df = df.sort_values(by=['Date'], ascending=True, na_position='first')

    fig = px.scatter_geo(df, lat="Latitude", lon="Longitude", color="Label",
                        hover_name="Label", size="Count",
                        animation_frame="Date",
                        projection="natural earth",
                        fitbounds=False)
                        # fitbounds="locations"
                        # scope="europe"

    fig.show()