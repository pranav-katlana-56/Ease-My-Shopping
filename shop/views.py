from django.shortcuts import render
from django.http import HttpResponse
from .models import Mobile , Gadgets , Cashback , Contact
 
def home(request):
    Products = Mobile.objects.filter(Brand="Oneplus")
    budget = Mobile.objects.filter(Price__lte=30000)
    query = "Apple"
    query2 = "Oneplus"
    flagship = Mobile.objects.filter(Brand__icontains=query)
    flagship2 = Mobile.objects.filter(Brand__icontains=query2)
    flagship3 = Mobile.objects.filter(Brand__icontains="LG")
    Params = {"Products": Products , "budget":budget ,"flagship":flagship, "flagship2":flagship2, "flagship3":flagship3}
    return render(request, 'home.html', Params)

def product(request):
    item = Mobile.objects.all()
    return render(request, 'product.html', {"items":item})
 

def productview(request , myid, price):
    item = Mobile.objects.filter(id=myid)
    data = [item]
    cashback1 = 0.03*price
    cashback1 = format(cashback1 , ".2f")
    cashback2 = 0.02*price
    cashback2 = format(cashback2 , ".2f")

    database = {"items":item[0] ,"cashbacks1":cashback1, "cashbacks2":cashback2}
    return render(request, 'productview.html', database )


def orderforme(request, myid):
    item = Mobile.objects.filter(id=myid)
    return render(request, 'orderforme.html' , {"items":item[0]})

def gadgets(request):
    item = Gadgets.objects.all()
    database =  {"items": item}
    return render(request , 'gadgets.html', database)

def cashbackform(request):
    return render(request, "cashback.html")

def search(request):
    query = request.GET["search"]
    items = Mobile.objects.filter(Name__icontains=query)
    params = {"items":items}
    return render(request, 'search.html', params)

def specification(request, myid , Price):
    items = Mobile.objects.filter(id=myid)
    cashback1 = Price*0.03
    cashback2 = Price*0.02
    cashback1 = format(cashback1 , ".2f")
    cashback2 = format(cashback2 , ".2f")
    return render(request, "specifications.html", {"items":items , "cb1":cashback1, "cb2":cashback2})

def flipkart(request):
    return render(request, "flipkart.html")

def sucess(request):
    if request.method =="POST":
        buyer = request.POST["buyer"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        PN = request.POST["Product_Name"]
        price = request.POST["value"]
        date = request.POST["date"]
        idd = request.POST["orderid"]
        pf = request.POST["platform"]
        payment = request.POST["upi"]
        data = Cashback(Buyer_Name=buyer,Mobile=mobile,Email=email,Product_Name=PN,
        Purchase_Value=price,Date_of_Purchase=date,order_id=idd,Platform=pf,Upi=payment)
        data.save()

        

    return render(request, "success.html")


def contact(request):
    return render(request ,"contactus.html")

def trending(request):
    return render(request ,"trending.html")
def message(request):
    if request.method =="POST":
        buyer = request.POST["name"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        sub = request.POST["subject"]
        des = request.POST["value"]
        IO = Contact(Name=buyer,Mobile=mobile,Email=email,Subject=sub,Description=des )
        IO.save()
    return render(request ,"message.html")