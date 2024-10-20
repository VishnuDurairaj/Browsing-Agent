import asyncio
from utils.webscraper import WebSearch
from utils.textsplitter import CustomTextSplitter
from utils.vectorestores import QdrantVectorStore

class SearchTool:

    def __init__(self,top_n_urls=5,top_n_chunks=5):

        self.top_n_urls=top_n_urls

        self.top_n_chunks=top_n_chunks
        
        self.search_Engine = WebSearch(top_n_urls=self.top_n_urls)

        self.textsplitter =CustomTextSplitter()

        self.vectore_store = QdrantVectorStore()

    async def get_online_details(self,user_question):

        # We need to scrap data
        print("Collecting URLs....")
        scrapped_data = await self.search_Engine.search_online(user_question)

        # Split the web pages into smaller chunks

        print("Scrapping Data....")
        documents, metadata = self.textsplitter.get_chunks(scrapped_data)

        # Add chunks and metadata to the vector store

        print("Adding Data to Vectore Store....")
        self.vectore_store.add_documents(documents=documents,ids=[],metadata=metadata)

        # get the relevant documents
        print("Getting Data From Vectore Store....")
        relevant_documents = self.vectore_store.get_relavant_documents(user_question,top_n_similar_docs=self.top_n_chunks)

        # Format the documents

        final_data = ""

        for data in relevant_documents:

            final_data+=f"\n\nSource URL : {data['url']}\nData : {data['document']}\n\n"

        return final_data
    

if __name__ == "__main__":

    tool = SearchTool()

    print("Started......")

    data = asyncio.run(tool.get_online_details("Who is the CEO of Factspan"))

    print("Data: ",data)