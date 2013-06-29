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


    following_users = gitUser.get_user().get_following()
    follower_users = gitUser.get_user().get_followers()
    following_users_list = []
    follower_users_list = []

    print "Getting your following list..."
    for following_user in following_users:
        print "Github ID: %s and Github Name: %s" % (following_user.id, following_user.name)
        following_users_list.append(following_user)

    print "\nGetting your follower list..."
    for follower_user in follower_users:
        print "Github ID: %s and Github Name: %s" % (follower_user.id, follower_user.name)
        follower_users_list.append(follower_user.id)
    
    print "\n\n"
    for following_user in following_users_list:
        if following_user.id not in follower_users_list:
            gitUser.get_user().remove_from_following(following_user)
            print "Github user with ID: %s and Name: %s is not following you and automaticaly unfollowed by this script" % (following_user.id, following_user.name)

