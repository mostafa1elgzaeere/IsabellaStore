from operator import concat
from django import forms
from django.shortcuts import render
from .models import Categorie ,Product ,Comment
from .models import Contact as contact
from .models import FaQs as faqs
from .models import About as about


from cart.forms import ProductForm
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

    
def home(request):
    
    return render(request,'home.html')



def products(request,name_categorey):
    
    form= ProductForm()

    current_categorey=Categorie.objects.get(name=name_categorey)
    print(current_categorey)
    products=Product.objects.filter(categorey=current_categorey)
    paginator = Paginator(products, 8) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # paginator = Paginator(products, 7) 
    # page_number = request.GET.get('page')
    

    # page_obj = paginator.get_page(page_number)
    
    # return render(request,'products.html',{"current":current_categorey,"form":form})

    return render(request,'products.html',{"current_cat":current_categorey,"products":products,"form":form,"products":page_obj})


def product_detil(request,product_choice):
    form= ProductForm()
    product=Product.objects.get(id=product_choice,active=True)

    if request.method == "POST":
        user=request.user
        content=request.POST.get("content")


    return render(request,"product_detail.html",{"product":product,"form":form})

def product_detil(request,name_categorey,product_name):
    form= ProductForm()
    product=Product.objects.get(id=product_name)


    return render(request,"product_deatil.html",{"form":form,"product":product})
    




def Faqs(request):
    dataOne=faqs.objects.get(id=1)
    dataTwo=faqs.objects.get(id=2)
    dataThree=faqs.objects.get(id=3)
    dataFour=faqs.objects.get(id=4)
    dataFive=faqs.objects.get(id=5)
    dataSex=faqs.objects.get(id=6)
    dataSeven=faqs.objects.get(id=7)
    return render(request,"faqs.html",{"dataOne":dataOne,"dataTwo":dataTwo,"dataThree":dataThree,"dataFour":dataFour,"dataSex":dataSex,"dataSeven":dataSeven,"dataFive":dataFive})


def About(request):
    data=about.objects.first()
    return render(request,"about.html",{"data":data})



def Contact(request):
    data=contact.objects.first()
    
    return render (request,"contact.html",{"data":data})


