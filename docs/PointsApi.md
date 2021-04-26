# neurostore_api.PointsApi

All URIs are relative to *http://localhost:80/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**points_id_get**](PointsApi.md#points_id_get) | **GET** /points/{id} | GET a point
[**points_id_put**](PointsApi.md#points_id_put) | **PUT** /points/{id} | PUT/update a point


# **points_id_get**
> object points_id_get(id)

GET a point

Information about a particular MRI coordinate

### Example

```python
import time
import neurostore_api
from neurostore_api.api import points_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = points_api.PointsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # GET a point
        api_response = api_instance.points_id_get(id)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling PointsApi->points_id_get: %s\n" % e)
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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **points_id_put**
> points_id_put(id)

PUT/update a point

Update a particular MRI coordinate.

### Example

```python
import time
import neurostore_api
from neurostore_api.api import points_api
from neurostore_api.model.point import Point
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
    api_instance = points_api.PointsApi(api_client)
    id = "id_example" # str | 
    point = Point(
        coordinates=[
            63,
        ],
        space="UNKNOWN",
        kind="kind_example",
        image="image_example",
        label_id="label_id_example",
        x=3.14,
        y=3.14,
        z=3.14,
        value=[
            3.14,
        ],
        analysis="6kwPw6p79Ljm",
    ) # Point |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # PUT/update a point
        api_instance.points_id_put(id)
    except neurostore_api.ApiException as e:
        print("Exception when calling PointsApi->points_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PUT/update a point
        api_instance.points_id_put(id, point=point)
    except neurostore_api.ApiException as e:
        print("Exception when calling PointsApi->points_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **point** | [**Point**](Point.md)|  | [optional]

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

