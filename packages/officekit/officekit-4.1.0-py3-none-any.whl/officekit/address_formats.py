import re

from django.apps import apps
from django.utils.html import conditional_escape, format_html, mark_safe


from .apps import get_app_label

__all__ = ['AddressFormatDescriptor', 'register_address_format', 'lookup_address_format', 'get_address_format_choices',
           'POSTAL_ADDRESS_FORMAT_HTML', 'PHYSICAL_ADDRESS_FORMAT_HTML', 'DIRECTIONS_ADDRESS_FORMAT_HTML',
           'GOOGLE_MAPS_LINK_ADDRESS_FORMAT_HTML',
           'POSTAL_ADDRESS_FORMAT_PLAIN', 'PHYSICAL_ADDRESS_FORMAT_PLAIN', 'DIRECTIONS_ADDRESS_FORMAT_PLAIN',
           'GOOGLE_MAPS_LINK_ADDRESS_FORMAT_PLAIN']

APP_LABEL = get_app_label()
ADDRESS_FORMATS = dict()


class AddressFormatDescriptor:

    @property
    def identifier(self):
        return self.app_label + ":" + self.local_identifier

    def __init__(self, app_label, local_identifier, description, function):

        self.app_label = app_label
        self.local_identifier = local_identifier
        self.description = description
        self.function = function

        app = apps.get_app_config(self.app_label)
        self.app_name = app.verbose_name


def register_address_format(app_label, local_identifier, description, function):

    method = AddressFormatDescriptor(app_label=app_label, local_identifier=local_identifier, description=description,
                                     function=function)
    ADDRESS_FORMATS[method.identifier] = method
    return method


def lookup_address_format(identifier, default=None):
    return ADDRESS_FORMATS.get(identifier, default)


def get_address_format_choices():

    result = [(identifier, category.name + " [{}]".format(category.app_name.title()))
              for identifier, category in ADDRESS_FORMATS.items()]

    return result


def postal(address, link_text='', plain_text=False):

    br = "<br>"
    nbsp = "&nbsp;"

    if plain_text:
        br = "\n"
        nbsp = "\u00A0"
        esc = lambda x: x
    else:
        esc = conditional_escape

    result = ""

    if address.organisation:
        organisation = br.join(address.organisation.split("\n"))
        result += organisation + br

    if address.building_unit:
        if address.building:
            result += esc(address.building_unit) + "," + nbsp + esc(address.building) + br
        else:
            result += esc(address.building_unit) + br
    elif address.building:
        result += esc(address.building) + br

    if address.street:
        if address.building_number:
            result += esc(address.building_number) + nbsp + esc(address.street) + br
        else:
            result += esc(address.street) + br

    if address.locality:
        result += esc(address.locality) + br

    if address.town:
        result += esc(address.town) + br

    if address.postal_code:
        result += esc(address.postal_code) + br

    if address.country and address.country != "GB":
        result += esc(address.country.name) + br

    if not plain_text:
        result = mark_safe("<p>{}</p>".format(result))

    return result


def physical(address, link_text='', plain_text=False):
    return postal(address, link_text, plain_text=plain_text)


def directions(address, link_text='', plain_text=False):
    result = address.directions

    if plain_text:

        pass
    else:
        result = mark_safe(result)

    return result


def google_maps_link(address, link_text='', plain_text=False):
    result = address.google_maps_url

    if plain_text:
        return result

    result = format_html(f"<a href=\"{result}\">{{}}</a>", link_text if link_text else "Show on Google Maps")
    return result


POSTAL_ADDRESS_FORMAT_HTML = register_address_format(APP_LABEL, "postal_html", "Postal address format (HTML)", postal)
PHYSICAL_ADDRESS_FORMAT_HTML = register_address_format(APP_LABEL, "physical_html", "Physical address format (HTML)", physical)
DIRECTIONS_ADDRESS_FORMAT_HTML = register_address_format(APP_LABEL, "directions_html", "Directions address format (HTML)", directions)
GOOGLE_MAPS_LINK_ADDRESS_FORMAT_HTML = register_address_format(APP_LABEL, "google_maps_link_html", "Google maps link address format (HTML)", google_maps_link)

POSTAL_ADDRESS_FORMAT_PLAIN = register_address_format(APP_LABEL, "postal_plain", "Postal address format (Plain Text)", lambda x, **kwargs: postal(x, **kwargs, plain_text=True))
PHYSICAL_ADDRESS_FORMAT_PLAIN = register_address_format(APP_LABEL, "physical_plain", "Physical address format (Plain Text)", lambda x, **kwargs: physical(x, **kwargs, plain_text=True))
DIRECTIONS_ADDRESS_FORMAT_PLAIN = register_address_format(APP_LABEL, "directions_plain", "Directions address format (Plain Text)", lambda x, **kwargs: directions(x, **kwargs, plain_text=True))
GOOGLE_MAPS_LINK_ADDRESS_FORMAT_PLAIN = register_address_format(APP_LABEL, "google_maps_link_plain", "Google maps link address format (Plain Text)", lambda x, **kwargs: google_maps_link(x, **kwargs, plain_text=True))
