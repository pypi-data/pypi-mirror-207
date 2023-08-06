from os import path as osp, chdir
import numpy as np
import matplotlib.pyplot as plt
from co2mpas_driver import dsp as driver
from scipy.interpolate import interp1d
import pandas as pd


def init_the_model(sim_step, driver_style, gs_style, car_id, db_path=None):
    """Initialize the model"""
    # The desired speed
    vdes = 124 / 3.6
    v_start = 10
    # Duration of the simulation in seconds.
    duration = 100
    inputs = dict(
        vehicle_id=car_id,
        inputs=dict(
            inputs=dict(
                gear_shifting_style=gs_style,
                starting_velocity=v_start,
                desired_velocity=vdes,
                driver_style=driver_style,
                sim_start=0,
                sim_step=sim_step,
                duration=duration,
                degree=4,
                use_linear_gs=True,
                use_cubic=False,
            )
        ),
    )
    if db_path:
        inputs["db_path"] = db_path
    my_veh = driver(inputs)["outputs"]["driver_simulation_model"]

    return my_veh


def simple_run(
    my_veh,
    sim_step,
    velocities_rw,
    times,
    car_id,
):
    """
    Calculate the energy/fuel consumption and return results
    """
    v_start_rw = velocities_rw[0]
    res = {}
    drive_battery_initial_state_of_charge = 85
    for ii, myt in enumerate(times):
        if myt == times[0]:
            my_veh.reset(
                v_start_rw,
                drive_battery_initial_state_of_charge=drive_battery_initial_state_of_charge,
            )
            res = {
                "accel": [0],
                "speed": [v_start_rw],
                "position": [0],
                "gear": [0],
                "v_des": [v_start_rw],
                "fc": [0],
                "co2": [0],
                "p_electric_battery": [0],
                "veh_wheel_torque": [0],
                "final_drive_torque_in": [0],
                "gear_box_torques_in": [0],
                "veh_wheel_power": [0],
                "final_drive_power_in": [0],
                "gear_box_power_in": [0],
                "final_drive_speed": [0],
                "gear_box_speeds_in": [0],
                "p_engine": [0],
                "p_motor": [0],
                "drive_battery_state_of_charges": [
                    drive_battery_initial_state_of_charge
                ],
            }
            continue
        res["v_des"].append(velocities_rw[ii])

        (
            gear,
            gear_count,
            next_velocity,
            acc,
            final_drive_speed,
            gear_box_speeds_in,
            veh_wheel_torque,
            final_drive_torque_in,
            gear_box_torques_in,
            veh_wheel_power,
            final_drive_power_in,
            gear_box_power_in,
        ) = my_veh(sim_step, res["v_des"][-1])

        (
            fc,
            p_engine,
            p_motor,
            soc,
            co2,
            p_electric_battery,
        ) = my_veh.calculate_fuel_consumption(
            gear, sim_step, gear_box_speeds_in, gear_box_power_in
        )

        res["accel"].append(acc)
        res["speed"].append(next_velocity)
        res["gear"].append(gear)
        res["veh_wheel_torque"].append(veh_wheel_torque)
        res["final_drive_torque_in"].append(final_drive_torque_in)
        res["gear_box_torques_in"].append(gear_box_torques_in)
        res["veh_wheel_power"].append(veh_wheel_power)
        res["final_drive_power_in"].append(final_drive_power_in)
        res["gear_box_power_in"].append(gear_box_power_in)
        res["final_drive_speed"].append(final_drive_speed)
        res["gear_box_speeds_in"].append(gear_box_speeds_in)
        res["position"].append(res["position"][-1] + next_velocity * sim_step)
        res["fc"].append(fc)
        res["co2"].append(co2)
        res["p_electric_battery"].append(p_electric_battery)
        res["p_engine"].append(p_engine)
        res["p_motor"].append(p_motor)
        res["drive_battery_state_of_charges"].append(soc)

    distance_km = np.array(res["position"])[-1] / 1000
    print(distance_km)
    print(np.array(res["speed"]).mean() * 3.6)
    socs = np.array(res["drive_battery_state_of_charges"])
    delta_soc = socs[0] - socs[-1]
    print(socs[0], socs[-1], socs.min(), socs.max())

    from co2mpas_driver.common import vehicle_specs_class as vcc

    hardcoded_params = vcc.hardcoded_params()
    fc_gr = np.array(res["fc"]).sum()
    co2_gr = np.array(res["co2"]).sum()
    electric_p_kW = np.array(res["p_electric_battery"]).sum()

    if my_veh.fuel_type in hardcoded_params.FUEL_DENSITY.keys():
        fc_lt = fc_gr / hardcoded_params.FUEL_DENSITY[my_veh.fuel_type]
    else:
        fc_lt = fc_gr

    fc_lt_100km = fc_lt / distance_km * 100
    co2_g_km = co2_gr / distance_km
    electric_p_kWh = electric_p_kW / 3600
    print(fc_lt_100km)
    print(co2_g_km)
    print(electric_p_kWh)

    return res, fc_lt_100km, delta_soc, co2_g_km


