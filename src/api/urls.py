from django.urls import path, include
from .views import *

urlpatterns = [
    path('', takeNote.as_view(), name='takenote')
]
