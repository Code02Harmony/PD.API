from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'pdoctretinalstorage' # Must be replaced by your <storage_account_name>
    account_key = 'xJ6EuNBsBxjG7H3YrpMMpeG9C+zTMErcVPdARmgmxafD+5FztAYFh5WI4HpLwmXZy8RI418vM0xM+ASt9ytFGA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'pdoctretinalstorage' # Must be replaced by your storage_account_name
    account_key = 'xJ6EuNBsBxjG7H3YrpMMpeG9C+zTMErcVPdARmgmxafD+5FztAYFh5WI4HpLwmXZy8RI418vM0xM+ASt9ytFGA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
