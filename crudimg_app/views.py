import os
from django.shortcuts import redirect, render

from crudimg_app.models import product

# Create your views here.
def add(request):
    return render(request,'add.html')
def add_product(request):
    if request.method=='POST':
        
        pname=request.POST['product_name']
        price=request.POST['product_price']
        qty=request.POST['product_quantity']
        # image=request.FILES.get['file']
        image=request.FILES['file']
        pro=product(product_name=pname,price=price,quantity=qty,image=image)
        print("Saving Data")
        pro.save()
        return redirect('show_products')
    
def show_products(request):
    prodts=product.objects.all()
    return render(request,'show_product.html',{'prodts':prodts})

def editpage(request,pk):
    prodts=product.objects.get(id=pk)
    return render(request,'edit.html',{'prodts':prodts})
def edit_products(request,pk):
    if request.method=='POST':
        prod=product.objects.get(id=pk)
        prod.product_name =request.POST.get('pname')
        prod.price =request.POST.get('price')
        prod.quantity =request.POST.get('qty')
        if len(request.FILES)!=0:
            if len(prod.image)>0:
                os.remove(prod.image.path)
            prod.image=request.FILES.get('file')
        prod.save() 
        return redirect('show_products')
    return render(request,'edit.html')  
def deletepage(request,pk):
    p=product.objects.get(id=pk)
    if p.image and os.path.isfile(p.image.path):
        os.remove(p.image.path)
    p.delete()
    return redirect('show_products')