from django.conf.urls import url

from app.views import GetListOfLabsAndPrices


urlpatterns = [
    url(r'^get-list-of-labs-and-prices/?$', GetListOfLabsAndPrices.as_view()),
]
