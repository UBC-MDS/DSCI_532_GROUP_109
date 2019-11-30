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
                html.Img(src='https://cdn.wallpapersafari.com/86/85/XesSpa.jpg', 
                      width='820px'),

                html.H2("", style={'color': 'black', 'fontSize': 50}),
        
                html.H1("Fate of Titanic Passengers by Location on Ship", className="display-5"),
            ],
            fluid=False,
        )
    ],
    fluid=True
)

row1 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=1),

                dbc.Col(
                    html.H2("The Titanic was the world’s largest ocean liner just four days into its maiden voyage \
                        on April 12, 1912 when it struck an iceberg and sank into the Atlantic Ocean killing over \
                        1,500 of the estimated 2,224 passengers and crew on board in one of the worst maritime \
                        disasters of all time. This app has been created to support an exploratory research proposal on \
                        the correlation of passenger location with survival rates which may help to improve and democratize \
                        safety in the design of large passenger ships.", style={'color': 'black', 'fontSize': 20}),    
                width=7)
                ])

#Rows for spacing between intro and viz
row2 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 14}),    
                width=6)
                ])
row3 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 14}),    
                width=6)
                ])


row4 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=1),
                dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot',
                        height='420',
                        width='1300',
                        style={'border-width': '0.5px'},
                        ), width=8),

                dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot1',
                        height='420',
                        width='300',
                        style={'border-width': '0px'},
                        ), width=2),
                dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=1)]
            )

row5 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=1),
                dbc.Col(
                    html.H4("Choose a deck to display", style={'color': 'light blue', 'fontSize': 18}),    
                width=5),
                dbc.Col(
                    html.H4("Each deck has passenger cabins of all classes", style={'color': 'light blue', 'fontSize': 18}),
                width=3),
                dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=3)
                ])
            
row6 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=1),
                dbc.Col(    
                    dcc.Dropdown(
                        id='dd-chart',
                        options=[
                            {'label': 'Deck A', 'value': 'A'},
                            {'label': 'Deck B', 'value': 'B'}
                        ],
                        value='B', style=dict(width='45%')
                        ), width='6'
                    )])

#Rows for spacing between dropdown and bar charts
row7 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 14}),    
                width=7)
                ])

row8 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 14}),    
                width=7)
                ])

row9 = dbc.Row(
                [dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=1),

                dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot2',
                        height='550',
                        width='1600',
                        style={'border-width': '0px'},
                        srcDoc = make_class_plot().to_html()
                        ), width=4),

                dbc.Col(
                    html.Iframe(
                        sandbox='allow-scripts',
                        id='plot3',
                        height='550',
                        width='1600',
                        style={'border-width': '0px'},
                        srcDoc = make_deck_plot().to_html()
                        ), width=4),

                dbc.Col(
                    html.H2("", style={'color': 'black', 'fontSize': 20}),    
                width=3)])

footer = dbc.Container([
            dbc.Row(
                dbc.Col(
                    html.P('This Dash app was made Rob Blumberg, Trevor Kwan and George Thio')
                )
            )
         ]
)

app.layout = html.Div([jumbotron,
                       row1,
                       row2,
                       row3,
                       row4,
                       row5, 
                       row6,
                       row7,
                       row8,
                       row9,
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
