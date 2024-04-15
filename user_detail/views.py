from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from user_detail.models import Registermodel,Vendor,address,contact
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import Q



@csrf_exempt
@api_view(["POST"])
def Register(request):
    if request.method == 'POST':
        b = json.loads(request.body)
        if "id" not in b:
            obj= Registermodel.objects.create(firstname =b['firstname'],lasttname =b ['lasttname'],userid = b['userid'],
                                          password= b['password'],mblenum =b['mblenum'],email =b['email'])
            a=[{'Message':'Data Created'}]
        
            return HttpResponse(json.dumps(a))
        else:
            obj= Registermodel.objects.filter(id=b['id']).update(firstname =b['firstname'],lasttname =b ['lasttname'],userid = b['userid'],
                                          password= b['password'],mblenum =b['mblenum'],email =b['email'])
            a=[{'Message':'Data Updated'}]
        
        return HttpResponse(json.dumps(a))
    

@csrf_exempt
@api_view(["POST"])
def Vendormodel(request):
    if request.method=='POST':
        b = json.loads(request.body)
        if "id" not in b:
            obj= Vendor.objects.create(Name =b['Name'],Code =b ['Code'],GST = b['GST'],
                                          Pan= b['Pan'],Branch =b['Branch'],Address_id =b['Address'],Contact_id=b['Contact'],created_by=b['created_by'],updated_by=b['updated_by'])
            a=[{'Message':'Data Created'}]

            return HttpResponse(json.dumps(a))
        else:
            obj= Vendor.objects.filter(id=b['id']).update(Name =b['Name'],Code =b ['Code'],GST = b['GST'],
                                          Pan= b['Pan'],Branch =b['Branch'],Address_id =b['Address'],Contact_id=b['Contact'],created_by=b['created_by'],updated_by=b['updated_by'])
            a=[{'Message':'Data Updated'}]

        return HttpResponse(json.dumps(a))
            



@csrf_exempt
@api_view(["POST"])
def addressmodel(request):
    if request.method =='POST':
        b=json.loads(request.body)
        if "id" not in b:
            obj= address.objects.create(Line_1 =b['Line_1'],Line_2 =b ['Line_2'],Pincode = b['Pincode'],
                                          State= b['State'],District =b['District'],City =b['City'],created_by=b['created_by'],updated_by=b['updated_by'])
            a=[{'Message':'Data Created'}]
            return HttpResponse(json.dumps(a))
        else:
            obj= address.objects.filter(id=b['id']).update(Line_1 =b['Line_1'],Line_2 =b ['Line_2'],Pincode = b['Pincode'],
                                          State= b['State'],District =b['District'],City =b['City'],created_by=b['created_by'],updated_by=b['updated_by'])
            a=[{'Message':'Data Updated'}]
            return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(["POST"])
def contactmodel(request):
    if request.method =='POST':
        b=json.loads(request.body)
        if "id" not in b:
            obj= contact.objects.create(mobile =b['mobile'],Email =b ['Email'],Account = b['Account'],
                                          Benificary_Name= b['Benificary_Name'],created_by=b['created_by'],updated_by=b['updated_by'])
            a=[{'Message':'Data Created'}]
            
            return HttpResponse(json.dumps(a))
        else:
            obj= contact.objects.filter(id=b['id']).update(mobile =b['mobile'],Email =b ['Email'],Account = b['Account'],
                                          Benificary_Name= b['Benificary_Name'],created_by=b['created_by'],updated_by=b['updated_by'])
            a=[{'Message':'Data Updated'}]

        return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['GET'])
def getregister(request):
    if request.method =='GET':
        obj =Registermodel.objects.all()
        a=[]
        for i in obj:
            b={"firstname":i.firstname,"lasttname":i.lasttname}
            a.append(b)
        return HttpResponse([a])
    
@csrf_exempt
@api_view(['GET'])
def getvendor(request):
    if request.method =='GET':
        obj=Vendor.objects.all()
        a=[]
        for i in obj:
            b={"Name":i.Name,"Code":i.Code,"field_1":i.Address.Line_1,"field_2":i.Address.Line_2,"Pan":i.Pan,"Branch":i.Branch,"Mnum":i.Contact.mobile}
            a.append(b)
        return HttpResponse([a])
    
@csrf_exempt
@api_view(['GET'])    
def getaddress(request):
    if request.method=='GET':
        obj= address.objects.all()
        a=[]
        for i in obj:
            b={"Line_1":i.Line_1,"Line_2":i.Line_2}
            a.append(b)
        return HttpResponse([a])
    

    
@csrf_exempt
@api_view(['GET'])   
def getcontact(request):
    if request.method=='GET':
        obj=contact.objects.all()
        a=[]
        for i in obj:
            b={'Benificary_Name':i.Benificary_Name,"Email": i.Email}
            a.append(b)
        return HttpResponse(a)




