# import requests

# url = "https://f1-live-motorsport-data.p.rapidapi.com/session/2757"

# headers = {
# 	"X-RapidAPI-Key": "db76b0dd12msh4de05a8b50d9b9fp14b405jsn06de70f0c789",
# 	"X-RapidAPI-Host": "f1-live-motorsport-data.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

import numpy as np
from pathlib import Path
import json
JSON_INDENT = 4
JSON_SEP = (',', ':')

def is_array(x):
    return ('shape' in dir(x))

def load_json(path: str | Path) -> dict:
    """ load a dict as json file at path converting all iterables to numpy arrays """
    with open(path, 'r') as f:
        d = json.load(f, indent=JSON_INDENT, separators=JSON_SEP)
    if isinstance(d, dict):
        d = {k:np.array(v) if isinstance(v, list|tuple) else v for k,v in d.items()}
    elif isinstance(d, list|tuple):
        d = np.array(d)
    return d

def save_json(d: dict | str, path: Path):
    """ save a dict as json file at path """
    if isinstance(d, str):
        d = dict(d)
    for k, v in d.items():
        if is_array(v):
            d[k] = np.array(v).tolist()
        if isinstance(v, Path):
            d[k] = str(v)
    with open(path, 'w') as f:
        json.dump(d, f, indent=JSON_INDENT, separators=JSON_SEP)

import requests

url = "https://f1-live-motorsport-data.p.rapidapi.com/seasons"

headers = {
	"X-RapidAPI-Key": "db76b0dd12msh4de05a8b50d9b9fp14b405jsn06de70f0c789",
	"X-RapidAPI-Host": "f1-live-motorsport-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

save_json(response, './test.json')

print(response.text)