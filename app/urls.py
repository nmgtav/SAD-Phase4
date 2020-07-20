from django.urls import path

from app.views import GetListOfLabsAndPrices, TestDescriptionListAPIView


urlpatterns = [
    path('labs-and-prices/', GetListOfLabsAndPrices.as_view()),
    path('tests/', TestDescriptionListAPIView.as_view()),
]
