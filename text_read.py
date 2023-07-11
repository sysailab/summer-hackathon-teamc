import fitz
import os
import time
path = "./test_data"


class text_read():
    def __init__(self) -> None:
        pass

    
                    
    def main():
        
        
        def read_pdf(folder_path):
            t_list = []
            
            for filename in os.listdir(folder_path):
                text = ""
                if filename.endswith(".pdf"):
                    file_path = os.path.join(folder_path, filename)
                    doc = fitz.open(file_path)
                    for page in doc:
                        text += page.get_text()
                    t_list.append(text)
                    doc.close()
            return t_list

        text_list = read_pdf(path)

      

        return text_list

# text_read.main()