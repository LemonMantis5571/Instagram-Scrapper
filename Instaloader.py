
from cProfile import Profile
import profile
import instaloader

ig = instaloader.Instaloader()

dp = input("Introduce el nombre del perfil al que vas a descargar las fotos: ")

ig.download_profile(dp, profile_pic_only=True)


    

