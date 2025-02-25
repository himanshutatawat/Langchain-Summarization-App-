import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_groq import ChatGroq



### Streamlit App
st.set_page_config(page_title="Langchain: Summarize Text from YT or website", page_icon="🔗", layout="wide")
st.title("Summarize Text from Youtube or Website")
st.subheader("Enter a Youtube URL or a website URL to summarize the text content")



with st.sidebar:
    groq_api_key = st.text_input("Groq API Key",value="", type="password")

### Gemma Model using GROQ API
llm = ChatGroq(groq_api_key=groq_api_key,model="gemma2-9b-it")

prompt_template ="""
Provide a summary of the following content in 300 words or less:
Content:{text}
"""

prompt = PromptTemplate(template = prompt_template, input_variable=["text"])

url = st.text_input("URL",label_visibility="collapsed")
if st.button("Summarize"):
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the information")
    elif not validators.url(url):
        st.error("Invalid URL!!!")
        
    else:
        try:
            with st.spinner("Wait Its Loading..."):
                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url, add_video_info =True)
                else:
                    loader = UnstructuredURLLoader(urls =[url], ssl_verify = False,
                                                    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Version/116.0.0.0 Safari/537.36"})
                docs = loader.load()
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                
                output_summary = chain.run(docs)
                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")
            st.error("Something went wrong!!!")

