from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status


class TodoListAPI(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class TodoCreateAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()

        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)


class TodoRetrieveAPI(APIView):
    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = TodoSerializer(todo)

        return Response(serializer.data)


class TodoUpdateAPI(APIView):
    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


class TodoDeleteAPI(APIView):
    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response(
                {"error": "해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
