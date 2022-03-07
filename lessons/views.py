from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Unit, Chapter
from challenges.models import Challenge
from django.contrib import messages
import os

# Create your views here.
def index(request):
    units = Unit.objects.all()
    challenge = Challenge.objects.all().last()
    previous_challenge = Challenge.objects.all().first()
    if challenge == previous_challenge:
        previous_challenge = None
    return render(request, "index.html", {"title": "Home", "units": units,
                                            "challenge": challenge, "last_challenge": previous_challenge})

def article(request):
    return render(request, "article.html", {"title": "Weekly Article"})

def chapter_index(request, pk):
    unit = Unit.objects.filter(pk=pk).first()
    chapters = unit.chapter_set.all()
    return render(request, "chapter_index.html", {"title": unit.title, "chapters": chapters})

def chapter(request, pk, s_no):
    unit = Unit.objects.filter(pk=pk).first()
    last_chapter = unit.chapter_set.all().last()

    if not s_no > last_chapter.s_no:
        chapter_detail = unit.chapter_set.filter(s_no=s_no).first()
        next_chapter = chapter_detail.s_no + 1
        template = unit.template_dir + chapter_detail.template
        if os.path.isfile("lessons/templates/" + template):
            return render(request, template, {"title": chapter_detail.title,
                                "content": chapter_detail, "unit_no": unit.pk,
                                "next_chapter": next_chapter})
        else:
            return render(request, "coming-soon.html",
                          {"title": chapter_detail.title})
    else:
        messages.success(request, "Congratulations! You have completed your unit")
        return redirect("index")