def plot_results(res, my_veh, times, fc_lt_100km, driver_style):
    """Plot to debug"""
    socs = np.array(res["drive_battery_state_of_charges"])

    fig, ax = plt.subplots(nrows=6, sharex=True)

    ax[0].set_title(f"car:{my_veh.fuel_mode}, DS: {driver_style}", fontsize=16)
    ax[0].plot(times, np.array(res["speed"]) * 3.6, label=f"Simulated", color="blue")
    ax[0].plot(times, np.array(res["v_des"]) * 3.6, label=f"Desired speed", color="red")
    ax[0].set_ylim(0, 150)
    ax[0].set_ylabel("Speed \n[km/h]", fontsize=10)
    ax[0].legend(loc=8, fontsize=8)

    ax[1].plot(times, res["accel"], label=f"Acceleration", color="blue")
    ax[1].set_ylim(-5, 5)
    ax[1].set_ylabel("Acceleration \n[m/s]", fontsize=10)
    ax[1].legend(loc=8, fontsize=8)

    ax[2].plot(times, res["final_drive_speed"], label=f"Final drive", color="blue")
    ax[2].plot(
        times, res["gear_box_speeds_in"], label=f"Gear box speeds", color="green"
    )
    ax[2].set_ylim(0, 9000)
    ax[2].set_ylabel("Rot. Speeds \n[RPM]", fontsize=10)
    ax[2].legend(loc=8, fontsize=8)
    ax2 = ax[2].twinx()
    ax2.plot(times, res["gear"], label=f"Gears", color="black")
    ax2.set_ylim(-10, 8)
    ax2.set_ylabel("Gears \n[-]", fontsize=10)
    ax2.legend(loc=1)

    ax[3].plot(times, res["veh_wheel_torque"], label=f"Wheel", color="blue")
    ax[3].plot(times, res["final_drive_torque_in"], label=f"Final drive", color="green")
    ax[3].plot(times, res["gear_box_torques_in"], label=f"Gear box", color="red")
    ax[3].set_ylim(-2000, 2000)
    ax[3].set_ylabel("Torque \n[Nm]", fontsize=10)
    ax[3].legend(loc=8, fontsize=8)

    ax[4].plot(times, res["gear_box_power_in"], label=f"Gear box", color="blue")
    ax[4].plot(times, res["p_engine"], label=f"Engine power", color="green")
    ax[4].plot(times, res["p_motor"], label=f"Motor power", color="red")
    ax[4].set_ylim(-105, 105)
    ax[4].set_ylabel("Power \n[kW]", fontsize=10)
    ax[4].legend(loc=8, fontsize=8)

    ax[5].plot(times, res["fc"], label=f"fuel", color="blue")
    ax[5].set_ylabel("Fuel cons. \n[g]", fontsize=10)
    ax[5].set_ylim(0, 0.8)
    ax[5].set_xlabel("Time [s]", fontsize=10)
    ax[5].set_xlim(0, np.max(times))
    ax[5].legend(loc=8, fontsize=8)
    ax3 = ax[5].twinx()
    ax3.plot(times, res["drive_battery_state_of_charges"], label=f"SOC", color="black")
    ax3.set_ylim(0, 100)
    ax3.set_ylabel("SOC \n[%]", fontsize=10)
    ax3.legend(loc=1)
    ax3.text(
        times[-1] * 2 / 3,
        15,
        "SOC: Initial %s %%, final %s %%" % (round(socs[0]), round(socs[-1])),
        color="black",
        fontweight="bold",
        fontsize=12,
    )
    ax3.text(
        times[-1] * 2 / 3,
        50,
        "FC: %s lt/100km" % (round(fc_lt_100km, 2)),
        color="blue",
        fontweight="bold",
        fontsize=12,
    )

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # my_dir = osp.dirname(osp.abspath(__file__))
    # chdir(my_dir)
    # A sample car id from the database = {
    car_id = 26713  # the conventional version
    # car_id = 26714  # the hybrid CD version

    rw_trip_path = r"C:\Users\nyxok\PycharmProjects\check mitsos hMFC\co2mpas_driver\co2mpas_driver\db\Trip_405.0.xlsx"
    df_rw_trip = pd.read_excel(rw_trip_path, index_col=0)[
        ["seg_t", "VehicleSpeedVSOSig"]
    ]
    times_rw = df_rw_trip["seg_t"].values
    velocities_rw = df_rw_trip["VehicleSpeedVSOSig"].values / 3.6
    v_start_rw = velocities_rw[0]
    # sample time series
    # Duration of the simulation in seconds.
    duration = times_rw[-1]
    sim_step = 0.1
    times = np.arange(0, duration + sim_step, sim_step)
    driver_style = 0.4
    # The gear shifting style as described in the TRR paper.
    gs_style = 0.4

    my_veh = init_the_model(sim_step, driver_style, gs_style, car_id)
    res, fc_lt_100km, delta_soc = simple_run(
        my_veh,
        sim_step,
        velocities_rw,
        times,
        car_id,
    )
    plot_results(res, my_veh, times_rw, fc_lt_100km, driver_style)
