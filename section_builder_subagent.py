# section_builder.py
from states import section_builder_subagent  # import your graph properly

def final_answer(Overallstate):
    query = Overallstate['query']
    context = Overallstate['Relevent_context']
    answer_1 = Overallstate['answer_1']
    answer_2 = Overallstate['answer_2']
    
    final_output = (
        f"**Here's the answer from the perspective of a signals and systems:**\n{answer_1}\n\n"
        f"**Here's the answer from the perspective of a control systems:**\n{answer_2}"
    )
    return final_output

def invoke_agent(query: str, context: str = "") -> str:
    result = section_builder_subagent.invoke({
        "query": query,
        "Relevent_context": context,
        "answer_1": "",
        "answer_2": ""
    })
    return final_answer(result)
