from django.shortcuts import render,redirect
from sendev.models import contact
# from django.shortcuts import redirect
from .forms import ContactForm,Conection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# from django.http import HttpResponse
def connect(request):
    return render(request,'index.html')

# def connect(request):
#     form=Conection()
#     request.session['data']=request.POST
#     if request.method == 'POST':
#         utilisateur=authenticate(request,username=request.POST['username'],password=request.POST['password'])
#         if utilisateur is not None:
#             login(request, utilisateur)
#             return redirect('contact')
    
#     return render(request,'conection.html',{'form':form})


def delette(request,id_sup):
    contact.objects.get(id=id_sup).delete()
    return redirect('contact')


def modifpage(request):
    pass

def modifAction(request):
    pass


def detail( request,id_detail):
    contactid=contact.objects.get(id=id_detail)
    return render(request,'detail.html',{'contact':contactid})


def page(request):
    
    contacts=contact.objects.all()
    lscontact={'contacts':contacts}
    return render(request,'afficheContact.html',lscontact)


def ajoutcontact(request ):
    form=ContactForm
    erroemess=''
    if request.method == 'POST':
        
        form=ContactForm(request.POST, request.FILES )
        if form.is_valid():
            form= form.save()
            return redirect('contact')
        else:
            erroemess=form.errors
    return render(request,'ajoutContact.html',{'form':ContactForm,"message":erroemess})


def deconnection(request):
    logout(request)
    return redirect('index')
# @login_required
# def ajoutform(request):
    
#    return render(request ,'ajoutContact.html')

def test(request):
    if request.session:
        
        session=request.session['data']
        
        return render(request,'test.html',{'session':session})
    else:
        return redirect('index')
    