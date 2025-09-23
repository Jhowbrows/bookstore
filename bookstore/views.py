from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import git

@csrf_exempt
def update(request):
    if request.method == "POST":
        # AJUSTE ESTE CAMINHO QUANDO ESTIVER NO PYTHONANYWHERE
        repo = git.Repo('/home/Jhowbrows/bookstore') # Ex: /home/seu_usuario/bookstore
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())