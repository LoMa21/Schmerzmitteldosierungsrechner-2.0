import requests

BIN_API_URL = r'https://api.jsonbin.io/v3/b'

def load_data(api_key, bin_id):
    """
    Load entire bin
    """
    url = BIN_API_URL + '/' + bin_id + '/latest'
    headers = {'X-Master-Key': api_key}
    res = requests.get(url, headers=headers).json()
    return res['record']


def save_data(api_key, bin_id, data):
    """
    Save entire bin
    """
    url = BIN_API_URL + '/' + bin_id
    headers = {'X-Master-Key': api_key, 'Content-Type': 'application/json'}
    res = requests.put(url, headers=headers, json=data).json()
    return res


def load_key(api_key, bin_id, key, empty_value=[]):
    """
    Load key from bin
    """
    url = BIN_API_URL + '/' + bin_id + '/latest'
    headers = {'X-Master-Key': api_key}
    res = requests.get(url, headers=headers).json()
    res = res['record']
    if key in res:
        return res[key]
    else:
        return empty_value


def save_key(api_key, bin_id, key, data):
    """
    Save key to bin
    """
    url = BIN_API_URL + '/' + bin_id
    headers = {'X-Master-Key': api_key, 'Content-Type': 'application/json'}
    res = requests.get(url, headers=headers).json()
    res = res['record']
    if type(res) != dict:
        res = {key:data}  # generate new dict
    else:
        res[key] = data
    res = requests.put(url, headers=headers, json=res).json()
    return res