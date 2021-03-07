import sys
from repo_data_reader import yml_reader

version = "0.0.1"


def print_help():
    print("Usage: {} [--help][-h][--repo_file][-rf]".format(__file__[:-3]))
    print("--help, -h: prints this message")
    print("--repo_file, -rf: .yml file with list of repositories to clone")


def read_repos(file):
    yml_reader.read_repos_list(file)


def main():
    print("Welcome to the {} version {}".format(__file__[:-3], version))
    if len(sys.argv) == 0:
        print_help()
        return
    for arg in sys.argv[1:]:
        if arg == "--help" or arg == "-h":
            print_help()
            return
        if arg == "--repo_file" or arg == "-rf":
            file_index = sys.argv.index(arg)
            if file_index >= len(sys.argv):
                print("Error: missing repo .yml file argument")
                print_help()
                return
            a = sys.argv[file_index+1]
            b = sys.argv[file_index+1][-4:]
            if sys.argv[file_index+1] != "--help" \
                    and sys.argv[file_index+1] != "-h" \
                    and sys.argv[file_index+1] != "--repo_file" \
                    and sys.argv[file_index+1] != "-rf" \
                    and sys.argv[file_index+1][-4:] != ".yml":
                print("Error: bad argument: {}".format(sys.argv[file_index+1]))
                print_help()
                return
            read_repos(sys.argv[file_index+1])
            return
        else:
            print_help()
            return


if __name__ == "__main__":
    main()
