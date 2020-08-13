from django.shortcuts import render
from django.http import HttpResponse

class_3 = ['우태용', '조양권', '김진혁', '안홍선', '모혜림']

# Create your views here.
def home(request):
    name = '조양권'
    return render(request, 'home.html', {'username':name})

def result(request):
    print(request.POST['username'])
    is_student_class_3 = False

    username = request.POST['username']

    if username in class_3:
        is_student_class_3 = True
        
    return render(request, 'result.html', {'username':username, 'is_student_class_3':is_student_class_3})