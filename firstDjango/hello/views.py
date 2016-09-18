from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpRequest
from django.template import loader,Template
import datetime
from hello.models import Publisher
from hello.forms import Publisher_form

# Create your views here.
def hello(request):



    athlete = '1'
    athlete_list=[1,2,3,4,5,6]
    value = "This text will be HTML-escaped, and will appear in all lowercase."
    value1 = 10
    value2 = datetime.datetime.now()
    value3 = Template("<a href='http://www.maiziedu.com' target='blank'>麦子学院</a>")
    return render(request, 'a.html', locals())
    # return render_to_response('table.html', locals())
	# t = loader.get_template('table.html')
	# c = {'user_list':user_list}
	# return HttpResponse(t.render(c, request), content_type='text/html')



	# return redirect('http://www.baidu.com/')
# def test(request,id):
# 	user_list = User.objects.all()
# 	return render(request,'table.html',{'user_list':user_list})
# def test1(request,id,key):
# 	user_list = User.objects.all()
# 	return render(request,'table.html',{'user_list':user_list})
def add_publisher(request):
    if request.method=='POST':
        # 1.不使用django Form对象
        # Publisher.objects.create(
        #     name=request.POST['name'],
        #     address=request.POST['address'],
        #     city=request.POST['city'],
        #     state_province=request.POST['state_province'],
        #     country=request.POST['country'],
        #     website=request.POST['website'],
        # )
        publisher = Publisher_form(request.POST)
        if publisher.is_valid():
            # Publisher.objects.create(
            #     name=publisher.cleaned_data['name'],
            #     address=publisher.cleaned_data['address'],
            #     city=publisher.cleaned_data['city'],
            #     state_province=publisher.cleaned_data['state_province'],
            #     country=publisher.cleaned_data['country'],
            #     website=publisher.cleaned_data['website'],
            # )
            publisher.save()

        else:
            return render(request, 'add_publisher.html', locals())
        return HttpResponse("出版社信息添加成功")
    else:
        publisher = Publisher_form()
        return render(request, 'add_publisher.html', locals())