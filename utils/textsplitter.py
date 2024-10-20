from semantic_text_splitter import TextSplitter

class CustomTextSplitter:

    def __init__(self,max_chunk_length=300,model_name="gpt-4o"):

        self.splitter = TextSplitter.from_tiktoken_model(model_name, max_chunk_length)

    def get_chunks(self,documents):

        all_chunks = []

        metedata = []

        for doc in documents:

            chunks = self.splitter.chunks(doc[1])

            metedata.extend([{"url":doc[0]}]*len(chunks))

            all_chunks.extend(chunks)

        return all_chunks,metedata
    
# textsplitter =CustomTextSplitter()

# chunks = textsplitter.get_chunks(paragraphs)