import streamlit as st
from langchain_google_genai.llms import GoogleGenerativeAI
import pycountry

country_names = [country.name for country in pycountry.countries]

st.set_page_config(
   page_title="Compass : AI Career Counselor",
   page_icon="🧭",
   layout="centered",
   initial_sidebar_state="expanded",
)
st.title(' 🧭 Compass : AI Career Counselor')
st.sidebar.title("Compass : AI Career Counselor")
openai_api_key = st.sidebar.text_input('Input Your Google Studio Gemini API Key. If you do not have you can create for free\
                                       from here https://aistudio.google.com/app/apikey')
st.sidebar.divider()  # 👈 Draws a horizontal rule

st.sidebar.markdown("👋 Hi, Thank you for checking my app. My name is James. Connect with me if you are looking for Generative AI developer.\
                 My Tech stack is : Langchain for LLM Framework, Google Vertex/Gemini LLM, StreamLit for frontend. https://www.linkedin.com/in/mascarenhasjames")

def generate_response(input_text):
  llm = GoogleGenerativeAI(model="gemini-1.0-pro-latest", google_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('Form1'):
  getText=text = st.text_area('`1` Tell us what you want to become')
  getEconmics=st.selectbox('`2` To better assist let us know if You are economically', ['Poor Class', 'Middle Class','Rich Class'], key=1)
  getClass=slider1=st.slider(label='`3` Which class you are studying in.', min_value=0, max_value=30, key=2)
  getNationality=st.selectbox('`4` Select your nationality(So that you get your region specific learning path)', country_names, key=3)
  getLanguage=st.selectbox('`4` Select your language(So that you get your language specific learning path)', ['english', 'Hindi','spanish','chinese','french  '], key=4)
  getAge=st.slider(label='`5` Select your age(So that you get your age specific learning path)', min_value=0, max_value=100, key=5)
  getsubmittedForm = st.form_submit_button('Submit 1')
  
  createPrompt=f"You are expert in career counseling. Give a structured career map in {getLanguage} language. For every step give online link or resources originating from {getNationality} which can help the student. \
    I am economically {getEconmics} person from {getNationality}. I am {getAge} old and currently studing in class {getClass}. I want to become a {getText} in {getNationality}"
  
  if not openai_api_key:
      st.warning('To get answer please enter your Gemini API Key in the sidebar OR create for free  https://aistudio.google.com/app/apikey', icon='⚠')
  if getsubmittedForm and openai_api_key:
    print(createPrompt)
    generate_response(createPrompt)