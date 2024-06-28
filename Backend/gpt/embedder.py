from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
# from gpt.gpt_wrapper import GptWrapper
from settings import PERSIST_DIRECTORY,DOCUMENT_COUNT,CHUNK_SIZE,CHUNK_OVERLAP

class Embedder:
    @staticmethod
    def storeDocEmbeds(directory):
        persist_directory = PERSIST_DIRECTORY
        chunk_size = CHUNK_SIZE
        chunk_overlap = CHUNK_OVERLAP
        text_splitter = RecursiveCharacterTextSplitter(
            separators= "\n",   # type: ignore
            chunk_size = chunk_size,
            chunk_overlap  = chunk_overlap,
            length_function = len,
        )
        loader = DirectoryLoader(directory, loader_cls=PyPDFLoader, show_progress=True, use_multithreading=True)
        try: 
            docs=loader.load_and_split(text_splitter)
            for doc in docs:
                doc_name = doc.metadata['source']
                path_parts=doc_name.split('\\')
                file_name_with_extension = path_parts[-1]
                file_name = file_name_with_extension.split('.')[0]
                doc.metadata={
                    "file_name":file_name
                }
            # docs=loader.load()
        except Exception as error:
            print(error)

        try:
            embedding = OpenAIEmbeddings(model="text-embedding-3-small")
            vectordb = Chroma.from_documents(documents=docs, embedding=embedding, persist_directory=persist_directory)
        except Exception as oai_exception:
            print("OpenAI Exception:", oai_exception)

        vectordb.persist()


    @staticmethod
    def getSearchResults(query:str,doc_list:list[str]):
        """
        Retrieves relavant documents
        """
        k = DOCUMENT_COUNT
        persist_directory = PERSIST_DIRECTORY
        embedding = OpenAIEmbeddings(model="text-embedding-3-small")
        db = Chroma(persist_directory=persist_directory, embedding_function=embedding)

        final_docs=[]
        for doc in doc_list:
            filter={
                "file_name": {
                    "$eq": doc
                }
            }
            for d in db.similarity_search_with_score(query, k=k,filter=filter):
                final_docs.append(d[0])
        print(final_docs)
        values = ','.join(str(v.page_content) for v in final_docs)
        return values
        # docs = db.similarity_search(query,include=['documents'], k=k)
        # final_docs = [d[1] for d in db.similarity_search_with_score(query, k=k) if d[1] < 0.34]
        # return final_docs
