from django.urls import path
from .views import ExampleView

urlpatterns = [
    path('examples/', ExampleView.as_view(), name='examples'),
]
