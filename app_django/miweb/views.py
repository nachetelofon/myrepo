from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("HOLA RETAMAR. ESTO ES EL INDEX DE MI WEBAPP")
