from django.urls import path
from .views import sign_up, live_matches


urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('live-matches/', live_matches, name='live-scores')
]
