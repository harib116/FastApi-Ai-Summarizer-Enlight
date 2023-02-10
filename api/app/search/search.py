from app.search.sources import WikiMediaAPI

class Search:
    async def __call__(self, query, sources=["wikipedia"], textract=True):
        self.query = query
        self.sources = sources
        results = []
        if "wikipedia" in sources and textract == True:
            results.append({"wiki_extract": await self.search_wiki_textract(query)})
        return {
            "query": query,
            "results": results
        }


    async def search_wiki_textract(self, query):
        wiki = WikiMediaAPI()
        titles = await wiki.wiki_opensearch(query)
        if not titles:
            return {"titles": titles, "wiki_extracts": None}
        wiki_extracts = await wiki.wiki_textracts("|".join(titles))
        return {"titles": titles, "wiki_extracts": wiki_extracts}
