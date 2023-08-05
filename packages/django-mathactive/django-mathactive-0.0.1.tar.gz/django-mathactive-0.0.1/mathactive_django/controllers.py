from .models import UserData

def get_user_data(user_id):
    user = UserData.objects.filter(user_id=user_id).first()
    if user is None:
        return {}
    return serialize_user(user)


def update_user_data(user_id, skill_score=None, state=None, answer=None):
    user = UserData.objects.filter(user_id=user_id).first()
    if user is None:
        return None

    if skill_score is not None:
        user.skill_score = skill_score
    if state is not None:
        user.state = state
    if answer is not None:
        user.answer = answer
    user.save()
    return user


def serialize_user(user):
    user_data =  {
        "user_id": user.user_id,
        "skill_score": user.skill_score,
        "state": user.state,
    }
    if user.answer is not None:
        user_data["answer"] = user.answer
    return user_data
