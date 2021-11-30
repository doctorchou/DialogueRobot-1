from django.contrib import admin
from django.urls import path

from DiaRobot.view import handle_wx

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wx/', handle_wx)
]
