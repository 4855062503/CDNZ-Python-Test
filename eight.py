import yaml

classes_to_return = []

def classes_from_yaml(filepath):
    '''
    Opens a yaml file, creates classes from it
    '''
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor, Loader=yaml.Loader)
        for class_name in data:
            for element in data[class_name]:
                classes_to_return.append(type(class_name, (), data[class_name][element]))

classes_from_yaml('test.yaml')
for x in classes_to_return:
    print(x)
