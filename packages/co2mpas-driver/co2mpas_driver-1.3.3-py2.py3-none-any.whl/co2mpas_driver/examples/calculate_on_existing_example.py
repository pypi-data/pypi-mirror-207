import numpy as np
import pandas as pd
from mfc_post_proc_trajectory import init_the_model, simple_run, plot_results

# Car id selection from the database.
car_id = 26713  # the conventional version
car_id = 26714  # the hybrid CD version
car_id = 26716  # the hybrid version
# Database selection.
db_path = r"../db/EuroSegmentCar_cleaned.csv"

# Driver parameters
driver_style = 0.4
# The gear shifting style as described in the TRR paper.
gs_style = 0.4

# Trip parameters
rw_trip_path = r"data/wltp_10_hz.xlsx"
df_rw_trip = pd.read_excel(rw_trip_path, index_col=0)[["seg_t", "VehicleSpeedVSOSig"]]
times_rw = df_rw_trip["seg_t"].values
velocities_rw = df_rw_trip["VehicleSpeedVSOSig"].values / 3.6
v_start_rw = velocities_rw[0]
# sample time series
# Duration of the simulation in seconds.
duration = times_rw[-1]

# Simulation parameters
sim_step = 0.1
times = np.arange(0, duration + sim_step, sim_step)

my_veh = init_the_model(sim_step, driver_style, gs_style, car_id, db_path=db_path)
res, fc_lt_100km, delta_soc, co2_km = simple_run(
    my_veh,
    sim_step,
    velocities_rw,
    times,
    car_id,
)
plot_results(res, my_veh, times, fc_lt_100km, driver_style)
