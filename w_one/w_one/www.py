from django.http import HttpResponse
import datetime
def index(request):
    s = datetime.datetime.now()
    return HttpResponse(s)
def one(request):
    return HttpResponse('你们这群傻逼')

def two(request,id):
    s = "我来自%s,你来自%s"%(id)
    return HttpResponse(s)

def there(request,id):
    return HttpResponse('什么东西')


def four(request,id,name):
    s = 'shenmmmm%s,%s'%(id,name)
    return HttpResponse(s)