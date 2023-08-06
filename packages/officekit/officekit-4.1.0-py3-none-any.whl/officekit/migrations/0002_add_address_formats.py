import os
import codecs
import csv

from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.db import migrations, transaction
from django.core.exceptions import ImproperlyConfigured
from django.utils import timezone
from django.core.files.base import ContentFile


def add_address_formats(apps, schema_editor):

    # noinspection PyPep8Naming
    AddressFormat = apps.get_model('officekit', 'AddressFormat')

    with transaction.atomic():
        postal_format = AddressFormat()
        postal_format.identifier = 'postal_html'
        postal_format.description = 'Postal Format (HTML)'
        postal_format.method = 'officekit:postal_html'
        postal_format.save()

        physical_format = AddressFormat()
        physical_format.identifier = 'physical_html'
        physical_format.description = 'Physical Format (HTML)'
        physical_format.method = 'officekit:physical_html'
        physical_format.save()

        directions_format = AddressFormat()
        directions_format.identifier = 'directions_html'
        directions_format.description = 'Directions Format (HTML)'
        directions_format.method = 'officekit:directions_html'
        directions_format.save()

        google_maps_link_format = AddressFormat()
        google_maps_link_format.identifier = 'google_maps_link_html'
        google_maps_link_format.description = 'Google Maps Link Format (HTML)'
        google_maps_link_format.method = 'officekit:google_maps_link_html'
        google_maps_link_format.save()

        postal_format = AddressFormat()
        postal_format.identifier = 'postal_plain'
        postal_format.description = 'Postal Format (Plain Text)'
        postal_format.method = 'officekit:postal_plain'
        postal_format.save()

        physical_format = AddressFormat()
        physical_format.identifier = 'physical_plain'
        physical_format.description = 'Physical Format (Plain Text)'
        physical_format.method = 'officekit:physical_plain'
        physical_format.save()

        directions_format = AddressFormat()
        directions_format.identifier = 'directions_plain'
        directions_format.description = 'Directions Format (Plain Text)'
        directions_format.method = 'officekit:directions_plain'
        directions_format.save()

        google_maps_link_format = AddressFormat()
        google_maps_link_format.identifier = 'google_maps_link_plain'
        google_maps_link_format.description = 'Google Maps Link Format (Plain Text)'
        google_maps_link_format.method = 'officekit:google_maps_link_plain'
        google_maps_link_format.save()


class Migration(migrations.Migration):
    dependencies = [
        ('officekit', '0001_initial')
    ]

    operations = [
        migrations.RunPython(add_address_formats),
    ]
