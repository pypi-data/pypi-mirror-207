from .utils import convert_sequence_to_string


def generate_question_data(start, stop, step, question_num=1):
    """returns question by provided number with filled parameters

    >>> generate_question_data(1, 4, 1)
    {'question': 'What number comes 1 number after 3?\n1, 2, 3',
    'answer': 4,
    'start': 1,
    'stop': 4,
    'step': 1}
    >>> generate_question_data(1, 12, 1)
    {'question': 'What number comes 1 number after 11?\n1, 2, 3 ... 9, 10, 11',
    'answer': 12,
    'start': 1,
    'stop': 12,
    'step': 1}

    parameters
    ----------
    :start: current number
    :stop: stop value
    :step: interval between current and next numbers
    :question_num: question number"""
    seq = convert_sequence_to_string(start, stop, step)
    question_stop = stop - step
    questions = [
        f"Let's practice counting   {convert_sequence_to_string(start, stop, step, sep='... ')}   After {question_stop}, what is the next number you will count?\n{seq}",
        f"What number comes {step} number after {question_stop}?\n{seq}",
        f"We're counting by {step}s.  What number is 1 after {question_stop}?\n{seq}",
        f"What is {step} number up from {question_stop}?\n{seq}",
        f"If we count up {step} from {question_stop}, what number is next?\n{seq}",
    ]
    questions_data = []
    for quest in questions:
        questions_data.append(
            {
                "question": quest,
                "answer": stop,
                "start": start,
                "stop": stop,
                "step": step,
            }
        )
    return questions_data[question_num]
