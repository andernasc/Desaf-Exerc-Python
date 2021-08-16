import phonenumbers

from phonenumbers import geocoder

phone = input('Digite um número no formato +551140028922: ')

phone_numbers = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_numbers, 'pt'))