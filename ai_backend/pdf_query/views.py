from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .pdf_reader import analyze_pdf
import os
import uuid

@csrf_exempt
def analyze_pdf_view(request):
    if request.method == "POST":
        try:
            query = request.POST.get("query")
            file = request.FILES.get("file")

            if not query or not file:
                return JsonResponse({"error": "Query and PDF file are required."}, status=400)

            # Ensure the data folder exists
            upload_dir = os.path.join("pdf_query", "data")
            os.makedirs(upload_dir, exist_ok=True)

            # Save file
            unique_filename = f"{uuid.uuid4().hex}_{file.name}"
            pdf_path = os.path.join(upload_dir, unique_filename)
            with open(pdf_path, "wb+") as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            # Analyze
            result = analyze_pdf(query, pdf_path)

            # Delete file only if processing was successful
            if not result.get("error"):
                os.remove(pdf_path)

            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({"error": f"Server exception: {str(e)}"}, status=500)

    return JsonResponse({"error": "Only POST requests allowed."}, status=405)
