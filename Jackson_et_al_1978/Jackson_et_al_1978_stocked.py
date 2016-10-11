
"""
Python model Jackson_et_al_1978_stocked.py
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
    'INITIAL TIME': 'initial_time',
    'TIME': 'time',
    'Intensity of Opposition Reaction to State Action b': 'intensity_of_opposition_reaction_to_state_action_b',
    'TIME STEP': 'time_step',
    'Coercive Authoritarianism': 'coercive_authoritarianism',
    'Manifest Conflict': 'manifest_conflict',
    'Baseline Conflict a': 'baseline_conflict_a',
    'FINAL TIME': 'final_time',
    'SAVEPER': 'saveper',
    'Time': 'time',
    'Baseline Coersion c': 'baseline_coersion_c',
    'Intensity of State Reaction to Opposition Action d': 'intensity_of_state_reaction_to_opposition_action_d'}


@cache('step')
def _dmanifest_conflict_dt():
    """
    Implicit
    --------
    (_dmanifest_conflict_dt)
    See docs for manifest_conflict
    Provides derivative for manifest_conflict function
    """
    return coercive_authoritarianism() * intensity_of_opposition_reaction_to_state_action_b()


def _init_coercive_authoritarianism():
    """
    Implicit
    --------
    (_init_coercive_authoritarianism)
    See docs for coercive_authoritarianism
    Provides initial conditions for coercive_authoritarianism function
    """
    return baseline_coersion_c()


@cache('step')
def _dcoercive_authoritarianism_dt():
    """
    Implicit
    --------
    (_dcoercive_authoritarianism_dt)
    See docs for coercive_authoritarianism
    Provides derivative for coercive_authoritarianism function
    """
    return manifest_conflict() * intensity_of_state_reaction_to_opposition_action_d()


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
def intensity_of_state_reaction_to_opposition_action_d():
    """
    Intensity of State Reaction to Opposition Action d
    --------------------------------------------------
    (intensity_of_state_reaction_to_opposition_action_d)


    """
    return 1.1


def _init_manifest_conflict():
    """
    Implicit
    --------
    (_init_manifest_conflict)
    See docs for manifest_conflict
    Provides initial conditions for manifest_conflict function
    """
    return baseline_conflict_a()


@cache('run')
def intensity_of_opposition_reaction_to_state_action_b():
    """
    Intensity of Opposition Reaction to State Action b
    --------------------------------------------------
    (intensity_of_opposition_reaction_to_state_action_b)


    """
    return 1.1


@cache('run')
def baseline_conflict_a():
    """
    Baseline Conflict a
    -------------------
    (baseline_conflict_a)


    """
    return 1


@cache('step')
def coercive_authoritarianism():
    """
    Coercive Authoritarianism
    -------------------------
    (coercive_authoritarianism)


    """
    return _state['coercive_authoritarianism']


@cache('run')
def baseline_coersion_c():
    """
    Baseline Coersion c
    -------------------
    (baseline_coersion_c)


    """
    return 1


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
def time():
    """
    TIME
    ----
    (time)
    None
    The time of the model
    """
    return _t


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


@cache('step')
def manifest_conflict():
    """
    Manifest Conflict
    -----------------
    (manifest_conflict)


    """
    return _state['manifest_conflict']


def time():
    return _t
functions.time = time
functions.initial_time = initial_time
