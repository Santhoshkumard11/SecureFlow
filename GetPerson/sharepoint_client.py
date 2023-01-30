import os
from GetPerson.constants import SHAREPOINT_URLS
from GetPerson.microsoft_graph_api import GraphClient


class SharePointClient:
    """Use to interact with the SharePoint APIs"""

    def __init__(self, msft_graph_client: GraphClient) -> None:
        """Initialize the Microsoft Graph client

        Args:
            msft_graph_client (GraphClient): Microsoft Graph Client
        """

        # ID of the SharePoint page
        self.site_id = os.getenv("SITE_ID")
        self.list_id = os.getenv("LIST_ID")
        self.msft_graph_client = msft_graph_client

    def get_all_lists(self) -> None:
        """Get all the SharePoint Tracker List"""

        url = SHAREPOINT_URLS.get("get_url").format(
            **{"site_id": self.site_id, "list_id": self.list_id}
        )

        return self.msft_graph_client.send_msft_graph_request(url)
