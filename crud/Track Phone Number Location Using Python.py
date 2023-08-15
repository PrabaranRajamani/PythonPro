import phonenumbers
from test import number
from phonenumbers import geocoder
import opencage

ch_phonenumber = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_phonenumber,"en"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))