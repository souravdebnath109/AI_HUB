from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .youtube_qa import run_youtube_qa

@csrf_exempt
def youtube_qa_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        video_url = data.get("video_url")
        question = data.get("question")

        try:
            answer = run_youtube_qa(video_url, question)
            return JsonResponse({"answer": answer})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Only POST method allowed"}, status=400)
