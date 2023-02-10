import httpx


class BaseSource():
    """Base class
    """
    def __init__(self, name, api_url) -> None:
        self.name = name
        self.api_url = api_url
    
    def __str__(self) -> str:
        return f"{self.name} ({self.api_url})"
    
    async def collect_response_data(self, url, params=None):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            print(response.url)
            data = response.json()
        return response, data


class WikiMediaAPI(BaseSource):
    def __init__(self, name="wikipedia", api_url="https://en.wikipedia.org/w/api.php") -> None:
        super().__init__(name, api_url)

    async def wiki_opensearch(self, search):
        """
        Ref: https://www.mediawiki.org/wiki/API:Opensearch
        Searches for title

        Args:
            search (str): search
        """
        print("@opensearch")
        params = {
            "action": "opensearch",
            "format": "json",
            "requestid": "request_id",
            "servedby": 1,
            "curtimestamp": 1,
            # 
            "search": search,
            "limit": 5,
            "warningsaserror": True,
            "formatversion": 2
            
        }
        status, data = await self.collect_response_data(self.api_url, params=params)
        return data[1]

    async def wiki_textracts(self, titles: str):
        """
        Inbuild Wiki Extract
        Ref: https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page

        Args:
            titles (str): Page titles of wiki page
        """
        print("@extract")
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": titles,
            "formatversion": "2",
            # "exsentences": "10",
            "exintro": 1,
            "explaintext": 1
        }
        status, data = await self.collect_response_data(self.api_url, params=params)
        return data["query"]["pages"]

