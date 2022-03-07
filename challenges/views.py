from django.shortcuts import render, redirect
from .models import Challenge, Answer

# Create your views here.
def answer(request, pk):
    challenge = Challenge.objects.filter(pk=pk).first()
    if request.user.is_authenticated:
        user_answer = challenge.answer_set.filter(user=request.user).first()
    else:
        user_answer = None
    if request.method == "POST":
        answer_data = request.POST.get("answer")
        answer = Answer(challenge=challenge, content=answer_data, user=request.user)
        answer.save()
        return redirect("challenge-answer", challenge.id)
    return render(request, "challenges/answer.html", {"title": "Answer Challenge", "challenge": challenge, "answer": user_answer})

def last_challenge(request, pk):
    challenge = Challenge.objects.filter(pk=pk).first()
    if request.user.is_authenticated:
        user_answer = challenge.answer_set.filter(user=request.user).first()
    else:
        user_answer = None
    return render(request, "challenges/last_challenge.html", {"title": "Last Challenge", "challenge": challenge, "answer": user_answer})
