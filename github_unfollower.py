#!/usr/bin/env python
from github import Github
from github.GithubException import GithubException
from getpass import getpass

if __name__ == '__main__':
    gitHubPAT = getpass('Please enter your Github personal access token: ').strip()
    
    gitUser = Github(gitHubPAT)
    
    following_count = 0
    followers_count = 0

    try:
        print('Your Github ID is: {}\nYour Github Name is: {}'.format(gitUser.get_user().id, gitUser.get_user().name))
        print('You got {} followers and following {} Github users...'.format(gitUser.get_user().followers, gitUser.get_user().following))
    except GithubException as e:
        print('This script can\'t connect to Github with following information:\n\Token: {}'.format(gitHubPAT))
        print('Run this script again if you want to use it... :)')
        exit()

    followers = [follower.id for follower in gitUser.get_user().get_followers()] 

    print('\n\n')

    for following in gitUser.get_user().get_following():
        print('Checking Github ID: {} and Github Name: {}'.format(following.id, following.name))
        if following.id not in followers:
            gitUser.get_user().remove_from_following(following)
            print('Github user with ID: {} and Name: {} is not following you and automaticaly unfollowed by this script'.format(following.id, following.name))
