# Simple, clean config:
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config()}
else:
    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3'}}

# Always enable CORS for Vercel
CORS_ALLOW_ALL_ORIGINS = True  # or list specific origin
