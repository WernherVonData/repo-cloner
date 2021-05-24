from repo_cloner.cloner import execute_arguments

"""
Small note regarding mocking from documentation:
"The basic principle is that you patch where an object is looked up,
which is not necessarily the same place as where it is defined."

In our case read_repos_list is DEFINED in the yml_reader, but the context of calling this function lies in the 
repo_cloner script itself.

If for example we had import of the whole yml_reader script inside repo_cloner script, then the path could be:
repo_cloner.yml_reader.read_repos_list.
"""


def test_repo_file_argument(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _read_repo_list.return_value = ["repo1", "repo2", "repo3"]
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "--repo_file", "test.yml"])

    assert _read_repo_list.call_count == 1
    assert _clone_repositories_mock.call_count == 1
    assert _print_help_mock.call_count == 0


def test_rf_argument(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _read_repo_list.return_value = ["repo1", "repo2", "repo3"]
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "-rf", "test.yml"])

    assert _read_repo_list.call_count == 1
    assert _clone_repositories_mock.call_count == 1
    assert _print_help_mock.call_count == 0


def test_wrong_path_argument(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "-rf", "test"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1


def test_missing_file_argument(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "-rf"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1


def test_help_argument(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "--help"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1


def test_h_argument(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "-h"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1


def test_v_argument(mocker):
    _print_get_version_mock = mocker.patch('repo_cloner.cloner._get_version')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "-v"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_get_version_mock.call_count == 1


def test_version_argument(mocker):
    _print_get_version_mock = mocker.patch('repo_cloner.cloner._get_version')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "--version"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_get_version_mock.call_count == 1


def test_all_arguments_with_help(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "-rf", "test.yml", "-v", "--help"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1


def test_all_arguments_with_h(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["script_name", "-rf", "test.yml", "--version", "-h"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1


def test_no_arguments(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments([])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1


def test_one_argument(mocker):
    _print_help_mock = mocker.patch('repo_cloner.cloner._print_help')
    _read_repo_list = mocker.patch('repo_cloner.cloner.read_repos_list')
    _clone_repositories_mock = mocker.patch('repo_cloner.cloner.clone_repositories')

    execute_arguments(["test_name"])

    assert _read_repo_list.call_count == 0
    assert _clone_repositories_mock.call_count == 0
    assert _print_help_mock.call_count == 1