from django.shortcuts import redirect

def redirection(request):
    return redirect("/covid/home")