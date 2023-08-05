import numpy
import pandas
import random
from scipy.interpolate import interp1d
from typing import Literal
from pathlib import Path

DATA_DIR = Path(__file__).parent.absolute() / 'data'

def get_next_skill_score(
    skill_score,
    do_increase_skill_score: Literal["increase", "decrease", "leave"] = "leave",
):
    if do_increase_skill_score == "leave":
        for i in numpy.arange(0.03, 1, 0.05):
            i = round(i, 2)
            if round(i - 0.02, 2) <= skill_score <= round(i + 0.02, 2):
                i = 0.97 if str(i) == str(0.98) else i
                next_skill_score = round(
                    random.uniform(round(i - 0.02, 2), round(i + 0.02, 2)), 2
                )
                break
    elif do_increase_skill_score == "increase":
        if skill_score >= 0.95:
            next_skill_score = round(random.uniform(0.95, 0.99), 2)
        else:
            next_skill_score = round(
                random.uniform(skill_score + 0.01, skill_score + 0.05), 2
            )
    elif do_increase_skill_score == "decrease":
        if skill_score <= 0.05:
            next_skill_score = round(random.uniform(0.01, 0.05), 2)
        else:
            next_skill_score = round(
                random.uniform(skill_score - 0.05, skill_score - 0.01), 2
            )

    return next_skill_score


def generate_start_stop_step(
    skill_score: float, csv_file_path: str = f'{DATA_DIR}/difficulty_start_stop_step.csv'
):
    """generate start and step values interpolating results to function built from data from file"""
    df = pandas.read_csv(
        csv_file_path, delimiter=",", header=0, names=['skill_score', 'start', 'stop', 'step']
    )
    data_rows = df.loc[:]

    difficulties = [row_data["skill_score"] for _, row_data in data_rows.iterrows()]
    starts = [row_data["start"] for _, row_data in data_rows.iterrows()]
    stops = [row_data["stop"] for _, row_data in data_rows.iterrows()]
    steps = [row_data["step"] for _, row_data in data_rows.iterrows()]

    interp_start_func = interp1d(difficulties, starts)
    interp_stop_func = interp1d(difficulties, stops)
    interp_step_func = interp1d(difficulties, steps)
    start = round(float(interp_start_func(skill_score)))
    stop = round(float(interp_stop_func(skill_score)))
    step = round(float(interp_step_func(skill_score)))

    return {
        'start': start,
        'stop': stop,
        'step': step
    }


def convert_sequence_to_string(start, stop, step, sep=", "):
    """
    >>> convert_sequence_to_string(1, 11, 1, 10)
    '1, 2, 3, ... 8, 9, 10'
    >>> convert_sequence_to_string(1, 11, 1, 9)
    '1, 2, 3, 4, 5, 6, 7, 8, 9, 10'
    """
    num_steps = start_stop_step_to_num_steps(start, stop, step)
    if num_steps and num_steps >= 10:
        stop = start + num_steps * step
        num_seq = [str(num) for num in range(start, stop, step)]
        return sep.join(num_seq[:3]) + sep + "... " + sep.join(num_seq[-3:])
    num_seq = [str(num) for num in range(start, stop, step)]
    return sep.join(num_seq)


def start_stop_step_to_num_steps(start, stop, step):
    """
    >>> start_stop_step_to_num_steps(1, 11, 1)
    10
    >>> start_stop_step_to_num_steps(1, 12, 1)
    11
    """
    num_steps = abs((start - stop) // step)
    return num_steps
