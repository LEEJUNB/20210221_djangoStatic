from django.contrib import admin
from django.urls import path, include # include 추가하여 url 단순화
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('vision/',views.vision),
    path('service/', include('service.urls')), # service/로 시작하는 모든 url은 service앱의 urls.py에서 관리
    path('review/', include('review.urls')),
]
