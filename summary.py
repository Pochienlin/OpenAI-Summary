'''
Summary script uses openAI's davinci-002 model to summarize texts, page by page

This script first converts all pdf within the folder into images, then reads the text off the images 
The same was attempted using pdfplumber to extract text directly from pdf, but resulted in issues due to spacings and how the text was parsed, so this is the workaround

Running this script directly will call the for-loop to iterate through the entire folder, alternatively one can import the methods from this file without calling the for-loop at the end

PRE-REQUISITES:
- Download fitz
- Download openai
- Download PyTesseract
the above can be done using terminal with homebrew

- Set pdfs to be summarised within directory, copy the directory path and set it below in -SETTINGS-
- Set a folder in the directory to store the images. Remove these images after summarizing to avoid taking up too much memory
    - Script cannot remove it for you due to permission issues
- Set this script in the directory

OUTPUT:
- You'll end up with a folder with the pdf's name and a .txt file with the same name as the folder inside
- The .txt file will have the contents summarised
'''
###     ---IMPORTS----
# Summary AI
import openai
import numpy as np
# Fitz is used to convert pdf to image
import fitz
# PIL is used with tesseract to read text from image
from PIL import Image
from pytesseract import pytesseract
# For file management
import os
import glob

###      ----SETTINGS----
DIRECTORY = "/Users/pochienlin/Desktop/OpenAI Summary"
path_to_tesseract = r'/usr/local/bin/tesseract'
# Use a check dir line to create an image file if it doesn't exist yet?

###     ----FUNCTIONS----
def convertPDFtoImage(file):
    dpi = 300  # choose desired dpi here
    zoom = dpi / 72  # zoom factor, standard: 72 dpi
    magnify = fitz.Matrix(zoom, zoom)  # magnifies in x, resp. y direction
    doc = fitz.open(file)  # open document
    # get the name of the pdf file
    file_name = os.path.basename(file)
    # remove the .pdf extension
    file_name = file_name[:-4]
    # create image folder under the same directory
    #check if DIRECTORY/file_name exists
    if not os.path.exists(DIRECTORY+"/"+file_name):
        os.mkdir(DIRECTORY+"/"+file_name)
        os.mkdir(DIRECTORY+"/"+file_name+"/images")
    for page in doc:
        pix = page.get_pixmap(matrix=magnify)  # render page to an image
        pix.save(f"{file_name}/images/page-{page.number}.png")
    return True

def call_openai(model, prompt):
    response = openai.Completion.create(model=model,prompt=prompt,temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0]["text"]

def SummariseProse(pageText,output_name, page_no):
    tldr_tag = "Summarize the following, ignoring standalone phrases. Use bullet points describing supporting evidence. Format as markdown format in bullet points:\n"
    openai.api_key = open("api_key.txt", "r").read()
    # engine_list = openai.Engine.list() # calling the engines available from the openai api 
    text = tldr_tag+pageText
    summary = call_openai("text-davinci-003", text)
    # # Remove line breaks
    # summary = summary.replace("\n","")
    # # Add line break before headers
    # summary = summary.replace("###","\n###")
    # # Add line break before points
    # summary = summary.replace("- ","@@")
    # summary = summary.replace("@@","\n- ")
    # summary = summary.replace("/n","")
    with open(output_name, "a") as f:
        f.write("\n\n ## PAGE "+str(page_no+1)+"\n\n"+summary + "/n")
    return summary

def CompileImages(folder_name, output_name):
    # loop through images, call davinci to summarise and write into file
    for i in range(len(os.listdir(folder_name))):
        filename = f"page-{i}.png"
        f = os.path.join(folder_name,filename)
        print(f)
        # opening image using PIL Image
        img = Image.open(f)
        # path where the tesseract module is installed
        pytesseract.tesseract_cmd = path_to_tesseract
        # converts the image to result and saves it into result variable
        result = pytesseract.image_to_string(img)
        # use Davinci-002 in OpenAI to clean up the text
        # print(result)
        extractedText = SummariseProse(result,output_name,i)
        # print(extractedText)

###     ---FUNCTION CALLS----
if __name__ == "__main__":
    # iterate through all .pdf files within DIRECTORY
    for file in glob.glob(DIRECTORY+"/PDFs/*.pdf"):
        # convert pdf to images
        convertPDFtoImage(file)
        # get the name of the pdf file
        file_name = os.path.basename(file)
        # remove the .pdf extension
        file_name = file_name[:-4]
        # create a new folder with the same name as the pdf file
        # os.mkdir(DIRECTORY+"/"+file_name)
        # compile images into a markdown file
        print(file_name)
        images_folder=file_name+"/images"
        output_file_name=DIRECTORY+"/"+file_name+"/"+file_name+".md"
        CompileImages(images_folder,output_file_name)





