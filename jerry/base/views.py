from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import NameForm
from base.models import Employees,Points
from datetime import date, datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# Create your views here.

def other(request):
    return render(request, "other.html")

def vote(request):
    return render(request, "other.html")

def hello(request):
    html = "<html><body>It is now %s.</body></html>"
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pk = int(data['your_name'])
            pk2 = data['passwor_d']
            lst = []
            for i in  Points.objects.filter(employeepoints_id=pk):
                dict={"zidi":i.passwordz,"employeezidi":i.employeepoints_id,"datii":i.pointsattained,"role":i.seniority}
                lst.append(dict)
            ed = lst[0]["datii"]
            return HttpResponse("<html><body>You have these points %s.</body></html>" % ed )
        else:
            form = NameForm()
        return render(request, 'hello.html', {'form': form})
    return render(request,"hello.html")
    
    

def get_name(request):
    if request.method == 'POST':

        # return HttpResponse("<html><body>It is now</body></html>")
        form = NameForm(request.POST)
        if form.is_valid():
            pk=request.POST['your_name']
            print(pk)
            return HttpResponse("<html><body>It is now %s.</body></html>" % pk)
        else:
            form = NameForm()
        return render(request, 'hello.html', {'form': form})