#!/usr/bin/env python3
import PySimpleGUI as sg
import hashlib


left_col = sg.Frame('Choose the downloaded file:',[[sg.Input(), sg.FileBrowse(key="-IN-")],[sg.Text("Paste HASH: "), sg.InputText("",key="-PHASH-")],[sg.Button('VERIFY'),
                                                                                                                                                      sg.Button('CLOSE APP')],[sg.Text("0%"),sg.ProgressBar(100,size=(50,5),style='clam',key="-PBAR-",bar_color=('yellow','black')),sg.Text("100%")]])

right_col = sg.Frame('Verification results',[[sg.HorizontalSeparator(color='#RRGGBB')],
                [sg.Text("", size=(80, 1), key='-LISTBOX-'),sg.Text("", key='-V-')],
                [sg.Text("", size=(80, 1), key='-LISTBOX2-'),sg.Text("", key='-V1-')],
                [sg.Text("", size=(80, 1), key='-LISTBOX3-'),sg.Text("", key='-V2-')],
                [sg.Text("", size=(80, 1), key='-LISTBOX4-'),sg.Text("", key='-V3-')],
                [sg.Text("", size=(80, 1), key='-LISTBOX5-'),sg.Text("", key='-V4-')],
                [sg.HorizontalSeparator(color='#RRGGBB')]])

layout = [[sg.Titlebar('HASH Verify')],
    [sg.Text('HASH-Verify')],
        [left_col, sg.VerticalSeparator(), right_col]]

          

window = sg.Window('RHV - RinzlerHashVerify', layout)



while True:
    event, values = window.read()

   
    if event == 'VERIFY':
        # If OK
        
        
        file=values["-IN-"]
        BLOCK_SIZE = 65536 # The size of each read from the file
        
        file_hash = hashlib.sha256() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f: # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        phash=values['-PHASH-']   
        if phash!=file_hash.hexdigest():
            window['-V-'].update("- - -  SHA256 NO MATCH - - -")
            window['-PHASH-'].Update('')
            window['-PBAR-'].update('20')
        else:
            window['-LISTBOX-'].update([file_hash.hexdigest()])
            window['-V-'].update("- - - SHA256 VERIFIED!")
            window['-PHASH-'].Update('')
            event = ''
            window['-PBAR-'].update('20')
            
        
        
        file=values["-IN-"]
        BLOCK_SIZE = 65536 # The size of each read from the file
        
        file_hash = hashlib.sha1() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f: # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        phash=values['-PHASH-']   
        if phash!=file_hash.hexdigest():
            window['-V1-'].update("- - -  SHA1 NO MATCH - - -")
            window['-PHASH-'].Update('')
            window['-PBAR-'].update('40')
        else:
            window['-LISTBOX2-'].update([file_hash.hexdigest()])
            window['-V1-'].update("- - - SHA1 VERIFIED!")
            window['-PHASH-'].Update('')
            event = ''
            window['-PBAR-'].update('40')
        
        file=values["-IN-"]
        BLOCK_SIZE = 65536 # The size of each read from the file
        
        file_hash = hashlib.md5() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f: # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        phash=values['-PHASH-']   
        if phash!=file_hash.hexdigest():
            window['-V2-'].update("- - -  MD5 NO MATCH - - -")
            window['-PHASH-'].Update('')
            window['-PBAR-'].update('60')
            
        else:
            
            window['-LISTBOX3-'].update([file_hash.hexdigest()])          
            window['-V2-'].update("- - - MD5 VERIFIED!")    
            window['-PHASH-'].Update('')
            event = ''
            window['-PBAR-'].update('60')
        
        file=values["-IN-"]
        BLOCK_SIZE = 65536 # The size of each read from the file
               
        file_hash = hashlib.sha3_256() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f: # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        phash=values['-PHASH-']   
        if phash!=file_hash.hexdigest():
            window['-V3-'].update("- - -  SHA3_256 NO MATCH - - -")
            window['-PHASH-'].Update('')
            window['-PBAR-'].update('80')
                    
        else:
                    
            window['-LISTBOX4-'].update([file_hash.hexdigest()])          
            window['-V3-'].update("- - - SHA3_256 VERIFIED!")    
            window['-PHASH-'].Update('')
            event = ''  
            window['-PBAR-'].update('80')
    
        file=values["-IN-"]
        BLOCK_SIZE = 65536 # The size of each read from the file
                   
        file_hash = hashlib.sha512() # Create the hash object, can use something other than `.sha256()` if you wish
        with open(file, 'rb') as f: # Open the file to read it's bytes
            fb = f.read(BLOCK_SIZE) # Read from the file. Take in the amount declared above
            while len(fb) > 0: # While there is still data being read from the file
                file_hash.update(fb) # Update the hash
                fb = f.read(BLOCK_SIZE) # Read the next block from the file
        phash=values['-PHASH-']   
        if phash!=file_hash.hexdigest():
            window['-V4-'].update("- - -  SHA512 NO MATCH - - -")
            window['-PHASH-'].Update('')
            window['-PBAR-'].update('100')
                        
        else:
                        
            window['-LISTBOX5-'].update([file_hash.hexdigest()])          
            window['-V4-'].update("- - - SHA512 VERIFIED!")    
            window['-PHASH-'].Update('')
            event = ''
            window['-PBAR-'].update('100')
            
    
    if event in (sg.WIN_CLOSED, 'CLOSE APP'):
        break    

window.close()
