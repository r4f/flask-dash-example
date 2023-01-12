from flask import Flask
from dash import Dash, html, dcc, Output, Input
#from flask import send_from_directory

example_data = {
    'id1': {'title': 'first example',
            'content': 'first example content',},
    'id2': {'title': 'second example',
            'content': 'second example content',},
}

server = Flask(__name__)

dash_app = Dash(
    __name__,
    server=server,
    url_base_pathname='/dash/',
)

dash_app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.H1("Dash-Flask-Whitenoise-Gunicorn", id="top-h1"),
    html.Div([
        html.H2("[Example title]", id="portfolio-title"),
        html.Div([
        ], id="portfolio-info"),
    ], id="portfolio-container"),
], id='main-container')


@dash_app.callback(
    Output('portfolio-title', 'children'), #title
    Output('portfolio-info', 'children'), #content
    Input('url', 'pathname'))
def display_page(pathname):
    id = pathname.split('/')[-1]
    return_data = example_data[id]
    title = return_data['title']
    content = return_data['content']
    content += f'[path = {pathname}]'
    return title, content

@server.route("/")
def overview():
    response = """
    <html>
    <head>
    <style>
        body {
            background-color: rgb(190, 220, 220);
        }
    </style>
    </head>
    <body>
    <ul>
    """
    for id, di in example_data.items():
        title = di['title']
        response += f"<li><a href='/dash/{id}'>{title}</a></li>"
    response += """
    </ul></body></html>
    """
    return response

@server.route("/dash/<portfolio_id>")
def my_dash_app(portfolio_id):
    print(f"requestiong portfolio {portfolio_id}")
    return dash_app.index()

if __name__ == '__main__':
	dash_app.run_server(host="0.0.0.0", port=8001, debug=True)
