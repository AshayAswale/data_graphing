import plotly.express as px
import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu


cost_df = pd.read_csv('./combined_small_scores.csv', header=0)
time_df = pd.read_csv('./combined_small_runtimes.csv', header=0)

fig = px.box(cost_df[["2 Skills", "4 Skills", "8 Skills"]], points="all", labels={
                     "value": "Greedy cost / MILP solver first solution",
                     "variable": ""
                 },)

fig.update_layout(
    # title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=36
    ),
    width=1005,
    height=1005
)
# fig.update_yaxes(range=[0.95, 1.93]) 
# fig.show()
fig.write_image("../svg_files/Greedy_FirstSols_cost.svg")

fig = px.box(time_df[["2 Skills", "4 Skills", "8 Skills"]], points="all", labels={
                     "value": "Log10(Greedy WCST / MILP solver FS-WCST)",
                     "variable": ""
                 },)

fig.update_layout(
    # title="Solving wall clock time",
    legend_title="Legend Title",
    font=dict(
        family="Arial",
        size=38
    ),
    width=1005,
    height=1005
)
# fig.update_yaxes(range=[-6.8, -2.2]) 
# fig.show()
fig.write_image("../svg_files/Greedy_FirstSols_time.svg")
