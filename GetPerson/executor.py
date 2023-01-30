from GetPerson.sharepoint_client import SharePointClient, GraphClient
import logging
from collections import Counter


class Executor:
    def __init__(self) -> None:
        self.issue_list = None
        self.graph_client_obj = GraphClient()
        self.graph_client_obj.get_graph_access_token()
        self.sharepoint_client_obj = SharePointClient(self.graph_client_obj)

    def get_person_with_bandwidth(self):
        """Process the list and get the person with bandwidth

        Return:
            str: email of the person
        """

        emails_list = []

        # iterate through the result list
        for list_item in self.issue_list.get("value"):
            # get each list field values
            fields_dict = list_item.get("fields")

            emails_list.append(fields_dict.get("Email"))

        # get the lest work name
        return Counter(emails_list).most_common()[-1][0]

    def execute(self):
        logging.info("Starting executor")
        self.issue_list = self.sharepoint_client_obj.get_all_lists()

        person_email = self.get_person_with_bandwidth()

        logging.info(f"Email of the person with bandwidth - {person_email}")

        logging.info("Ended executor")
        return person_email
