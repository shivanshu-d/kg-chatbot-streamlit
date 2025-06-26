import fitz
doc = fitz.open("D:\\Data Science\\knowledge-graph-chatbot\\data\\Ebay user agreement.pdf")
text = "".join([page.get_text() for page in doc])

with open("D:\\Data Science\\knowledge-graph-chatbot\\data\\cleaned_user_agreement.txt", "w", encoding="utf-8") as f:
    f.write(text)
