# django-rest-apikey

Add a per-user API key to authenticate in Django REST Framework

## Installation

Install using pip:

    pip install git+https://github.com/ybulach/django-rest-apikey.git

Add 'django_rest_apikey' to `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'django_rest_apikey',
    )

And add the authentication class:

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            ...
            'django_rest_apikey.authentication.APIKeyAuthentication',
        ),
        ...
    }

Additionally, you can add this to your router to allow users to manage there API keys:

    from django_rest_apikey.views import APIKeyViewSet
    ...
    your_router.register(r'apikeys', APIKeyViewSet, base_name='apikeys')


### Usage

The `API-Key` header is looked by the class to authenticate the user.

```python
response = requests.get(
    url="http://0.0.0.0:8000/api/your_model",
    headers={
        "Api-Key": "fd8b4a98c8f53035aeab410258430e2d86079c93",
    },
)
```
