from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .models import Link

def index(request):

	links = Link()
	template_name =  'index.html'
	local_url = 'http://127.0.0.1:8000/'
	if request.method == 'POST':

		links.url_original = request.POST['link']
		links.save()

	links.url_generated = local_url + str(links.id)
	links.save()
	
	context = {
		'links' : links
	}

	return render(request,template_name,context)


def modf(request, pk):
	
	link = get_object_or_404(Link,pk=pk)
	new_url = Link.objects.get(pk=pk)

	return redirect(new_url.url_original)
	
