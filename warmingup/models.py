from django.db import models

# Create your models here.


class Attendance(models.Model):
    NONE = "NO"
    ATTENDANCE = "AT"
    ABSENT = "AB"
    PART = "PT"

    STATUS_CHOICES = [
        (NONE, "미지정"),
        (ATTENDANCE, "출석"),
        (ABSENT, "결석"),
        (PART, "일부참여"),
    ]

    name = models.CharField(verbose_name="이름", max_length=10)
    date = models.DateField(verbose_name="날짜")
    status = models.CharField(
        verbose_name="출석 여부", max_length=2, choices=STATUS_CHOICES, default=NONE
    )
    description = models.TextField(verbose_name="비고", blank=True)

    def __str__(self):
        return f"출석부 : {self.name} ({self.date})"

    class Meta:
        verbose_name = "출석부"
        verbose_name_plural = "출석부 목록"


class Question(models.Model):
    title = models.CharField(verbose_name="제목", max_length=50)
    content = models.TextField(verbose_name="내용", blank=True, null=True)
    is_answered = models.BooleanField(
        verbose_name="답변 여부", default=False, help_text="체크가 되어 있으면, 답변이 완료된 항목입니다", null=True
    )
    screenshot = models.ImageField(
        verbose_name=" 스크린샷", null=True, blank=True, upload_to="qs/image/"
    )

    created_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="갱신일", auto_now=True)

    def __str__(self):
        return f"질문 : {self.title}"

    class Meta:
        verbose_name = "질문"
        verbose_name_plural = "질문 목록"
