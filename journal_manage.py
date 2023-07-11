import openai
import glob
from journal import Journal

class JournalMangaement :
    def __init__(self, ai_key, model, path):
        openai.api_key = ai_key
        self.model = model
        self.path = path
        self.pdf_list = []
        self.result_data = []
        self.first_q = "1. 논문의 제목 \n-English : \n-Korean : \n\n\
            2.저자명 \n-English : \n-Korean : "
        
    def set_journal_list(self) :
        self.pdf_list = glob.glob(f'{self.path}/*.pdf')
        
    def get_journal(self) :
        if self.pdf_list == [] :
            return None
        return self.pdf_list.pop()
    
    def set_ai_content(self, path) :
        journal = Journal(path)
        journal.read_text()
        
        journal.check_data_type()
        if journal.data != "image" :
            journal.image_to_text()    
        if journal.data_clensing_front() :
            journal.data_clensing_back()
                
        return journal.get_data() + f"해당 글을 {self.first_q} \n지금 너에게 준 형식들로 맞춰서 나에게 알려줘\n"
        
    def input_text(self, data) :
        response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": data}, 
                    ]
            )
        return response.choices[0].message.content
    
    def run_ai(self) : 
        for path in self.pdf_list : 
            content = self.set_ai_content(path)
            print(f"\n\n {path}")
            print(content)
            # result = self.input_text(content)
            #self.result_data.append({"path" : content, "data" : result})