"""Determine if a PR has approvals from specific teams"""

import argparse
from collections import defaultdict
import sys

import github

from orf_utils import common


def _format_team_name(team_name: str) -> str:
    """Formatting utility to support passing arguments via GitHub actions. Converts '-' and '_' characters to spaces
    and converts all characters to lowercase for comparisons

    :param team_name: The team name to format
    :return: The formatted team name
    """
    return team_name.replace("-", " ").replace("_", " ").lower()


def team_member_has_approved_pr(team: github.Team.Team, pull: github.PullRequest.PullRequest) -> bool:
    """Determine if a member of the given team as approved the given pull request

    :param team: The Team in question
    :param pull: The PullRequest in question
    :return: True if a member of the given team has approved the PR, False if not
    """
    team_members = team.get_members()

    # Get list of reviews sorted by user
    reviews_by_user = defaultdict(list)

    # Retrieved in chronological order from GitHub
    for review in pull.get_reviews():
        # Ignore any reviews by users not in the relevant team
        if review.user in team_members:
            reviews_by_user[review.user].append(review)

    # Go over each users review in reverse chronological order, ignoring plain comments and handling
    # approvals and change requests accordingly
    for reviews in reviews_by_user.values():
        for review in reversed(reviews):
            # At least one member of the team's last PR review of note was an approval
            if review.state == common.APPROVED:
                print(f'Team "{team.name}" approval condition was met')
                return True

            # This member's last review of note was a change request so stop looking
            if review.state == common.CHANGES_REQUESTED:
                break

    print(f'Team "{team.name}" approval condition was NOT met')
    return False


def pr_has_appropriate_reviews(
    client: github.MainClass.Github, org_str: str, repo: str, pr_num: int, team_names: list[str]
) -> bool:
    """Given a repository, PR number, and list of teams, determine if the given PR has at least one approval from each
    of the listed teams

    :param client: Authenticated Github client
    :param org: The GitHub organization to inspect
    :param repo: The GitHub repo to inspect
    :param pr_num: The Pull Request number in the given repo
    :param team_names: The list of teams that are required to be approvers
    :return: True if the PR has appropriate reviews, False if not
    """
    # Ignore caps for downstream lookup
    team_names = [_format_team_name(team_name) for team_name in team_names]

    try:
        org = client.get_organization(org_str)
    except github.GithubException as failed_org_query:
        raise common.ConfigurationError("Could not authenticate with given secret") from failed_org_query

    teams = [team for team in org.get_teams() if _format_team_name(team.name) in team_names]

    if missing_teams := set(team_names) - {_format_team_name(team.name) for team in teams}:
        raise common.ConfigurationError(f"Could not find these teams: {', '.join(missing_teams)}")

    try:
        pull = org.get_repo(repo).get_pull(pr_num)
    except github.GithubException as failed_pull_query:
        raise common.ConfigurationError(f"Could not find PR in repo {repo} with number {pr_num}") from failed_pull_query

    all_teams_approved = True

    # Do this instead of an "all" so that each team's result is processed and output to stdout
    for team in teams:
        all_teams_approved &= team_member_has_approved_pr(team, pull)

    return all_teams_approved


def parse_args():
    """Parse commandline args"""

    parser = argparse.ArgumentParser(description="Determine if relevant teams have approved a PR")

    parser.add_argument("-s", "--secret", required=True, help="GitHub token for authentication")

    parser.add_argument("-o", "--org", required=True, help="The GitHub organization to inspect")

    parser.add_argument("-r", "--repo", required=True, help="The GitHub repository to inspect")

    parser.add_argument("-p", "--pull-request", type=int, required=True, help="The PR to inspect")

    parser.add_argument("-t", "--teams", required=True, nargs="+", help="Teams required for approval")

    return parser.parse_args()


def main():
    """Main entrypoint"""
    opts = parse_args()

    github_client = github.Github(opts.secret)

    if pr_has_appropriate_reviews(github_client, opts.org, opts.repo, opts.pull_request, opts.teams):
        sys.exit(0)

    sys.exit(1)


if __name__ == "__main__":
    main()
