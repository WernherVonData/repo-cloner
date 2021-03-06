import yaml


def _verify_structure(data):
    return False


def read_repos_list(path_to_yaml):
    with open(path_to_yaml) as file:
        doc = yaml.load(file, Loader=yaml.FullLoader)
        data = yaml.dump(doc, sort_keys=True)
        print(data)
        return data
