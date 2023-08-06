"""Tag the current git commit based on version information in a JSON file"""

import argparse
from datetime import date

import git

from orf_utils import common


def tag_current_commit(git_repo: common.Repo, new_version: common.VersionTag, add_date: bool = False) -> None:
    """Given a new version, tag the current commit accordingly

    :param new_version: The new version to use to tag
    :param add_date: Append current date to the tag
    :raises common.InvalidVersion: If the new version does not make sense with respect to the current version
    """
    try:
        old_version = common.VersionTag(git_repo.git.describe(tags=True))
        old_version.assert_valid_new_version(new_version)
        new_tag = str(new_version) if new_version > old_version else old_version.get_new_release()
    except git.GitError:
        common.VersionTag("0.0.0-1").assert_valid_new_version(new_version)
        new_tag = str(new_version)

    curr_date = date.today().strftime("%Y-%m-%d")

    if add_date:
        new_tag = f"{new_tag}-{curr_date}"

    try:
        git_repo.create_tag(new_tag, m=new_tag)
    except git.GitError as git_error:
        raise common.ConfigurationError(f"Could not lay down tag {new_tag} - try pulling main/master") from git_error

    print(f"Created new tag {new_tag}")


def parse_args():
    """Parse commandline args"""

    parser = argparse.ArgumentParser(description="Determine if relevant teams have approved a PR")

    parser.add_argument("-r", "--repo-path", required=True, help="Path to local git repository")

    parser.add_argument("-j", "--json", required=True, help="JSON file path")

    parser.add_argument("-d", "--date", action="store_true", required=False, help="Add a date string to the tag")

    return parser.parse_args()


def main():
    """Main entrypoint"""
    opts = parse_args()

    json_version = common.VersionTag.from_json(opts.json)

    tag_current_commit(git.Repo(opts.repo_path), json_version, opts.date)


if __name__ == "__main__":
    main()
