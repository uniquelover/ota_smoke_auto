import virtkey
from time import sleep



def send_tab_key():

    v = virtkey.virtkey()
    sleep(3)
    print('click tab key one time')
    v.press_keysym(65289) 
    v.release_keysym(65289) 
    print('end to click')
    


# def send_space_key():

#     v = virtkey.virtkey()
#     v.press_keysym(65289) 
#     v.release_keysym(65289) 



if __name__ == "__main__":

	send_tab_key()