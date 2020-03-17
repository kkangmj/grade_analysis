from django.urls import path
from .views import *

urlpatterns = [
    # as_view() : 클래스형 뷰로 진입하기 위한 진입 메소드
    path('', FileUploadView.as_view())
]