import asyncio
from ddg import Duckduckgo
from crawl4ai import AsyncWebCrawler

class WebSearch:

    def __init__(self,top_n_urls=5):

        self.top_n_urls=top_n_urls

        self.ddg_api = Duckduckgo()

    def get_urls(self,searc_query):

        "Collects URLs using the duckduckgo API"
        
        results = self.ddg_api.search(searc_query)

        urls = [i['url'] for i in results['data']][0:self.top_n_urls]

        return urls
    
    async def scrap_url(self,url):
        "Scraps Individual URLs"

        async with AsyncWebCrawler(verbose=True) as crawler:

            result = await crawler.arun(url=url)

            return (url,result.markdown)
        
    async def search_online(self,search_query):

        "Main method to scrap data from websites"

        urls = self.get_urls(search_query)

        tasks = [self.scrap_url(url) for url in urls]

        results = await asyncio.gather(*tasks)

        return results

if __name__ == "__main__":

    search_Engine = WebSearch()

    content = asyncio.run(search_Engine.search_online("Who is the CEO of OpenAI"))

    print("-----------------------------------")
    print(content)
    print("-----------------------------------")
