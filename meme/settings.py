"""
settings.py - Это файл настроек Django, 
который содержит все настройки проекта.

Приложение (app) - это набор функций,
которые работают вместе для выполнения определенной задачи.

127.0.0.1:8000 - это локальный адрес, который используется для тестирования проекта.
"""

from pathlib import Path

# BASE_DIR - это путь к каталогу проекта Django.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECRET_KEY - это секретный ключ Django, для безопасности проекта.
SECRET_KEY = "django-insecure-=1$-0@fjb#5-f(r7bl2m)lib&kqpz7l8wg61q93-^qrym&402+"

# DEBUG - это переменная, которая включает или отключает режим отладки.
DEBUG = True

# ALLOWED_HOSTS - это список доменов, которые могут обслуживаться этим проектом.
ALLOWED_HOSTS = []

# INSTALLED_APPS - это список всех приложений, которые установлены в проекте Django.
INSTALLED_APPS = [
    'jazzmin',

    "django.contrib.admin", # Приложение администратора Django.
    "django.contrib.auth", # Приложение аутентификации Django.
    "django.contrib.contenttypes", # Приложение типов контента Django.
    "django.contrib.sessions", # Приложение сессий Django.
    "django.contrib.messages", # Приложение сообщений Django.
    "django.contrib.staticfiles", # Приложение статических файлов Django.

    # Third-party apps
    "debug_toolbar",

    # Custom apps
    "post", # "post.apps.PostConfig"
    "user", # "user.apps.UserConfig"
]

# MIDDLEWARE - это список всех промежуточных программ, которые используются в проекте Django.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware", # Промежуточная программа безопасности Django.
    "django.contrib.sessions.middleware.SessionMiddleware", # Промежуточная программа сессий Django.
    "django.middleware.common.CommonMiddleware", # Промежуточная программа общего доступа Django.
    "django.middleware.csrf.CsrfViewMiddleware", # Промежуточная программа CSRF Django.
    "django.contrib.auth.middleware.AuthenticationMiddleware", # Промежуточная программа аутентификации Django.
    "django.contrib.messages.middleware.MessageMiddleware", # Промежуточная программа сообщений Django.
    "django.middleware.clickjacking.XFrameOptionsMiddleware", # Промежуточная программа XFrameOptions Django.
    # "post.middleware.URLRewriteMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "querycount.middleware.QueryCountMiddleware"
]

# ROOT_URLCONF - это корневой URL-адрес проекта Django.
ROOT_URLCONF = "meme.urls"


# TEMPLATES - это список всех шаблонов, которые используются в проекте Django.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates", # Шаблоны Django.
        "DIRS": [
            BASE_DIR / "templates", # Каталог шаблонов Django.
        ], # Каталоги шаблонов Django.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [  # TODO
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI_APPLICATION - это приложение WSGI, которое используется в проекте Django.
WSGI_APPLICATION = "meme.wsgi.application"


# DATABASES - это список всех баз данных, которые используются в проекте Django.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# AUTH_PASSWORD_VALIDATORS - это список всех валидаторов паролей, которые используются в проекте Django.
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# LANGUAGE_CODE - это язык, который используется в проекте Django.
LANGUAGE_CODE = "en-us"

# TIME_ZONE - это часовой пояс, который используется в проекте Django.
TIME_ZONE = "UTC"

# USE_I18N - это переменная, которая включает или отключает интернационализацию.
USE_I18N = True

# USE_TZ - это переменная, которая включает или отключает использование часовых поясов.
USE_TZ = True

# STATIC_URL - это URL-адрес статических файлов, который используется в проекте Django.
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# DEFAULT_AUTO_FIELD - это поле по умолчанию для моделей Django.
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

USER_MODEL = "user.User"

INTERNAL_IPS = [
    "127.0.0.1",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "django.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True, # propagate - это переменная, которая включает или отключает передачу сообщений логгера.
        },
    },
}


JAZZMIN_SETTINGS = {
    "site_title": "39-1",
    "site_header": "39-1",
    "site_brand": "39-1",

    "site_logo": None,
    "login_logo": None,
    "login_logo_dark": None,

    "site_logo_classes": "img-circle",
    "site_icon": None,

    "welcome_sign": "Welcome to the library",
    "copyright": "Acme Library Ltd",

    "search_model": ["auth.User", "auth.Group"],

    "user_avatar": None,

    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "books": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    # "language_chooser": True,
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cerulean",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}