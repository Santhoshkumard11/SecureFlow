from GetPerson.sharepoint_client import SharePointClient, GraphClient


class Executor:
    def __init__(self) -> None:
        self.issue_list = None
        self.graph_client_obj = GraphClient()
        self.graph_client_obj.get_graph_access_token()
        self.sharepoint_client_obj = SharePointClient(self.graph_client_obj)

    def get_person_with_least_work(self):
        pass

    def execute(self):
        self.issue_list = self.sharepoint_client_obj.get_all_lists()
