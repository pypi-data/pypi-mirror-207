"""Defaults values of arguments"""

from .datatypes import Order, Boolean


_default_order = Order.NAME
_default_reverse = Boolean.FALSE
_default_hidebroken = Boolean.FALSE
_default_offset = 0
_default_limit = 100000

_default_name_exact = Boolean.FALSE
_default_country_exact = Boolean.FALSE
_default_state_exact = Boolean.FALSE
_default_language_exact = Boolean.FALSE
_default_tag_exact = Boolean.FALSE
_default_has_geo_info = Boolean.FALSE
_default_has_extended_info = Boolean.FALSE
_default_is_https = Boolean.FALSE