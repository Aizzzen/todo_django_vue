from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]
    filterset_fields = ['title', 'user', 'is_complete']
    search_fields = ['title']
    ordering_fields = ['is_complete', 'created_at', 'updated_at']
