import copy
from typing import List, Union, Tuple, Optional
import numpy as np

import commonroad.geometry.transform
from commonroad.common.util import AngleInterval
from commonroad.common.validity import (
    is_valid_orientation,
    is_real_number_vector,
    is_real_number,
    ValidTypes,
    is_natural_number,
    is_positive,
)
from commonroad.geometry.shape import Shape
from commonroad.common.util import make_valid_orientation

__author__ = "Stefanie Manzinger, Christian Pek"
__copyright__ = "TUM Cyber-Physical Systems Group"
__credits__ = ["Priority Program SPP 1835 Cooperative Interacting Automobiles"]
__version__ = "2022.1"
__maintainer__ = "Stefanie Manzinger, Christian Pek"
__email__ = "commonroad@lists.lrz.de"
__status__ = "Released"

from commonroad.visualization.drawable import IDrawable
from commonroad.visualization.param_server import ParamServer
from commonroad.visualization.renderer import IRenderer
from commonocean.scenario.state import State



class Trajectory(IDrawable):
    """ Class to model the movement of an object over time. The states of the
    trajectory can be either exact or
    uncertain (see :class:`commonocean.scenario.state.State`); however,
    only exact time_step are allowed. """

    def __init__(self, initial_time_step: int, state_list: List[State]):
        """
        :param initial_time_step: initial time step of the trajectory
        :param state_list: ordered sequence of states over time representing
        the trajectory. It is assumed that
        the time discretization between two states matches the time
        discretization of the scenario.
        """
        self.initial_time_step: int = initial_time_step
        self.state_list: List[State] = state_list

    @property
    def initial_time_step(self) -> int:
        """ Initial time step of the trajectory."""
        return self._initial_time_step

    @initial_time_step.setter
    def initial_time_step(self, initial_time_step):
        assert isinstance(initial_time_step, int), (
            '<Trajectory/initial_time_step>: argument initial_time_step of '
            'wrong type. Expected type: %s. Got type: %s.'
            % (int, type(initial_time_step))
        )
        self._initial_time_step = initial_time_step

    @property
    def state_list(self) -> List[State]:
        """ List of states of the trajectory over time."""
        return self._state_list

    @state_list.setter
    def state_list(self, state_list):
        assert isinstance(state_list, list), (
            '<Trajectory/state_list>: argument state_list of wrong type. '
            'Expected type: %s. Got type: %s.' % (list, type(state_list))
        )
        assert len(state_list) >= 1, (
            '<Trajectory/state_list>: argument state_list must contain at least one state.'
            ' length of state_list: %s.' % len(state_list)
        )
        assert all(isinstance(state, State) for state in state_list), (
            '<Trajectory/state_list>: element of '
            'state_list is of wrong type. Expected type: '
            '%s.' % List[State]
        )
        assert all(
            is_natural_number(state.time_step)
            for state in state_list
            if hasattr(state, 'time_step')
        ), '<Trajectory/state_list>: Element time_step of each state must be an integer.'
        assert all(
            state_list[0].attributes == state.attributes for state in state_list
        ), (
            '<Trajectory/state_list>: all states must have the same attributes. Attributes of first state: %s.'
            % state_list[0].attributes
        )
        self._state_list = state_list
        assert self.state_list[0].time_step == self.initial_time_step, \
            f"state_list[0].time_step={self.state_list[0].time_step} != " \
            f"self.initial_time_step={self.initial_time_step}"

    @property
    def final_state(self) -> State:
        """ Final state of the trajectory."""
        return self._state_list[-1]

    def state_at_time_step(self, time_step: int) -> Union[State, None]:
        """
        Function to get the state of a trajectory at a specific time instance.

        :param time_step: considered time step
        :return: state of the trajectory at time_step
        """
        state = None
        if (
            self._initial_time_step
            <= time_step
            < self._initial_time_step + len(self._state_list)
        ):
            state = self._state_list[time_step - self._initial_time_step]
        return state

    def states_in_time_interval(self, time_begin: int, time_end: int) -> List[Union[State, None]]:
        """
        Function to get the states of a trajectory at a specific time interval.

        :param time_begin: first considered time step
        :param time_end: last considered time step
        :return: list of states
        """
        assert time_end >= time_begin
        return [self.state_at_time_step(time_step) for time_step in range(time_begin, time_end+1)]

    def translate_rotate(self, translation: np.ndarray, angle: float):
        """ First translates each state of the trajectory, then rotates each state of the trajectory around the
        origin.

        :param translation: translation vector [x_off, y_off] in x- and y-direction
        :param angle: rotation angle in radian (counter-clockwise)
        """
        assert is_real_number_vector(translation, 2), (
            '<Trajectory/translate_rotate>: argument translation is not '
            'a vector of real numbers of length 2.'
        )
        assert is_real_number(angle), (
            '<Trajectory/translate_rotate>: argument angle must be a scalar. '
            'angle = %s' % angle
        )
        assert is_valid_orientation(angle), (
            '<Trajectory/translate_rotate>: argument angle must be within the '
            'interval [-2pi,2pi]. angle = %s' % angle
        )

        for i in range(len(self._state_list)):
            self._state_list[i] = self._state_list[i].translate_rotate(
                    translation, angle)

    @classmethod
    def resample_continuous_time_state_list(cls, states: List[State],
                                            time_stamps_cont: np.ndarray,
                                            resampled_dt: float,
                                            num_resampled_states: int,
                                            initial_time_cont: float = 0) -> 'Trajectory':
        """
        This method resamples a given state list with continuous time vector in a fixed time resolution.
        The interpolation is done in a linear fashion.
        :param states: The list of states to interpolate
        :param time_stamps_cont: The vector of continuous time stamps (corresponding to the states)
        :param resampled_dt: Target time step length
        :param num_resampled_states: The resulting number of states. It must hold (t_0+N*dT) \\in time interval
        :param initial_time_cont: The initial continuous time stamp (default 0). It must hold t\\in time interval
        :return: The resampled trajectory
        """
        assert is_positive(
                resampled_dt), '<Trajectory/interpolate_state_list>: Time step size must be a positive number! ' \
                               'dT = {}'.format(resampled_dt)
        assert isinstance(states, list) and all(isinstance(x, State) for x in
                                                states), '<Trajectory/interpolate_state_list>: Provided state list ' \
                                                         'is not in the correct format! State list = {}'.format(
                states)
        assert is_real_number_vector(
                time_stamps_cont), '<Trajectory/interpolate_state_list>: Provided time vector is not in the ' \
                                   'correct format! time = {}'.format(
                time_stamps_cont)
        assert len(states) == len(
                time_stamps_cont), '<Trajectory/interpolate_state_list>: Provided time and state lists do not ' \
                                   'share the same length! Time = {} / States = {}'.format(
                len(time_stamps_cont), len(states))
        assert is_positive(num_resampled_states) and is_natural_number(
                num_resampled_states), '<Trajectory/interpolate_state_list>: Provided state horizon must be a ' \
                                       'positive Integer! N = {}'.format(
                num_resampled_states)
        assert is_real_number(
                initial_time_cont), '<Trajectory/interpolate_state_list>: Provided initial time must be a ' \
                                    'real number! t_0 = {}'.format(
                initial_time_cont)
        assert any(time_stamps_cont <= initial_time_cont) and any(
                initial_time_cont <= time_stamps_cont), '<Trajectory/interpolate_state_list>: Provided initial ' \
                                                        'time is not within time vector! t_0 = {}'.format(
                initial_time_cont)
        assert any(
                initial_time_cont + num_resampled_states * resampled_dt <= time_stamps_cont), \
            '<Trajectory/interpolate_state_list>: Provided end time is not within time vector! t_h = {}'.format(
                initial_time_cont + num_resampled_states * resampled_dt)

        slots = list()
        values = list()
        for s in State.__slots__:
            if hasattr(states[0], s):
                slots.append(s)
                values.append([])

        t_i = np.arange(initial_time_cont,
                        initial_time_cont + num_resampled_states * resampled_dt + resampled_dt,
                        resampled_dt)
        values_i = list()

        for s in slots:
            values = list()
            multiple = False
            for x in states:
                if hasattr(x, s):
                    val = getattr(x, s)
                    assert is_real_number(val) or is_real_number_vector(
                            val), '<Trajectory/interpolate_state_list>: Currently, this method only ' \
                                  'supports states with real numbers! val = {}'.format(
                            val)
                    if not multiple and hasattr(val, 'shape'):
                        if len(val) > 1:
                            multiple = True
                            for i in range(len(val)):
                                values.append([])
                    if multiple:
                        for i, v in enumerate(val):
                            values[i].append(v)

                    else:
                        values.append(val)
                else:
                    raise ValueError(
                            '<Trajectory/interpolate_state_list>: States do not share the same amount of variables!')

            if multiple:
                temp = list()
                for v in values:
                    temp.append(np.interp(t_i, time_stamps_cont, v))
                values_i.append(np.array(temp).transpose())

            else:
                values_i.append(np.interp(t_i, time_stamps_cont, values))

        states_new = list()
        for i in range(len(t_i)):
            variables = dict()
            for j, s in enumerate(slots):
                variables[s] = values_i[j][i]
            variables['time_step'] = i
            states_new.append(State(**variables))

        return cls(states_new[0].time_step, states_new)

    def __str__(self):
        traffic_str = '\n'
        traffic_str += 'Initial time step: {} \n'.format(self.initial_time_step)
        traffic_str += 'Number of states: {}\n'.format(len(self.state_list))
        traffic_str += 'State elements: {}'.format(
                self.state_list[0].attributes)
        return traffic_str

    def draw(self, renderer: IRenderer,
             draw_params: Union[ParamServer, dict, None] = None,
             call_stack: Optional[Tuple[str, ...]] = tuple()):
        renderer.draw_trajectory(self, draw_params, call_stack)
