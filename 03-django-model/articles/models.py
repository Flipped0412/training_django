from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)  # 데이터 베이스 테이블의 열을 나타냄. 이는 유효성 검사 측면에서 권장되는 선택 사항.
    content = models.TextField()  # 길이 제한 없는 대용량 텍스트 저장
    # 더 많은 필드는 장고 공식 사이트를 참고하여 그때그때 필요한 필드 찾아 사용하기
    # 여기서 필드는 하나의 클래스로 클래스를 불러와 지정해주는 방식

    created_at = models.DateTimeField(auto_now_add=True)  # 데이터가 처음 생성될 때만
    updated_at = models.DateTimeField(auto_now=True)  # 데이터가 저장될 때마다
