# django_tsp
django_tsp is a wrapper build on top of the tsp_wrapper

* Provide apis for calling the tsp_wrapper
* Provide django commands for tsp_wrapper
* Provide websocket template for tsp sloutions

## Installation
```bash
pip install django-tsp
```

## Getting started
* Add django_tsp to your install apps
```python
INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_tsp', # <--- here we added our package
]
```
* fill up the require variables in settings.py
```python
TSP_HOOK_URL="http://django:8000/api/tsp/hook/" # your webhook link
TSP_BROKER_URL = "amqp://guest:guest@rabbitmq:5672/"
```
* install django_channels and use following view in your routing
```python
from django_tsp.routing import ws_urlpatterns


application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(URLRouter(ws_urlpatterns))
})
```
* use add following apis to your urls.py (needs drf and drf_docs)
```python
from django_tsp.apis import WebhookApi, SolverApi 

urlpatterns = [
    path('tsp/', include(([
        path('solver/', SolverApi.as_view(), name="solver"),
        path('hook/', WebhookApi.as_view(), name="hook"),
    ], "tsp")), ),
]

```
* for the template websocket add following views inside of your urls.py
```python
from django_tsp.views import index
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('', index, name="index"), # the improtant template one
    path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
    path("doc/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
```

## Usage
* for running the bridge
```
python manage.py bridge
```
* for running the reciver
```
python manage.py reciver
```
