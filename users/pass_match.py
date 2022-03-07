from django.contrib import messages
from django.shortcuts import redirect

def pass_checks(function):
    def decorator(request):
        if request.method == "POST":
            page = request.get_full_path()
            if "token" in request.GET and "email" in request.GET:
                token = request.GET.get("token")
                email = request.GET.get("email")
                page += f"?token={token}&email={email}"

            passwd = request.POST.get("password")
            conf_passwd = request.POST.get("confirm_password")

            if len(passwd) >= 8:
                if passwd == conf_passwd:
                    return function(request)
                else:
                    messages.error(request, "Passwords do not match. Please retry")
                    return redirect(page)
            else:
                messages.error(request, "Password 8 characters long required. Please retry")
                return redirect(page)
        else:
            return function(request)
    return decorator