from django.shortcuts import render

# Create your views here.

### mainapp에서 최초 호출 함수로 사용..
def index(request):
    ### 외부 html 파일을 사용하기 위해 render() 사용
    # - 외부 html은 templates/mainapp에 만들도록 규칙을 만들었습니다.
    # - setting.py에서 templates 정의해 놓았음...
    return render(request,
                  "mainapp/index.html",
                  {})
    
    
    


