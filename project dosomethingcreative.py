# title: Project for Computer class
# author: Zain Nusairat
# description: NA

from earsketch import *
tempo = input("What do you want your tempo to be? volume warning hehe")
setTempo(int(tempo))

#Sounds (filemedia)
fitMedia(JWOLF_COTG_THEME_BASS_BRIDGE, 1, 1, 5)
fitMedia(JWOLF_COTG_THEME_BASS_CHORUS, 1, 5, 12)
fitMedia(JWOLF_COTG_THEME_BASS_VERSE, 2, 4, 12)
fitMedia(JWOLF_COTG_THEME_DRUMBEAT, 3, 5, 12)
fitMedia(Y02_BASS_1, 4, 6, 10)
fitMedia(RD_FUTURE_DUBSTEP_MAINBEAT_3, 2, 10, 12)
fitMedia(ZAIN047_DRUMSHITZAIN, 5, 10, 12)
fitMedia(ZAIN047_DRUMSHITZAIN, 4, 12, 14)
fitMedia(JWOLF_COTG_VOX_MISC_CHAOS_2, 7, 12, 14)

#Effects
setEffect(1, VOLUME, GAIN, -40, 1, 5, 5)

#the code is mine!!! i dont like the music that i did but its whatever i can always make more later.
