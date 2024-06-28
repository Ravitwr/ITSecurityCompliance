import json
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from gpt.prompt_selector import PROMPT
from gpt.gpt_wrapper import GptWrapper
from model.common_response import CommonResponse
from gpt.embedder import Embedder
from langchain_core.prompts import ChatPromptTemplate

class ControlSchema(BaseModel):
    control_family: str = Field(description="The category of controls pertaining to a specific function or area.")
    domain: str = Field(description="The broader category within which the control family falls.")
    sub_domain: str = Field(description="A more specific categorization within a domain, under which the control falls.")
    control_description: str = Field(description="A detailed explanation of what the control is and its purpose.")
    test_procedure: str = Field(description="A step-by-step guide to assess the efficacy and compliance of the control.")
    accepted_evidence: str = Field(description="The type of evidence that must be provided to demonstrate the control's effectiveness.")

class TestCasesQueryService:
    @staticmethod
    def get_testcase(query:str,doc_list:list[str])->CommonResponse:
        
        pydantic_parser = PydanticOutputParser(pydantic_object=ControlSchema)
        format_instructions = pydantic_parser.get_format_instructions()

        context=Embedder.getSearchResults(query,doc_list)
        # FORMATTED_PROMPT = PROMPT.format(query=query, context=context,format_instructions=format_instructions)


        prompt = ChatPromptTemplate.from_template(
            template=PROMPT,
            partial_variables = {
                "format_instructions": format_instructions,
                 "context":context
            }
        )
        llm=GptWrapper.get_gpt_35()
        full_chain = {"query": lambda x: x["query"]} | prompt | llm
        result_ = full_chain.invoke({"query": query})

        json_string=result_.content
        cleaned_string = json_string.replace('json', '').replace('```', '').strip()
        control_data = json.loads(cleaned_string)
        res={"response":control_data}
        return CommonResponse("success",result=res)