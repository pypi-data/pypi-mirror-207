from os import path as osp, chdir
import numpy as np
import matplotlib.pyplot as plt
from co2mpas_driver import dsp as driver
from scipy.interpolate import interp1d

my_dir = osp.dirname(osp.abspath(__file__))
chdir(my_dir)


def simple_run():
    """
    This example computes and plots the driving trajectories with the varying desired speed.

    """
    # A sample car id from the database = {
    car_id_db = {
        "fuel_engine": [
            35135,
            # 39393,
            # 27748,
            # 8188,
            # 40516,
            # 35452,
            # 40225,
            # 7897,
            # 7972,
            # 41388,
            # 5766,
            # 9645,
            # 9639,
            # 5798,
            # 8280,
            # 34271,
            # 34265,
            # 6378,
            # 39723,
            # 34092,
            # 2592,
            # 5635,
            # 5630,
            # 7661,
            # 7683,
            # 8709,
            # 9769,
            # 1872,
            # 10328,
            # 35476,
            # 41989,
            # 26799,
            # 26851,
            # 27189,
            # 23801,
            # 3079,
            # 36525,
            # 47766,
            # 6386,
            # 33958,
            # 33986,
            # 5725,
            # 5718,
            # 36591,
            # 4350,
            # 39396,
            # 40595,
            # 5909,
            # 5897,
            # 5928,
            # 5915,
            # 40130,
            # 42363,
            # 34760,
            # 34766,
            # 1835,
            # 36101,
            # 42886,
            # 1431,
            # 46547,
            # 44799,
            # 41045,
            # 39820,
            # 34183,
            # 34186,
            # 20612,
            # 20605,
            # 1324,
            # 9882,
            # 4957,
            # 5595,
            # 18831,
            # 18833,
            # 9575,
            # 5380,
            # 9936,
            # 7995,
            # 6331,
            # 18173,
            # 34286,
            # 34279,
            # 20706,
            # 34058,
            # 34057,
            # 24268,
            # 19028,
            # 19058,
            # 7979,
            # 22591,
            # 34202,
            # 40170,
            # 44599,
            # 5358,
            # 5338,
            # 34015,
            # 9872,
            # 9856,
            # 6446,
            # 8866,
            # 9001,
            # 9551,
            # 6222,
        ],
        "electric_engine": [],  # [47844],
        "hybrid_engine": [26712],
    }
    # car_id = 35135
    car_id = 47844
    # car_id = 26713 # the conventional version
    # car_id = 26712 # the hybrid version
    # car_id = 26714  # the hybrid CD version

    # The desired speed
    vdes = 124 / 3.6

    # Current speed
    v_start = 0

    # The simulation step in seconds
    sim_step = 0.1

    # The driving style as described in the TRR paper.
    driver_style = 0.8

    # Duration of the simulation in seconds.
    duration = 300

    # sample time series
    times = np.arange(0, duration + sim_step, sim_step)

    # The gear shifting style as described in the TRR paper.
    gs_style = 0.4

    # driver(dict(vehicle_id=car_id, inputs=dict(inputs=dict(
    #             gear_shifting_style=gs_style, starting_velocity=v_start,
    #             driver_style=driver_style, sim_start=0, sim_step=sim_step,
    #             duration=duration, degree=4, use_linear_gs=True, desired_velocity=vdes,
    #             use_cubic=False)))).plot()

    my_veh = driver(
        dict(
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
    )["outputs"]["driver_simulation_model"]
    # Plots workflow of the core model, this will automatically open an internet browser and show the work flow
    # of the core model. you can click all the rectangular boxes to see in detail sub models like load, model,
    # write and plot.
    # you can uncomment to plot the work flow of the model
    # driver.plot(1)  # Note: run your IDE as Administrator if file permission error.

    f_des = interp1d(
        [0, 210, 700, 1050, 1400, 3150, 4550, 5250],  # Position (m)
        [20, 20, 30, 5, 25, 35, 15, 0],  # Desired speed (m/s)
        kind="next",
    )
    res = {}
    drive_battery_initial_state_of_charge = 85
    for myt in times:
        if myt == times[0]:
            my_veh.reset(
                v_start,
                drive_battery_initial_state_of_charge=drive_battery_initial_state_of_charge,
            )
            res = {
                "accel": [0],
                "speed": [v_start],
                "position": [0],
                "gear": [0],
                "v_des": [f_des(0)],
                "fc": [0],
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
        res["v_des"].append(f_des(res["position"][-1]))

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

        if car_id in car_id_db["electric_engine"]:
            fc = 0
        else:
            fc, p_engine, p_motor, soc = my_veh.calculate_fuel_consumption(
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
        res["p_engine"].append(p_engine)
        res["p_motor"].append(p_motor)
        res["drive_battery_state_of_charges"].append(soc)

    distance_km = np.array(res["position"])[-1] / 1000
    print(distance_km)
    print(np.array(res["speed"]).mean() * 3.6)
    socs = np.array(res["drive_battery_state_of_charges"])
    print(socs[0], socs[-1], socs.min(), socs.max())

    from co2mpas_driver.common import vehicle_specs_class as vcc

    hardcoded_params = vcc.hardcoded_params()
    fc_gr = np.array(res["fc"]).sum()
    fc_lt = fc_gr / hardcoded_params.FUEL_DENSITY["petrol"]
    fc_lt_100km = fc_lt / distance_km * 100
    print(fc_lt_100km)

    fig, ax = plt.subplots(nrows=6, sharex=True)

    ax[0].set_title(f"car:{my_veh.fuel_mode}, DS: {driver_style}", fontsize=16)
    ax[0].plot(times, np.array(res["speed"]) * 3.6, label=f"Simulationed", color="blue")
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
    simple_run()
