import pdfplumber
import json
import os
import re

def get_file_path(file_name):
    current_directory = os.getcwd()

    # Concatenate the file name or relative path
    file_path = os.path.join(current_directory, file_name)
    return file_path

def text_extractor(pdf_file):
    with pdfplumber.open(pdf_file) as pdf: 
            text = ''
            for page in pdf.pages:
                text = text + page.extract_text(encoding='utf-8') #storing all the pdf texts in a single string
        #text = text.replace('\n','')
    pdf.close()
    return text

class PDFparser:
    def __init__(self) -> None:
        pass

    def pdftotext(self,pdf_file,output_text_file):
        text = text_extractor(pdf_file)

        with open(output_text_file, "w", encoding="utf-8") as file:
            file.write(text)
        file.close()
        
        file_path = get_file_path(output_text_file)
        print('Text file saved at location '+ file_path)

    def simplePdftoJson(self,pdf_file,output_json_file):
        text = text_extractor(pdf_file)
        temp_dict = {'text':text}

        with open(output_json_file,'w', encoding="utf-8")as file:
            json.dump(temp_dict,file,indent=4)

        file_path = get_file_path(output_json_file)
        print('JSON file saved at location '+ file_path)

    def pdftojsonl(self,pdf_file,output_jsonl_file):
        #This function converts pdf file containing question answer pairs into jsonl document
        '''To process documents in an optimal way, the PDF file containing Question-Answer pairs should be in the format:
        Question: some_random_question
        Answer: Answer to the question'''
        text = text_extractor(pdf_file)
        updated_text = text.replace('\n',' ')

        # Define the pattern for question-answer pairs using regular expressions
        pattern = r"Question:\s*(.*?)\s*Answer:\s*(.*?)(?=\s*Question:|$)"

        # Find all matches of question-answer pairs in the input string
        matches = re.findall(pattern, updated_text, re.DOTALL)
        qa_pairs = [{'prompt': match[0].strip(), 'completion': match[1].strip()} for match in matches]

        with open(output_jsonl_file,'w', encoding="utf-8")as file:
            json.dump(qa_pairs,file)

        file_path = get_file_path(output_jsonl_file)
        print('JSONL file saved at location '+ file_path)

    
