from django.urls import path
from .views import CustomUserView, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserView.as_view(), name='register'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view())
]
