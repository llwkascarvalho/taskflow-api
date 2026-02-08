from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def task_list(request):
    return Response({
        "message": "Task API is working!",
        "tasks": []
    })