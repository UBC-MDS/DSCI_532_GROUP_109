import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import altair as alt
from make_plot import make_titanic_plot, make_class_plot, make_deck_plot, make_deck_legend

app = dash.Dash(__name__, assets_folder='assets', external_stylesheets=[dbc.themes.CERULEAN])
server = app.server

app.title = 'Fate of Titanic Passengers by Location on Ship'

jumbotron = dbc.Jumbotron(
    [
        dbc.Container(
            [
                html.Img(src='https://www.thoughtco.com/thmb/JAh1c6CpoPyyuPo3H-kEi0ZocZ0=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/the-titanic-HK4695-001-57d8674f3df78c58339ac2fd.jpg', 
                      width='500px'),
                html.H1("Fate of Titanic Passengers by Location on Ship", className="display-3"),
            ],
            fluid=True,
        )
    ],
    fluid=True,
)

row1 = dbc.Row(
                [dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot',
                        height='550',
                        width='1600',
                        style={'border-width': '2px'},
                        ), width=10),

                dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot1',
                        height='550',
                        width='300',
                        style={'border-width': '2px'},
                        ), width=2)]
            )
            
row2 = dbc.Row(
                [dbc.Col(        
                    dcc.Dropdown(
                        id='dd-chart',
                        options=[
                            {'label': 'Deck A', 'value': 'A'},
                            {'label': 'Deck B', 'value': 'B'}
                        ],
                        value='B', style=dict(width='45%')
                        ), width='6'
                    )])

row3 = dbc.Row(
                [dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot2',
                        height='550',
                        width='1600',
                        style={'border-width': '0px'},
                        srcDoc = make_class_plot().to_html()
                        ), width=6),

                dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot3',
                        height='550',
                        width='1600',
                        style={'border-width': '0px'},
                        srcDoc = make_deck_plot().to_html()
                        ), width=6)]) 

footer = dbc.Container([
            dbc.Row(
                dbc.Col(
                    html.P('This Dash app was made Rob Blumberg, George Thio and Trevor Kwan')
                )
            )
         ]
)

app.layout = html.Div([jumbotron,
                       row1,
                       row2,
                       row3, 
                       footer])

@app.callback(
    dash.dependencies.Output('plot', 'srcDoc'),
    [dash.dependencies.Input('dd-chart', 'value')])
def update_plot(deck):
    '''
    Takes in a deck_level and calls make_titanic_plot to update our first figure
    '''
    updated_plot = make_titanic_plot(deck).to_html()
    return updated_plot

@app.callback(
    dash.dependencies.Output('plot1', 'srcDoc'),
    [dash.dependencies.Input('dd-chart', 'value')])
def update_plot_2(deck):
    '''
      Takes in a deck_level and calls make_deck_legend to update our second figure
    '''
    updated_plot_2 = make_deck_legend(deck).to_html()
    return updated_plot_2

if __name__ == '__main__':
    app.run_server(debug=True)
