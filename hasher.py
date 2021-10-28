#!/usr/bin/env python3
import PySimpleGUI as sg
import hashlib




layout=[[sg.Titlebar("Verify downloads")],
          [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse(key="-IN-")],
          [sg.Text("Paste HASH: "), sg.InputText("",key="-PHASH-")],
          [sg.Button('VERIFY'),  sg.Button('CLOSE APP')],
          [sg.HorizontalSeparator(color='#RRGGBB')],
          [sg.Text("", size=(80, 1), key='-LISTBOX-'),sg.Text("", key='-V-')],
          [sg.Text("", size=(80, 1), key='-LISTBOX2-'),sg.Text("", key='-V1-')],
          [sg.Text("", size=(80, 1), key='-LISTBOX3-'),sg.Text("", key='-V2-')],
          [sg.Text("", size=(80, 1), key='-LISTBOX4-'),sg.Text("", key='-V3-')],
          [sg.HorizontalSeparator(color='#RRGGBB')]]

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
            window.Element('-V-').update("- - -  SHA256 NO MATCH - - -")
            window.FindElement('-PHASH-').Update('')
        else:
            window.Element('-LISTBOX-').update([file_hash.hexdigest()])
            window.Element('-V-').update("- - - SHA256 VERIFIED!")
            window.FindElement('-PHASH-').Update('')
            event = ''
            
        
        
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
            window.Element('-V1-').update("- - -  SHA1 NO MATCH - - -")
            window.FindElement('-PHASH-').Update('')
        else:
            window.Element('-LISTBOX2-').update([file_hash.hexdigest()])
            window.Element('-V1-').update("- - - SHA1 VERIFIED!")
            window.FindElement('-PHASH-').Update('')
            event = ''
        
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
            window.Element('-V2-').update("- - -  MD5 NO MATCH - - -")
            window.FindElement('-PHASH-').Update('')
            
        else:
            
            window.Element('-LISTBOX3-').update([file_hash.hexdigest()])          
            window.Element('-V2-').update("- - - MD5 VERIFIED!")    
            window.FindElement('-PHASH-').Update('')
            event = ''
        
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
            window.Element('-V3-').update("- - -  SHA3_256 NO MATCH - - -")
            window.FindElement('-PHASH-').Update('')
                    
        else:
                    
            window.Element('-LISTBOX4-').update([file_hash.hexdigest()])          
            window.Element('-V3-').update("- - - SHA3_256 VERIFIED!")    
            window.FindElement('-PHASH-').Update('')
            event = ''        
    
    
    if event in (sg.WIN_CLOSED, 'CLOSE APP'):
        break    

window.close()
