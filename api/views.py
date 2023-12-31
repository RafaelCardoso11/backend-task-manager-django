
from django.http import JsonResponse
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model

# Create your views here.
User = get_user_model()
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if(user):
            user_from_db = User.objects.get(username=username)
        
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)
            }
            payload = {
                'tokens': tokens,
                'user': {
                    'email': user_from_db.email,
                    'username': user_from_db.username,
                }
              
            }
            return Response(payload)
           
        return Response({ 'message': 'Username ou senha inválidos'}, status=400)
    
class UserRegistrationView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
            }
            response_data = {
                'tokens': tokens,
                'user':  {
                    'username': serializer.data['username'],
                    'email': serializer.data['email']
                    },
                'message': 'Registrado com sucesso!',
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        # Filtra as tarefas apenas para o usuário autenticado
        return Task.objects.filter(user=self.request.user)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
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
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        # Filtra as tarefas apenas para o usuário autenticado
        return Task.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Garante que a tarefa seja atualizada apenas pelo usuário autenticado
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        # Garante que a tarefa seja excluída apenas pelo usuário autenticado
        instance.delete()
        
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
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        response_data = {
            'message': 'Tarefa recuperada com sucesso',
            'data': serializer.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
class CompleteMultipleTasksView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def patch(self, request):
        data = request.data
        updated_tasks = []
        
        for data in data["taskCompletions"]:
            task_id = data["taskId"]
            completed = data["completed"]
            updated_task_id = self.update_task_completion_status(task_id, completed)
            if updated_task_id != 0:
                updated_tasks.append(updated_task_id)
        if not updated_tasks:    
            return Response({"message": "Tarefas não encontradas"},status=status.HTTP_404_NOT_FOUND)
        
        data_tasks_updated = self.find_by_ids(updated_tasks)
        response_data = {
            "data": data_tasks_updated,
            "message": "Conclusão das Tarefas atualizadas com sucesso!"
        }
        return Response(response_data)

    def update_task_completion_status(self, id, completed):
        return Task.objects.filter(id=id).update(completed=completed)
    
    def find_by_ids(self, ids):
        return Task.objects.filter(id__in=ids).values()
       
        
        