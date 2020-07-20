from django.urls import path

from app.views import GetListOfLabsAndPrices, TestDescriptionListAPIView, AddressViewSet


urlpatterns = [
    path('labs-and-prices/', GetListOfLabsAndPrices.as_view()),
    path('tests/', TestDescriptionListAPIView.as_view()),
    path('addresses/', AddressViewSet.as_view({'get': 'list', 'post': 'create'}))
]
