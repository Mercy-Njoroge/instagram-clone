from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render (request, "welcome.html")

@login_required(login_url='/accounts/login/')
def home(request):
    pics = Image.posted_pics()
    comments = Comment.objects.all()
    print(comments)

    if request.method =='POST':
        form = WelcomeMessageForm(request.POST) 
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = WelcomeMessageRecipient(name=name,email=email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('home')
    else:
        form = WelcomeMessageForm()

    return render (request, 'all-photos/home.html',{"pics":pics,"letterForm":form, "comments":comments})


def user_profile(request):  
    current_user = request.user
    if request.method =='POST':
        form = EditProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

            return redirect("home")
    else:
        form = EditProfile()
    return render (request, 'all-photos/edit_profile.html',{"form":form})
