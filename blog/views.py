from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion

def listado(request):
    publicados = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {publicados:'publicados'})

def detalle(request, pk):
    det = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle.html', {'det': det})
# Create your views here.
