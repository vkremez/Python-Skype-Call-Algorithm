'''

'''
import sys
import time
import Skype4Py
from Skype4Py import call

num = raw_input("Please dial the phone number in the format of +708123125: ")
pause = raw_input("Please enter the desired delay call time in seconds: ")

while 1==1:
    # The var will get value in OnCall handler
    CallStatus = 0

CallIsFinished = set([Skype4Py.clsFailed, Skype4Py.clsFinished, Skype4Py.clsMissed, Skype4Py.clsMissed, Skype4Py.clsRefused, Skype4Py.clsBusy, Skype4Py.clsCancelled]);

def AttachmentStatusText(status):
    return Skype4Py.Convert.AttachmentStatusToText(status)

# The below-referenced is fired up when the status of Call object has changed.
def onCall(call, status):
    global CallStatus
    CallStatus = status
    print "Call status: " + CallStatusText(status)
    if CallStatusText(status) == "Call In Progress":
        call.Finish()
        print "Time To Pause..."

# This handler is fired up when Skype attachment status changes
def OnAttach(status):
    print "API Attachment Status: " + AttachmentStatusText(status)
    if status == Skype4Py.apiAttachAvailable:
        skype.Attach()

try:
    Cmdline = num
except:
    print "Phone Number Error!"
    sys.exit()

# Create a Skype object and assign event handlers.
skype = Skype4Py.Skype()
skype.onAttachmentStatus = OnAttach
skype.OnCallStatus = onCall

# Start Skype
if not skype.Client.IsRunning:
    print "Starting Skype..."
    skype.Client.Start()

# Attaching to Skype...
print "Connecting to Skype..."
skype.Attach()
skype.PlaceCall(Cmdline)

# Checking our contact list to see if there is a contact already there.
Found = False

# Loop untill CallStatus get "call terminated" values in OnCall handler
while not CallStatus in CallIsFinished:
    pass

time.sleep(int(pause))





