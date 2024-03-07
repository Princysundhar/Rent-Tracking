import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def forgot_password(request):
    return render(request,"forgot_password_page.html")

def forgot_password_post(request):
    email = request.POST['textfield']
    res = login.objects.filter(username=email)
    if res.exists():
        pwd = res[0].password
        import smtplib

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        # s.login("riss.princytv@gmail.com", "dnsb yopn jqxq hrko")
        s.login("demo@gmail.com", "dnsb yopn jqxq hrko")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "demo@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Your Password for Easy rent project"
        body = "Your Password is:- - " + str(pwd)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("<script>alert('Email sended');window.location='/'</script>")
    return HttpResponse("<script>alert('Mail Incorrect');window.location='/'</script>")

def log(request):
    # return render(request,"login.html")
    return render(request,"login_index.html")

def log_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        data = data[0]
        request.session['lid'] = data.id
        request.session['lg'] = "lin"
        if data.usertype == 'admin':
            return HttpResponse("<script>alert('Login Success');window.location='/admin_home'</script>")
        elif data.usertype == 'pending':
            return HttpResponse("<script>alert('wait for Authentication');window.location='/'</script>")
        else:
            return HttpResponse("<script>alert('Login Success');window.location='/store_home'</script>")
    else:
        return HttpResponse("<script>alert('Invalid Authentication');window.location='/'</script>")

def admin_home(request):
    if request.session['lg'] != 'lin':
        return HttpResponse("<script>alert('Please Login');window.location='/'</script>")
    # return render(request,"Admin/admin_home.html")
    return render(request,"Admin/admin_index.html")

def logout(request):
    request.session['lg'] = ""
    return HttpResponse("<script>alert('Successfully logout');window.location='/'</script>")

def change_password(request):
    return render(request,"Admin/change_password.html")

def change_password_post(request):
    old_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    data = login.objects.filter(password=old_password,id=request.session['lid'])
    if data.exists():
        if new_password == confirm_password:
            login.objects.filter(id=request.session['lid']).update(password=confirm_password)
            return HttpResponse("<script>alert('Password Updated');window.location='/change_password#ad'</script>")
        else:
            return HttpResponse("<script>alert('Password Mismatch');window.location='/change_password#ad'</script>")

    else:
        return HttpResponse("<script>alert('Error');window.location='/change_password#ad'</script>")


# CATEGORY MANAGEMENT ...............

def add_category(request):
    return render(request,"Admin/add_category.html")

def add_category_post(request):
    category_name = request.POST['textfield']
    data = category.objects.filter(category_name=category_name)
    if data.exists():
        return HttpResponse("<script>alert('Category Already Added,Try another!');window.location='/add_category#ad'</script>")
    else:
        obj = category()
        obj.category_name = category_name
        obj.save()
        return HttpResponse("<script>alert('Category Added');window.location='/add_category#ad'</script>")

def view_category(request):
    data = category.objects.all()
    return render(request,"Admin/view_category.html",{"data":data})

def update_category(request,id):
    data = category.objects.get(id=id)
    return render(request,"Admin/update_category.html",{"data":data,"id":id})

def update_category_post(request,id):
    categories = request.POST['textfield']
    category.objects.filter(id=id).update(category_name=categories)
    return HttpResponse("<script>alert('Category updated');window.location='/view_category#ad'</script>")


def delete_category(request,id):
    category.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Category Deleted');window.location='/view_category#ad'</script>")

def view_store(request):
    data = store.objects.filter(LOGIN__usertype='pending')
    return render(request,"Admin/view_store.html",{"data":data})

def approve_store(request,id):
    login.objects.filter(id=id).update(usertype='store')
    return HttpResponse("<script>alert('Store Approved');window.location='/view_store#ad'</script>")

def reject_store(request,id):
    login.objects.filter(id=id).update(usertype='reject')
    return HttpResponse("<script>alert('Store Rejected');window.location='/view_store#ad'</script>")

def view_approved_store(request):
    data = store.objects.filter(LOGIN__usertype='store')
    return render(request,"Admin/view_approved_store.html",{"data":data})

def view_rejected_store(request):
    data = store.objects.filter(LOGIN__usertype='reject')
    return render(request,"Admin/view_rejected_store.html",{"data":data})

