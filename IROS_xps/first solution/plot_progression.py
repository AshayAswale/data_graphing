        # "0.25313591957092285": 1290.387,
        # "0.26867079734802246": 1076.368,
        # "0.27039098739624023": 1029.68,
        # "0.3839879035949707": 1025.377,
        # "0.6648678779602051": 1019.25,
        # "1.2754650115966797": 911.642,
        # "17.74657392501831": 889.08,
        # "19.84072995185852": 878.857,
        # "25.785035848617554": 842.936,
        # "38.94089889526367": 834.042,
        # "124.71486401557922": 824.735
import plotly.graph_objs as go
import math

# Example vector of solution candidates
solution_candidates = [(math.log10(0.25313591957092285), (1290.387)),
(math.log10(0.26867079734802246), (1076.368)),
(math.log10(0.27039098739624023), (1029.68)),
(math.log10(0.3839879035949707), (1025.377)),
(math.log10(0.6648678779602051), (1019.25)),
(math.log10(1.2754650115966797), (911.642)),
(math.log10(17.74657392501831), (889.08)),
(math.log10(19.84072995185852), (878.857)),
(math.log10(25.785035848617554), (842.936)),
(math.log10(38.94089889526367), (834.042)),
(math.log10(124.71486401557922), (824.735)),
(math.log10(1806.7019188404083), (824.735))]

# Extract time and cost data into separate lists
times = [pair[0] for pair in solution_candidates]
costs = [pair[1] for pair in solution_candidates]

# Create a scatter plot of costs over time using Plotly
fig = go.Figure(data=go.Scatter(x=times, y=costs, mode='markers+lines'))
fig.update_layout(xaxis_title='Log10(Time in seconds)', yaxis_title='Solution cost',
    font=dict(
        family="Arial",
        size=36
    ),
    width=1000,
    height=1000)
fig.update_yaxes(range=[0.0, 1500]) 

# Show the plot in a new browser window
# fig.show()
fig.write_image("../svg_files/MILP_solution_progression.svg")
