import time
import win32com.client

# Shell Connection
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run("notepad")
time.sleep(1)
shell.AppActivate("Notepad")

# Message
msg = "Hi, everyone"

# SendKeys
shell.SendKeys(msg)
