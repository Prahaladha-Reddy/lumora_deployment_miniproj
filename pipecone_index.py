import os
from dotenv import load_dotenv
load_dotenv()
os.environ['PINECONE_API_KEY']=os.getenv("PINECONE_API_KEY")
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings


os.environ["GOOGLE_API_KEY"] =os.getenv("GOOGLE_API_KEY")
pinecone_api_key=os.getenv("PINECONE_API_KEY")

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

pc = Pinecone(api_key=pinecone_api_key)
index_name = "langchain-test-index"  
index = pc.Index(index_name) 


text_field = "text"  
vectorstoretest = PineconeVectorStore(  
    index, embeddings
)


"""
query = "What is relational db"  
relevent_data=vectorstoretest.similarity_search(  
    query,  
    k=3  
)
cont=[i.page_content for i in relevent_data]
print(cont)"""

