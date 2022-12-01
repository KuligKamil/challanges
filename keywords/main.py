import keyword
import yaml

keywords = list(keyword.kwlist)
keywords.pop(3)

with open('keywords/python-keywords.yaml', 'w') as f:
    data = yaml.dump(keywords, f)