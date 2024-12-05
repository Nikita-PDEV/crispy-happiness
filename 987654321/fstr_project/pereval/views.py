from rest_framework import status  
from rest_framework.decorators import api_view  
from rest_framework.response import Response  
from .serializers import PerevalSerializer  

@api_view(['POST'])  
def submit_data(request):  
    serializer = PerevalSerializer(data=request.data)  
    if serializer.is_valid():  
        pereval = serializer.save()  
        return Response({'id': pereval.id}, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)