from django.shortcuts import render, get_object_or_404, redirect
from .models import URL
from .form import URLForm

def homepagefn(request):
    form = URLForm(request.POST or None)
    short_url = None
    if form.is_valid():
        url_obj = form.save()
        short_url = request.build_absolute_uri(f"/{url_obj.short_code}/")
    return render(request, 'home.html', {'form': form, 'short_url': short_url})

def short_urlfn(request, short_code):
    url_obj = get_object_or_404(URL, short_code=short_code)
    return redirect(url_obj.original_url)
