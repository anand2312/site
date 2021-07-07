"""Functions and classes for interacting with the Github GraphQL API."""
import asyncio
import dataclasses
import re
from typing import List, Optional

import aiohttp
from loguru import logger


@dataclasses.dataclass(frozen=True)
class RepositoryLanguage:
    """
    Represents the most used language in a repository.
    """

    color: str
    name: str


@dataclasses.dataclass(frozen=True)
class PinnedRepository:
    """
    Represents the pinned repository data returned by the GraphQL API.
    """

    # attributes here are named with camelCase to remain consistent with the API
    name: str  # bare repo name
    nameWithOwner: str  # owner/repo format
    description: str
    openGraphImageUrl: str
    url: str
    language: RepositoryLanguage
    stargazerCount: int

    @property
    def custom_url(self) -> str:
        """
        Return an anand2312.tech/r/ URL if the repo is on my own account.
        """
        match = re.fullmatch(r"anand2312/.*", self.nameWithOwner)
        if match:
            return f"https://anand2312.tech/r/{self.name}"
        else:
            return self.url


class GHApiClient:
    """
    Client that will make requests to the GH GraphQL API periodically and cache the results.
    The view functions must then pull results from this cache.
    """

    API_URL = "https://api.github.com/graphql"

    def __init__(
        self, token: str, session: Optional[aiohttp.ClientSession] = None
    ) -> None:
        self._session = session
        self._token = token
        self.__exc_count = 0
        self._cached_response: List[PinnedRepository]

    @property
    def query(self) -> dict:
        return {
            "query": "query { viewer { itemShowcase { items(first:6) { nodes { __typename ... on Repository { name description nameWithOwner openGraphImageUrl url stargazerCount primaryLanguage { color name }}}}}}}"
        }

    def get_projects(self) -> List[PinnedRepository]:
        """Method to pull the cached list of pinned repositories."""
        return self._cached_response

    async def make_request(self) -> None:
        """
        Make the request to the API and return the results.
        """

        if not self._session:
            self._session = aiohttp.ClientSession(
                headers={"Authorization": f"Bearer {self._token}"}
            )

        async with self._session.post(GHApiClient.API_URL, json=self.query) as resp:
            raw_data = await resp.json()
            logger.info("Retrieved pinned repo data from github.")
            repos = raw_data["data"]["viewer"]["itemShowcase"]["items"]["nodes"]
            [
                repo.pop("__typename") for repo in repos
            ]  # remove the redundant typename field

        self._cached_response = []
        for repo in repos:
            raw_lang = repo.pop("primaryLanguage")
            lang = RepositoryLanguage(**raw_lang)
            obj = PinnedRepository(**repo, language=lang)
            self._cached_response.append(obj)

        logger.info("Parsed pinned repo data.")

    async def loop(self, duration: int = 1800) -> None:
        """
        Loop the make_request method periodically.
        """
        while True:
            try:
                await self.make_request()
            except Exception as e:
                logger.error(f"GH API: Error occured in loop | {e}")

                if self.__exc_count > 5:
                    logger.warning(
                        f"GH API data collection task loop broke as "
                        f"consequent error count exceeded 5."
                    )
                    break

                self.__exc_count += 1
            else:
                self.__exc_count = 0
                await asyncio.sleep(duration)

    def start(self, duration: int = 1800) -> asyncio.Task:
        """Start the underlying task loop."""
        return asyncio.get_running_loop().create_task(self.loop(duration=duration))
