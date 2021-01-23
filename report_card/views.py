from django.shortcuts import render, redirect
from .models import ReportCard
from .forms import ReportForm

# Create your views here.
def index(request):
    return render(request, 'report_card/index.html')

def Input(request):
    form = ReportForm

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'report_card/Input.html', context)

def modifyStudent(request, pk):

    student = ReportCard.objects.get(id=pk)
    form = ReportForm(instance=student)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentView')

    context = {"form": form}
    return render(request, 'report_card/modify.html', context)

def deleteStudent(request, pk):
    student = ReportCard.objects.get(id=pk)
    if request.method == "POST":
        student.delete()
        return redirect('studentView')
    context = {'item':student}
    return render(request, 'report_card/delete.html', context)

def studentView(request):
    students = ReportCard.objects.all()

    return render(request, 'report_card/students.html', {'students': students})

