from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # <domain>/polls/ (prepended for polls app in polling_project)
    path("", views.index, name="index"),
    # <domain>/polls/16/
    path("<int:question_id>/", views.detail, name="detail"),
    # <domain>/polls/16/vote/
    path("<int:question_id>/vote", views.vote, name="vote"),
    # <domain>/polls/16/results/
    path("<int:question_id>/results", views.results, name="results"),
]
