import os
from typing import Any, Dict

# EASY_THUMBNAILS SETTINGS
THUMBNAIL_CACHE_DIMENSIONS = True
""""""

# THUMBNAIL_CHECK_CACHE_MISS = True
THUMBNAIL_SUBDIR = "thumbs"
""""""

THUMBNAIL_ALIASES: Dict[str, Any] = {}
""""""

THUMBNAIL_PROCESSORS = [
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
]
""""""

THUMBNAIL_DEBUG = os.environ.get("DJANGO_ENV") != "production"
""""""
