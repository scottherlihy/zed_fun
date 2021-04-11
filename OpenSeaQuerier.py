import requests


class OpenSeaQuerier(object):
    def __init__(self):
        pass

    def GetAllCollections(self, limit=300):
        url = "https://api.opensea.io/api/v1/collections"
        querystring = {"offset": "0", "limit": str(limit)}
        response = requests.request("GET", url, params=querystring)
        return response.text

    def GetAssets(self):
        url = "https://api.opensea.io/api/v1/assets"
        querystring = {"order_direction": "desc", "offset": "0",
                       "limit": "1", "collections": "ZED RUN Racehorse"}
        response = requests.request("GET", url, params=querystring)
        return response.text


def main():
    querier = OpenSeaQuerier()
    # print querier.GetAllCollections()
    print querier.GetAssets()


if __name__ == "__main__":
    main()
