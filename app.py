import dash
from dash import dcc, Output, Input
from dash import html
import dash_bootstrap_components as dbc

# Local File
import recommend
import analysis


theme = [dbc.themes.FLATLY]
app = dash.Dash(__name__, external_stylesheets=theme, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])

server = app.server
app.title = 'InnovateServe Recommender'
app._favicon = "logo_final-01.jpg"

app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[

            dbc.NavItem(dbc.NavLink(
                html.A("Recommend", href="/", className="me-1 text-white text-decoration-none fs-5", id='predict_link',
                       n_clicks=0))),
            dbc.NavItem(dbc.NavLink(
                html.A("Analysis", href="analysis", className="me-1 text-white text-decoration-none fs-5",
                       id='model_link',
                       n_clicks=0))),

            dbc.NavItem(
                dbc.NavLink(html.A("Source Code", href="https://github.com/majedelleuch",
                                   className="me-1 text-white text-decoration-none fs-5"))),
            dbc.NavItem(html.A(
                [dbc.CardImg(src=r"assets/logo_final-01.jpg", style={'width': '30px', 'height': '30px'}, className='my-2')],
                href='https://github.com/majedelleuch')),

        ], fixed='top',
        brand="InnovateServe Recommender",
        brand_href="/",
        color="#3559E0",
        dark=True,
        className='py-0'),
    html.Br(),
    html.Br(),

    dbc.Row([
        dcc.Location(id='url', refresh=True),
    ], id='display')

], fluid=True)


@app.callback(
    Output('display', 'children'),
    Input('url', 'pathname'))
def update(x):
    if x == '/':
        return recommend.recommend_div
        pass
    elif x == '/analysis':
        return analysis.dashboard


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8080, debug=False)
    # app.run_server(host='0.0.0.0', port=8080, debug=True)
