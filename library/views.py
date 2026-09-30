from  datetime import date
from django.shortcuts import render, get_object_or_404  # 👈 اضافه کردن get_object_or_404 در این خط
from .models import Book, Member, Borrowing
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


def borrow_book(request, book_id, member_id):
    book = get_object_or_404(Book, id=book_id)
    member = get_object_or_404(Member, id=member_id)

    if book.available:
        book.available = False
        book.borrow_count += 1
        book.save()

        Borrowing.objects.create(
            book=book,
            member=member,
            borrowed_at=date.today()
        )

    return redirect('book_list')

# 2. پس گرفتن کتاب
def return_book(request, book_id):
    borrowing = Borrowing.objects.filter(
        book_id=book_id,
        returned_at__isnull=True
    ).order_by('-borrowed_at').first()

    if borrowing:
        borrowing.returned_at = date.today()
        borrowing.save()

        borrowing.book.available = True
        borrowing.book.save()

    return redirect('book_list')