import os

COMPANY_AUTH_KEY_MAPPING = ["Microsoft", os.getenv("MICROSOFT_ACCESS_KEY")]

SHAREPOINT_URLS = {
    "get_url": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items?expand=fields(select=Category,Progress,Email)",
    "update_url": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}/fields",
}
