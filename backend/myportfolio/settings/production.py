from .base import *

if DEBUG:
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

    INSTALLED_APPS += (
        "cloudinary_storage",
        "cloudinary",
    )

    DATABASESs = {
        "default": dj_database_url.config(
            default=env("DATABASE_URL"),
            conn_max_age=60,
        )
    }

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

    # Cloudinary Settings For Media Files
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": env("CLOUD_NAME"),
        "API_KEY": env("API_KEY"),
        "API_SECRET": env("API_SECRET"),
    }
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

    # Emails configurations
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env("EMAIL_HOST")
    EMAIL_PORT = env("EMAIL_PORT")
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    RECIPIENT_ADDRESS = env("RECIPIENT_ADDRESS")
