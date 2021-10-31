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
city_options = data['City'].unique()

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Sales overview of each city"),
                className="mb-2 mt-5"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising each city\'s top-selling product lines, along with the branch\'s busiest days and hours'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_city',
                    options=[
                       {'label': city, 'value': city} for city in city_options
                    ],
                    value='Mandalay',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='first-graph'
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='second-graph'
                ),
                className="mb-4"
            )
        ]),

    html.Hr(),

        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='third-graph'
                ),
                width=7, className="mb-3"
            ),
            dbc.Col(
                dcc.Graph(
                    id='fourth-graph'
                ),
                width=5, className="mb-8"
            )
        ])
    ])
])

@app.callback(
    Output('first-graph', 'figure'),
    Output('second-graph', 'figure'),
    Output('third-graph', 'figure'),
    Output('fourth-graph', 'figure'),
    Input('selected_city', 'value')
)
def city_sales(city):
    fig = px.bar(data[data['City'] == city].groupby(['Product line'])['Quantity'].sum().reset_index(), x='Product line', y='Quantity', 
    color = 'Product line', title=f'Amount of product sales in {city}', color_discrete_sequence=px.colors.qualitative.Prism)

    fig1 = px.bar(data[data['City'] == city].groupby(['Product line'])['Total'].sum().reset_index(), x='Product line', y='Total', 
    color = 'Product line', title=f'Total money spent on each product line in {city}', color_discrete_sequence=px.colors.qualitative.Prism)

    fig2 = px.bar(data[data['City'] == city].groupby(['Day'])['Quantity'].sum().reset_index(), x='Day', y='Quantity', 
    color = 'Day', title=f'Sales in {city} per day of the month', color_continuous_scale = 'viridis')

    fig3 = px.bar(data[data['City'] == city].groupby(['Hour'])['Quantity'].sum().reset_index(), x='Hour', y='Quantity', 
    color = 'Hour', title=f'Sales in {city} per hour', color_continuous_scale = 'viridis')
    return [fig, fig1, fig2, fig3]