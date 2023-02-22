import json
from pathlib import Path
from httpx import AsyncClient
from pprint import pprint

class BrittanicaSource:
    API_URL = "https://syndication.api.eb.com/production"
    _KEY_MAIN = "660f90a0-8bf2-4ca2-b9e9-d16bcb73aac7"
    _dump_file = Path(__file__).parent / 'brittanica.dump.json'

    @classmethod
    async def get(cls, endpoint, params={}, xml=False):
        _headers = {"x-api-key": cls._KEY_MAIN}
        async with AsyncClient() as client:
            r = await client.get(cls.API_URL+endpoint, params=params, headers=_headers, timeout=30)
            print(r.url)
            assert r.status_code == 200
        return r.json() if not xml else r.text

    # @classmethod
    # async def call_article_api(cls):
    #     _endpoint = "/articles"
    #     _params = {
    #         "articleTypeId": 1,
    #         # "categoryId": 1,
    #         # "lastUpdated": "2022-12-31",
    #         # "page":3
    #     }
    #     return await cls.get(_endpoint, _params)

    @classmethod
    async def get_full_article_list(cls):
        _endpoint = "/articles"
        _params = {
            "articleTypeId": 1,
            # "categoryId": 1,
            # "lastUpdated": "2022-12-31",
            # "page":3
        }
        total_pages = round((await cls.get(_endpoint, _params))["totalCount"]/1000) +1
        print(total_pages)
        _data = []
        _error = []
        for i in range(1, total_pages+2):
            _params.update({'page': i})
            try:
                articles = (await cls.get(_endpoint, _params)).get('articles')
                print(len(articles))
                _data.extend(articles)
            except Exception as E:
                print(articles)
                _error.append({"page": i, "error": "Failed"})
                
        print(len(_data), len(_error))
        return _data, _error

    @classmethod
    async def dump_full_article_list(cls):
        data, _error = await cls.get_full_article_list()
        _cwd = Path(__file__).parent
        print(_cwd)
        with open(_cwd / 'brittanica.dump.json', 'w') as f:
            json.dump(data, f)
        return not bool(_error), _error

    @classmethod
    async def retrieve_dump_data(cls):
        with open(cls._dump_file) as f:
            articles = json.load(f)
        return articles
    
    @classmethod
    async def _search(cls, search):
        articles = await cls.retrieve_dump_data()
        _final = [article for article in articles if str.lower(search) in str.lower(article.get('title'))]
        print("matches:", len(_final))
        return _final
    
    @classmethod
    async def get_article_detail(cls, article_id):
        _endpoint = f"/article/{article_id}/xml"
        return await cls.get(_endpoint, xml=True)
    
    @classmethod
    async def collect_search_data(cls, search: str) -> list:
        _articles = await cls._search(search)
        results = [
            {
                "article": article,
                "xml": await cls.get_article_detail(article.get("articleId"))
            } for article in _articles]
        return results



    @classmethod
    async def asmain(cls):
        data = await cls.collect_search_data("tz an")
        pprint(data)


if __name__ == "__main__":
    import asyncio
    asyncio.run(BrittanicaSource.asmain())
