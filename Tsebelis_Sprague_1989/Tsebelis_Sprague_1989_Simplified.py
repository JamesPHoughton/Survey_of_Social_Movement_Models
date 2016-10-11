
"""
Python model Tsebelis_Sprague_1989_Simplified.py
Translated using PySD version 0.6.4
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.functions import cache
from pysd import functions

_subscript_dict = {}

_namespace = {
    'Decrease in Revolution': 'decrease_in_revolution',
    'TIME STEP': 'time_step',
    'Increase in Coersion': 'increase_in_coersion',
    'FINAL TIME': 'final_time',
    'Decrease in Coersion': 'decrease_in_coersion',
    'Increase in Revolution': 'increase_in_revolution',
    'Natural Decrease in Coersion': 'natural_decrease_in_coersion',
    'TIME': 'time',
    'Coercive Influence on Revolution g': 'coercive_influence_on_revolution_g',
    'Influence of Revolution on Coersion h': 'influence_of_revolution_on_coersion_h',
    'Coersion C': 'coersion_c',
    'Natural Decrease in Coersion Parameter k': 'natural_decrease_in_coersion_parameter_k',
    'Natural Decrease in Revolution': 'natural_decrease_in_revolution',
    'Decrease in Revolution due to Coersion': 'decrease_in_revolution_due_to_coersion',
    'Exogenous increase in Revolution beta': 'exogenous_increase_in_revolution_beta',
    'Time': 'time',
    'SAVEPER': 'saveper',
    'Revolution R': 'revolution_r',
    'Natural Decrease in Revolution Parameter d': 'natural_decrease_in_revolution_parameter_d',
    'INITIAL TIME': 'initial_time',
    'Increase in Coersion due to Revolution': 'increase_in_coersion_due_to_revolution'}


@cache('run')
def coercive_influence_on_revolution_g():
    """
    Coercive Influence on Revolution g
    ----------------------------------
    (coercive_influence_on_revolution_g)
    [-1,1]

    """
    return 0.025


@cache('run')
def initial_time():
    """
    INITIAL TIME
    ------------
    (initial_time)
    Month
    The initial time for the simulation.
    """
    return 0


@cache('step')
def increase_in_coersion_due_to_revolution():
    """
    Increase in Coersion due to Revolution
    --------------------------------------
    (increase_in_coersion_due_to_revolution)


    """
    return influence_of_revolution_on_coersion_h() * revolution_r()


def _init_revolution_r():
    """
    Implicit
    --------
    (_init_revolution_r)
    See docs for revolution_r
    Provides initial conditions for revolution_r function
    """
    return 1


@cache('run')
def time_step():
    """
    TIME STEP
    ---------
    (time_step)
    Month [0,?]
    The time step for the simulation.
    """
    return 1


@cache('run')
def natural_decrease_in_revolution_parameter_d():
    """
    Natural Decrease in Revolution Parameter d
    ------------------------------------------
    (natural_decrease_in_revolution_parameter_d)


    """
    return 0.001


@cache('run')
def final_time():
    """
    FINAL TIME
    ----------
    (final_time)
    Month
    The final time for the simulation.
    """
    return 100


@cache('run')
def natural_decrease_in_coersion_parameter_k():
    """
    Natural Decrease in Coersion Parameter k
    ----------------------------------------
    (natural_decrease_in_coersion_parameter_k)


    """
    return 0.001


@cache('step')
def _drevolution_r_dt():
    """
    Implicit
    --------
    (_drevolution_r_dt)
    See docs for revolution_r
    Provides derivative for revolution_r function
    """
    return increase_in_revolution() - decrease_in_revolution()


@cache('step')
def natural_decrease_in_revolution():
    """
    Natural Decrease in Revolution
    ------------------------------
    (natural_decrease_in_revolution)


    """
    return natural_decrease_in_revolution_parameter_d() * revolution_r()


@cache('step')
def increase_in_revolution():
    """
    Increase in Revolution
    ----------------------
    (increase_in_revolution)


    """
    return exogenous_increase_in_revolution_beta()


@cache('step')
def decrease_in_coersion():
    """
    Decrease in Coersion
    --------------------
    (decrease_in_coersion)


    """
    return natural_decrease_in_coersion()


@cache('step')
def coersion_c():
    """
    Coersion C
    ----------
    (coersion_c)


    """
    return _state['coersion_c']


@cache('run')
def exogenous_increase_in_revolution_beta():
    """
    Exogenous increase in Revolution beta
    -------------------------------------
    (exogenous_increase_in_revolution_beta)
    [-1,5]

    """
    return 0.025


@cache('run')
def influence_of_revolution_on_coersion_h():
    """
    Influence of Revolution on Coersion h
    -------------------------------------
    (influence_of_revolution_on_coersion_h)
    [-1,1]

    """
    return 0.25


@cache('step')
def _dcoersion_c_dt():
    """
    Implicit
    --------
    (_dcoersion_c_dt)
    See docs for coersion_c
    Provides derivative for coersion_c function
    """
    return increase_in_coersion() - decrease_in_coersion()


@cache('step')
def decrease_in_revolution_due_to_coersion():
    """
    Decrease in Revolution due to Coersion
    --------------------------------------
    (decrease_in_revolution_due_to_coersion)


    """
    return coercive_influence_on_revolution_g() * coersion_c()


def _init_coersion_c():
    """
    Implicit
    --------
    (_init_coersion_c)
    See docs for coersion_c
    Provides initial conditions for coersion_c function
    """
    return 1


@cache('step')
def natural_decrease_in_coersion():
    """
    Natural Decrease in Coersion
    ----------------------------
    (natural_decrease_in_coersion)


    """
    return natural_decrease_in_coersion_parameter_k() * coersion_c()


@cache('step')
def revolution_r():
    """
    Revolution R
    ------------
    (revolution_r)


    """
    return _state['revolution_r']


@cache('step')
def saveper():
    """
    SAVEPER
    -------
    (saveper)
    Month [0,?]
    The frequency with which output is stored.
    """
    return time_step()


@cache('step')
def increase_in_coersion():
    """
    Increase in Coersion
    --------------------
    (increase_in_coersion)


    """
    return increase_in_coersion_due_to_revolution()


@cache('step')
def time():
    """
    TIME
    ----
    (time)
    None
    The time of the model
    """
    return _t


@cache('step')
def decrease_in_revolution():
    """
    Decrease in Revolution
    ----------------------
    (decrease_in_revolution)


    """
    return natural_decrease_in_revolution() + decrease_in_revolution_due_to_coersion()


def time():
    return _t
functions.time = time
functions.initial_time = initial_time
