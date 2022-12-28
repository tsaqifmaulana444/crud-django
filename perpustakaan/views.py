from django.shortcuts import render, redirect
from .models import Buku
from .forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'berhasil daftar')
            return redirect('signup')
        else:
            messages.error(request, 'gagal daftar')
            return redirect('signup')
    else:
        form = UserCreationForm()
        ctx = {
            'form': form,
        }
    return render(request, 'signup.html', ctx)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)   
def ubah_buku(request, id_buku):
    book = Buku.objects.get(id=id_buku)
    template = 'ubah_buku.html'
    if request.POST:
        form =  FormBuku(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "berhasil")
            return redirect('ubah_buku', id_buku=id_buku)
    else:   
        form = FormBuku(instance=book)
        ctx = {
            'form': form,
            'book': book,
        }
    return render(request, template, ctx)

@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    books = Buku.objects.all()
    # books = Buku.objects.filter(kelompok_id__nama="komedi")
    # books = Buku.objects.filter(kelompok_id__nama="komedi")[:2]
    ctx = {
        'books': books,
    }
    return render(request, 'buku.html', ctx)

def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            pesan = "berhasil"

            ctx = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah_buku.html', ctx)
            
    else:
        form = FormBuku()

        ctx = {
            'form': form,
        }

    return render(request, 'tambah_buku.html', ctx)