from langchain_core.prompts import PromptTemplate

template=PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

1. Explanation Style: {style_input}
2. Explanation Length: {length_input}

3. Mathematical Details:
   - Include the relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

4. Analogies:
   - Use relatable analogies to simplify complex ideas.

5. If certain information is not available in the paper, respond with
   "Insufficient information available" instead of guessing.
""",
input_variables=['paper_input','style_input','length_input']
)

template.save('template.json')
