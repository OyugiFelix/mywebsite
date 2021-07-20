from connect.form import InquiryForm
from django.shortcuts import redirect, render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    d = now.day
    m = now.month
    y = now.year
    my_time =f'{d}/{m}/{y}'
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=True)
            comment.save()
            
            return redirect('index.html')
    else:
         form = InquiryForm()
    return render(request, 'index.html', {'form': form , 'my_time':my_time})


