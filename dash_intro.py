import dash 
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

app = dash.Dash()

app.layout = html.Div([

    html.H1("Title 1"),
    html.H2("Title 2"),
    html.H3("Title 3"),

    html.Button("Click me !!", id="my-button"),

    html.Div(id="my-output")
])

@app.callback(
    [Output("my-output", "children")],
    [Input("my-button", "n_clicks")]
)

def clicked_output(v):
    if v == None:
        raise PreventUpdate
    return [f"You clicked {v} times"]


app.run_server(debug=True)


