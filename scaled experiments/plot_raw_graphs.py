import plotly.express as px
import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu


cost_df = pd.read_csv('./scaling_comparision.csv', header=0)

fig = px.box(cost_df[["180_4_8_4_0","210_4_16_4_0","240_4_32_4_0","300_8_32_4_0","330_16_32_4_0","360_4_8_8_0","390_4_16_8_0","420_4_32_8_0","480_8_32_8_0","510_16_32_8_0"]], points="all", labels={
                     "value": "Solution cost/Optimal cost",
                     "variable": "510_16_32_8_0"
                 },)

fig.update_layout(
    # title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)
# fig.update_yaxes(range=[-2.25, 2.25])

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
