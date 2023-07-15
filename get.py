from truecallerpy import search_phonenumber
import os

def get_truecaller_info(phone_number):
    api_key = os.environ.get('TRUECALLER_API_KEY')
    country_code = "IN"
    data = search_phonenumber(phone_number, country_code, api_key)
    
    return data
