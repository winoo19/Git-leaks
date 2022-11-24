import git


REPO_DIR="./skale/skale-manager"


def extract():
    repo = git.Repo(REPO_DIR)
    with open("commits.txt", "w") as f:
        for commit in repo.iter_commits():
            f.write(commit.message)


def search_for_leaks(word):
    matches = []
    with open("commits.txt", "r") as f:
        for line in f.readlines():
            if word in line:
                matches.append(line)
    return matches


if __name__ == "__main__":
    extract()

    for string in ("password", "user", "private", "pass", "key"):
        match = search_for_leaks(string)
        if match:
            print(match)
