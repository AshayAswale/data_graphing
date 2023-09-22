import plotly.express as px
import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu


milp_df = pd.read_csv('./optimal_small_results.csv', header=0)

fig = px.box(milp_df[["2 Skills", "4 Skills", "8 Skills"]], points="all", labels={
                     "value": "MILP Solution Cost",
                     "variable": ""
                 },)

fig.update_layout(
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=36
    ),
    width=1000,
    height=1000,
)
# fig.update_yaxes(range=[-6.8, -2.2]) 
# fig.show()
fig.write_image("svg_files/MILP_cost.svg")
