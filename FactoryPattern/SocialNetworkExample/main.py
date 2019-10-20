from FactoryPattern.SocialNetworkExample.profile import facebook
from FactoryPattern.SocialNetworkExample.profile import linkedin

########################################################
#                   Main Program
########################################################
if __name__ == '__main__':

    # Uncomment this section to test creation from command line
    # profile_type = input("Which profile would you like to create? LinkedIn or FaceBook: ")
    # profile = eval(profile_type.lower())()
    # print(f"Creating profile... {type(profile).__name__}")
    # print(f"Profile has sections: {profile.getSections()}")

    fb_profile = facebook()
    li_profile = linkedin()

    print(f"Facebook profile has sections: {[x.__name__ for x in fb_profile.getSections()]}")
    print(f"Linked profile has sections: {[x.__name__ for x in li_profile.getSections()]}")