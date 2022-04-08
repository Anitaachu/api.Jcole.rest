from django.shortcuts import render
from .models import Cole
from .serializers import ColeSerializer
from rest_framework.generics import ListAPIView
import random



# Generate random 
def pick_random_object():
   return random.randrange(1, Cole.objects.all().count() + 1)


class ColeView(ListAPIView):
    serializer_class = ColeSerializer
    model = Cole
    
    """
    Method to get random id from model
    """
    
    def get_queryset(self):
        cole_pk = Cole
        # return Cole.objects.all().filter(pk=id)
        return Cole.objects.all().filter(id = pick_random_object())

        
        