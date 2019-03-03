from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # <domain>/polls/ (prepended for polls app in polling_project)
    path("", views.IndexView.as_view(), name="index"),
    # <domain>/polls/16/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # <domain>/polls/16/vote/
    path("<int:question_id>/vote", views.vote, name="vote"),
    # <domain>/polls/16/results/
    path("<int:pk>/results", views.ResultsView.as_view(), name="results"),
]
