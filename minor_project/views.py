from django.shortcuts import render
from .forms import SignUpForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#Imports ###############
import tempfile
from django.core.files import File
from .forms import UploadFileForm
from .models import ModelFormWithFile,UserWiseInterviewDetail
from .checker import *
from .processing import speechtotext,pause_count,word_per_minutes

############
def index(request):
	#print(request.user.is_authenticated)
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def feature(request):
	return render(request,'project-single.html')

def blog(request):
	return render(request,'blog.html')

def contact(request):
	return render(request,'contact.html')
def register(request):
	registered=False
	if request.method=='POST':
		user_form = SignUpForm(data=request.POST)

		if user_form.is_valid() and user_form.cleaned_data['password']==user_form.cleaned_data['confirm_password']:
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered=True

		else:
			if user_form.data['password'] != user_form.data['confirm_password']:
				user_form.add_error('confirm_password', 'The passwords do not match')
			print(user_form.errors)
	else:
		user_form=SignUpForm()
	if registered:
		return index(request)
	else:
		return render(request,'login_signup.html',{'user_form':user_form,'registered':registered})



def user_login(request):

	if request.method=='POST':
		username=request.POST.get("username")
		password=request.POST.get("password")

		user =authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('minor_project:index'))
			else:
				return HttpResponse("ACCOUNT Not ACTIVE")
		else:
			print("Someone tried to run login and failed!")
			print("Username : {} and password: {}".format(username,password))
			return HttpResponse("Invalid login try")
	else:
		if not request.user.is_authenticated:
			return render(request,'login_signup.html',{})
		else:
			return index(request)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('minor_project:index'))

def handle_uploaded_file(f):
    with open('minor_project/dataset/audioFiles/base.wav', 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return destination
 
@login_required
def upload_file(request,pk):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file=handle_uploaded_file(request.FILES['audio_data'])
        PC=pause_count()
        ans=speechtotext()
        word_min=word_per_minutes()
        print(PC,ans,word_min)
        score=0
        if ans!=0:
        	score=correctness(ans,pk,PC if type(PC)==int else 0)
        if pk==0:
        	user=request.user
        	#print(user.userwiseinterviewdetail.interview_no)
        	#if user.userwiseinterviewdetail.interview_no:

        	user.userwiseinterviewdetail.interview_no+=1
        	user.userwiseinterviewdetail.save()


    
        if form.is_valid():
        	instance=form.save(commit=False)
        	instance.upload= request.FILES['audio_data'] 
        	instance.name = str(request.user)+str(request.user.userwiseinterviewdetail.interview_no)+str(pk)
        	instance.user=request.user
        	instance.ques_no=pk
        	instance.interview_no=request.user.userwiseinterviewdetail.interview_no
        	instance.filler_word = PC if type(PC)==int else 0
        	instance.transcript = ans if ans!=0 else ""
        	instance.word_per_minute = word_min if type(word_min)==int else None
        	instance.score = score
        	instance.save()
        	return HttpResponse('success')
        else:
        	print(form.errors)
        return render(request,'index.html')
       
    else:
        form = UploadFileForm()
        ques=['What is Data Structure ?','What is Linked List ?','What is Greedy Algorithms ?','What is Stack ?','What is Recursion ?','asjkfajlf','7','8','9','10']
    if pk==5:
    	return render(request,'loading.html',{'interview_no':request.user.userwiseinterviewdetail.interview_no})
    	#return result(request,request.user.userwiseinterviewdetail.interview_no)
    else:	
    	return render(request, 'chinu.html', {'form': form, 'ques': ques[pk], 'prev_ques':ques[pk-1], 'ques_no':pk+1 })

def result(request,interview_number):
	posts=ModelFormWithFile.objects.filter(user=request.user,interview_no=interview_number)
	print(posts)
	filler_words=[]
	word_per_min=[]
	trans=[]
	scores=[]
	for post in posts:
		filler_words.append(post.filler_word)
		word_per_min.append(post.word_per_minute)
		scores.append(post.score)
		trans.append(post.transcript)
	scores=sum(scores)//len(scores)
	filler_words=sum(filler_words)//len(filler_words)
	clarity=100-5*filler_words
	args={'filler_words':filler_words,'word_per_min':word_per_min,'scores':scores,'trans':trans,'clarity':clarity,'user':request.user,'interview_no':interview_number}
	#print(args)
	return render(request,'web/result.html',args)