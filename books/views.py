

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db import connections
from django.conf import settings
from django.db import router

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')
        
        author, created = Author.objects.get_or_create(name=author_name)
        
        db_alias = router.db_for_write(Book)
        print("Database Alias:", db_alias)
        
        
        
        Book.objects.create(title=title, author=author, published_date=published_date, isbn=isbn)
        return redirect('book_list')
    
    return render(request, 'book_form.html')

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_name = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.isbn = request.POST.get('isbn')
        
        author, created = Author.objects.get_or_create(name=author_name)
        book.author = author
        
        book.save()
        return redirect('book_list')
    
    return render(request, 'book_form.html', {'book': book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})


