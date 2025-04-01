from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Enhance
from .forms import UploadFileForm

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         file = request.FILES('file')
#     else:
#         form = UploadFileForm()
#     return render(request, "/", {'form':form})
def index(request):
    if request.method == "POST":
        input_file = UploadFileForm(request.POST, request.FILES)
        file = request.FILES('file')
        ai_model=request.POST.get('ai_model')
        # output_path=request.POST.get('output_path')
        ai_precision=request.POST.get('ai_precision')
        in_resolution=request.POST.get('in_resolution')
        interpolation=request.POST.get('interpolation')
        img_output=request.POST.get('img_output')
        vid_output=request.POST.get('vid_output')
        enhance=Enhance(ai_model=ai_model,ai_precision=ai_precision,in_resolution=in_resolution,interpolation=interpolation,img_output=img_output,vid_output=vid_output,date=datetime.today())
        enhance.save()
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message,date=datetime.today())
        contact.save()
    return render(request, "contact.html")

# input_file=input_file,,output_path=output_path