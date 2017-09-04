import time

class payload:
    def __init__(self):
        self.name = "startchat"
        self.description = "start a chat room with the user. both you and the user can respond"
        self.type = "applescript"
        self.id = 301

    def run(self,session,server,command):

        message = raw_input(server.h.COLOR_INFO+"[*]  "+server.h.WHITE+"Send Message> ")

        payload = """
tell application "Finder"
    activate

    set myprompt to \"""" + message + """\n\nEnter your response to this message:\"

    repeat
        try
            set d_returns to display dialog myprompt default answer "" buttons {"Send Response"} default button "Send Response" with icon path to resource "AlertNoteIcon.icns" in bundle "/System/Library/CoreServices/CoreTypes.bundle"
            set response to text returned of d_returns
            if response > "" then exit repeat
            end try
    end repeat
    try
        do shell script "echo " & quoted form of response
    end try
end tell
"""
        response = server.sendCommand("prompt",payload,self.type,session.conn)
        #display response
        print server.h.COLOR_INFO+"[*]  "+server.h.WHITE+"User Response: "+server.h.GREEN+response+server.h.WHITE

        sendAgain = raw_input(server.h.COLOR_INFO+"[*]  "+server.h.WHITE+"Would you like to reply? (Y/n) ")

        if not sendAgain:
            sendAgain = "y"
        if sendAgain.lower() != "y":
            return ""
        self.run(session,server,command)
