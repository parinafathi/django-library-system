from django.shortcuts import render, get_object_or_404  # 👈 اضافه کردن get_object_or_404 در این خط
from .models import Book, Member
from .form import BookForm

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def member_list(request):
    members = Member.objects.all()  # دریافت همه اعضا از دیتابیس
    return render(request, 'library/member_list.html', {'members': members})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'library/add_book.html', {'form': form})    
