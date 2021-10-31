import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.figure_factory as ff
import base64

from app import app 

# Data Preprocessing
data = pd.read_csv('supermarket_sales.csv')
data_female = data[data['Gender'] == 'Female']
data_male = data[data['Gender'] == 'Male']
fig = go.Figure()

# Detecting outliers
female_gross = data_female['gross income']
male_gross = data_male['gross income']
female_out = female_gross.quantile(0.75)+1.5*(female_gross.quantile(0.75)-female_gross.quantile(0.25))
male_out = male_gross.quantile(0.75)+1.5*(male_gross.quantile(0.75)-male_gross.quantile(0.25))

# Removing outliers
female_filt = data_female[data_female['gross income'] <= 48.42700000000001]
male_filt = data_male[data_male['gross income'] <= 45.96025]

# Hypothesis test
female = female_filt['gross income']
male = male_filt['gross income']
t,p = stats.ttest_ind(female, male, equal_var=False)
pop = np.random.normal(female.mean(), male.std(), 100000)
ci = stats.norm.interval(0.90, female.mean(), male.std())
hist_data = [pop]
group_labels = ['distplot']

# Making distribution plot
fig = ff.create_distplot(hist_data, group_labels, bin_size=.2)
fig.add_vline(pop.mean(), line_width=2, line_dash="dash", line_color="rgb(237, 173, 8)", annotation_text="mean", annotation_position="top right")

fig.add_vline(ci[0], line_width=2, line_dash="dash", line_color="rgb(204, 80, 62)")
fig.add_vline(ci[1], line_width=2, line_dash="dash", line_color="rgb(204, 80, 62)", annotation_text="CV", annotation_position="top right")

fig.add_vline(pop.mean() + t*pop.std(), line_width=2, line_dash="dash", line_color="rgb(148, 52, 110)", annotation_text="p-value", annotation_position="top left")
fig.add_vline(pop.mean() - t*pop.std(), line_width=2, line_dash="dash", line_color="rgb(148, 52, 110)")

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Hypothesis Testing",
                className="text-center"),
                className="mb-2 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Based on the data that is required, there is quite a difference between the amount of products the female customers have bought (2,869) and the male customers have bought (2,641). '),
                className="mb-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='In this hypothesis testing, we are going to find out whether the difference in amount of products bought causes a significant difference between the gross income '
                'the female and male customers contribute to the supermarket'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='graph-one',
                    animate = True,
                    figure = px.bar(data.groupby(['Gender'])['gross income'].sum().reset_index(), x = 'Gender', y="gross income", color = 'Gender', color_discrete_sequence=px.colors.qualitative.Prism)
                ),
                width=6, className="mb-4"
            ),
            dbc.Col(
                dcc.Graph(
                    id = 'graph-two',
                    animate = True,
                    figure = px.box(data.reset_index(), x = 'Gender', y="gross income", color = 'Gender', color_discrete_sequence=px.colors.qualitative.Prism)
                ),
                width=6, className="mb-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Because there are a few outliers, they have to be removed before the hypothesis testing'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H3(children='The Hyphotheses'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='The method that will be used is two-tailed Independent two sample test, '
                'with a critical value of 5%. The null and alternate hypotheses are as follows:'),
                className="mb-1"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='H\u2080: There is no significant difference between the amount of gross income the female and male customers contribute to the supermarket')
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='H\u2081: There is a significant difference between the amount of gross income the female and male customers contribute to the supermarket'),
                className="mb-3"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='The hypotheses can also be written as:'),
                className="mb-1"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='H\u2080: U(Female) = U(Male)')
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='H\u2081: U(Female) != U(Male)')
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='graph-three',
                    animate = True,
                    figure = fig
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H3(children='The Conclusion'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='These are the values that are obtained from the indepentent t-test: '
                'female sample mean of 15.624, male sample mean of 14.594, t-stat value of 1.428, and p-value of 0.153.'),
                className="mb-1"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='From the results, the obtained p-value (0.153) is greater than the critical value (0.05). '
                'This means, the null hypothesis (H\u2080) is accepted because there is not enough evidence to reject it. '),
                className="mb-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='Meaning, even though the female customers buy more products than the male customers, '
                'there is no significant difference between the amount of gross income the female and male customers contribute to the supermarket.'),
                className="mb-5"
            )
        ])
    ])
])