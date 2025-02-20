from django.http import JsonResponse
from .serializer import DrinkSerializer
from .models import Drink 


def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data}, safe=False)