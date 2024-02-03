from django.urls import path
from .views import PredictionAPIView

urlpatterns = [
    path('', PredictionAPIView.as_view(), name="Predict Parkinson's Disease"),
]
