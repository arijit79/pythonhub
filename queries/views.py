from django.shortcuts import render, redirect
from .models import Query
from django.http import HttpResponse
from .user_check import user_check
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def query_index(request):
    user = request.user
    queries = user.query_set.all()
    if len(queries) != 0:
        queries = reversed(user.query_set.all())
        return render(request, "queries/index.html", {"title":"Queries", "queries": queries})
    else:
        return render(request, "queries/index.html", {"title":"Queries"})

@login_required
def new_query(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        content = request.POST.get("content")
        query = Query(title=title, content=content, asked_by=user)
        query.save()
        return redirect("query-index")
    return render(request, "queries/new-query.html", {"title": "New Query"})

@login_required
@user_check
def view_query(request, query_id):
    query = Query.objects.filter(pk=query_id).first()
    return render(request, "queries/view-query.html", {"query": query, "title": query.title})

@login_required
@user_check
def update_query(request, query_id):
    query = Query.objects.filter(pk=query_id).first()
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        update_query = Query.objects.filter(id=query_id)
        update_query.update(title=title, content=content)
        messages.success(request, "Your Query Has Been Ppdated")
        return redirect("query-index")
    return render(request, "queries/update-query.html", {"query": query, "title": "Update Query"})

@login_required
@user_check
def delete_query(request, query_id):
    query = Query.objects.filter(pk=query_id).first()
    if request.method == "POST":
        Query.objects.filter(pk=query_id).delete()
        return redirect("query-index")
    return render(request, "queries/delete-query.html", {"title": "Delete" + query.title, "query": query})
