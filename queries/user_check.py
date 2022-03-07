from django.http import HttpResponse
from .models import Query

def user_check(function):
    def decorator(request, query_id):
        query = Query.objects.filter(pk=query_id).first()
        if request.user == query.asked_by:
            return function(request, query_id)
        else:
            return HttpResponse("403 Forbidden")
    return decorator
