from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Dados
df = pd.DataFrame({
    'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai'],
    'Vendas': [1000, 1500, 1200, 1800, 2000]
})

fig = px.line(df, x='Mês', y='Vendas', markers=True, title='Vendas Mensais')

app.layout = html.Div([
    html.H1('Dashboard Demo', style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)