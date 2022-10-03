from django.shortcuts import redirect

from django.views.generic import TemplateView

from .models import Attendance, Question

# Create your views here.


def index(request):
    return redirect("attendance_list")


class AttendanceView(TemplateView):
    template_name = "attendance/list.html"

    def get_context_data(self, *args, **kwargs):
        attendance_qs = Attendance.objects.all().order_by("-date")

        context = {}
        context["attendance_qs"] = attendance_qs
        return context


class AttendanceCreateView(TemplateView):
    template_name = "attendance/enrolled.html"

    def get(self, request, **kwargs):
        response = super(AttendanceCreateView, self).get(self, request)
        return response

    def post(self, request):
        name = request.POST.get("name", None)
        date = request.POST.get("date", None)
        status = request.POST.get("status", None)
        description = request.POST.get("description", None)

        Attendance.objects.create(name=name, date=date, status=status, description=description)

        return redirect("attendance_list")


class QuestionView(TemplateView):
    template_name = "question/list.html"

    def get_context_data(self, *args, **kwargs):
        question_qs = Question.objects.all().order_by("created_at")

        context = {}
        context["question_qs"] = question_qs
        return context


class QuestionCreateView(TemplateView):
    template_name = "question/enrolled.html"

    def get(self, request, **kwargs):
        response = super(QuestionCreateView, self).get(self, request)
        return response

    def post(self, request):
        title = request.POST.get("title", None)
        content = request.POST.get("content", None)
        is_answered = request.POST.get("is_answered", None)
        screenshot = request.FILES.get("screenshot", None)

        Question.objects.create(
            title=title, content=content, is_answered=is_answered, screenshot=screenshot
        )

        return redirect("question_list")


class QuestionDetailView(TemplateView):
    template_name = "question/detail.html"

    def get_context_data(self, pk, *args, **kwargs):
        Question.objects.all()

        question = Question.objects.filter(id=pk).last()

        context = {}
        context["question"] = question
        return context
