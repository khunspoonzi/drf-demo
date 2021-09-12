# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ DJANGO IMPORTS
# └─────────────────────────────────────────────────────────────────────────────────────

from django.core.exceptions import ValidationError
from django.db import models


# ┌─────────────────────────────────────────────────────────────────────────────────────
# │ COUNTRY
# └─────────────────────────────────────────────────────────────────────────────────────


class Country(models.Model):
    """ Country Model """

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ CURRENCY
    # └─────────────────────────────────────────────────────────────────────────────────

    # currency = models.ForeignKey(
    #     "currency.Currency",
    #     related_name="countries",
    #     on_delete=models.PROTECT,
    #     blank=True,
    #     null=True,
    # )

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ NAME
    # └─────────────────────────────────────────────────────────────────────────────────

    name = models.CharField(max_length=255, unique=True)
    name_native = models.CharField(max_length=255, unique=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ ISO
    # └─────────────────────────────────────────────────────────────────────────────────

    iso2 = models.CharField(max_length=2, unique=True)
    iso3 = models.CharField(max_length=3, unique=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ POPULATION
    # └─────────────────────────────────────────────────────────────────────────────────

    population = models.IntegerField(blank=True, null=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ COORDINATES
    # └─────────────────────────────────────────────────────────────────────────────────

    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ UN MEMBER STATUS
    # └─────────────────────────────────────────────────────────────────────────────────

    is_un_member = models.BooleanField()
    is_un_member_at = models.DateTimeField(blank=True, null=True)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ FLAG
    # └─────────────────────────────────────────────────────────────────────────────────

    flag = models.ImageField(upload_to="location/country/flag")

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ SAVE
    # └─────────────────────────────────────────────────────────────────────────────────

    def save(self, *args, **kwargs):
        """ Custom Save Method """

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ ISO
        # └─────────────────────────────────────────────────────────────────────────────

        # Uppercase and strip ISO codes
        self.iso2, self.iso3 = [iso.upper().strip() for iso in (self.iso2, self.iso3)]

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ UN MEMBER STATUS
        # └─────────────────────────────────────────────────────────────────────────────

        # Check if is UN member
        if self.is_un_member:

            # Check if is UN member at is null
            if not self.is_un_member_at:

                # Raise ValidationError
                raise ValidationError(
                    "Country.is_un_member_at cannot be null if Country.is_un_member "
                    "is True"
                )

        # Otherwise handle non-UN member
        else:

            # Nullify is UN member at
            self.is_un_member_at = None

        # ┌─────────────────────────────────────────────────────────────────────────────
        # │ SAVE
        # └─────────────────────────────────────────────────────────────────────────────

        # Save object
        return super().save(*args, **kwargs)

    # ┌─────────────────────────────────────────────────────────────────────────────────
    # │ META
    # └─────────────────────────────────────────────────────────────────────────────────

    class Meta:

        # Define verbose names
        verbose_name = "Country"
        verbose_name_plural = "Countries"

        # Define unique together constraints
        unique_together = [["latitude", "longitude"]]
