from abc import ABC, abstractmethod

from balpy_v2.lib import Chain
from balpy_v2.lib.gql import gql


class GraphQLClient(ABC):
    def __init__(self, chain) -> None:
        self.url = self.get_url(chain)

    async def instance_query(self, query, variables=dict()):
        return await gql(self.url, query, variables=variables)

    @abstractmethod
    def get_url(self, chain):
        pass

    @classmethod
    async def query(cls, chain=Chain.mainnet, query=None, variables=dict()):
        if not query:
            raise ValueError("query must be provided")

        client = cls(chain)
        return await client.instance_query(query, variables)
