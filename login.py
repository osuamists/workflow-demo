from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Dados do dashboard
df = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    'Vendas': [1000, 1500, 1200, 1800, 2000]
})

fig = px.line(df, x='Mês', y='Vendas', markers=True, title='Vendas Mensais')

# Layout do painel de login
login_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                html.H2("🔐 Login", className="text-center mb-4"),
                
                dbc.Card([
                    dbc.CardBody([
                        dbc.Label("Usuário"),
                        dbc.Input(
                            id="username-input",
                            type="text",
                            placeholder="Digite seu usuário",
                            className="mb-3"
                        ),
                        
                        dbc.Label("Senha"),
                        dbc.Input(
                            id="password-input",
                            type="password",
                            placeholder="Digite sua senha",
                            className="mb-3"
                        ),
                        
                        dbc.Button(
                            "Entrar",
                            id="login-button",
                            color="primary",
                            className="w-100 mb-3"
                        ),
                        
                        html.Div(id="login-message", className="text-center")
                    ])
                ], className="shadow")
            ], style={'maxWidth': '400px', 'margin': 'auto', 'marginTop': '100px'})
        ], width=12)
    ])
], fluid=True)

# Layout do Dashboard
dashboard_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.H1('📊 Dashboard Demo', className="mb-4")
                    ], width=8),
                    dbc.Col([
                        dbc.Button("Sair", id="logout-button", color="danger", className="float-end")
                    ], width=4)
                ]),
                
                html.Hr(),
                
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Vendas Mensais"),
                        dcc.Graph(figure=fig)
                    ])
                ], className="shadow")
            ], style={'padding': '20px'})
        ])
    ])
], fluid=True)

# Layout principal
app.layout = html.Div([
    dcc.Store(id='session-store', data={'logged_in': False}),
    html.Div(id='page-content')
])

# Callback para mostrar login ou dashboard
@app.callback(
    Output('page-content', 'children'),
    Input('session-store', 'data')
)
def display_page(session_data):
    if session_data and session_data.get('logged_in'):
        return dashboard_layout
    else:
        return login_layout

# Callback para validar o login
@app.callback(
    Output('session-store', 'data'),
    Output('login-message', 'children'),
    Input('login-button', 'n_clicks'),
    State('username-input', 'value'),
    State('password-input', 'value'),
    prevent_initial_call=True
)
def validate_login(n_clicks, username, password):
    if username == "admin" and password == "123456":
        return (
            {'logged_in': True},
            dbc.Alert("✅ Login realizado!", color="success", duration=2000)
        )
    else:
        return (
            {'logged_in': False},
            dbc.Alert("❌ Usuário ou senha incorretos!", color="danger")
        )

# Callback para logout
@app.callback(
    Output('session-store', 'data', allow_duplicate=True),
    Input('logout-button', 'n_clicks'),
    prevent_initial_call=True
)
def logout(n_clicks):
    return {'logged_in': False}

if __name__ == '__main__':
    app.run(debug=True, port=8051)