from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI()

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#template = load_prompt('template.json')
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

#Fill in the placeholders 
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})



if st.button('Summarize'):
    result=model.invoke([prompt])
    st.write(result.content)