
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
    
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'data': serializer.data,
                'message': 'Tarefa criada com sucesso',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            'data': serializer.data,
            'totalCounts': queryset.count()
        }
        return JsonResponse(response_data)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Tarefa atualizada com sucesso',
                'data': serializer.data,
            }
        return JsonResponse(response_data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        response_data = {
            'message': 'Tarefa excluída com sucesso',
        }
        return JsonResponse(response_data)