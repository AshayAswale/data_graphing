import plotly.express as px
import numpy as np
import pandas as pd

from scipy.stats import mannwhitneyu


cost_df = pd.read_csv('./cost_compare.csv', header=0)
time_df = pd.read_csv('./time_compare.csv', header=0)

stat, p_value = mannwhitneyu(cost_df["Optimal cost"], cost_df["Raw ADMM"])
print("Cost stats")
print(f" Mann–Whitney U Test: statistic={stat:.4f}, p-value={p_value:.4f}")

stat, p_value = mannwhitneyu(time_df["Central"], time_df["Raw ADMM"])
print("Wall clock time stats")
# print(time_df["CBAA"], time_df["ADMM"])
print(f" Mann–Whitney U Test: statistic={stat:.4f}, p-value={p_value:.4f}")
exit()
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

fig = px.box(cost_df[["CBAA", "ADMM"]], points="all", labels={
                     "value": "Cost compared to optimal cost",
                     "variable": "Methods"
                 },)

fig.update_layout(
    title="Solution quality",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36,
        color="RebeccaPurple"
    )
)

fig.show()

fig = px.box(time_df[["CBAA", "ADMM"]], points="all", labels={
                     "value": "Wall clock time compared to centralized",
                     "variable": "Methods"
                 },)

fig.update_layout(
    title="Solving wall clock time",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=36,
        color="RebeccaPurple"
    )
)
fig.show()