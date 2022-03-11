from django.shortcuts import render

# Create your views here.
PAGES = {
    "Home":"", 
    "O mnie":"me", 
    "Kontakt":"contact"
}

def home(request):
    c = {"title": "Home", "navi": PAGES}
    return render(
        request=request,
        template_name="infos/home.html",
        context=c
    )

def me(request):
    c = {"title": "O mnie", "navi": PAGES}
    return render(
        request=request,
        template_name="infos/me.html",
        context=c
    )

def contact(request):
    c = {"title": "Kontakt", "navi": PAGES}
    return render(
        request=request,
        template_name="infos/contact.html",
        context=c
    )