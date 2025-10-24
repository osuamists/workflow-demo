from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout do painel de login
app.layout = dbc.Container([
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

# Callback para validar o login
@app.callback(
    Output("login-message", "children"),
    Input("login-button", "n_clicks"),
    State("username-input", "value"),
    State("password-input", "value"),
    prevent_initial_call=True
)
def validate_login(n_clicks, username, password):
    # Validação simples (em produção, use banco de dados)
    if username == "admin" and password == "123456":
        return dbc.Alert("✅ Login realizado com sucesso!", color="success")
    else:
        return dbc.Alert("❌ Usuário ou senha incorretos!", color="danger")

if __name__ == '__main__':
    app.run(debug=True, port=8051)                                   