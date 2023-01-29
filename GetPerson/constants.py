import os

COMPANY_AUTH_KEY_MAPPING = ["Microsoft", os.getenv("MICROSOFT_ACCESS_KEY")]

SHAREPOINT_URLS = {
    "get_url": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items",
    "update_url": "https://graph.microsoft.com/v1.0/sites/{site_id}/lists/{list_id}/items/{item_id}/fields",
}
    """
    $env:BLOB_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=azureisonskincancer981e;AccountKey=1SsOfZwg9vE1454Er5NjtMK+1EBXgEw+adyNK/n84hnlNuJZGgZ05Yx1F4amZlQDBY0J5XjUgU9U+AStk0VgXQ==;EndpointSuffix=core.windows.net"
$env:BLOB_STORAGE_CONTAINER_NAME = "azureison-skin-cancer-center-sample-image-storage"
$Env:MSFT_CLIENT_ID = "4f70e31c-fa0c-4a2b-8d35-f4c5e13d106b"
$Env:MSFT_CLIENT_SECRET = "Jn18Q~yOv4eUwS-yiG_QEp-LdDzu_EJzcBMN4bSr"
$Env:TENANT_ID = "f547f2eb-18b1-47c7-9f2d-587162a7e029"
$Env:SITE_ID = "z3dr3.sharepoint.com,2ea0a942-b08e-4435-8e96-2f4ae8816c85,916b3a5b-a7a8-4805-95a5-c30f2892b7d6"
$Env:LIST_ID = "6109a252-7fb3-44fc-b265-3d20b991aee9"

    """