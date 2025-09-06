from django.contrib import admin
from django.urls import path
from hackathon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', views.chat_with_openai, name="chat"),
]
