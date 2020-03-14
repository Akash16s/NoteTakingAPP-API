from django.urls import path, include
from .views import *

urlpatterns = [
    path('', getNote.as_view(), name='get'),
    path('write/', takeNote.as_view(), name='take'),
    path('signup/', registration.as_view(), name="signup"),
    path('login/', login.as_view(), name="login")
]
