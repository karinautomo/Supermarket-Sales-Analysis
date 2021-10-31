import plotly.express as px
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app 

# Data Preprocessing
data = pd.read_csv('supermarket_sales.csv')
product_line = pd.DataFrame(data, columns = ['City', 'Gender', 'Customer type'])

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Products sales at a glance"),
                className="mb-2 mt-5"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising sales trends based on different categories'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_category',
                    options=[
                       {'label': category, 'value': category} for category in product_line.columns.unique()
                    ],
                    value='City',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph'
                ),
                className="mb-3"
            )
        ]),

    html.Hr(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='secondary-graph'
                ),
                className="mb-8"
            )
        ])
    ])
])

@app.callback(
    Output('main-graph', 'figure'),
    Output('secondary-graph', 'figure'),
    Input('selected_category', 'value')
)
def product_sales(category):
    fig = px.bar(data.groupby([category])['Quantity'].sum().reset_index(), x = category, y = 'Quantity', 
    color = category, title = f'Overall sales based on {category}',
    color_discrete_sequence = px.colors.qualitative.Prism)

    fig1 = px.bar(data.groupby(['Product line', category])['Quantity'].sum().reset_index(), x = 'Product line', y = 'Quantity', 
    color = category, title = f'Sales per product line based on {category}', barmode = 'group',
    color_discrete_sequence = px.colors.qualitative.Prism)
    return [fig, fig1]