def view_user(request):
    data = user.objects.all()
    return render(request,"Admin/view_user.html",{"data":data})

def view_complaint(request):
    data = complaint.objects.all()
    return render(request,"Admin/view_complaint.html",{"data":data})

def send_reply(request,id):
    return render(request,"Admin/send_reply.html",{"id":id})

def send_reply_post(request,id):
    reply = request.POST['textarea']
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    complaint.objects.filter(id=id).update(reply = reply,reply_date=dt)
    return HttpResponse("<script>alert('Reply sended ');window.location='/view_complaint#ad'</script>")

def view_feedback(request):
    data = feedback.objects.all()
    return render(request,"Admin/view_feedback.html",{"data":data})


# ........................................................................ STORE MODULE

def store_home(request):
    return render(request,"Store/store_index.html")

def register_store(request):
    return render(request,"store_register.html")

def register_store_post(request):
    name = request.POST['textfield']
    Email = request.POST['textfield2']
    contact = request.POST['textfield3']
    lattitude = request.POST['textfield8']
    longitude = request.POST['textfield9']
    password = request.POST['textfield6']
    data = login.objects.filter(username=Email)
    # print("kkkkkk",data)
    if data.exists():
        return HttpResponse("<script>alert('Already registered');window.location='/'</script>")
    else:
        log_obj = login()
        log_obj.username = Email
        log_obj.password = password
        log_obj.usertype = 'pending'
        log_obj.save()

        obj = store()
        obj.store_name = name
        obj.email = Email
        obj.contact = contact
        obj.lattitude = lattitude
        obj.logitude = longitude
        obj.LOGIN = log_obj
        obj.save()
        return HttpResponse("<script>alert('Registered succesfully ');window.location='/'</script>")

def view_profile(request):
    data = store.objects.get(LOGIN=request.session['lid'])
    return render(request,"Store/view_profile.html",{"data":data})

def view_categories(request):
    data = category.objects.all()
    return render(request,"Store/view_categories.html",{"data":data})


# PRODUCT MANAGEMENT

def add_product(request):
    data = category.objects.all()
    return render(request,"Store/add_product.html",{"data":data})

def add_product_post(request):
    categories = request.POST['select']
    name = request.POST['textfield']
    date = request.POST['textfield2']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Rent_Tracking\Track_app\static\Images\\"+dt+'.jpg',photo)
    path = '/static/Images/'+dt+'.jpg'
    amount = request.POST['textfield3']
    count = request.POST['textfield4']
    data = product.objects.filter(product_name=name)
    if data.exists():
        return HttpResponse("<script>alert('Already Exists,Add Another Products');window.location='/add_product#ad'</script>")
    else:

        obj = product()
        obj.product_name = name
        obj.product_date = date
        obj.image = path
        obj.amount = amount
        obj.count = count
        obj.CATEGORY = category.objects.get(id=categories)
        obj.STORE = store.objects.get(LOGIN=request.session['lid'])
        obj.save()
        return HttpResponse("<script>alert('Added succesfully ');window.location='/add_product#ad'</script>")


def view_product(request):
    data = product.objects.filter(STORE__LOGIN=request.session['lid'])
    return render(request,"Store/view_product.html",{"data":data})




def update_product(request,id):
    data = category.objects.all()
    data1 = product.objects.get(id=id)
    return render(request,"Store/update_product.html",{"data":data,"data1":data1,"id":id})

def update_product_post(request,id):
    categories = request.POST['select']
    name = request.POST['textfield']
    date = request.POST['textfield2']
    amount = request.POST['textfield3']
    count = request.POST['textfield4']
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\Rent_Tracking\Track_app\static\Images\\" + dt + '.jpg', photo)
        path = '/static/Images/' + dt + '.jpg'
        product.objects.filter(id=id).update(image=path)
        return HttpResponse("<script>alert('Updated succesfully ');window.location='/view_product#reg'</script>")
    else:
        product.objects.filter(id=id).update(product_name=name,product_date=date,amount=amount,count=count,
                                             CATEGORY=category.objects.get(id=categories),STORE=store.objects.get(LOGIN=request.session['lid']))
        return HttpResponse("<script>alert('Updated succesfully ');window.location='/view_product#ad'</script>")

def delete_product(request,id):
    product.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted succesfully ');window.location='/view_product#ad'</script>")

