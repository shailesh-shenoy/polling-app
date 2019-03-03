"""Process request on call from Url Handler, return HttpResponse."""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# Create your views here.


# def index(request):
#     """Get latest questions from model, return polls/index template."""

#     latest_question_list = Question.objects.order_by("-publication_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-publication_date")[:5]


class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question
    # def detail(request, question_id):
    #     """Get question details for corresponding question_id, return polls/detail template."""

    # question = get_object_or_404(Question, pk=question_id)
    # context = {"question": question}
    # return render(request, "polls/detail.html", context)


class ResultsView(generic.DetailView):
    template_name = "polls/results.html"
    model = Question


# def results(request, question_id):
#     """Get question for coresponding question id, return poll/results template"""

#     question = get_object_or_404(Question, pk=question_id)
#     context = {"question": question}
#     return render(request, "polls/results.html", context)


def vote(request, question_id):
    """Get choice from post data, increase vote count and redirect to polls/results template"""

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay voting page with error
        context = {"question": question, "error_message": "You didn't select a choice"}
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # return HttpResponseRedirect o prevent form from posting twice
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