def Q_register(request):
    if request.method =='GET':
        a1= request.GET.get('firstname','lasttname')
        obj =Registermodel.objects.filter(Q(firstname__icontains=a1)|Q(lasttname__icontains=a1))
        a=[]
        for i in obj:
            b={"firstname":i.firstname,"lasttname":i.lasttname}
            a.append(b)
        return HttpResponse([a])
    

    
@csrf_exempt
@api_view(['GET'])   
def Q_contact(request):
    if request.method=='GET':
        b1= request.GET.get('Benificary_Name','Email')
        obj=contact.objects.filter(Q(Benificary_Name__icontains=b1)|Q(Email__icontains=b1))
        a=[]
        for i in obj:
            b={'Benificary_Name':i.Benificary_Name,"Email": i.Email}
            a.append(b)
        return HttpResponse(a)
    
@csrf_exempt
@api_view(['GET'])
def Q_vendor(request):
    if request.method =='GET':
        b1= request.GET.get('Name')
        obj=Vendor.objects.filter(Name__icontains=b1)
        a=[]
        for i in obj:
            b={"Name":i.Name,"Code":i.Code,"field_1":i.Address.Line_1,"field_2":i.Address.Line_2,"Pan":i.Pan,"Branch":i.Branch,"Mnum":i.Contact.mobile}
            a.append(b)
        return HttpResponse([a])
    
@csrf_exempt
@api_view(['GET'])    
def Q_address(request):
    if request.method=='GET':
        b1=request.GET.get('Line_1','Line_2')
        obj= address.objects.filter(Q(Line_1__icontains=b1)|Q(Line_2__icontains=b1))
        a=[]
        for i in obj:
            b={"Line_1":i.Line_1,"Line_2":i.Line_2}
            a.append(b)
        return HttpResponse([a])

@csrf_exempt
@api_view(['GET'])
def display_register(request,pk):
    print(pk)
    ob=Registermodel.objects.get(id=pk)
    a={"firstname":ob.firstname,"lasttname":ob.lasttname,"userid":ob.userid,"password":ob.password,
            "mblenum":ob.mblenum,"email":ob.email}
    return HttpResponse([a])


@csrf_exempt
@api_view(['GET'])
def display_address(request,pk):
    obj = address.objects.get(id=pk)
    a={'Line_1':obj.Line_1,'Line_2':obj.Line_2,'State':obj.State,'City':obj.City}
    return HttpResponse([a])

@csrf_exempt
@api_view(['GET'])
def display_contact(request,pk):
    obj=contact.objects.get(id=pk)
    a={'mobile':obj.mobile,'Email':obj.Email,'Account':obj.Account,'Benificary_Name':obj.Benificary_Name}
    return HttpResponse([a])

@csrf_exempt
@api_view(['GET'])
def display_vendor(request,pk):
    obj=Vendor.objects.get(id=pk)
    a={'Name':obj.Name,'Code':obj.Code,'GST':obj.GST,'Pan':obj.Pan,'Branch':obj.Branch}
    return HttpResponse([a])


@csrf_exempt
@api_view(['POST', 'GET'])
def index(request):
    if request.method =="POST":
        pass
    return render(request,template_name="index.html")


@csrf_exempt
@api_view(['GET'])
def gregister(request):
    if request.method == 'GET':
        firstname = request.GET.get('firstname','')
        lasttname = request.GET.get('lasttname','')
        if firstname !="":
            condition=Q(firstname=firstname)
        if lasttname !="":
            condition=Q(lasttname=lasttname)
        # if firstname and lasttname:
        obj = Registermodel.objects.filter(condition)
        for i in obj:
            data ={'firstname':i.firstname ,'lastname': i.lasttname}
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse("No matching record found for firstname and lasttname")    
            
    
@csrf_exempt
@api_view(['DELETE'])
def delete_register(request,pk):
    obj =Registermodel.objects.filter(id=pk).delete()
    a=[{'Message':'Record Deleted successfully'}]
    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['DELETE'])
def delete_address(request,pk):
    obj= address.objects.filter(id=pk).delete()
    a=[{'Message':'Record Deleted successfully'}]
    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['DELETE'])
def delete_contact(request,pk):
    obj=contact.objects.filter(id=pk).delete()
    a=[{'Message':'Record Deleted successfully'}]
    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['DELETE'])
def delete_vendor(request,pk):
    obj=Vendor.objects.filter(id=pk).delete()
    a=[{'Message':'Record Deleted successfully'}]
    return HttpResponse(json.dumps(a))


@csrf_exempt
@api_view(['POST'])
def find_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userid')
        password = data.get('password')
        # Assuming Registermodel is your model for user registration
        user = Registermodel.objects.filter(userid=username, password=password).first()
        if user:
            return JsonResponse({'Message': 'Success'})
        else:
            return JsonResponse({'Message': 'Failed'})
    else:
        return JsonResponse({'Message': 'Invalid Method'})

@csrf_exempt
@api_view(['POST', 'GET'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return JsonResponse({'Message': 'Invalid Method'})