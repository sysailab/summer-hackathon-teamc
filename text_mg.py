from text_read import text_read
from text_ai import text_ai


class text_mg():
    def __init__(self) -> None:
        pass

    def main():
        text = text_read.main()

        for i in range(len(text)):
            
            b_text = text_ai.main(text[i])

            print(f"---------------------------------------\n")
            print(b_text)
            print("---------------------------------------\n")


text_mg.main()