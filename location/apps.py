# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.apps import AppConfig

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ LOCATION CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


class LocationConfig(AppConfig):
    """ Location Config """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Set name
    name = "location"