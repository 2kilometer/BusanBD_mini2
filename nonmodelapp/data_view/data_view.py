import seaborn as sns
import matplotlib.pyplot as plt

class Data_View :
    ### 클래스 생성 시에 데이터수집부터 시각화까지 함수 실행시키기
    # - 초기화 함수 생성 (생성자)
    # - 생성자 함수는 클래스 생성시에 자동으로 호출되어 실행됨
    def __init__(self) :
        # 데이터 읽어들이는 함수 호출
        self.initDataFrame()
        
        # 데이터 전처리하는 함수 호출
        self.data_preprocess()
        
        # 데이터 시각화하는 함수 호출
        self.initVisualization()
        
        # 시각화를 이미지로 저장하는 함수 호출
        self.saveFig()
    
    # 데이터 읽어들이는 함수
    def initDataFrame(self):
        self.ans = sns.load_dataset("anscombe")
    
    # 데이터 전처리하는 함수
    def data_preprocess(self):
        self.data1 = self.ans[self.ans["dataset"] == "I"]
        self.data2 = self.ans[self.ans["dataset"] == "II"]
        self.data3 = self.ans[self.ans["dataset"] == "III"]
        self.data4 = self.ans[self.ans["dataset"] == "IV"]
    
    # 데이터 시각화하는 함수
    def initVisualization(self):
        ### 그래프 상위 객체 변수에 담기
        self.fig = plt.figure()
        
        ### 4개의 그래프가 들어갈 수 있는 공간 만들기
        # - add_subplot(행, 열, 위치번호) : 작은 공간 만들기
        ax1 = self.fig.add_subplot(2, 2, 1)
        ax2 = self.fig.add_subplot(2, 2, 2)
        ax3 = self.fig.add_subplot(2, 2, 3)
        ax4 = self.fig.add_subplot(2, 2, 4)
        
        ### 각 그래프에 제목 넣기
        ax1.set_title("data1")
        ax2.set_title("data2")
        ax3.set_title("data3")
        ax4.set_title("data4")
        
        ### 각각의 공간에 데이터를 넣어서 그래프 그리기
        ax1.plot(self.data1["x"], self.data1["y"], "o", c="b")
        ax2.plot(self.data2["x"], self.data2["y"], "o", c="r")
        ax3.plot(self.data3["x"], self.data3["y"], "o", c="g")
        ax4.plot(self.data4["x"], self.data4["y"], "o", c="y")
        
        ### 전체 그래프 제목
        self.fig.suptitle("Anscombe Data")
        
        ### 정렬
        self.fig.tight_layout()
    
    # 시각화를 이미지로 저장하는 함수
    def saveFig(self):
        save_path = "./nonmodelapp/static/nonmodelapp/data_img/fig.png"
        self.fig.savefig(save_path)