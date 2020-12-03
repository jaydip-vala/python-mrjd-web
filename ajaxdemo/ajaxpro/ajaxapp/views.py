from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .form import DreamrealForm
from .models import book



def index(request):
    return render(request, 'index.html')

def save_book1(request):
    b_name = request.GET['name']
    b_price = request.GET['price']
    n_pages = request.GET['pages']
    s_book = book(book_name=b_name,book_price=b_price,no_pages=n_pages)
    try:
        s_book.save()
        return HttpResponse('success')
    except:
        return HttpResponse("error... ")

# def dreamreal(request):
# #    form = DreamrealForm()
#    return render(request, 'dreamreal.html')

# def create(request):
#     if request.method == 'POST':
#         form = DreamrealForm(request.POST)
#         if form.is_valid(): 
#             print('load')
#             form.save()
#             # this method will add a record in the table
#             return redirect('index')
#         else:
#             print('error')
#     form = DreamrealForm()
#     return render(request, 'dreamreal1.html', {'form': form})
def create(request):
    if request.method == 'POST':
        form = DreamrealForm(request.POST)
        if form.is_valid():
            form.save()
            # this method will add a record in the table
            return HttpResponse('success')
        else:
            return HttpResponse("failed ... ")
    else:
        form = DreamrealForm()
        return render(request, 'dreamreal1.html', {'form': form})

