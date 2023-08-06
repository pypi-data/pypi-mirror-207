import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
from pypicor import credentials as creds

def GetBAQ(baq_name : str, parameters : dict = {}, filters : dict = {}, select : list = []):
    # Get a BAQ from Epicor
    # str: baq_name = Name of the BAQ to run
    # Dictionary: parameters = Dictionary of parameters to pass to the BAQ
    # Returns: Pandas dataframe with the results of the BAQ
    # Example:
    #   df = GetBAQ('PartList', ['PartNum:1234', 'Company:000'])
    url = f"https://centralusdtapp01.epicorsaas.com/SaaS515/api/v2/odata/{creds.EPICOR_COMPANY_ID}/BaqSvc/{baq_name}/Data"
    auth = HTTPBasicAuth(creds.EPICOR_USERNAME, creds.EPICOR_USER_PASSWORD)
    headers = {
        "x-api-key": creds.EPICOR_API_KEY,
        "Content-Type": "application/json",
    }
    
    hasFilter = len(filters) > 0
    hasSelect = len(select) > 0
    
    if hasFilter and hasSelect:
        url += '?'
        url = _addFilterToUrl(url, filters)
        url += '&'
        url = _addSelectToUrl(url, select)
    elif hasFilter:
        url += '?'
        url = _addFilterToUrl(url, filters)
    elif hasSelect:
        url += '?'
        url = _addSelectToUrl(url, select)
         
    responce = requests.get(url, headers=headers, auth=auth, params=parameters)
    data = responce.json()
    return pd.DataFrame(data['value'])

def _addFilterToUrl(url : str, filters : dict):
    url += '$filter='
    num_filters = len(filters)
    for i, (key, value) in enumerate(filters.items()):
        
        if isinstance(value, bool):
            url += f"{key} eq {str(value).lower()}"
        elif isinstance(value, str):
            url += f"{key} eq '{value}'"
        elif isinstance(value, int):
            url += f"{key} eq {value}"
        
        if i < num_filters - 1:
            url += ' and '
            
    return url
            
def _addSelectToUrl(url : str, select : list):
    url += '$select='
    num_select = len(select)
    for i, item in enumerate(select):
        url += f'{item}'
        if i < num_select - 1:
            url += ','
            
    return url
            
        