import json
import os
import pdfplumber
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from gpt.prompt_selector import EVIDENCE_PROMPT
from gpt.gpt_wrapper import GptWrapper
from model.common_response import CommonResponse
from langchain_core.prompts import ChatPromptTemplate


class EvidenceResultSchema(BaseModel):
    result: str = Field( description="The pass and fail status of the evidence after verification against the test case.")
    summary: str = Field(description="A 20 word summary of the evidence content and how it pertains to the test case.")

    
def extract_text_from_pdf_with_pdfplumber(filename):
    text = []
    with pdfplumber.open(filename) as pdf:
        for page in pdf.pages:
            text.append(page.extract_text())
    return '\n'.join([t for t in text if t])

class EvidenceUploadService:
    @staticmethod
    def verify_evidence(evidence_list: list[dict[str, str]])->CommonResponse:
        
        pydantic_parser = PydanticOutputParser(pydantic_object=EvidenceResultSchema)
        format_instructions = pydantic_parser.get_format_instructions()
        res=[]
        for evidence in evidence_list:
            cwd = os.getcwd()  # Get the current working directory (cwd)
            cwd+="\\test_case_files\\"
            filepath=cwd+evidence["filename"]
            pdf_text = extract_text_from_pdf_with_pdfplumber(filepath)
            prompt = ChatPromptTemplate.from_template(
                template=EVIDENCE_PROMPT,
                partial_variables = {
                    "name": evidence['name'],
                    "context":evidence['description'],
                    "evidence": evidence["evidence"], 
                    "description": evidence["description"],
                    "format_instructions": format_instructions
                }
            )
            llm=GptWrapper.get_gpt_35()
            full_chain = {"pdf_text": lambda x: x["pdf_text"]} | prompt | llm
            result_ = full_chain.invoke({"pdf_text": pdf_text})

            json_string=result_.content
            cleaned_string = json_string.replace('json', '').replace('```', '').strip()
            control_data = json.loads(cleaned_string)
            control_data["id"]=evidence["id"]
            res.append(control_data)
        return CommonResponse("success",result=res)
    


