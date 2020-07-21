from django.urls import path

from app.views import LabsAndPricesAPIView, TestDescriptionListAPIView, TimeSlotListAPIView, AddressViewSet, \
    PaymentStateAPIView, TestRequestAPIView


urlpatterns = [
    path('labs-and-prices/', LabsAndPricesAPIView.as_view()),
    path('tests/', TestDescriptionListAPIView.as_view()),
    path('time-slots/', TimeSlotListAPIView.as_view()),
    path('test-requests/', TestRequestAPIView.as_view()),
    path('payment-state/<int:pk>/', PaymentStateAPIView.as_view()),
    path('addresses/', AddressViewSet.as_view({'get': 'get', 'post': 'post'}))
]
