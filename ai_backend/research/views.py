from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .summery_generator import generate_summary
@csrf_exempt
def summarize_topic(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            topic = data.get("topic", "")
            style = data.get("style", "simple")
            length = data.get("length", "Short")

            if not topic.strip():
                return JsonResponse({"error": "Topic is required."}, status=400)

            summary = generate_summary(topic, style, length)
            return JsonResponse({"summary": summary})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
