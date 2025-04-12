#https://pypi.org/project/phonenumbers/
import phonenumbers# region of the Earth #customerdetails #simdetails
from phonenumbers import timezone,geocoder,carrier

number=input("Enter your phone number: ")
phone=phonenumbers.parse(number)#Country Code: National Number:
time = timezone.time_zones_for_number(phone)#using timezone as a function
sim_details=carrier.name_for_number(phone,"en")#  we want carrier_details in english so we "en"
register=geocoder.description_for_number(phone,"en")#we want the location to be in english


print("Phone Number:", number)
print(phone)
print("Timezone:",time)
print("Carrier:", sim_details)
print("Location:", register)
