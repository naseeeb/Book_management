

from django.shortcuts import render, get_object_or_404, redirect
from .models import *

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
        
        # Get or create the author
        author, created = Author.objects.get_or_create(name=author_name)
        
        # Create the book
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
        
        # Get or create the author
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
