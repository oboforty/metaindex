try:
    from playsound import playsound
except:
    pass


def ding():
    try:
        playsound('modules/db_builder/ding.wav')
    except:
        print("---------------------------------------\nDONE!")
