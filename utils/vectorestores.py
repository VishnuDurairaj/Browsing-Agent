
import sys
sys.dont_write_bytecode =True

# ------------------------------------------------- Qdrant Vector Store -------------------------------- #

import uuid
import hashlib
from tqdm import tqdm
from qdrant_client import QdrantClient

class QdrantVectorStore:
    
    def __init__(self,db_location="qdrant",dense_model="sentence-transformers/all-MiniLM-L6-v2",sparse_model = "prithivida/Splade_PP_en_v1",hybird=True) -> None:
        
        self.client = QdrantClient(path=f"vector_stores/{db_location}")
        
        self.client.set_model(dense_model)

        # comment this line to use dense vectors only
        if hybird:
            self.client.set_sparse_model(sparse_model)

            self.client.recreate_collection(
                collection_name="default_schema",
                vectors_config=self.client.get_fastembed_vector_params(),
                # comment this line to use dense vectors only
                sparse_vectors_config=self.client.get_fastembed_sparse_vector_params(),  
            )
        else:

            self.client.recreate_collection(
                collection_name="default_schema",
                vectors_config=self.client.get_fastembed_vector_params()
            )

    def add_documents(self,documents,ids=[],metadata=[],collection_name="default_schema"):

        if not len(ids):

            ids = [self.generate_uuid_based_id(doc) for doc in documents]

        self.client.add(
        collection_name=collection_name,
        documents=documents,
        metadata = metadata,
        ids=tqdm(ids))

    def get_relavant_documents(self, text: str,collection_name:str="default_schema",top_n_similar_docs=6):
        search_result = self.client.query(
            collection_name=collection_name,
            query_text=text,
            limit=top_n_similar_docs, 
        )
        metadata = [{"id":hit.id,"document":hit.metadata['document'],"url":hit.metadata['url']} for hit in search_result]

        return metadata
    
    def generate_uuid_based_id(self, text):
        """
        Generate a full UUID based on the given text using UUID5.

        :param text: Input text to generate the unique ID from.
        :return: A UUID string.
        """
        # Generate a UUID based on a namespace and the text
        namespace = uuid.NAMESPACE_DNS  # You can use different namespaces (DNS, URL, etc.)
        
        # Create a UUID5 based on the text and namespace
        unique_uuid = uuid.uuid5(namespace, text)
        
        return str(unique_uuid)

    def delete_existing_data(self):

        return self.client.delete_collection("default_schema")