def store_change_password(request):
    return render(request,"Store/change_password.html")

def store_change_password_post(request):
    old_password = request.POST['textfield']
    new_password = request.POST['textfield2']
    confirm_password = request.POST['textfield3']
    data = login.objects.filter(password=old_password,id=request.session['lid'])
    if data.exists():
        if new_password == confirm_password:
            data = login.objects.filter(id=request.session['lid']).update(password=confirm_password)
                # print("kkkk",data)
            return HttpResponse("<script>alert('Password updated');window.location='/store_change_password'</script>")
        else:
            return HttpResponse("<script>alert('Password mismatch');window.location='/store_change_password'</script>")
    else:
        return HttpResponse("<script>alert('Error');window.location='/store_change_password'</script>")



def view_rating(request):
    res = rating.objects.filter(STORE__LOGIN=request.session['lid'])
    fs = "/static/star/full.jpg"
    hs = "/static/star/half.jpg"
    es = "/static/star/empty.jpg"
    data = []

    for rt in res:
        print(rt)
        a = float(rt.rating)

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]
            data.append(
                {
                    "rating":ar,
                    "USER":rt.USER,
                    "STORE":rt.STORE,
                    "date":rt.date

                }
            )

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )

        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]
            data.append(
                {
                    "rating": ar,
                    "USER": rt.USER,
                    "STORE": rt.STORE,
                    "date": rt.date

                }
            )
        print(data)
    return render(request,"Store/view_rating.html",{"data":data})
    # return render_template('admin/adm_view_apprating.html',data=re33,r1=ar,ln=len(ar55))




def view_orders(request):
    data = orders.objects.filter(STORE__LOGIN=request.session['lid'],status='pending')
    return render(request,"Store/view_orders.html",{"data":data})

def approve_order(request,id):
    orders.objects.filter(id=id).update(status='approve')
    return HttpResponse("<script>alert('Approved');window.location='/view_orders#ad'</script>")


def reject_order(request,id):
    orders.objects.filter(id=id).update(status='reject')
    return HttpResponse("<script>alert('Rejected');window.location='/view_orders#ad'</script>")

def view_approved_order(request):
    data = orders.objects.filter(STORE__LOGIN=request.session['lid'],status='approve')
    return render(request,"Store/view_approved_order.html",{"data":data})


def view_product_on_rent(request,id):
    data = order_sub.objects.filter(ORDERS=id)
    return render(request,"Store/view_product_on_rent.html",{"data":data})


def view_order_history(request):
    data = orders.objects.filter(STORE__LOGIN=request.session['lid'],status='returned')
    return render(request,"Store/view_previous_order.html",{"data":data})

def return_entry(request,id):
    data = orders.objects.filter(id=id).update(status='returned')
    data2 = order_sub.objects.filter(ORDERS=id)
    for i in data2:
        oldstock = product.objects.filter(id = i.PRODUCT_id)
        org = int(oldstock[0].count) + int(i.quantity)
        oldstock.update(count=org)


    return HttpResponse("<script>alert('Order returned');window.location='/view_orders'</script>")




#.............................................................................. ANDROID USER MODULE


def android_login(request):
    username = request.POST['username']
    password = request.POST['password']
    data = login.objects.filter(username=username,password=password)
    if data.exists():
        lid = data[0].id
        type = data[0].usertype
        res = user.objects.get(LOGIN=lid)
        name = res.name
        email = res.email
        photo= res.photo
        print(photo)
        return JsonResponse({"status":"ok","lid":lid,"type":type,"name":name,"email":email,"photo":photo})
    else:
        return JsonResponse({"status":None})

def android_user_registration(request):
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']
    id_proof = request.FILES['pic']
    fs = FileSystemStorage()
    dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    fs.save(r"C:\Users\DELL\PycharmProjects\Rent_Tracking\Track_app\static\id_proof\\" + dt + '.pdf',id_proof)
    path = '/static/id_proof/' + dt + '.pdf'
    data = login.objects.filter(username=email,password=password)
    if data.exists():
        return HttpResponse("<script>alert('Already exists');window.location='/'</script>")
    else:

        log_obj = login()
        log_obj.username = email
        log_obj.password = password
        log_obj.usertype = 'user'
        log_obj.save()

        obj = user()
        obj.name = name
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.email = email
        obj.contact = contact
        obj.photo = path
        obj.LOGIN = log_obj
        obj.save()
        return JsonResponse({"status":"ok"})

