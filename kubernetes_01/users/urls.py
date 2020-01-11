from django.urls import path
from .views import HelloKubernetesApiView

app_name = 'users'

urlpatterns = [

	path('users', HelloKubernetesApiView.as_view(), name='get-users')
]