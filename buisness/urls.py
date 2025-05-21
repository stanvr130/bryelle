from django.urls import path
from buisness.views import BusinessView
urlpatterns = [
    path('', BusinessView.as_view())
]