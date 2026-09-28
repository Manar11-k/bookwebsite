from django.shortcuts import render
from django.http import HttpResponse

# ✅ دالة بسيطة من اللاب السابق (اختياري)
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))
    # مثال: http://127.0.0.1:8000/books/index2/3/

# ✅ دالة الصفحة الرئيسية (Lab 4)
def index(request):
    return render(request, "bookmodule/index.html")

# ✅ صفحة عرض قائمة الكتب
def list_books(request):
    return render(request, "bookmodule/list_books.html")

# ✅ صفحة عرض كتاب واحد
def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}
    return render(request, 'bookmodule/one_book.html', context)

# ✅ صفحة "About Us"
def aboutus(request):
    return render(request, "bookmodule/aboutus.html")
