import plotly.graph_objects as go
import pandas as pd

def plot_ccl_por_cedear(df:pd.DataFrame):
    temp = df.sort_values("ccl cedear", ascending=False)
    min_ccl = temp["ccl cedear"].iloc[-1]
    max_ccl = temp["ccl cedear"].iloc[0]
    fig = go.Figure()

    # Define a color scale
    colorscale = [[0, 'green'], [1, 'red']]

    # Use the color scale to set the color of the markers
    fig.add_trace(go.Scatter(x = temp["tickers USA"], y = temp["ccl cedear"], mode = "markers",
                            marker = dict(size = 10, color = temp["ccl cedear"], colorscale = colorscale, cmin = min_ccl, cmax = max_ccl)))

    fig.update_yaxes(range = [min_ccl*.99, max_ccl*1.01], tickformat = ",")
    fig.update_layout(template = None, font_family = "georgia", separators = ",.",
                    title_text = "CCL por CEDEAR")
    fig.add_hline(y=temp["ccl promedio"].iloc[0], annotation_text="Mediana", line_dash = "dash")
    return fig