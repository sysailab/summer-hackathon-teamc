import openai
from config import OPENAI_KEY

openai.api_key = OPENAI_KEY

MODEL = "gpt-3.5-turbo"

first_q = "1. 논문의 제목 \n-English : \n-Korean : \n\n\
    2.논문의 저자명 \n-English : \n-Korean : \n\n\
        3.논문의 저자소속 \n -Korean : \n\n\
            4. 논문의 사사문구"


class text_ai():
    def __init__() -> None:
        pass

    
    
    def main(r_text):
  
        text = ""
        def input_text(r_text):
            response = openai.ChatCompletion.create(
                    model=MODEL,
                    messages=[
                        {"role": "user", "content": f"해당 글을 {first_q} \n지금 너에게 준 형식들로 맞춰서 나에게 알려줘\n{r_text}"}, 
                    ]
            )
            return response.choices[0].message.content
        
        r_text = r_text[:1400] + r_text[len(r_text)-2600:]
        # print(r_text)
        text += input_text(r_text)
        # print(text)

        # print(text)
        return text
        

    
