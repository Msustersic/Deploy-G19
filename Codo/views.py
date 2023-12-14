from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class Funcion(TemplateView):
    template_name = "byFunction.html"

class Comentarios(TemplateView):
    template_name = "comments.html"

class Login(TemplateView):
    template_name = "fLogin.html"

class Dejar_comentario(TemplateView):
    template_name = "fComments.html"

