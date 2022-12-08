# OpenAI-Summary
 Takes in a pdf file within the "PDFs" path and creates markdown notes for the files

# Set up
You must have Python3 on your machine.

The following python libraries are required before running the programme:
- [Fitz](https://pymupdf.readthedocs.io/en/latest/module.html)
- [Pytesseract](https://pypi.org/project/pytesseract/)
- [OpenAI](https://beta.openai.com/docs/api-reference?lang=python)

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

# Detailed installation guide
Download the code from this repo and unpack it somewhere convenient

If you do not have Python...
- Go to Python's [download page](https://www.python.org/downloads/) and download the installer. Run as per instructed 

(For Mac users) If you do not have Homebrew installed...
- Open terminal
    - INTEL MAC: Run ```/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```
    - ARM MAC: Run ```arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"```

Downloading Fitz:
- Mac: Run ```python3 -m pip install PyMuPDF```
- Windows: Run ```python -m pip install PyMuPDF```

Download PyTesseract:
- Install PyTesseract:
    - Mac: Run ```brew install tesseract```
        - Note: you need to download Homebrew to use brew formulae
    - Windows: Run ```python -m pip install pytesseract```
- Find your path to Tesseract
    - For Mac users, type ```which tesseract``` in terminal. It should give you a path as a response
    - Open summary.py in the zip you downloaded and check that the path under settings is the same as the one the terminal told you
        - if they are not the same, paste the address in the settings (line 40) as ```path_to_tesseract = <your path>```

If any of the above installation doesn't work, it may be due to permission issues. add ```sudo ``` in front of the command to run as administrator. You may be prompted to key in your profile's password in terminal


Get an API Key from OpenAI:
- Sign up for OpenAI at [this page](https://beta.openai.com/signup/)
- Once signed up, go to top right and click your icon > View API Keys
- Generate the API key and copy it into a .txt document. Name this "api_key.txt" and put it in the same folder as summary.py
Note: DO NOT PUBLISH THIS KEY
- If the money runs out for your key... you gotta set up your payment methods to top it up. Go to [OpenAI](https://beta.openai.com/) page to find out more on billing.

Once you set up, this is how to use your summarizer:
1. Put the PDFs you want to summarise into "PDFs" folder
2. Open summary.py in a code editor and hit run/ build
    1. If you do not have a code editor, right click on summary.py > Get Info > copy the path under "Where: "
    2. Open terminal, key in ```cd {path copied}```", where {path copied} is the path to the folder containing summary.py. Add a backslash before any spaces in the path
    3. Hit enter to change directory to the folder, if successful, terminal should echo back the folder name
    4. Run ```python3 summary.py``` if you are on MacOS, or ```python summary.py``` on Windows
3. Once it starts running, folders with the PDFs' names will be created. 
4. When the script stops running, you can remove the "images" folder under each created folder. I can't get python to do this automatically because of security reasons so please remove these manually!
5. There will also be a file in .md format, this is your summarized bullet points. 
    1. You can import this into Notion or Obsidian
    2. You can also change line 122 in summary.py from ```output_file_name=DIRECTORY+"/"+file_name+"/"+file_name+".md"``` to ```output_file_name=DIRECTORY+"/"+file_name+"/"+file_name+".txt"``` if you want .txt file instead.