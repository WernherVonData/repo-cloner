import os
from repo_cloner.yml_reader import read_repos_list

path_to_test = os.path.dirname(os.path.abspath(__file__))
_expected_listed_repos_structure = ["repo1", "repo2", "repo3"]
_expected_path_repos_structure = {"path1": ["repo1", "repo2", "repo3", "repo4"], "path2": ["repo5", "repo6", "repo7"]}
_expected_empty_array = []


def test_read_listed_repos():
    path_to_yml = path_to_test + '/listed_repos.yml'
    received_data = read_repos_list(path_to_yml)
    assert (_expected_listed_repos_structure == received_data)


def test_read_path_repos():
    path_to_yml = path_to_test + '/path_repos.yml'
    received_data = read_repos_list(path_to_yml)
    assert (_expected_path_repos_structure == received_data)


"""
If you are having a value with nested data you CAN'T have a mixed elements.
Yaml parser does not allow for such action.
"""


def test_verify_mixed_structures():
    path_to_yml = path_to_test + '/mixed_repos_structure.yml'
    received_data = read_repos_list(path_to_yml)
    assert (_expected_empty_array == received_data)


def test_verify_bad_path_structure():
    path_to_yml = path_to_test + '/bad_path_structure.yml'
    received_data = read_repos_list(path_to_yml)
    assert (_expected_empty_array == received_data)
