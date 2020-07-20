from django.urls import path

from app.views import LabsAndPricesAPIView, TestDescriptionListAPIView, TimeSlotListAPIView, AddressViewSet


urlpatterns = [
    path('labs-and-prices/', LabsAndPricesAPIView.as_view()),
    path('tests/', TestDescriptionListAPIView.as_view()),
    path('time-slots/', TimeSlotListAPIView.as_view()),
    path('addresses/', AddressViewSet.as_view({'get': 'list', 'post': 'create'}))
]
