
from dash import Dash, html, dcc,Input,Output
import plotly.express as pt
import pandas as pd
df=pd.read_csv('Data.csv').to_dict(orient='list')
Year=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
app = Dash(__name__)
app.layout = html.Div(children=[
    html.H1(children='Marist Student Population from 2010 to 2021',style={'textAlign':'center'}),

    html.Div(children='''
        Students attributes
    ''',
    ),
    html.Div(
        [
             dcc.Dropdown(['Full-Time Traditional Undergraduate',
'Part-Time Traditional Undergraduate',
'Total Headcount Traditional Undergraduate',
'Full-Time Adult',
'Part-Time Adult',
'Total Headcount Adult',
'Full-Time High School',
'Part-Time High School',
'Total Headcount High School',
'Total Full-time Undergraduate',
'Total Part-time Undergraduate',
'Total Headcount Undergraduate',
'Full-Time Graduate',
'Part-Time Graduate',
'Total Headcount Graduate',
'Total Student'
],
    id='yaxis',
    value='Total Student',
    clearable=False,
    ),
    ],
    style={'width': '40%', 'display': 'inline-block'},
    ),
    dcc.Graph(id='graph'),

],
)
@app.callback(
    Output('graph','figure'),
    Input('yaxis','value')
)
def display(y_axis):
    
    fig=pt.bar(x=Year, y=df.get(y_axis))
    fig.update_yaxes(title=y_axis)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)