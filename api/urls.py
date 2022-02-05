from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    # path('test/', Test.as_view()),
    path('v1/games/', GameCreateView.as_view(),name='create-games' ),
    path('v1/best_value_games/', BestValueView.as_view(),name='best-value-games' ),    
    path('v1/status/', DbStatusView.as_view(), name='db-status')
]