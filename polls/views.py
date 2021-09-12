from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question,Choice


# Create your views here.
# def index(request):
#       return HttpResponse("This is my index")

def index(request):
      questions = Question.objects.all()
      context = {
            "question_list":questions
      }
      return render(request,"polls/index.html",context)

def detail(request, ques_id):
      question = get_object_or_404(Question, pk=ques_id)
      context = {
          "question": question
      }
      return render(request,"polls/detail.html",context)

def vote(request,ques_id):
      question = get_object_or_404(Question, pk=ques_id)
      try:
       choice_id= request.POST['choice']
       choice_obj= question.choice_set.get(pk=choice_id)

      except (KeyError,Choice.DoesNotExist):
            return render(request,'polls/detail.html',{'question': question,'error-message':'something went wrong!'})
      else:
            choice_obj.votes += 1
            choice_obj.save()

      return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


def results(request,ques_id):
      question= get_object_or_404(Question, pk=ques_id)
      context = {
            "question": question
      }
      return render(request, "polls/results.html", context)