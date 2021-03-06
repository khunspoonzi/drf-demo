# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.db.models import Q

# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO REST FRAMEWORK IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from rest_framework.generics import get_object_or_404


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ GET COUNTRY BY LOOKUP OR 404
# └─────────────────────────────────────────────────────────────────────────────────────


def get_country_by_lookup_or_404(queryset, lookup, lookup_field="pk"):
    """ Returns a Country instance based on an arbitrary string lookup """

    # Check if lookup is an alpha string
    if lookup and lookup.isalpha():

        # Uppercase lookup assuming that it is an ISO code
        lookup = lookup.upper()

        # Get Country instance by ISO lookup
        country = get_object_or_404(queryset, (Q(iso2=lookup) | Q(iso3=lookup)))

    # Otherwise handle non-alpha lookup
    else:

        # Get Country instance by primary key lookup
        country = get_object_or_404(queryset, **{lookup_field: lookup})

    # Return Country instance
    return country
