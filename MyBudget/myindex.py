from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


from app import *
from components import sidebar, extratos, dashboards




# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[               #layout principal do dash
    dbc.Row([                                       #definidas as linhas
        dbc.Col([                                   #definidas as colunas
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2,),                                   #de 10 partes divididas do dash, 2 serão pra esse sidebar (1/6 da tela)
        dbc.Col([
            content
        ], md=10,)
    ])
    


], fluid=True,)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')]) #Output('parte fixa', 'parte que será alterada (no caso conteúdo)')
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout

    if pathname == '/extratos':
        return extratos.layout 


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)