# MGS 627 Final Group Project
# GitHub Link: https://github.com/nidhipar/MGS_627_Group_Project

# Imports
import requests
import pandas as pd
import ast
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import os

# Census API key
api_key = os.getenv("API_KEY")

# Function to get demographics data using census API
'''
This function call census data to get demographic data for age groups of
filter: values = state|region
'''
def get_demographics_data(filter):
    base_url = "https://api.census.gov/data/2020/dec/dp?"
    fetched_data = "get=NAME,DP1_0001C,DP1_0006C,DP1_0007C,DP1_0008C,DP1_0009C,DP1_0010C,DP1_0011C,DP1_0012C,DP1_0013C,DP1_0014C,DP1_0015C,STATE"
    url = base_url + fetched_data + "&for="+filter+":*&key="+api_key
    response = requests.get(url)
    response_text = response.text.replace('null','None')
    data_array = ast.literal_eval(response_text)
    columns = data_array[0]
    data_values = data_array[1:]
    response_data = pd.DataFrame(data_values,columns=columns)
    return response_data


# Fetching demographics data
population_data = get_demographics_data('state')
numeric_columns = ['DP1_0001C','DP1_0006C','DP1_0007C','DP1_0008C','DP1_0009C','DP1_0010C','DP1_0011C','DP1_0012C','DP1_0013C','DP1_0014C','DP1_0015C']
population_data[numeric_columns] = population_data[numeric_columns].apply(pd.to_numeric,errors='coerce').fillna(0)

# Mapping age groups with data keys from response
age_data_keys = pd.DataFrame([
            {
                "age_group":"20 to 24 years",
                "data_key":"DP1_0006C"
            },
            {
                "age_group":"25 to 29 years",
                "data_key":"DP1_0007C"
            },
            {
                "age_group":"30 to 34 years",
                "data_key":"DP1_0008C"
            },
            {
                "age_group":"35 to 39 years",
                "data_key":"DP1_0009C"
            },
            {
                "age_group":"40 to 44 years",
                "data_key":"DP1_0010C"
            },
            {
                "age_group":"45 to 49 years",
                "data_key":"DP1_0011C"
            },
            {
                "age_group":"50 to 59 years",
                "data_key":"DP1_0012C"
            },
            {
                "age_group":"55 to 59 years",
                "data_key":"DP1_0013C"
            },
            {
                "age_group":"60 to 64 years",
                "data_key":"DP1_0014C"
            },
            {
                "age_group":"65 to 69 years",
                "data_key":"DP1_0015C"
            }
        ])



# Initialize Dash app for the dashboard
app = dash.Dash(__name__)

# Static bar graph
static_bar = px.bar(
    population_data,
    x='NAME',
    y='DP1_0001C',
    title='Population by State (2020)',
    labels={'DP1_0001C': 'Total Population', 'NAME': 'State'},
    color='NAME',

)

# App layout
app.layout = html.Div([
    ## Dashboard Heading
    html.Div(children=[
        html.Img(src='https://png.pngtree.com/png-clipart/20210128/ourmid/pngtree-world-population-day-png-image_2809418.jpg',
        # Add margin to the logo
        style={'width':'80px', 'height':'80px','marginRight':'20px'}),
        html.H1("U.S. Population and Demographics Dashboard", style={'textAlign': 'center'})
    ], style={'display':'flex','justifyContent': 'center','alignContent':'center', 'marginBottom':'50px'}),

    ## Chart showing overall population across all states
    html.Div(children=[
        html.H2("Overall Population Across All States"),
        html.Div(children=[
            dcc.Graph(
            id='static-bar',
            figure=static_bar)
        ], style={'border':'1px solid black'})
    ]),

    ## Chart showing population across states based on selected age group
    html.Div(children=[
        html.H2("Population Distribution Across States For Selected Age Groups"),
        html.Div(children=[
            html.Div(children=[
                html.Label("Select an age group :", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='age-dropdown',
                    options=[{'label': age_group, 'value': age_group} for age_group in age_data_keys["age_group"]],
                    placeholder='Select age group',
                ),
                dcc.Graph(id='dynamic-bar'),
            ],style={'width':'90%'}),
        ],style={'display':'flex','justifyContent':'center'}),
    ], style={'marginTop':'50px'}),

    ## Chart showing population across states based on selected age group
        html.Div(children=[
            html.H2("Population Breakdown By Age Group For Selected State"),
            html.Div(children=[
                html.Div(children=[
                    html.Label("Select a state :", style={'fontWeight': 'bold'}),
                    dcc.Dropdown(
                        id='state-dropdown',
                        options=[{'label': state, 'value': state} for state in population_data['NAME']],
                        placeholder='Select a state',
                    ),
                    dcc.Graph(id='dynamic-pie')
                ], style={'width':'50%'}),
            ],style={'display':'flex','justifyContent':'center'}),
        ], style={'marginTop':'50px'}),

],style={'paddingLeft': '50px', 'paddingRight':'50px'})

#Dynamic pie chart for showing age group data in a state
#Callback function to update the pie chart showing age distribution for a specific state
@app.callback(
    Output('dynamic-pie', 'figure'),
    Input('state-dropdown', 'value')
)
def update_pie_chart(state):
    try:
        selected_state = "Alabama"
        if state:
            selected_state = state

        # Filter data for the selected state
        filtered_data = population_data[population_data['NAME'] == selected_state]

        labels = ['20 to 24 years', '25 to 29 years', '30 to 34 years', '35 to 39 years','40 to 44 years','45 to 49 years','50 to 54 years','55 to 59 years','60 to 64 years','65 to 69 years']
        values = filtered_data[['DP1_0006C','DP1_0007C','DP1_0008C','DP1_0009C','DP1_0010C','DP1_0011C','DP1_0012C','DP1_0013C','DP1_0014C','DP1_0015C']].values[0]

        data ={
            'names': labels,
            'values': values
        }

        # Create the pie chart
        fig = px.pie(
            data,
            names='names',
            values='values',
            title=f'Population Distribution for {selected_state} (2020)',
        )
        return fig
    except Exception as e:
        print(e)
    finally:
        print("Chart generated")

#Dynamic bar chart for showing data across all states for a specific age group
#Callback to update the pie chart showing age distribution for a specific state
@app.callback(
    Output('dynamic-bar', 'figure'),
    Input('age-dropdown', 'value')
)
def update_state_age_chart(age_group):
    try:
        # Setting default value for age group
        selected_group = age_data_keys["age_group"][0]
        if age_group:
            selected_group = age_group

        # Get data key for the selected age group
        filtered_group_data = age_data_keys[age_data_keys["age_group"] == selected_group]

        # Create the bar chart
        fig = px.bar(population_data, x='NAME', y=filtered_group_data['data_key'].values[0],
            title=f'Population Distribution for {selected_group} (2020)',
        )

        fig.update_layout(
            yaxis_title = 'Population',
            xaxis_title = 'State',
        )
        return fig
    except Exception as e:
        print(e)
    finally:
        print("Chart generated")

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)