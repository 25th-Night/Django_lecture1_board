from django.db import models

# Create your models here.


class Profile(models.Model):
    """

    Args:
        models.XXXField(verbose_name="한글", {option})

        - verbose_name : optional
    """

    name = models.CharField(verbose_name="이름", max_length=10)
    age = models.PositiveSmallIntegerField(verbose_name="나이")
    email = models.EmailField(verbose_name="이메일", blank=True)
    description = models.TextField(verbose_name="소개", blank=True)

    created_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name="갱신일", auto_now=True, null=True)

    def __str__(self):
        """

        __str__ : 객체를 문자열로 표현한 것을 반환해주는 함수

        """
        return f"{self.name}의 프로필"

    # # model method
    # #   모델이 저장될 때, 필수적으로 수행하는 것들을 logic으로 넣을 수 있음.
    # def save(
    #     self,
    #     force_insert: bool = ...,
    #     force_update: bool = ...,
    #     using: Optional[str] = ...,
    #     update_fields: Optional[Iterable[str]] = ...,
    # ) -> None:
    #     # 로직 (저장될 때마다 수행되는 로직)
    #     #   예시 : 결제 주문서가 생성될 때, 난수값으로 생성함
    #     # order_code =
    #     return super().save(force_insert, force_update, using, update_fields)

    # # 모델을 이용해서 object를 뽑을 때, 사용
    # def get_name():
    #     return f"{self.name}"

    # object.get_name()

    class Meta:
        """

        verbose_name : 사용잦가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시됨. 영어를 기준으로 단수형
        verbose_name_plural : 사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시되는 것은 동일하나, 영어를 기준으로 복수형.
        한국어에서는 굳이 단수와 복수를 구별해 사용하지 않음.

        """

        verbose_name = "프로필"
        verbose_name_plural = "프로필 목록"


# 실무 패턴
## BaseModel 생성 후, 해당 모델을 상속받아서 다른 모델을 만듦.
##    created_at과 updated_at은 항상 필요하기 때문

# class BaseModel(models.Model):
#     created_at = models.DateTimeField(verbose_name="생성일", auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(verbose_name="갱신일", auto_now=True, null=True)


# class Profile(BaseModel):
#     """_summary_

#     Args:
#         models.XXXField(verbose_name="한글", {option})

#         - verbose_name : optional
#     """
#     name = models.CharField(vebose_name="이름", max_length=10)
#     age = models.PositiveSmallIntegerField(verbose_name="나이")
#     email = models.EmailField(verbose_name="이메일", blank=True)
#     description = models.TextField(verbose_name="소개", blank=True)
