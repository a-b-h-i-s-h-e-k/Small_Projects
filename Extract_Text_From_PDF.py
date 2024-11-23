'''

Sometimes a Python developer needs to collect some text information from PDF 
files. So extracting text from a PDF is a problem we should know how to solve 
as a Python developer.



we must know how to collect text from pdf as a Python developer. This skill is 
useful when working with resumes. Extracting text from a pdf file is not a difficult 
task at all. For this task, you need to install a Python library known as PyPDF2.

we can easily install this Python library by using the pip command in your terminal 
or command prompt as mentioned below:

    pip install pypdf2

After installing this Python library, we are all prepared for extracting text from 
any pdf file.

'''



# import PyPDF2
# pdf = open("Python_Complete_Notes.pdf", "rb")
# reader = PyPDF2.PdfFileReader(pdf)
# page = reader.getPage(0)
# print(page.extractText())


# In the fourth line of the above code, the getPage() method will help you specify 
# the page number you want to extract text from.




import PyPDF2

with open('Python_Complete_Notes.pdf', 'rb') as pdf:
    reader = PyPDF2.PdfReader(pdf)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

print(text)



'''
-> Class Name: PdfFileReader has been replaced with PdfReader.
-> Accessing Pages: Instead of using getNumPages() and getPage(), 
we can directly iterate over reader.pages.
'''