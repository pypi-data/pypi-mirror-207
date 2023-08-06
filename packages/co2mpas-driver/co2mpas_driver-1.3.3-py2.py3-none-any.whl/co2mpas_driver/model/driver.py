# -*- coding: utf-8 -*-
#
# Copyright 2019 European Commission (JRC);
# Licensed under the EUPL (the 'Licence');
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at: http://ec.europa.eu/idabc/eupl

from co2mpas_driver.common import functions as func, vehicle_specs_class as vcc
from .co2mpas import estimate_f_coefficients
import math
import numpy as np


class Driver:
    """
    Blueprint for driver.
    """

    def __init__(
        self,
        vehicle_mass,
        car_type,
        final_drive,
        gearbox_type,
        max_power,
        fuel_type,
        fuel_mode,
        type_of_car,
        car_width,
        car_height,
        transmission,
        gs,
        curves,
        curves_dec,
        driver_style,
        drive_battery_voltage,
        drive_battery_capacity,
        motor_full_load_curve,
        full_load_curve,
        r_dynamic=None,
        gear_box_ratios=None,
        engine_max_torque=None,
        fuel_eng_capacity=None,
        fuel_engine_stroke=None,
        fuel_turbo=None,
    ):
        self.vehicle_mass = vehicle_mass
        self.r_dynamic = r_dynamic
        self.car_type = car_type
        self.final_drive = final_drive
        self.gear_box_ratios = gear_box_ratios
        self.gearbox_type = gearbox_type
        self.engine_max_torque = engine_max_torque
        self.fuel_eng_capacity = fuel_eng_capacity
        self.max_power = max_power
        self.fuel_engine_stroke = fuel_engine_stroke
        self.fuel_type = fuel_type
        self.fuel_mode = fuel_mode
        self.type_of_car = type_of_car
        self.car_width = car_width
        self.car_height = car_height
        self.fuel_turbo = fuel_turbo

        self.transmission = transmission
        self.gs = gs
        self.curves = list(curves)
        self.curves_dec = list(curves_dec)
        self.driver_style = driver_style
        self._velocity = self.position = self._gear_count = self._gear = None
        self.hardcoded_params = vcc.hardcoded_params()

        self.fuel_engine_power_in = None
        self.maximum_drive_battery_current = 200
        self.drive_battery_currents_range = np.linspace(
            -self.maximum_drive_battery_current, self.maximum_drive_battery_current, 100
        )
        self.drive_battery_capacity = drive_battery_capacity

        drive_battery_internal_resistance = 0.2
        motor_efficiency = 0.9
        self.drive_battery_internal_resistance = drive_battery_internal_resistance
        self.motor_efficiency = motor_efficiency
        self.drive_battery_voltage = drive_battery_voltage
        self.drive_battery_powers_range = (
            (drive_battery_voltage * self.drive_battery_currents_range)
            - (
                drive_battery_internal_resistance
                * self.drive_battery_currents_range**2
            )
        ) / 1000
        self.drive_battery_electric_powers_range = (
            drive_battery_voltage * self.drive_battery_currents_range / 1000
        )
        self.electric_motor_power_range = (
            self.drive_battery_powers_range
            * motor_efficiency ** np.sign(self.drive_battery_currents_range)
        )
        self.drive_battery_voltage = drive_battery_voltage
        self.motor_full_load_curve = motor_full_load_curve
        self.full_load_curve = full_load_curve

    def reset(self, starting_velocity, drive_battery_initial_state_of_charge=50):
        from .simulation import gear_for_speed_profiles as func

        self._gear, self._gear_count = func(self.gs, starting_velocity, 0, 0)
        self._gear_count, self.position, self._velocity = 0, 0, starting_velocity
        self.drive_battery_initial_state_of_charge = (
            drive_battery_initial_state_of_charge
        )
        self.previous_drive_battery_state_of_charge = (
            drive_battery_initial_state_of_charge
        )
        return self

    def update(self, next_velocity, gear, gear_cnt, sim_step):
        from .simulation import gear_for_speed_profiles as func

        g, gc = func(self.gs, next_velocity, gear, gear_cnt)
        cnt = int(divmod(10 * 0.5, 10 * sim_step)[0])
        is_between = 0 < gear_cnt < cnt
        if g == gear and is_between:
            gc += 1
        elif g == gear and gear_cnt in [0, cnt]:
            gc = gear_cnt
        self._gear, self._gear_count, self._velocity = g, gc, next_velocity
        return g, gc

    def __call__(self, dt, desired_velocity, slope=0, update=True):
        from .simulation import gear_for_speed_profiles, accMFC, correct_acc_clutch_on

        g, gc = gear_for_speed_profiles(
            self.gs, self._velocity, self._gear, self._gear_count
        )
        self.g = g

        a = correct_acc_clutch_on(
            gc,
            accMFC(
                self._velocity,
                self.driver_style,
                desired_velocity,
                self.curves[g - 1],
                self.curves_dec[g - 1],
            ),
            self.transmission,
        )
        v = self._velocity + a * dt

        road_loads = estimate_f_coefficients(
            self.vehicle_mass, self.type_of_car, self.car_width, self.car_height
        )

        if self.gearbox_type == "manual":
            veh_params = self.hardcoded_params.params_gearbox_losses["Manual"]
        else:
            veh_params = self.hardcoded_params.params_gearbox_losses["Automatic"]

        n_wheel_drive = self.car_type

        # The power on wheels in kW
        veh_wheel_power = func.calculate_wheel_power(
            v, a, road_loads, self.vehicle_mass, slope
        )

        # The speed on the wheels in [RPM]
        veh_wheel_speed = func.calculate_wheel_speeds(v, self.r_dynamic)

        # # The torque on the wheels in [N*m]
        veh_wheel_torque = func.calculate_wheel_torques(
            veh_wheel_power, veh_wheel_speed
        )

        # Calculates final drive speed in RPM
        final_drive_speed = func.calculate_final_drive_speeds_in(
            veh_wheel_speed, self.final_drive
        )

        # Final drive torque losses [N*m].
        final_drive_torque_losses = func.calculate_final_drive_torque_losses_v1(
            n_wheel_drive,
            veh_wheel_torque,
            self.final_drive,
            self.hardcoded_params.final_drive_efficiency,
        )

        # Final drive torque in [N*m].
        final_drive_torque_in = func.calculate_final_drive_torques_in(
            veh_wheel_torque, self.final_drive, final_drive_torque_losses
        )

        final_drive_power_in = (
            final_drive_torque_in * final_drive_speed * math.pi / 30 / 1000
        )

        gear_box_speeds_in = func.calculate_gear_box_speeds_in_v1(
            g, final_drive_speed, self.gear_box_ratios, 0
        )
        self.gear_box_speeds_in = gear_box_speeds_in

        gearbox_params = func.create_gearbox_params(veh_params, self.engine_max_torque)

        gear_box_torques_in = func.gear_box_torques_in(
            self.hardcoded_params.min_engine_on_speed,
            final_drive_torque_in,
            gear_box_speeds_in,
            final_drive_speed,
            gearbox_params,
            gc,
        )
        self.gear_box_torques_in = gear_box_torques_in

        gear_box_power_in = (
            2 * math.pi * gear_box_torques_in * gear_box_speeds_in / 60000
        )
        self.gear_box_power_in = gear_box_power_in

        if update:
            self._gear, self._gear_count, self._velocity = g, gc, v
        return (
            g,
            gc,
            v,
            a,
            final_drive_speed,
            gear_box_speeds_in,
            veh_wheel_torque,
            final_drive_torque_in,
            gear_box_torques_in,
            veh_wheel_power,
            final_drive_power_in,
            gear_box_power_in,
        )

    def redefine_ds(self, dt, desired_velocity, ids_new, update=True):
        from .simulation import gear_for_speed_profiles, accMFC, correct_acc_clutch_on

        g, gc = gear_for_speed_profiles(
            self.gs, self._velocity, self._gear, self._gear_count
        )

        a = correct_acc_clutch_on(
            gc,
            accMFC(
                self._velocity,
                ids_new,
                desired_velocity,
                self.curves[g - 1],
            ),
            self.transmission,
        )
        v = self._velocity + a * dt
        s = self.position + self._velocity * dt + 0.5 * a * dt**2

        if update:
            self._gear, self._gear_count, self._velocity, self.position = g, gc, v, s
        return g, s, v, a

    def fuel_engine_model(self, g, gear_box_powers_in, sim_step, gear_box_speeds_in):
        lower_heating_value = self.hardcoded_params.LHV[self.fuel_type]

        engine_power_range = gear_box_powers_in - self.electric_motor_power_range

        fuel_range = [
            self.calculate_fuel_consumption(
                g,
                sim_step,
                gear_box_speeds_in,
                engine_power_range[i],
                optimisation=False,
            )[0]
            for i in range(len(engine_power_range))
        ]
        fuel_power_range = np.array(fuel_range) * lower_heating_value / 1000 / sim_step
        fuel_power_range[engine_power_range < 0] = np.inf

        return fuel_power_range, engine_power_range

    def calculate_drive_battery_currents(self, electric_motor_power_in):
        battery_power = (
            electric_motor_power_in
            * np.where(
                electric_motor_power_in < 0,
                self.motor_efficiency,
                1 / self.motor_efficiency,
            )
            * 1000
        )
        delta = (
            self.drive_battery_voltage**2
            - 4 * self.drive_battery_internal_resistance * battery_power
        )
        if delta < 0:
            delta = 0
        delta_sqrt = np.sqrt(delta)
        curr = (
            (self.drive_battery_voltage - delta_sqrt)
            / 2
            / self.drive_battery_internal_resistance
        )
        return curr

    def calculate_drive_battery_state_of_charge(
        self, electric_motor_power_in, sim_step
    ):
        prev = self.previous_drive_battery_state_of_charge

        drive_battery_electric_current = self.calculate_drive_battery_currents(
            electric_motor_power_in
        )
        diff = drive_battery_electric_current * sim_step / 3600
        diff /= self.drive_battery_capacity / 100

        return (
            prev - diff,
            self.drive_battery_voltage
            * drive_battery_electric_current
            / 1000
            * sim_step,
        )

    def calculate_ecms_s(self, dsoc=10, k=3, l=2.3):
        ecms_s = l + (
            (
                (
                    self.drive_battery_initial_state_of_charge
                    - self.previous_drive_battery_state_of_charge
                )
                / dsoc
            )
            ** k
        )

        return ecms_s

    def power_split(self, g, gear_box_powers_in, sim_step, gear_box_speeds_in):
        fuel_power_range, engine_power_range = self.fuel_engine_model(
            g, gear_box_powers_in, sim_step, gear_box_speeds_in
        )
        ecms_s = self.calculate_ecms_s()

        fuel_power_range[
            (engine_power_range) > self.full_load_curve(gear_box_speeds_in)
        ] = np.inf
        drive_battery_electric_powers_range = (
            self.drive_battery_electric_powers_range.copy()
        )
        drive_battery_electric_powers_range[
            (
                self.electric_motor_power_range
                > self.motor_full_load_curve(gear_box_speeds_in)
            )
            | (
                self.electric_motor_power_range
                < -self.motor_full_load_curve(gear_box_speeds_in)
            )
        ] = np.inf

        h = fuel_power_range + ecms_s * self.drive_battery_electric_powers_range
        # h[(self.electric_motor_power_range>self.motor_full_load_curve(gear_box_speeds_in))
        #   |(self.electric_motor_power_range<-self.motor_full_load_curve(gear_box_speeds_in))] = np.inf

        if all(np.isinf(h)):
            fuel_engine_power_in = 0
            electric_motor_power_in = gear_box_powers_in
        else:
            min_value = np.min(h)
            ind = np.where(h == min_value)[0][0]
            fuel_engine_power_in = engine_power_range[ind]
            electric_motor_power_in = self.electric_motor_power_range[ind]

        if gear_box_powers_in < 0:
            fuel_engine_power_in = 0
            electric_motor_power_in = gear_box_powers_in

        return fuel_engine_power_in, electric_motor_power_in

    def calculate_fuel_consumption(
        self, gear, sim_step, gear_box_speeds_in, gear_box_powers_in, optimisation=True
    ):
        if self.fuel_mode == "electric engine":
            fuel_engine_power_in = 0
            electric_motor_power_in = gear_box_powers_in
            fc = 0
            co2 = 0
            (
                soc,
                drive_battery_electric_power,
            ) = self.calculate_drive_battery_state_of_charge(
                electric_motor_power_in,
                sim_step,
            )
            self.previous_drive_battery_state_of_charge = soc
            return (
                fc,
                fuel_engine_power_in,
                electric_motor_power_in,
                soc,
                co2,
                drive_battery_electric_power,
            )

        fuel_engine_power_in = gear_box_powers_in
        electric_motor_power_in = 0
        if optimisation and self.fuel_mode == "hybrid":
            fuel_engine_power_in, electric_motor_power_in = self.power_split(
                gear, gear_box_powers_in, sim_step, gear_box_speeds_in
            )

        br_eff_pres = func.calculate_brake_mean_effective_pressures(
            gear_box_speeds_in,
            fuel_engine_power_in,
            self.fuel_eng_capacity,
            self.hardcoded_params.min_engine_on_speed,
        )

        engine_cm = func.mean_piston_speed(gear_box_speeds_in, self.fuel_engine_stroke)

        params = func.parameters(
            self.max_power, self.fuel_eng_capacity, self.fuel_type, self.fuel_turbo
        )
        fuel_A, fuel_B, fuel_C = func.calculate_fuel_ABC(
            params, engine_cm, br_eff_pres, 100
        )

        # if br_eff_pres > 20:
        #     # Control for unrealistic Break Mean Effective Pressure values.
        #     print('BMEP> %.2f bar, EngineCM: %.2f, Gear: %d : Check out the MFC output. The engine will blow up!!!!' % (
        #         br_eff_pres, engine_cm, gear))

        if br_eff_pres > 0:  # initially: -0.5
            # Fuel mean effective pressure
            VMEP = func.calculate_VMEP(fuel_A, fuel_B, fuel_C)
        else:
            VMEP = 0

        lower_heating_value = self.hardcoded_params.LHV[self.fuel_type]

        # Fuel consumption in grams.
        fc = func.calc_fuel_consumption(
            VMEP,
            self.fuel_eng_capacity,
            lower_heating_value,
            gear_box_speeds_in,
            sim_step,
        )

        fuel_carbon_content = self.hardcoded_params.CARBON_CONTENT[self.fuel_type]
        co2 = fc * fuel_carbon_content

        # calculate drive battery state of charge
        if optimisation:
            (
                soc,
                drive_battery_electric_power,
            ) = self.calculate_drive_battery_state_of_charge(
                electric_motor_power_in,
                sim_step,
            )
            self.previous_drive_battery_state_of_charge = soc
            return (
                fc,
                fuel_engine_power_in,
                electric_motor_power_in,
                soc,
                co2,
                drive_battery_electric_power,
            )

        return fc, fuel_engine_power_in, electric_motor_power_in
