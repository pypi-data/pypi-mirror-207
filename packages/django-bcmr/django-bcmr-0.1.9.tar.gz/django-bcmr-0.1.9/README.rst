=====
BCMR
=====

BCMR or Bitcoin Cash Metadata Registry is a Django app for storing, accessing and managing CashToken BCMR.

Quick start (development)
---------------------------

1. Add the following to your requirements.txt::
    
    Pillow==9.4.0
    django-bcmr==x.x.x

2. Add "bcmr" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bcmr',
    ]

3. Include the bcmr URLconf in your project urls.py like this::

    from django.conf.urls.static import static
    from django.conf import settings

    urlpatterns = [
        ...
        path('bcmr/', include('bcmr.urls')),
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

4. Add media and DRF (to restrict public access on root API auth token filter) config on settings.py::

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    REST_FRAMEWORK = {
        ...
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer'
        ]
    }

5. Start the development server and visit http://localhost:8000/admin/
   to access the DB (you'll need the Admin app enabled).

6. Visit http://localhost:8000/bcmr/ to check API endpoints for the BCMR and tokens.


Additional steps for deployment
---------------------------------

1. Add media and API location paths on nginx configuration file::

    location /media {
        proxy_pass http://127.0.0.1:<YOUR_DESIRED_MEDIA_PORT_HERE>;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
    }

    location /bcmr {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }

2. Add ``<YOUR_DESIRED_MEDIA_PORT_HERE>`` to your yml file::

    ports:
      ...
      - "<YOUR_DESIRED_MEDIA_PORT_HERE>:<YOUR_DESIRED_MEDIA_PORT_HERE>"

3. Run simple http server hosting for media files using supervisor. Add to supervisord.conf::

    [program:media_server]
    command=python -m http.server <YOUR_DESIRED_MEDIA_PORT_HERE>
    autorestart=true
    stdout_logfile=/dev/stdout
    stdout_logfile_maxbytes=0
    stderr_logfile=/dev/stderr
    stderr_logfile_maxbytes=0
    stopasgroup=true


REST API
-----------

Check docs on http://localhost:8000/api/docs/

Tokens created by a user can only be modified/deleted by that user (owner).

All endpoints are restricted on its usage for prevention of users tampering other user's tokens.
An auth token generated upon creation of either a token helps impose this restriction.
This token is used as a header for identification if the user modifying token data is the owner.
Header name is ``Bcmr-Auth``.

The endpoints are restricted as follows::

    GET = no header required
    POST = if header is supplied, created token/registry will belong to that auth token owner
         = if header is not supplied, a new auth token will be generated (new owner)
    PUT/PATCH = header required
    DELETE = header required


Main BCMR
------------

Fetch at http://localhost:8000/bcmr/registries/main/

Only the admin can add/remove tokens in the BCMR. After adding tokens, ask permission from the admin to include your token to the BCMR.


.. Create Fungible Token Form
.. -----------------------------

.. Creating a token from the REST API can be a hassle as one needs to process the image before passing it
.. as payload. This special route helps ease that burden by simply providing users to create a token and
.. upload an image without having to login to the admin:: `create_token/fungible/`
