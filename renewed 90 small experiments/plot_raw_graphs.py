import plotly.express as px
import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu


cost_df = pd.read_csv('./large_results.csv', header=0)

fig = px.violin(cost_df[["2 Skills", "4 Skills", "8 Skills"]], points="all", labels={
                     "value": "Solution cost/Optimal cost",
                     "variable": "Solution cost compared to optimal solution"
                 },)

fig.update_layout(
    # title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)
fig.update_yaxes(range=[0.7, 2.35])

fig.show()


# fig = px.violin(cost_df[["median score", "mean score"]][30:60], points="all", labels={
#                      "value": "Compared to Optimal %",
#                      "variable": "Final score of solution for 4 skills"
#                  },)

# fig.update_layout(
#     title="Solution quality",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=36
#     )
# )

# fig.show()


# fig = px.violin(cost_df[["median score", "mean score"]][60:95], points="all", labels={
#                      "value": "Compared to Optimal %",
#                      "variable": "Final score of solution for 8 skills"
#                  },)

# fig.update_layout(
#     title="Solution quality",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=36
#     )
# )

# fig.show()


#######



# fig = px.violin(cost_df[["median run time", "mean run time"]][0:30], points="all", labels={
#                      "value": "Run time compared to gurobi %",
#                      "variable": "Solving wall clock time for 2 skills"
#                  },)

# fig.update_layout(
#     title="Solution quality",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=36
#     )
# )

# fig.show()


# fig = px.violin(cost_df[["median run time", "mean run time"]][30:60], points="all", labels={
#                      "value": "Run time compared to gurobi %",
#                      "variable": "Solving wall clock time for 4 skills"
#                  },)

# fig.update_layout(
#     title="Solution quality",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=36
#     )
# )

# fig.show()


# fig = px.violin(cost_df[["median run time", "mean run time"]][60:95], points="all", labels={
#                      "value": "Run time compared to gurobi %",
#                      "variable": "Solving wall clock time for 8 skills"
#                  },)

# fig.update_layout(
#     title="Solution quality",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=36
#     )
# )

# fig.show()
