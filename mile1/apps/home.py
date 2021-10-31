import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Supermarket Sales Dashboard",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Welcome! My name is Karina Utomo and this is the dashboard of my first milestone project for Hacktiv8 Indonesia\'s Full Time Data Science Program'),
                className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(
                html.H5(children='You can choose whether you want to see the data visualizations for the sales overviews, to see the hypothesis testing, or to access the original dataset'),
                className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='See the sales overview of each branch here',
                        className="text-center"),
                        dbc.Button("Branch",
                        href="/apps/branch",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),

            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='See the sales overview of each product line here',
                        className="text-center"),
                        dbc.Button("Product line",
                        href="/apps/sales",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='See the hypothesis testing here',
                        className="text-center"),
                        dbc.Button("Hypothesis testing",
                        href="/apps/hypothesis_testing",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Get the original dataset here',
                        className="text-center"),
                        dbc.Button("Supermarket sales dataset",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5")
    ])
])