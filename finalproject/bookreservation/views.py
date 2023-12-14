from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bookreservation.models import Book, Student
from django.core.paginator import Paginator
from django.views.generic import ListView


@login_required
def index(request):
    students = Student.objects.all()
    studentCount  = Student.objects.count()
    averageGpa = 0

    for s in students:
        averageGpa += s.gpa 

    averageGpa = averageGpa / studentCount

    seniorsCount = Student.objects.filter(year='Senior').count()
    juniorsCount = Student.objects.filter(year='Junior').count()
    sophomoresCount = Student.objects.filter(year='Sophomore').count()
    freshmanCount = Student.objects.filter(year='Freshman').count()


    context = {'studentCount': studentCount, 'averageGPA': averageGpa, 'seniorsCount': seniorsCount, 'juniorsCount': juniorsCount,
               'sophomoresCount': sophomoresCount, 'freshmanCount': freshmanCount}

    return render(request=request, template_name='bookreservation/dashboard.html', context=context)

@login_required
def studentDetails(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)

    pageNumber = request.GET.get("page")
    page = paginator.get_page(pageNumber)
    

    return render(request, template_name="bookreservation/studentdetails.html", context={"page": page, 'data': page})

@login_required
def bookDetails(request):
    books = Book.objects.all().order_by('-number_of_times_checked_out')
    paginator = Paginator(books, 10)

    pageNumber = request.GET.get("page")
    page = paginator.get_page(pageNumber)
    

    return render(request, template_name="bookreservation/bookdetails.html", context={"page": page, 'data': page})

@login_required
def reserve(request):
    students = Student.objects.all()
    books = Book.objects.filter(currently_checked_out=False)

    return render(request, template_name="bookreservation/reserve.html", context={'students': students, 'books': books})

@login_required
def reservePost(request):
    bookResponse = request.GET.get('book')
    studentResponse = request.GET.get('student')

    book = Book.objects.get(id= bookResponse)
    student = Student.objects.get(id= studentResponse)

    print(student.booksReserved)
    if (student.booksReserved == 4):
        return HttpResponse('failed')
    if (book.currently_checked_out):
        return HttpResponse('failed')
    
    book.currently_checked_out = True
    book.number_of_times_checked_out = book.number_of_times_checked_out + 1
    student.booksReserved = student.booksReserved + 1
    book.save()
    student.save()

    return HttpResponse('success')
    


def login(request):
    return HttpResponse("Login")