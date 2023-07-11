import fitz

class Journal : 
    def __init__(self, path) :
        self.type = "" #journal or abstract
        self.data_type = "" #text or img
        
        self.data = "" #journal text
        
        self.path = path #pdf path
        
        self.title = "" #journal title
        self.acknowl = "" #journal acknolegement 
        self.author = [] #journal Author
        
        #front : fitz document
        #back : fitz document
            
    def read_text(self) : 
        #journal의 type 설정 후 확인 데이터 확인
        doc = fitz.open(self.path)
        front, back, self.type = self.count(len(doc))
        
        self.front = doc[:front]
        self.back = doc[-back:]
        
    def count(self, page) :
        #1페이지, 2~3페이지, 10페이지 이하, 30페이지 이하, 이상
        if page <= 1 :
            return (1, 0, "abstract")
        elif page <= 3 :
            return (1, 1, "abstract")
        elif page <= 10 :
            return (3, 2, "journal")
        elif page <= 30:
            return (3, 5, "journal")
        else :
            return (3, 10, "journal")
    
    def check_data_type(self) :
        #Pdf : img or text
        for text in self.front : 
            self.data += text
            
        if len(self.data) <= 1000 :
            self.data_type = "image"
            
                
    def data_clensing_front(self) :      
        text = self.data.lower().replace(" ", "")
        #대소문자 구분 및 공백 제거
                
        #앞에 사사문구가 있을경우
        if "ackowledgments" in text or "감사의말" in text:
            return self.data            
        
        #초록, 서론의 문구가 있을경우
        if "서론" in text or "introduction" in text : 
            return self.data
    
    def data_clensing_back(self) : 
        for page in reversed(self.back) :
            text = page.get_text()
            check = text.lower().replace(" ", "")
            
            #사사문구 페이지
            if "ackowledgments" in check or "감사의말" in check :
                bac_data = text
                break 
             
            #참고 논문과 이전페이지만 봄        
            if "reference" in check or "참고논문" in check :
                bac_data = text
                continue
        
        self.data += bac_data
         