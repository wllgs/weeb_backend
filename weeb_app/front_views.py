from django.shortcuts import render

def blog(request):
    """
    Page frontend très simple qui consomme l'API /api/articles/
    et affiche la liste côté client (fetch).
    """
    return render(request, "blog.html")

