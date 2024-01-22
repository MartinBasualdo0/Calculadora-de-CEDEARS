import dash
from dash import dcc, html, State
from dash.dependencies import Output, Input
import dash_ag_grid as dag

from style import external_stylesheets, external_scripts
from src.tablas import main_table
from src.estimated_price import calculate_price
from src.constants import CEDEARS_COMPLETO, CEDEARS_SELECTOS
from src.plots import plot_ccl_por_cedear

df = main_table(CEDEARS_SELECTOS)
default_ticker = "AAPL"

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)

app.title = 'Calculadora de precios para CEDEARS'


app.layout = html.Div([
    html.Div([
        html.H1('Calculadora de precios para CEDEARS', className='display-4 mb-3')
    ], className='container'),
    html.Div([
        dcc.Input(
            id='estimate-input',
            type='text',
            value=default_ticker,
            className='mb-3',
            placeholder="Escribir ticker...",
            debounce=True,
        ),
        dcc.Store(
            id='input-store',
            storage_type='session'
        ),
        html.Button(
            'Add Ticker',
            id='add-ticker-button',
            className='btn btn-primary mb-3'
        ),
        dcc.Loading(
            id="loading",
            type="circle",
            children=[html.Div(id='estimate-result', className='lead')]
        ),
        dcc.Dropdown(
            id='ticker-dropdown',
            options=[{'label': ticker, 'value': ticker} for ticker in CEDEARS_SELECTOS], 
            value=CEDEARS_SELECTOS,
            multi=True,
            className='mb-3'
        ),
        dag.AgGrid(id='output-div'),
        html.Button("Download Excel", id="btn_xlsx", className='btn btn-primary mb-3'),
        dcc.Download(id="download-dataframe-xlsx"),
        dcc.Graph(
            id = 'tc-por-cedear-plot',
            figure=plot_ccl_por_cedear(df)
        )
    ], className='container'),
])

@app.callback(
    Output('output-div', 'rowData'),
    Output('output-div', 'columnDefs'),
    Input('ticker-dropdown', 'value')
)
def update_output(ticker):
    columnDefs = [{"headerName": col, "field": col} for col in df.columns]
    rowData = df.to_dict('records')
    
    return rowData, columnDefs

@app.callback(
    Output('input-store', 'data'),
    Input('estimate-input', 'value')
)
def store_input(value):
    value = value.upper()
    return value

@app.callback(
    Output('output-div', 'rowData', allow_duplicate=True),
    Output('output-div', 'columnDefs', allow_duplicate=True),
    # Output('estimate-input', 'value'),
    Input('add-ticker-button', 'n_clicks'),
    State('input-store', 'data'),
    prevent_initial_call = True
)
def add_ticker(n_clicks, ticker):
    global CEDEARS_SELECTOS
    global df
    if n_clicks > 0 and ticker not in CEDEARS_SELECTOS:
        CEDEARS_SELECTOS.append(ticker)
    df = main_table(CEDEARS_SELECTOS) # Run the main_table function with the updated list
    columnDefs = [{"headerName": col, "field": col} for col in df.columns]
    rowData = df.to_dict('records')
    
    return rowData, columnDefs

@app.callback(
    Output('estimate-result', 'children'),
    Input('estimate-input', 'value')
)
def update_estimate(selected_ticker):
    selected_ticker = selected_ticker.upper()
    try:
        estimate = calculate_price(selected_ticker, df)
    except Exception as e:
        return "Cedear incorrecto, intente de nuevo"
    return estimate

@app.callback(
    Output("download-dataframe-xlsx", "data"),
    Input("btn_xlsx", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_excel, "calculadora cedears.xlsx")

if __name__ == '__main__':
    app.run_server(debug=True)
