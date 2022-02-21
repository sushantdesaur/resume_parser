from pyresparser import ResumeParser
import os 
from docx import Document

data = ResumeParser('/home/rsilvergun/Documents/Work/Python/Resume-Parser/src/resume.docx').get_extracted_data()

print(data)
