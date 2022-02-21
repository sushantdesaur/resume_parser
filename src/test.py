from pyresparser import ResumeParser
import os 
from docx import Document

file = os.path.join( '/home/rsilvergun/Documents/Work/Python/Resume-Parser/sample-data/resume.docx')


data = ResumeParser(file).get_extracted_data()

print(data)
