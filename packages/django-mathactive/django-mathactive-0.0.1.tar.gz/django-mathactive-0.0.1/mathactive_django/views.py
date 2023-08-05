import json
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mathactive_django.microlessons.num_one import process_user_message

@csrf_exempt
@require_http_methods(["POST"])
def start_quiz(request):
    data = json.loads(request.body)
    user_id = data["user_id"]
    message = data["message_text"]

    return JsonResponse(process_user_message(user_id, message))
