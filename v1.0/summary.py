import openai
import pdfplumber
import numpy as np

paperFilePath = "input.pdf"
counter=0

def displayPaperContent(paperContent, page_start=0, page_end=5):
    for page in paperContent[page_start:page_end]:
        print(page.extract_text())


def showPaperSummary(paperContent):
    counter=0
    tldr_tag = "\n in summary:"
    openai.api_key = open("api_key.txt", "r").read()
    engine_list = openai.Engine.list() # calling the engines available from the openai api 
    
    for page in paperContent:    
        text = page.extract_text()+ tldr_tag
        response = openai.Completion.create(engine="davinci",prompt=text,temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["{}"]
        )
        counter+=1
        print(response["choices"][0]["text"])
        # append this page's summary into an output.md file
        with open("output.txt", "a") as f:
            f.write(response["choices"][0]["text"] + "/n")
    print(f"\n end of summary,total pages: {counter}")

paperContent = pdfplumber.open(paperFilePath).pages
showPaperSummary(paperContent)