def android_change_password(request):
    lid = request.POST['lid']
    current_password = request.POST['crp']
    new_password = request.POST['new_password']
    confirm_password =request.POST['confirm_password']
    data = login.objects.filter(password=current_password,id= lid)
    if data.exists():
        if new_password == confirm_password:
            if login.objects.filter(password=new_password).exists():
                return JsonResponse({"status":"No"})
            else:
                login.objects.filter(id=lid).update(password=confirm_password)
                return JsonResponse({"status":"ok"})
        else:
            return JsonResponse({"status":"mismatch"})
    else:
        return JsonResponse({"status":"error"})


def android_view_profile(request):
    lid = request.POST['lid']
    data = user.objects.get(LOGIN=lid)
    return JsonResponse({"status":"ok","name":data.name,"place":data.place,"post":data.post,"pin":data.pin,
                         "email":data.email,"contact":data.contact,"photo":data.photo})

def android_edit_profile(request):
    lid = request.POST['lid']
    data = user.objects.get(LOGIN=lid)
    return JsonResponse({"status":"ok","name":data.name,"place":data.place,"post":data.post,"pin":data.pin,"email":data.email,
                         "contact":data.contact,"image":data.photo})

def android_edit_profiles(request):
    lid = request.POST['lid']
    try:
        name = request.POST['name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        email = request.POST['email']
        contact = request.POST['contact']
        photo = request.FILES['pic']
        fs = FileSystemStorage()
        dt = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fs.save(r"C:\Users\DELL\PycharmProjects\Rent_Tracking\Track_app\static\Images\\" + dt + '.jpg', photo)
        path = '/static/Images/' + dt + '.jpg'
        user.objects.filter(LOGIN=lid).update(name = name,place=place,post = post,pin=pin,email=email,contact = contact,photo=path)
        return JsonResponse({"status":"ok"})
    except Exception as e:
        name = request.POST['name']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        email = request.POST['email']
        contact = request.POST['contact']
        user.objects.filter(LOGIN=lid).update(name = name,place=place,post = post,pin=pin,email=email,contact = contact)
        return JsonResponse({"status":"ok"})



def android_view_products(request):
    print(request.POST['uid'])
    res = product.objects.filter(STORE=request.POST['uid'])
    ar = []
    for i in res:
        ar.append(
            {
                "pid":i.id,
                "product_name":i.product_name,
                "date":i.product_date,
                "image":i.image,
                "category":i.CATEGORY.category_name,
                "amount":i.amount,
                "store_name":i.STORE.store_name,
                "count":i.count
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_store(request):
    res = store.objects.filter(LOGIN__usertype='store')
    ar = []
    for i in res:
        ar.append(
            {
                "sid":i.id,
                "store_name":i.store_name,
                "latitude":i.lattitude,
                "longitude":i.logitude,
                "email":i.email,
                "contact":i.contact
            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_view_rating(request):
    sid = request.POST['sid']
    res = rating.objects.filter(STORE=sid)
    # res = rating.objects.all()
    ar = []
    for i in res:
        ar.append(
            {
                "rid":i.id,
                "rate":i.rating,
                "date":i.date,
                "store_name":i.STORE.store_name,
                "contact":i.STORE.contact
            }
        )
    return JsonResponse({"status":"ok","data":ar})


def android_send_rating(request):
    rate = request.POST['rate']
    lid = request.POST['lid']
    sid = request.POST['sid']
    dt = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    obj = rating()
    obj.rating = int(float(rate))
    obj.date = dt
    obj.USER = user.objects.get(LOGIN=lid)
    obj.STORE_id = sid
    obj.save()
    return JsonResponse({"status":"ok"})

def android_view_reply(request):
    lid = request.POST['lid']
    res = complaint.objects.filter(USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "cid":i.id,
                "complaint":i.complaint,
                "date":i.date,
                "reply":i.reply,
                "reply_date":i.reply_date

            }
        )
    return JsonResponse({"status":"ok","data":ar})

def android_send_complaint(request):
    complaints = request.POST['complaint']
    lid = request.POST['lid']
    obj = complaint()
    obj.complaint = complaints
    obj.date = datetime.datetime.now().strftime("%Y/%m/%d-%H/%M/%S")
    obj.reply ='pending'
    obj.reply_date = 'pending'
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

def android_send_feedback(request):
    lid = request.POST['lid']
    feedbacks = request.POST['feedback']
    obj = feedback()
    obj.feedback = feedbacks
    obj.date = datetime.datetime.now().strftime("%Y/%m/%d-%H/%M/%S")
    obj.USER = user.objects.get(LOGIN=lid)
    obj.save()
    return JsonResponse({"status":"ok"})

# ..........CART ........................
def android_add_to_cart(request):
    quantity = request.POST['quantity']
    lid = request.POST['lid']
    pid = request.POST['pid']
    data = cart.objects.filter(USER__LOGIN=lid,PRODUCT=pid)
    if data.exists():
        return JsonResponse({"status":"no"})
    else:
        obj = cart()
        obj.USER = user.objects.get(LOGIN=lid)
        obj.PRODUCT = product.objects.get(id=pid)
        obj.quantity = quantity
        obj.save()
        return JsonResponse({"status":"ok"})

def android_view_cart(request):
    lid =request.POST['lid']
    res = cart.objects.filter(USER__LOGIN=lid)
    amount=0
    ar = []
    for i in res:
        product_price = i.PRODUCT.amount
        amount = int(amount) + int(product_price)
        ar.append(
            {
                "cart_id":i.id,
                "product_name":i.PRODUCT.product_name,
                "date":i.PRODUCT.product_date,
                "image":i.PRODUCT.image,
                "category":i.PRODUCT.CATEGORY.category_name,
                "amount":i.PRODUCT.amount,
                "store_info":i.PRODUCT.STORE.store_name,
                "count":i.PRODUCT.count
            }
        )
        # print(ar)
    return JsonResponse({"status":"ok","data":ar,"total_amount":amount})



def android_place_order(request):
    amount = request.POST['amount']
    lid = request.POST['lid']
    data = cart.objects.filter(USER = user.objects.get(LOGIN=lid))
    if data.exists():
        for r in data:
            storeexists = orders.objects.filter(STORE=r.PRODUCT.STORE,USER=r.USER,status='pending')
            if storeexists.exists():
                
                currentamount = int(storeexists[0].amount)
                total = currentamount +  int(r.quantity)* int(r.PRODUCT.amount)
                storeexists.update(amount = total)
                obj1 = order_sub()
                obj1.ORDERS_id = storeexists[0].id
                obj1.quantity = r.quantity
                obj1.PRODUCT = r.PRODUCT
                obj1.save()
            else:
                obj = orders()
                obj.date = datetime.datetime.now().strftime("%Y/%m/%d-%H/%M/%S")
                obj.status = 'pending'
                obj.amount = int(r.quantity)* int(r.PRODUCT.amount)
                obj.STORE = r.PRODUCT.STORE
                obj.USER = user.objects.get(LOGIN=lid)
                obj.payment_status = 'pending'
                obj.save()
                obj1 = order_sub()
                obj1.ORDERS = obj
                obj1.quantity =r.quantity
                obj1.PRODUCT =r.PRODUCT
                obj1.save()

    cart.objects.filter(USER__LOGIN=lid).delete()
    return JsonResponse({"status":"ok"})

def android_cancel_order(request):
    cart_id = request.POST['cart_id']
    cart.objects.get(id=cart_id).delete()
    return JsonResponse({"status":"ok"})


def android_view_orders(request):
    lid = request.POST['lid']
    res = orders.objects.filter(status='returned',payment_status='pending',USER__LOGIN=lid)
    ar = []
    for i in res:
        ar.append(
            {
                "order_id":i.id,
                "date":i.date,
                "status":i.status,
                "amount":i.amount,
                "store_name":i.STORE.store_name,
                "payment_status":i.payment_status
            }
        )

    return JsonResponse({"status":"ok","data":ar})


def android_offline_payment(request):
    order_id = request.POST['order_id']
    mode = request.POST['mode']
    orders.objects.filter(id=order_id).update(payment_status=mode)

    return JsonResponse({"status":"ok"})

def android_online_payment(request):
    bid = request.POST['bid']
    orders.objects.filter(id=bid).update(payment_status='online')
    return JsonResponse({"status":"ok"})



