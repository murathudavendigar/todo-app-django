from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializers import TodoSerializers
# Create your views here.

class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers