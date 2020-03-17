from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer

# APIView 말고 ViewSet로 코드 바꿔볼까?
class FileUploadView(APIView):
    # FileUploadParser는 JSONParser와 비슷한 역할을 함.
    parser_class = (FileUploadParser, )

    # 파일 생성(업로드)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
