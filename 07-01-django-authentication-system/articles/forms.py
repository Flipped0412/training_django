from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    # Python의 Inner class라는 문법과 무관.
    # 모델 클래스 지정
    class Meta:
        # 어떤 클래스의 모든 필드를 사용자가 입력하지 ㅏㅇㄶ기 때문에
        # 어떤 필드를 입력받을건지 명시
        model = Article
        fields = '__all__'
        # fields = ('title', 'content')
        # exclude = ('title',)  # . . ? 이건 뭔지 몰겠음
