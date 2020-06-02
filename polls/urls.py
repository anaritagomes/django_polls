from django.urls import path

from . import views

app_name = 'polls'

# Generic views - index, detail and results are similar
urlpatterns = [
    # index
    path('', views.IndexView.as_view(), name='index'),
    # detail
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # question id
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
