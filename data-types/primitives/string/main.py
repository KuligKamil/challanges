import os
import yaml

proprtise = dir('')
print(proprtise)
with open(f'{os.getcwd()}/data-types/primitives/string/python-propertise.yaml', 'w') as f:
    data = yaml.dump(proprtise, f)