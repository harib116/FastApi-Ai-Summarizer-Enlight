from app.sources.brittanica import BrittanicaSource


class Search:
    async def __call__(self, search, *args, **kwds):
        self.search = search
        if search.source == "brittanica":
            return await self.search_brittanica(search)
        if search.source == "wikipedia":
            return "wikipedia"

    async def search_brittanica(self, search):
        print("search_brittanica:", search.search)
        results = await BrittanicaSource.collect_search_data(search.search)
        return {
            "total": len(results),
            "results": results
        }
