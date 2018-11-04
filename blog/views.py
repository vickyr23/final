from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion
from .forms import PostForm
from django.shortcuts import redirect

def listado(request):
    publicados = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {publicados:'publicados'})

def detalle(request, pk):
    det = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/detalle.html', {'det': det})

def nuevo(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                p = form.save(commit=False)
                p.autor = request.user
                p.save()
                return redirect('detalle', pk=p.pk)
        else:
            form = PostForm()
        return render(request, 'blog/editar.html', {'form': form})

def editar(request, pk):
        post = get_object_or_404(Publicacion, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('detalle', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/editar.html', {'form': form})

def borrador(request):
    draft = Publicacion.objects.filter(fecha_publicacion__isnull=True).order_by('fecha_creacion')
    return render(request, 'blog/borrador.html', {'draft': draft})
# Create your views here.
def publicacion(request, pk):
    pu = get_object_or_404(Publicacion, pk=pk)
    pu.publish()
    return redirect('detalle', pk=pk)

def publish(self):
    self.fecha_publicacion = timezone.now()
    self.save()

def eliminar(request, pk):
    rv = get_object_or_404(Publicacion, pk=pk)
    rv.delete()
    return redirect('/')
