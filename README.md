# OpenAI-Summary
 Takes in a pdf file within the "PDFs" path and creates markdown notes for the files

# Set up
You must have Python3 on your machine.

The following python libraries are required before running the programme:
- [Fitz](https://pymupdf.readthedocs.io/en/latest/module.html)
- [Pytesseract](https://pypi.org/project/pytesseract/)

Sign up for OpenAi and obtain an API Key, put this key in a file under the same folder and name it "api_key.txt"

Under settings, indicate where tesseract is downloaded. 

# How to use
Download the repo.
Put the PDFs you want to summarise under the ```PDFs``` folder
Run ```summary.py``` 
Once the programme finishes running, there should be folders with the PDFs' titles and markdown notes within those folders that summarises each page of the pdf

# How it works
- First the programme saves each page of the PDF as an image
- Tesseract then reads those images and extracts the texts out 
- The text in each page is attached to a prompt and is sent to OpenAI's API to be summarised
- The response is captured in an output text file

There are alternatives such as PDFplumber that can extract the texts out. I have opted otherwise because the formatting and accuracy of the text appears off when PDFplumber is used in this context. 

You should try building this yourself! This is a fairly simply project and most of the heavylifting is done by OpenAI already.

