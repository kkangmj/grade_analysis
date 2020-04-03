from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import FileSerializer


class FileUploadView(APIView):
    # FileUploadParser는 JSONParser와 비슷한 역할을 함.
    parser_class = (FileUploadParser, )

    # 파일 생성(업로드)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        # 여기서 data 값을 다룰 수 있도록 받아와야 함. !!!
        # 일단 리액트 공부를 좀 해야할듯... 2주 뒤 이 프로젝트로 돌아와야지...

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
