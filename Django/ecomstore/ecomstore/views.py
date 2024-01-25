from django.http import HttpResponse
from django.template import loader


def file_not_found_404(request, exception):
    page_title = "Pate Not Found"
    template = loader.get_template("404.html")
    context = {
        "page_title": page_title,
    }
    return HttpResponse(template.render(context))
