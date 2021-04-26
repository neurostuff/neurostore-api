# neurostore_api.DatasetsApi

All URIs are relative to *http://localhost:80/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasets_get**](DatasetsApi.md#datasets_get) | **GET** /datasets/ | GET a list of datasets
[**datasets_id_get**](DatasetsApi.md#datasets_id_get) | **GET** /datasets/{id} | GET a dataset
[**datasets_id_put**](DatasetsApi.md#datasets_id_put) | **PUT** /datasets/{id} | PUT/update a dataset
[**datasets_post**](DatasetsApi.md#datasets_post) | **POST** /datasets/ | POST/create a dataset


# **datasets_get**
> [object] datasets_get()

GET a list of datasets

Get a list of datasets.

### Example

```python
import time
import neurostore_api
from neurostore_api.api import datasets_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datasets_api.DatasetsApi(api_client)
    search = "imagin" # str | search for entries that contain the substring (optional)
    sort = "created_at" # str | Parameter to sort results on (optional) if omitted the server will use the default value of "created_at"
    page = 0 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 1 # int | number of results to show on a page (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET a list of datasets
        api_response = api_instance.datasets_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling DatasetsApi->datasets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional]
 **sort** | **str**| Parameter to sort results on | [optional] if omitted the server will use the default value of "created_at"
 **page** | **int**| page of results | [optional]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional]
 **page_size** | **int**| number of results to show on a page | [optional]

### Return type

**[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_id_get**
> object datasets_id_get(id)

GET a dataset

Retrieve the information of a dataset with the matching dataset ID.

### Example

```python
import time
import neurostore_api
from neurostore_api.api import datasets_api
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
    api_instance = datasets_api.DatasetsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # GET a dataset
        api_response = api_instance.datasets_id_get(id)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling DatasetsApi->datasets_id_get: %s\n" % e)
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
**200** | Dataset found |  -  |
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **datasets_id_put**
> datasets_id_put(id)

PUT/update a dataset

Update a dataset.

### Example

```python
import time
import neurostore_api
from neurostore_api.api import datasets_api
from neurostore_api.model.dataset import Dataset
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
    api_instance = datasets_api.DatasetsApi(api_client)
    id = "id_example" # str | 
    dataset = Dataset(
        name="name_example",
        description="description_example",
        publication="publication_example",
        doi="doi_example",
        pmid="pmid_example",
        nimads_data=DatasetNimadsData(
            dataset=[
                Study(
                    analysis=,
                    doi="10.1016/S0926-6410(97)00020-7",
                    name="Functional magnetic resonance imaging of category-specific cortical activation: evidence for semantic maps.",
                    metadata={},
                    description="description_example",
                    publication="publication_example",
                    pmid="pmid_example",
                ),
            ],
        ),
        user="user_example",
    ) # Dataset |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # PUT/update a dataset
        api_instance.datasets_id_put(id)
    except neurostore_api.ApiException as e:
        print("Exception when calling DatasetsApi->datasets_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PUT/update a dataset
        api_instance.datasets_id_put(id, dataset=dataset)
    except neurostore_api.ApiException as e:
        print("Exception when calling DatasetsApi->datasets_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **dataset** | [**Dataset**](Dataset.md)|  | [optional]

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

# **datasets_post**
> Dataset datasets_post()

POST/create a dataset

Create a dataset.

### Example

```python
import time
import neurostore_api
from neurostore_api.api import datasets_api
from neurostore_api.model.dataset import Dataset
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = datasets_api.DatasetsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # POST/create a dataset
        api_response = api_instance.datasets_post()
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling DatasetsApi->datasets_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

