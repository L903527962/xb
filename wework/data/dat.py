"""
解析yam
"""
import json

import yaml

# with open('token.yml', 'r') as f:
#     data = yaml.load(f.read(),Loader=yaml.FullLoader)
#     #
#     # ya = yaml.safe_load(f)
#     print(data)
#     print(type(data))
def data(data1):
    with open(data1, 'r') as f:
        data = json.load(f)
    return data

