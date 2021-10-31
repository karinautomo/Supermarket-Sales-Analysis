import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import home, branch, hypothesis_testing, sales

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Sales Overview", header=True),
                dbc.DropdownMenuItem("Branch", href="/apps/branch"),
                dbc.DropdownMenuItem("Product line", href="/apps/sales"),
            ],
            nav=True,
            in_navbar=True,
            label="Visualizations",
        ),
            dbc.NavItem(dbc.NavLink("Hypothesis", href='/apps/hypothesis_testing')),
        ],
        brand="Supermarket Sales Dashboard",
        brand_href="/apps/home",
        color="dark",
        dark=True,
        sticky='top' #biar tetep keliatan di atas pas di scroll
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])


@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')])
def display_page(pathname):
    if pathname == '/apps/branch':
        return branch.layout
    elif pathname == '/apps/sales':
        return sales.layout
    elif pathname == '/apps/hypothesis_testing':
        return hypothesis_testing.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=True)