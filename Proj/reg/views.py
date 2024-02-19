from django.shortcuts import render, redirect
from reg.models import Applicant
import uuid, random, string, time
from .models import Item

# Create your views here.

def preRegistration(request):
    if request.method == 'GET':
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        refno = f"{random_chars}"
        return render(request, 'registration_form.html', {"refno": refno})
    if request.method == 'POST':
        studentId = request.POST.get('studentId')
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        suffix = request.POST.get('suffix')
        gender = request.POST.get('gender')
        # age = request.POST.get('age')
        birthofdate = request.POST.get('birthofdate')
        birthofplace = request.POST.get('birthofplace')
        religion = request.POST.get('religion')
        citizenship = request.POST.get('citizenship')
        contactno = request.POST.get('contactno')
        DateRegistered = request.POST.get('DateRegistered')
        presentAddress = request.POST.get('presentAddress')
        homeAddress = request.POST.get('homeAddress')
        motherFirstname = request.POST.get('motherFirstname')
        motherLastname = request.POST.get('motherLastname')
        motherMiddlename = request.POST.get('motherMiddlename')
        motherOccupation = request.POST.get('motherOccupation')
        motherContact = request.POST.get('motherContact')
        fatherFirstname = request.POST.get('fatherFirstname')
        fatherMiddlename = request.POST.get('fatherMiddlename')
        fatherLastname = request.POST.get('fatherLastname')
        fatherOccupation = request.POST.get('fatherOccupation')
        fatherContactno = request.POST.get('fatherContactno')
        GuardianName = request.POST.get('GuardianName')
        GuardianOccupation = request.POST.get('GuardianOccupation')
        GuardianAddress = request.POST.get('GuardianAddress')
        GuardianContactno = request.POST.get('GuardianContactno')
        SpouseName = request.POST.get('SpouseName')
        SpouseOccupation = request.POST.get('SpouseOccupation')
        SpouseAddress = request.POST.get('SpouseAddress')
        JHSLastAttended = request.POST.get('JHSLastAttended')
        JHSdateLastAttended = request.POST.get('JHSdateLastAttended')
        SHSLastAttended = request.POST.get('SHSLastAttended')
        SHSDateLastAttended = request.POST.get('SHSDateLastAttended')
        CollegiateLastAttended = request.POST.get('CollegiateLastAttended')
        CollegiateDateLastAttended = request.POST.get('CollegiateDateLastAttended')
        # ref_no = str(uuid.uuid4().fields[-1])[:8]
        Clearance = request.POST.get('Clearance')
        Sid = request.POST.get('Sid')
        psa = request.POST.get('psa')
        Form148 = request.POST.get('Form148')
        Form137 = request.POST.get('Form137')
        GoodMoral = request.POST.get('GoodMoral')
        Credential = request.POST.get('Credential')
        Picture = request.POST.get('Picture')
        Envelop = request.POST.get('Envelop')
        studentStatus = request.POST.get('studentStatus')
        password = request.POST.get('f_contact')
        refno = request.POST.get('refno')
        user = Applicant.objects.create(firstname=firstname, middlename=middlename, lastname=lastname, suffix=suffix,
                                        gender=gender, birthofdate=birthofdate, birthofplace=birthofplace, religion=religion,
                                        citizenship=citizenship, contactno=contactno, DateRegistered=DateRegistered,
                                        presentAddress=presentAddress, homeAddress=homeAddress, motherFirstname=motherFirstname,
                                        motherMiddlename=motherMiddlename, motherLastname=motherLastname, motherOccupation=motherOccupation,
                                        motherContact=motherContact, fatherFirstname=fatherFirstname, fatherMiddlename=fatherMiddlename,
                                        fatherContactno=fatherContactno, fatherOccupation=fatherOccupation, GuardianName=GuardianName,
                                        fatherLastname=fatherLastname, GuardianOccupation=GuardianOccupation, GuardianAddress=GuardianAddress,
                                        GuardianContactno=GuardianContactno, SpouseName=SpouseName, SpouseOccupation=SpouseOccupation,
                                        SpouseAddress=SpouseAddress, JHSLastAttended=JHSLastAttended, JHSdateLastAttended=JHSdateLastAttended,
                                        SHSLastAttended=SHSLastAttended, SHSDateLastAttended=SHSDateLastAttended,
                                        CollegiateLastAttended=CollegiateLastAttended, CollegiateDateLastAttended=CollegiateDateLastAttended,
                                        Clearance=Clearance, psa=psa, Form148=Form148, Form137=Form137, GoodMoral=GoodMoral,
                                        Sid=Sid, Credential=Credential, Picture=Picture, Envelop=Envelop, studentId=studentId,
                                        refno=refno, password=contactno, studentStatus=studentStatus)
        # return redirect('/user_login/')
        return render(request, 'login.html', locals())


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        refno = request.POST.get('refno')
        password = request.POST.get('password')
        users = Applicant.objects.filter(refno=refno)
        if len(users):
            for user in users:
                if password == user.password:
                    request.session['login_info'] = {'refno': user.refno}
                    return redirect('/home/')
                    # return render(request, 'dashboard.html', locals())
                else:
                    return render(request, 'login.html')
        else:
            return render(request, 'login.html')


def home(request):
    return render(request, 'home.html', )


def check_application(request, nid):
    user = Applicant.objects.get(refno=nid)
    return render(request, 'dashboard.html', {'user': user})


def signout(request):
    request.session.clear()
    return redirect('/user_login/')


def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        return redirect('/')
    return render(request, 'add.html')


def index(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)