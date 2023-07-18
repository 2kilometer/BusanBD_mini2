### 행렬데이터 처리 라이브러리
import pandas as pd

### 사용하는 라이브러리(패키지)
# - install 해야 사용가능
# conda install -c conda-forge folium
import folium

class Map_View :
    ### 최초 실행되는 생성자 만들기
    # - 생성자 호출시 자동으로 3개의 함수를 순서대로 실행시키게 됨..
    def __init__(self) :
        ### 데이터 읽어들이는 함수 호출
        self.initDataFrame()
        ### 지도맵(기본지도) 그리는 함수 호출
        self.map_base()
        ### 타입별로 마커표시하는 함수 호출
        self.map_location()
        
    
    ### 데이터 읽어들이는 함수 호출
    def initDataFrame(self) :
        file_path = "./nonmodelapp/map_view/4_4_seoul_starbucks_list.xlsx"
        self.seoul_starbucks = pd.read_excel(file_path)
    
    ### 지도맵(기본지도) 그리는 함수 호출
    def map_base(self) :
        self.starbucks_map = folium.Map(
            ### 최초에 보여줄 지도의 중심위치(위/경도) 지정
            # - 서울 중심점
            location = [37.573050, 126.979189],
            
            ### 지도 스타일 지정하기
            # 도시형 건물 스타일 지정(가장 일반적 스타일)
            tiles = "openstreetmap",
            
            ### 최초에 보여줄 zoom 사이즈 지정하기
            zoom_start = 11,
            
            ### 지도 너비 
            width = "100%",
            
            ### 지도 높이
            height = "100%"
        )
    
    ### 타입별로 마커표시하는 함수 호출
    def map_location(self) :
        for idx in self.seoul_starbucks.index :
            # print(idx)
            lat = self.seoul_starbucks.loc[idx, "위도"]
            lng = self.seoul_starbucks.loc[idx, "경도"]
            s_type = self.seoul_starbucks.loc[idx, "매장타입"]
            
            f_color = ""
            size = 1
            
            if s_type == "general" :
                f_color = "green"
                size = 3
                
            elif s_type == "reserve" :
                f_color = "blue"
                size = 5
            
            else :
                f_color = "red"
                size = 5
                
            ### 지도에 표시할 마킹 모양 등 스타일 지정
            folium.CircleMarker(
                # 마커의 위치 지정 : 위도, 경도
                location = [lat, lng],
                # 마커 채우기 색상 
                fill_color = f_color,
                # 마커 투명도(0~1)
                fill_opacity = 1,
                # 마커 테두리 색상
                color = "yellow",
                # 마커 테두리 두께
                weight = 1,
                # 마커 크기
                radius = size
            ).add_to(self.starbucks_map)
            
            
    ### 지도맵 데이터를 HTML로 처리하기(views.py에 리턴해주기)
    def getMap(self) :
        ### _repr_html_() : 지도맵을 html로 변환해 주는 함수...
        return self.starbucks_map._repr_html_()
    
    ### 사용된 데이터프레임도 리턴하기
    def getDataFrame(self) :
        return self.seoul_starbucks