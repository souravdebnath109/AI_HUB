from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .langchain_agent import run_conversion_agent

@csrf_exempt
def convert_currency(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            amount = float(data["amount"])
            from_currency = data["from_currency"]
            to_currency = data["to_currency"]

            result = run_conversion_agent(amount, from_currency, to_currency)
            return JsonResponse({"converted_amount": result}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST allowed"}, status=405)
