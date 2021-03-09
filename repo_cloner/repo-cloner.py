import subprocess
import sys
import pathlib
import yml_reader

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


def main():
    print("Welcome to the {} version {}".format(_script_name_without_extension, _version))
    if len(sys.argv) == 0:
        _print_help()
        return
    for arg in sys.argv[1:]:
        if arg in _help_arguments:
            _print_help()
            return
        if arg in _repo_file_arguments:
            file_index = sys.argv.index(arg)
            if file_index >= len(sys.argv):
                print("Error: missing repo .yml file argument")
                _print_help()
                return
            if sys.argv[file_index+1] not in _help_arguments \
                    and sys.argv[file_index+1] not in _repo_file_arguments \
                    and _verify_yml_extension(sys.argv[file_index+1]) == False:
                print("Error: bad argument for --repo_file: {}".format(sys.argv[file_index+1]))
                _print_help()
                return
            clone_repositories(yml_reader.read_repos_list(sys.argv[file_index+1]))
            return
        else:
            _print_help()
            return


if __name__ == "__main__":
    main()
