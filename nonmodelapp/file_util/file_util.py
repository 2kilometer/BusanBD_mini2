### 파일 업로드(저장) 처리를 위한 라이브러리
from django.core.files.storage import FileSystemStorage

### 파일 다운로드 처리를 위한 라이브러리
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import os
from django.http import HttpResponse

class File_Util :
    ### 기본 설정 변수 정의하기
    # 파일 원본 이름
    file_nm = ""
    # 물리적인 파일 업로드 경로
    upload_dir = ""
    # 물리적인 다운로드 경로
    download_dir = ""
    # 물리적인 다운로드 경로 + 파일명
    download_full_name = ""
    # 물리적인 이미지 경로
    img_dir = ""
    # 물리적인 이미지 경로 + 파일명
    img_full_name = ""
    # 파일 사이즈
    file_size = 0
    # 순수 파일명
    filename = ""
    
    ########### [File Upload 처리] ########
    # - File Upload를 위한 변수값 setting하기
    def setUpload(self, file_nm, upload_dir, img_dir, download_dir) :
        self.file_nm        = file_nm
        self.upload_dir     = upload_dir
        self.img_dir        = img_dir
        self.download_dir   = download_dir 
        
    # - File Upload 하기
    def fileUpload(self) :
        # 파일 처리를 위한 라이브러리 클래스 생성
        fs = FileSystemStorage(self.upload_dir, self.download_dir)
        
        ### 서버 영역에 파일 저장시키기 
        # - save(파일명, 파일정보) : 실제 파일 업로드시키는 함수
        # - self.filename : 실제 업로드된 파일이름
        self.filename = fs.save(self.file_nm.name, self.file_nm)
        
        ### 파일 업로드 이후 기본값 셋팅하기
        self.setParameter()
        
    ### 파일 업로드 이후 별도로 사용할 기본값 셋팅함수 
    # - 아래 변수들을 이용해서 DB에 저장 또는 
    #   html 페이지에 보여주면 됩니다.
    def setParameter(self) :
        # 파일 사이즈
        self.file_size = self.file_nm.size
        # 이미지 경로+파일명
        self.img_full_name = self.img_dir + self.filename
        # 다운로드 경로 + 파일명
        self.download_full_name = self.download_dir + self.filename
        
        
    ########### [File Download 처리] ########
    ### 파일 다운로드를 위한 다운로드 변수 셋팅
    def setDownload(self, download_full_name) :
        # 물리적인 다운로드 경로 + 파일명
        self.download_full_name = download_full_name
        
    ### 실제 파일 다운로드 처리하기
    def fileDownload(self) :
        # rb : r은 읽기(read), b는 바이너리(binary)
        binary_file = open(self.download_full_name, "rb")
        response = HttpResponse(binary_file.read(),
                                content_type="application/octet-stream; charset=utf-8")
        
        response["Content-Disposition"] = "attachment; filename=" + os.path.basename(self.download_full_name)
        
        return response