from repo_cloner.repo_cloner import execute_arguments


# def test_simple(mocker):
#     _read_repo_list = mocker.patch('repo_cloner.yml_reader.read_repos_list', return_value=["repo1", "repo2", "repo3"])
#     _clone_repositories_mock = mocker.patch('repo_cloner.repo_cloner.clone_repositories')
#     execute_arguments(["script_name", "--repo_file", "test.yml"])
#     assert _read_repo_list.call_count == 1
#     assert _clone_repositories_mock.call_count == 1