import subprocess
import sys
import pathlib
from repo_cloner.yml_reader import read_repos_list

_version = "0.0.1"
_help_arguments = ["--help", "-h"]
_repo_file_arguments = ["--repo_file", "-rf"]
_script_name_without_extension = __file__[:-3]


def _print_help():
    print("Usage: {} [--help][-h][--repo_file][-rf]".format(_script_name_without_extension))
    print("--help, -h: prints this message")
    print("--repo_file, -rf: .yml file with list of repositories to clone")


def _verify_yml_extension(filename):
    if pathlib.Path(filename).suffix == ".yml":
        return True
    return False


def clone_repositories(repos):
    for repo in repos:
        print("Cloning: {}".format(repo))
        clone_repo = subprocess.run(["git", "clone", repo])
        print("The exit code was: {}".format(str(clone_repo.returncode)))


def execute_arguments(args):
    if len(args) <= 1:
        _print_help()
        return

    for h in _help_arguments:
        if h in args:
            _print_help()
            return

    for arg in args[1:]:
        if arg in _repo_file_arguments:
            file_index = args.index(arg)+1
            if file_index >= len(args):
                print("Error: missing repo .yml file argument")
                _print_help()
                return
            if args[file_index] not in _help_arguments \
                    and args[file_index] not in _repo_file_arguments \
                    and _verify_yml_extension(args[file_index]) == False:
                print("Error: bad argument for --repo_file: {}".format(args[file_index]))
                _print_help()
                return
            clone_repositories(read_repos_list(args[file_index]))
            return
        else:
            _print_help()
            return


def main():
    print("Welcome to the repo_cloner version {}".format(_version))
    execute_arguments(sys.argv)


if __name__ == "__main__":
    main()