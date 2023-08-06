from typing import Iterator, Dict, List, Union
from colorama import Fore

# imports for get_packges()
from pip._internal.commands.show import search_packages_info
from pkg_resources import working_set


def get_packages() -> Iterator[Dict[str, Union[str, List[str], None]]]:
    site_packages = [
        package.project_name for package in working_set
        if package.location.endswith("site-packages")
    ]
    return search_packages_info(site_packages) #type:ignore


# pip._internal.commands.show.search_packages_info returns ...
# Generator[_PackageInfo, None, None] for pip>=22.0
# Iterator[Dict[str, str]] for pip<=21.0
# (this does not take the minor versions into consideration)

def show_dependency_tree(packages) -> None:
    for package in packages:
        if not package.required_by:
            if package.requires:
                print(
                    f"{Fore.BLUE}{package.name}={package.version}{Fore.RESET}",
                    '\n'.join('    ' + s for s in package.requires),
                    sep="\n",
                )
            else:
                print(
                    f"{Fore.BLUE}{package.name}={package.version}{Fore.RESET}",
                )

def show_dependency_tree21(packages) -> None:
    for package in packages:
        if not package['required_by']:
            if package['requires'] != []:
                print(
                    f"{Fore.BLUE}{package['name']}={package['version']}{Fore.RESET}",
                    '\n'.join('    ' + s for s in package['requires']),
                    sep="\n",
                )
            else:
                print(
                    f"{Fore.BLUE}{package['name']}={package['version']}{Fore.RESET}",
                )


def main() -> None:
    packages = get_packages()
    try:
        from pip._internal.commands.show import _PackageInfo
    except ImportError:
        show_dependency_tree21(packages)
    else:
        show_dependency_tree(packages)

if __name__ == "__main__":
    main()

