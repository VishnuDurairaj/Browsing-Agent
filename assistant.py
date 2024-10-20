import asyncio
from swarm import  Agent
from dotenv import load_dotenv
from swarm.repl import run_demo_loop
from utils.search_tool import SearchTool
 
load_dotenv() 

# Create tools ---------------------- 

# initialise Search tool
search_tool = SearchTool()

def search_internal_database(user_query):
    """
    Use this tool to search in internal database

    Args:
    user_query (str) : The user question to search in database

    Returns:

    str : It returns available text data from internal database.
    """
    print("************* Using Internal Search *************")

    return search_tool.vectore_store.get_relavant_documents(user_query)

def search_online(user_query):
    """
    Use this tool to search in online

    Args:
    user_query (str) : The user question to search in online

    Returns:

    str : It returns text data from various websites.
    """
    print("************* Using Online Search *************")
    return asyncio.run(search_tool.get_online_details(user_query))

instructions = """You are a helpful assistant tasked with answering user queries by first checking the internal database. 
If the information is not available there, only then should you search online.
Additionally, when providing answers from online sources, you must include the URL or source details. 
This order must be strictly followed.
"""

Search_Agent = Agent(
    name="Web Search Agent",
    instructions=instructions,
    functions=[search_internal_database,search_online],
    model = "gpt-4o-mini",
)

if __name__=="__main__":

    run_demo_loop(Search_Agent)

    # clinet.run()



