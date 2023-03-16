import plotly.express as px
import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu


cost_df = pd.read_csv('./combined_data.csv', header=0)

fig = px.violin(cost_df[["meets_score_diff", "alws_score_diff"]][0:30], points="all", labels={
                     "value": "Compared to solution without stochasticity",
                     "variable": "Final score of solution for 2 skills"
                 },)

fig.update_layout(
    title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)

fig.show()


fig = px.violin(cost_df[["meets_score_diff", "alws_score_diff"]][30:60], points="all", labels={
                     "value": "Compared to solution without stochasticity",
                     "variable": "Final score of solution for 4 skills"
                 },)

fig.update_layout(
    title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)

fig.show()


fig = px.violin(cost_df[["meets_score_diff", "alws_score_diff"]][60:95], points="all", labels={
                     "value": "Compared to solution without stochasticity",
                     "variable": "Final score of solution for 8 skills"
                 },)

fig.update_layout(
    title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)

fig.show()


#######



fig = px.violin(cost_df[["meets_time_diff", "alws_time_diff"]][0:30], points="all", labels={
                     "value": "Compared to solution without stochasticity",
                     "variable": "Solving wall clock time for 2 skills"
                 },)

fig.update_layout(
    title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)

fig.show()


fig = px.violin(cost_df[["meets_time_diff", "alws_time_diff"]][30:60], points="all", labels={
                     "value": "Compared to solution without stochasticity",
                     "variable": "Solving wall clock time for 4 skills"
                 },)

fig.update_layout(
    title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)

fig.show()


fig = px.violin(cost_df[["meets_time_diff", "alws_time_diff"]][60:95], points="all", labels={
                     "value": "Compared to solution without stochasticity",
                     "variable": "Solving wall clock time for 8 skills"
                 },)

fig.update_layout(
    title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)

fig.show()
