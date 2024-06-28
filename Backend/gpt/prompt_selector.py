PROMPT="""you are helpful chatbot that helps in drafting test cases for control test cases based on the query 
and context.
query={query}
context={context}

{format_instructions}
"""

EVIDENCE_PROMPT="""You are a helful chatbot that helps in verifying the evidence against the given test case.Provided info is
name:{name}
description:{description}
evidence: {evidence}

this is the text content of the pdf. {pdf_text}

{format_instructions}
"""