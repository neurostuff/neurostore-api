# neurostore_api.StudiesApi

All URIs are relative to *http://localhost:80/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studies_get**](StudiesApi.md#studies_get) | **GET** /studies/ | GET a list of studies
[**studies_id_get**](StudiesApi.md#studies_id_get) | **GET** /studies/{id} | GET a study
[**studies_id_put**](StudiesApi.md#studies_id_put) | **PUT** /studies/{id} | PUT/update a study
[**studies_post**](StudiesApi.md#studies_post) | **POST** /studies/ | POST/create a study


# **studies_get**
> [object] studies_get()

GET a list of studies

List studies

### Example

```python
import time
import neurostore_api
from neurostore_api.api import studies_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = studies_api.StudiesApi(api_client)
    search = "imagin" # str | search for entries that contain the substring (optional)
    sort = "created_at" # str | Parameter to sort results on (optional) if omitted the server will use the default value of "created_at"
    page = 0 # int | page of results (optional)
    desc = True # bool | sort results by descending order (as opposed to ascending order) (optional)
    page_size = 1 # int | number of results to show on a page (optional)
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET a list of studies
        api_response = api_instance.studies_get(search=search, sort=sort, page=page, desc=desc, page_size=page_size, nested=nested)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling StudiesApi->studies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| search for entries that contain the substring | [optional]
 **sort** | **str**| Parameter to sort results on | [optional] if omitted the server will use the default value of "created_at"
 **page** | **int**| page of results | [optional]
 **desc** | **bool**| sort results by descending order (as opposed to ascending order) | [optional]
 **page_size** | **int**| number of results to show on a page | [optional]
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional]

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

# **studies_id_get**
> object studies_id_get(id)

GET a study

Get a study.

### Example

```python
import time
import neurostore_api
from neurostore_api.api import studies_api
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
    api_instance = studies_api.StudiesApi(api_client)
    id = "id_example" # str | 
    nested = True # bool | whether to show the URI to a resource (false) or to embed the object in the response (true) (optional)

    # example passing only required values which don't have defaults set
    try:
        # GET a study
        api_response = api_instance.studies_id_get(id)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling StudiesApi->studies_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET a study
        api_response = api_instance.studies_id_get(id, nested=nested)
        pprint(api_response)
    except neurostore_api.ApiException as e:
        print("Exception when calling StudiesApi->studies_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **nested** | **bool**| whether to show the URI to a resource (false) or to embed the object in the response (true) | [optional]

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
**200** | Study Found |  -  |
**404** | Example response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **studies_id_put**
> studies_id_put(id)

PUT/update a study

Update a study.

### Example

```python
import time
import neurostore_api
from neurostore_api.api import studies_api
from neurostore_api.model.inline_response422 import InlineResponse422
from neurostore_api.model.study import Study
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = studies_api.StudiesApi(api_client)
    id = "id_example" # str | 
    study = Study(
        analysis=,
        doi="10.1016/S0926-6410(97)00020-7",
        name="Functional magnetic resonance imaging of category-specific cortical activation: evidence for semantic maps.",
        metadata={},
        description="description_example",
        publication="publication_example",
        pmid="pmid_example",
    ) # Study |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # PUT/update a study
        api_instance.studies_id_put(id)
    except neurostore_api.ApiException as e:
        print("Exception when calling StudiesApi->studies_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # PUT/update a study
        api_instance.studies_id_put(id, study=study)
    except neurostore_api.ApiException as e:
        print("Exception when calling StudiesApi->studies_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **study** | [**Study**](Study.md)|  | [optional]

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

# **studies_post**
> studies_post()

POST/create a study

Create a study

### Example

```python
import time
import neurostore_api
from neurostore_api.api import studies_api
from neurostore_api.model.study import Study
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:80/api
# See configuration.py for a list of all supported configuration parameters.
configuration = neurostore_api.Configuration(
    host = "http://localhost:80/api"
)


# Enter a context with an instance of the API client
with neurostore_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = studies_api.StudiesApi(api_client)
    study = [
        Study(
            analysis=,
            doi="10.1016/S0926-6410(97)00020-7",
            name="Functional magnetic resonance imaging of category-specific cortical activation: evidence for semantic maps.",
            metadata={},
            description="description_example",
            publication="publication_example",
            pmid="pmid_example",
        ),
    ] # [Study] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # POST/create a study
        api_instance.studies_post(study=study)
    except neurostore_api.ApiException as e:
        print("Exception when calling StudiesApi->studies_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study** | [**[Study]**](Study.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

