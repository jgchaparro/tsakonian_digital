from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    # Load the template
    template = loader.get_template("translator/index.html")

    # Set the context
    text_to_show = """
Καούρ εκάνατε! Εγκείνι ενι το πρώκιου ηλεκτρονικό Τσακώνικο λεξικό!"""
    context = {
        "text_to_show": text_to_show,
    }

    return HttpResponse(template.render(context, request))