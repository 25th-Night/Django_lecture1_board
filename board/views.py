from django.shortcuts import HttpResponse, render
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# 1.
#    request를 받아서 response를 보내는 함수
#    화면에 보여줄건데, 브라우저에서 화면을 출력하는 기준? URL!!
#    views.py에서 함수 생성 후, urls.py에 해당 함수를 통해 response를 화면에 출력할 주소를 연결해줘야 함.
# def index_function(request):
#     return HttpResponse("index by function called")

# 2. View를 생성하는 2가지 방법
#   Function Based View (FBV)
def index_function(request):
    # GET
    if request.method == "GET":
        return HttpResponse("index by GET function called")
    # POST
    if request.method == "POST":
        return HttpResponse("index by POST function called")


#   Class Based View (CBV)
class IndexClass(View):
    # GET
    def get(self, request):
        return HttpResponse("index by GET class called")

    # POST
    def post(self, request):
        return HttpResponse("index by POST class called")


@csrf_exempt
def index_function2(request):
    # GET
    if request.method == "GET":
        return render(request, "practice/index_f2.html", {})
    # POST
    if request.method == "POST":
        return HttpResponse("index by POST function2 called")


@csrf_exempt
def index_function3(request):
    # GET
    if request.method == "GET":
        # context는 dictionary 형태(key : value)로 되어 있는 우리의 data를 전달함.
        #   웹페이지라는 것은 결국은 어떠한 정보를 전달하기 위한 페이지이고,
        #   그런 데이터를 우리는 context를 이용하여 전달함.
        context = {
            "method": request.method,
            "user": request.user,
            "temp": "welcome to my site!!",
        }
        return render(request, "practice/index_f3.html", context)
    # POST
    if request.method == "POST":
        return HttpResponse("index by POST function3 called")


@csrf_exempt
def index_function4(request, name, code):
    # GET
    if request.method == "GET":
        context = {
            "method": request.method,
            "user": request.user,
            "temp": "welcome to my site!!",
            "name": name,
            "code": code,
        }
        return render(request, "practice/index_f4.html", context)
    # POST
    if request.method == "POST":
        return HttpResponse("index by POST function4 called")


class IndexClass2(TemplateView):
    # 명시적으로 template_name을 선언
    template_name = "practice/index_c2.html"
    # GET
    def get(self, request):
        response = super(IndexClass2, self).get(self, request)
        return response

    # POST
    def post(self, request):
        return HttpResponse("index by POST class2 called")
