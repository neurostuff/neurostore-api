import time
import neurostore_api
from neurostore_api.api import analyses_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3000
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = analyses_api.AnalysesApi(api_client)
    search = "imagin" # str | search for entries that contain the substring (optional)
    sort = "created_at" # str | Parameter to sort results on (optional) if omitted the server will use the default value of "created_at"
    page = 0 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 1 # int | number of results to show on a page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Your GET endpoint
        api_response = api_instance.analyses_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling AnalysesApi->analyses_get: %s\n" % e)