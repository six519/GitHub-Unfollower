#!/usr/bin/env python
from github import Github
from github.GithubException import GithubException
from getpass import getpass

if __name__ == "__main__":
    gitHubUsername = raw_input("Please enter your Github username: ").strip()
    gitHubPassword = getpass("Please enter your Github password: ").strip()
    
    gitUser = Github(gitHubUsername, gitHubPassword)
    
    try:
        gitHubName = gitUser.get_user().name
        gitHubId = gitUser.get_user().id
        print "Your Github ID is: %s\nYour Github Name is: %s" % (gitHubId, gitHubName)
        print "You got %s followers and following %s Github users..." % (gitUser.get_user().followers, gitUser.get_user().following)
    except GithubException as e:
        print "This script can't connect to Github with following information:\n\nUsername: %s\nPassword: %s" % (gitHubUsername,gitHubPassword)
        print "Run this script again if you want to use it... :)"
        exit()


    followers = [follower.id for follower in gitUser.get_user().get_followers()] 

    print "\n\n"
    for following in gitUser.get_user().get_following():
        print "Checking Github ID: %s and Github Name: %s" % (following.id, following.name)
        if following.id not in followers:
            gitUser.get_user().remove_from_following(following)
            print "Github user with ID: %s and Name: %s is not following you and automaticaly unfollowed by this script" % (following.id, following.name)
