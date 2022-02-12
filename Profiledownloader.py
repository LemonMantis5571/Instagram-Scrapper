
import os
import instaloader
from instaloader import Profile


usernamenv = os.environ.get('USERNAME_KEY')
password = os.environ.get('PASSWORD_KEY')

def profiledownloader(PROFILE):
    ig = instaloader.Instaloader()

    profile = Profile.from_username(ig.context, PROFILE)

    post_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

    for post in post_sorted_by_likes:
        print(post.likes)
        ig.download_post(post, PROFILE)


def getinstagramid(username):
    ig  = instaloader.Instaloader()
    profile_id = ig.check_profile_id(username)
    print(profile_id)


def downloadprofilepic(username):
    ig  = instaloader.Instaloader()
    profile = username
    ig.download_profile(profile, profile_pic_only=True)


def downloadigstories(username):
    ig = instaloader.Instaloader()
    ig.login(usernamenv,password)
    profile_id = int(input("inserta el id del perfil: "))
    ig.download_stories(userids=[profile_id])

if __name__ == "__main__":
    username = input("Introduce el nombre del perfil: ")
    while True:
        modo = input("Introduce el modo de descarga, (P) para bajar todo el perfil, (I) para obtener el ID del perfil, (S) para bajar las historias, (F) para una foto de perfil, (U) para cambiar de usuario o (Q) para salir:  ").lower()

        if modo == "q":
            break

        elif modo == "p":
            profiledownloader(username)

        elif modo == "i":
            getinstagramid(username)
            
        
        elif modo == "s":
            downloadigstories(username)

        elif modo == "f":
            downloadprofilepic(username)

        elif modo == "u":
            username = input("Introduce el nuevo nombre del perfil: ")
            continue

        else:
            continue

