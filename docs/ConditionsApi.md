# neurostore_api.ConditionsApi

All URIs are relative to *http://localhost:80/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conditions_id_get**](ConditionsApi.md#conditions_id_get) | **GET** /conditions/{id} | GET a condition
[**conditions_id_put**](ConditionsApi.md#conditions_id_put) | **PUT** /conditions/{id} | PUT/update a condition


# **conditions_id_get**
> object conditions_id_get(id)

GET a condition

Retrieve a condition (e.g., 2-back) that can be used in contrasts (e.g., 2-back - 1-back)

### Example

```python
import time
import neurostore_api
from neurostore_api.api import conditions_api
from neurostore_api.model.inline_response404 import InlineResponse404
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conditions_api.ConditionsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # GET a condition
        api_response = api_instance.conditions_id_get(id)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling ConditionsApi->conditions_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **conditions_id_put**
> conditions_id_put(id)

PUT/update a condition

update a condition

### Example

```python
import time
import neurostore_api
from neurostore_api.api import conditions_api
from neurostore_api.model.condition import Condition
from neurostore_api.model.inline_response422 import InlineResponse422
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = conditions_api.ConditionsApi(api_client)
    id = "id_example" # str | 
    condition = Condition(
        name="name_example",
        description="description_example",
    ) # Condition |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # PUT/update a condition
        api_instance.conditions_id_put(id)
    except neurostore_api.ApiException as e:
        print("Exception when calling ConditionsApi->conditions_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PUT/update a condition
        api_instance.conditions_id_put(id, condition=condition)
    except neurostore_api.ApiException as e:
        print("Exception when calling ConditionsApi->conditions_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **condition** | [**Condition**](Condition.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

