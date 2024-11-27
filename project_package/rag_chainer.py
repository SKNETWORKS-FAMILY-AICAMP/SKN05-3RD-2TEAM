from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from resource.config import api_key, llm_base, llm_finetune

class EmergencyRAGChainer:
  def __init__(self, db_path):
    self.db_path = db_path
    self.embedding_model = OpenAIEmbeddings(api_key=api_key)
    template = '''Answer the question in korean, based only on the following context: 

    context :
    {context}

    Question: {question}
    '''
    self.prompt = ChatPromptTemplate.from_template(template)
    self.model = ChatOpenAI(
        model=llm_base,
        temperature=0,
        max_tokens=500,
        api_key=api_key
    )

  def load_vectorstore(self):
    return Chroma(
        persist_directory=self.db_path,
        embedding_function=self.embedding_model,
        collection_metadata={'hnsw:space' : 'cosine'}
    )

  def create_retriever(self, vector_store):
    return vector_store.as_retriever(
      search_type="mmr",
      search_kwargs={
          "k": 20,
          "alpha": 0.5,
      }
    )

  def format_docs(self, docs):
      return '\n\n'.join([d.page_content for d in docs])

  def create_rag_chain(self):
    vector_store = self.load_vectorstore()
    retriever = self.create_retriever(vector_store)

    return {'context': retriever | self.format_docs, 'question':RunnablePassthrough()} | self.prompt | self.model | StrOutputParser()