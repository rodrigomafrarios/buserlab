from rest_framework import routers, serializers,viewsets
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ('id','title','text','datetime')