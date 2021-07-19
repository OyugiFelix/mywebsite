from connect.form import InquiryForm
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=True)
            comment.save()
            
            return redirect('index.html')
    else:
         form = InquiryForm()
    return render(request, 'index.html', {'form': form})


def formView(request):

   pass
