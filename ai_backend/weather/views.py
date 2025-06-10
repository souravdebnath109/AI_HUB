from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .agent import get_weather_response

@csrf_exempt
def weather_query(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            question = body.get("question", "")
            if not question:
                return JsonResponse({"error": "No question provided."}, status=400)

            answer = get_weather_response(question)
            return JsonResponse({"answer": answer})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"message": "Send a POST request with 'question'"})
