# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.apps import AppConfig


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ USER CONFIG
# └─────────────────────────────────────────────────────────────────────────────────────


class UserConfig(AppConfig):
    """ User Config """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CLASS ATTRIBUTES
    # └─────────────────────────────────────────────────────────────────────────────────

    # Set name
    name = "user"