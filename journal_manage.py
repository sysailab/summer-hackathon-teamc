import openai
import glob
from journal import Journal

class JournalMangaement :
    def __init__(self, ai_key, model, path):
        openai.api_key = ai_key
        self.model = model
        self.path = path
        self.pdf_list = []
        
    def set_journal_list(self) :
        self.pdf_list = glob.glob(f'{self.path}/*.pdf')
        
    def get_journal(self) :
        if self.pdf_list == [] :
            return None
        return self.pdf_list.pop()
    


    