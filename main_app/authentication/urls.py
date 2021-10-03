from django.urls import path
from .views import CustomUserView, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserView.as_view()),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view())
]
