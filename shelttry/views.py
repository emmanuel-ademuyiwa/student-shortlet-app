import email
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Profile, Subscriber, Contact, Testimonial, Upload
from .form import CreateUserForm, DocumentForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from decimal import Decimal as D
from django import forms
from django.views.generic.edit import FormView
#from .form import FileFieldForm
from django.forms import modelformset_factory
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

#from django.core.mmail import send_mail, BadHeaderError
# Create your views here.


@login_required
def post(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DocumentForm(initial={'landlord': request.user})
    return render(request, 'post.html', {'form': form})


def edit(request, id):
    hall = get_object_or_404(Upload, id=id)
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES, instance=hall)
        if form.is_valid():
            hall = form.save(commit=False)
            #hall.landlord = request.user
            hall.save()
            return redirect('dashboard')
    else:
        form = DocumentForm(instance=hall)
    context = {'form': form}
    return render(request, 'edit.html', context)


def policy(request):
    return render(request, 'policy.html')

def privacy(request):
    return render(request, 'privacy.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def agent_check(request):
    agent = 'Agent'
    profile = Profile.objects.get(email=request.email)
    return profile.purpose == agent


@login_required
@user_passes_test(agent_check)
def dashboard(request):
    list = Upload.objects.filter(landlord=request.user)
    #return render(request, 'dashboarddaa.html', {'list': list})
    #return render(request, 'dashboard.html', {'list': list})
    return render(request, 'dashboard.html', {'list': list})

def delete(request, id):
    post = Upload.objects.get(id=id)
    post.delete()
    #return HttpResponse('deleted')
    #return render(request, 'dashboard.html')
    return redirect('dashboard')

def user_log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Success: Account created for ' + user + '\n was successful.')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def detail(request, slug):
    products = Upload.objects.filter(slug=slug)
    context = {'products': products}
    return render(request, 'detail.html', context)


def explore(request):
    title = 'Available Houses'
    dests = Upload.objects.all()    
    return render(request, 'explore.html', {'dests': dests, 'title':title})

def ago(request):
    title = 'Houses in Ago'
    post = Upload.objects.filter(town__icontains="ago-iwoye")
    return render(request, 'destinations.html', {'post': post, 'title': title})

def ijebu(request):
    title = 'Houses in Ijebu-Igbo'
    post = Upload.objects.filter(town__icontains="ijebu-igbo")
    return render(request, 'destinations.html', {'post': post, 'title': title})

def oru(request):
    title = 'Houses in Oru'
    post = Upload.objects.filter(town__icontains="oru")
    return render(request, 'destinations.html', {'post': post, 'title': title})


def index(request):
    test = Contact.objects.all()
    dests = Upload.objects.all()
    #profile = Profile.objects.get(email=request.user)
    context = {'dests': dests, 'test': test}
    return render(request, 'index.html', context)



def dashboardhouses(request):
    return render(request, 'houses.html')

def about(request):
    return render(request, 'about.html')


def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        house = Contact(name=name, email=email, message=message)
        recipients = ["shelttry@gmail.com"]
        house.save()
        return redirect('/')

def success(request):
    return HttpResponse('Successfully uploaded, Note: Your post will be reviewed and uploaded as fast as possible')



def search(request):
    if request.method == 'GET':
        town = request.GET.get('town')
        type = request.GET.get('type')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        title = 'Searched Houses'
        search = Upload.objects.filter(town__icontains=town, type__icontains=type,
                                       price__range=(min_price, max_price))
        return render(request, 'search.html', {'search': search, 'title': title})
    #return render(request, 'post.html')

def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        email = request.POST.get('email', False)
        house = Subscriber(name=name, email=email)
        house.save()
        return redirect('/')
    else:
        return render(request, 'index.html')


'''
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'dashboarddaa.html', {'form': form})



def signup1(request):
    if request.method == 'POST':
        #form = SignUpForm(request.POST)
        #if form.is_valid():
            #form.save()
        name = request.POST.get('name', False)
        raw_password = request.POST.get('password1')
        user = authenticate(username=name, password=raw_password)
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'index8.html')
'''


'''
def post1(request):
    if request.method == 'POST':
        hallname = request.POST['hall_name']
        description = request.POST['description']
        town = request.POST['town']
        type = request.POST['type']
        price = request.POST['price']
        landlord_name = request.POST['landlordname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        image1 = request.POST['image1']
        image2 = request.POST['image2']
        image3 = request.POST['image3']
        image4 = request.POST['image4']


        house = Houses(hallname=hallname, description=description,
                       town=town, type=type, price=price,
                        landlord_name=landlord_name, email=email, phone_number=phone_number,
                       image1=image1, image2=image2, image3=image3, image4=image4,)
        if house:
            house.save()
            return redirect('success')
    else:
        return render(request, 'rentout.html')


@login_required
def post1(request):

    ImageFormSet = modelformset_factory(Images,
                                        form=ImageForm, extra=4)

    if request.method == 'POST':

        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Images.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            messages.success(request,
                             "Posted!")
            return HttpResponseRedirect("dashboard")
        else:
            postForm = PostForm()
            return render(request, 'post',
                          {'postForm': postForm, 'error_message': 'something error message'})
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'post2.html',
                  {'postForm': postForm, 'formset': formset})



def test(request):
    if request.method == 'POST':
        hallname = request.POST['hall_name']
        description = request.POST['description']
        town = request.POST['town']
        type = request.POST['type']
        price = request.POST['price']
        landlord_name = request.POST['landlordname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        image = request.POST['image']


        house = Test(hallname=hallname, description=description,
                       town=town, type=type, price=price,
                        landlord_name=landlord_name, email=email, phone_number=phone_number,)

        h = TestImages(image=image,)
        house.save()
        h.save()
        return render(request, 'post.html')
    else:
        return render(request, 'post.html')




class CreateMyModelView(CreateView):
    model = Houses
    form_class = MyModelForm
    template_name = 'myapp/template.html'
    success_url = 'myapp/success.html'


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...  # Do something with each file.
            return self.form_valid(form)


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html',
                      {'uploaded_file_url': uploaded_file_url})
    return render(request, 'core/simple_upload.html')



def dest(request):
    dests = Houses.objects.all()
    img1 = Houses.img1
    img2 = Houses.img2
    img3 = Houses.img3
    img4 = Houses.img4
    imgs = [img1, img2, img3, img4]
    return render(request, 'dest.html', {'imgs': imgs})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'index8.html', {'form': form})


def room(request):
    test = Contact.objects.all()
    return render(request, 'index.html', {'test': test})

'''

