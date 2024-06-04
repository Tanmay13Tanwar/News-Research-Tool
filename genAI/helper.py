from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain import hub
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_groq import ChatGroq
import os
import warnings
warnings.filterwarnings("ignore")

os.environ['GROQ_API_KEY'] = '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'
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def process(url,question):
    loader = WebBaseLoader(url)
    data = loader.load()

    # Split
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
    all_splits = text_splitter.split_documents(data)

    # Store splits
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=embeddings, collection_name = 'url_embeddings' ,persist_directory='db')

    # RAG prompt
    prompt = hub.pull("rlm/rag-prompt-llama")

    # LLM
    llm = ChatGroq(name = "llama3-70b-8192")

    # RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    #question = "What are the approaches to Task Decomposition?"
    result = qa_chain({"query": question})
    return result["result"]