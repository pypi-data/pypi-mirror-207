from sentry_sdk.utils import BadDsn
from mathactive_django.controllers import get_user_data, update_user_data, serialize_user
from mathactive_django.generators import start_interactive_math
from mathactive_django.hints import generate_hint
from mathactive_django.models import UserData
try:
    from mathactive_django.logger import *
except BadDsn:
    pass


def process_user_message(user_id, message_text=""):
    """
    there are 2 possible states: question and hint, default is question
    Algorithm:
    1. load user by user id
    2. create new user in case he doesn't exist
    3. get student state, skill level and last answer result (right or wrong)
    4.
        4.1. If last state is question and last answer is wrong get user a hint
        4.2. If last state is question and last answer is right increase the skill_score and get new question
        4.3. If last state is hint and last answer is wrong decrease the skill_score and get user a new question
        4.4. If last state is hint and last answer is right leave the skill_score on the same level, but generate new question with same skill_score
    10. dump user
    """
    user_id = str(user_id)

    user_data = get_user_data(user_id)
    if user_data == {}:
        user_data = UserData(user_id=user_id, skill_score=0.01, state="question")
        user_data.save()
        user_data = serialize_user(user_data)
    state = user_data["state"]
    if (
        state == "hint"
        and "answer" in user_data
        and user_data["answer"] == int(message_text)
    ) or (
        state == "question"
        and (
            message_text == ""
            or "answer" in user_data
            and user_data["answer"] == int(message_text)
        )
    ):
        do_increase_skill_score = (
            "leave"
            if state == "hint" or state == "question" and message_text == ""
            else "increase"
        )
        output = start_interactive_math(
            user_data["skill_score"], do_increase_skill_score
        )
        user_data["state"] = "question"
    elif "answer" in user_data and user_data["answer"] != int(message_text):
        if state == "hint":
            do_increase_skill_score = "decrease"
            user_data["state"] = "question"
        elif state == "question":
            do_increase_skill_score = "leave"
            user_data["state"] = "hint"
        output = (
            start_interactive_math(user_data["skill_score"], do_increase_skill_score)
            if state == "hint"
            else generate_hint(**{"skill_score": user_data["skill_score"], "state": user_data["state"], "answer": user_data["answer"]})
        )

    user_data["answer"] = output["answer"]
    user_data["skill_score"] = output["skill_score"]
    update_user_data(user_data["user_id"], user_data["skill_score"], user_data["state"], user_data["answer"])

    text = output["text"]
    message_package = {
        "messages": [text],
        "input_prompt": message_text,
        "state": user_data["state"],
    }
    return message_package
