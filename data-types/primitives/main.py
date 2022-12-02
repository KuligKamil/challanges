import os
import yaml

primitives = {
    'string': dir(''),
    'boolean': dir(bool()),
    # numbers
    'integer': dir(int()),
    'float': dir(float()),
    'complex': dir(complex()),
    'list': dir(list()),
    'set': dir(set()),
    'bytes': dir(bytes()),
    'bytearray': dir(bytearray()),
    'memoryview': dir(memoryview(bytes())),
    'none': dir(None),
    
}
# proprtise = dir('')

print(primitives)
with open(f'{os.getcwd()}/data-types/primitives/python-propertise.yaml', 'w') as f:
    data = yaml.dump(primitives, f)