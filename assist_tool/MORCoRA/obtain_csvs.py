import pathlib

root = pathlib.Path("/Users/leichen/data/MORCoRA/auto/MORCoRE")
repos = ["auto", "mockito"]


def extract_csvs():
    for repo in repos:
        path = root.joinpath(repo, "MORCoRE", "csv")
        print(path)


if __name__ == "__main__":
    extract_csvs()
