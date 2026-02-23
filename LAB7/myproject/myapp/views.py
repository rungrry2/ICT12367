from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>หน้าแรก</h1>")

def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    return render(request, 'form.html')

def contact(request):
    return HttpResponse("<h1>ติดต่อ 0937085511 ศุภกร นรินทรกุล ณ อยุธยา</h1>")