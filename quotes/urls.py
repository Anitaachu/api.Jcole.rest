from django.urls import path, include
# from quotes import urls as quotes_urls
from .views import ColeView




urlpatterns = [
    path("cole/", ColeView.as_view(), name="cole-quotes")
]
