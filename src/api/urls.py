from django.urls import path, include
from .views import *

urlpatterns = [
    path('', takeNote.as_view(), name='takenote'),
    path('signup/', registration.as_view(), name="signup"),
    path('login/', login.as_view(), name="login")
]
