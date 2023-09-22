import plotly.express as px
import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu


cost_df = pd.read_csv('./cost_comparison.csv', header=0)
# time_df = pd.read_csv('./comparison_time.csv', header=0)

# stat, p_value = mannwhitneyu(cost_df["Raw ADMM"], cost_df["Raw CBAA"], alternative='less', nan_policy='omit')
# print("Cost stats")
# print(f" Mann–Whitney U Test: statistic={stat:.4f}, p-value={p_value:.4f}")

# stat, p_value = mannwhitneyu(time_df["Raw ADMM"], time_df["Raw CBAA"], alternative='less', nan_policy='omit')
# print("Wall clock time stats")
# print(time_df["CBAA"], time_df["ADMM"])
# print(f" Mann–Whitney U Test: statistic={stat:.4f}, p-value={p_value:.4f}")
# exit()
# from numpy import genfromtxt
# np.set_printoptions(linewidth=np.inf, suppress=True)

# admm_data = df["ADMM"].to_numpy()
# cbaa_data = df["CBAA"].to_numpy()
# opt_data = df["Optimal cost"].to_numpy()

# perc_admm = np.divide(admm_data,opt_data)
# perc_cbaa = np.divide(admm_data,opt_data)

# raw_data = genfromtxt('cost_compare.csv', delimiter=',')
# raw_data[1:,1:]

# perc_diff = np.zeros((raw_data.size[0]-1, 2))
# perc_diff[0] = 

# data = df.to_numpy
# print(data)

# fig = px.violin(cost_df[["128 Tasks", "256 Tasks", "512 Tasks", "1024 Tasks"]], points="all", labels={
#                      "value": "Log10 of wall clock solving time",
#                      "variable": "Solving wall clock time for each configuration"
#                  },)

# fig.update_layout(
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=36
#     )
# )
# # fig.update_yaxes(range=[0.95, 1.93]) 
# fig.show()

# fig = px.box(time_df[["2 Skills", "4 Skills", "8 Skills"]], points="all", labels={
#                      "value": "Log10(Guided WCST / Unguided WCST)",
#                      "variable": "Relative solving times"
#                  },)

# fig.update_layout(
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=36
#     )
# )
# # fig.update_yaxes(range=[-6.8, -2.2]) 
# fig.show()
# "128 Tasks",	"256 Tasks",	"512 Tasks",	"1024 Tasks"

fig = px.box(cost_df[["2 Skills", "4 Skills", "8 Skills"]], points="all", labels={
                     "value": "Greedy cost / Optimal cost",
                     "variable": "Updated greedy result"
                 },)

fig.update_layout(
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36
    )
)
# fig.update_yaxes(range=[0.95, 1.9]) 
fig.show()