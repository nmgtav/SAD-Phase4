from django.urls import path

from app.views import LabsAndPricesAPIView, TestDescriptionListAPIView, TimeSlotListAPIView



urlpatterns = [
    path('labs-and-prices/', LabsAndPricesAPIView.as_view()),
    path('tests/', TestDescriptionListAPIView.as_view()),
    path('time-slots/', TimeSlotListAPIView.as_view()),

]
