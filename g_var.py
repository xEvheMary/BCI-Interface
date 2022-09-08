# IMPORTS
import os

# DEFAULT

# DS RELATED
base_path = os.path.dirname(os.path.realpath(__file__))
ds_path = os.path.join(base_path, 'DS')
# PLOT RELATED
plot_duration = 5       # how many seconds of data to show
update_interval = 60    # ms between screen updates
pull_interval = 200     # ms between each pull operation
# PROCESS RELATED
time_window_len = 2     # Length of classifier time window