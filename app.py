from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

import pandas as pd

#to index the rows & columns to make them easier to call
#listOfCountryNumbers = []

#for loop to create listOfCountryNumbers
#for i in range(200):
    #listOfCountryNumbers.append("country"+str(i))

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
#print(df[0][0])
print(normalizeData(df))
print(df)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        df['year'].min(),
        df['year'].max(),
        step=None,
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        id='year-slider'
    )
])


@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig


if __name__ == '__main__':
    app.run(debug=True)

#read the file before it is separated based on the commas
def normalizeData(file):
    print(file.loc[:,"year"])
    df['year'] = df['year'].astype(float)
    file.loc[:,"year"] = file.loc[:,"year"]/100.0
    #for i in range(0, len(yearColumn)):
        #yearColumn[i] = yearColumn[i] / 100