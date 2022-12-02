import fs from 'fs';
import yaml from 'js-yaml';
const propertiseJS = Object.getOwnPropertyNames(String.prototype)

try {
    let fileContents = fs.readFileSync('./data-types/primitives/string/python-propertise.yaml', 'utf8');
    let propertisePython: String[] = yaml.load(fileContents);

    console.log('JS', propertiseJS.length)
    console.log('Python', propertisePython.length)
    console.log();
    propertisePython = propertisePython.filter(temp => !temp.includes('_') )
    console.log('JS', propertiseJS.length)
    console.log('Python', propertisePython.length)
    console.log(propertiseJS);
    console.log(propertisePython);

} catch (e) {
    console.log(e);
}

