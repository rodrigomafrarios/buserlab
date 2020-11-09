from django.http.response import JsonResponse
from .models import Register
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import datetime

@api_view(['GET'])
def list(request):
        registers = Register.objects.all()
        serializer = RegisterSerializer(registers, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view(['POST'])
def create(request):
        payload = request.POST
        
        #is title or text are empty?
        if not payload['title'] or not payload['text']:
                return JsonResponse({'error':'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
                register = Register.objects.create(
                        title=payload['title'],
                        text=payload['text']
                )
                serializer = RegisterSerializer(register)
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        except Exception:
                return JsonResponse({'error':'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def update(request,id=int):
        payload = request.POST
        
        #is title or text are empty?
        if not payload['title'] or not payload['text']:
                return JsonResponse({'error':'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
                register = Register.objects.filter(id=id)
                register.update(title=payload['title'],text=payload['text'],updated_at=datetime.now())
                return JsonResponse(payload, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
                print('exception',e)
                return JsonResponse({'error':'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def remove(request,id=int):
        try:
                register = Register.objects.filter(id=id)
                register.delete()
                return JsonResponse({'status':'deleted'}, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
                print('exception',e)
                return JsonResponse({'error':'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)