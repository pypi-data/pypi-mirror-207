# ms-mailbox-reader
A python package for windows which allows easy reading of email 
messages from a local mailbox. Tested with Outlook + Microsoft Exchange on a Windows 11 PC. 


### Basic Usage
```python
from datetime import datetime, timedelta
from ms_mailbox_reader.reader import MsOutlookMessageReader, MessageFilter

# Create the message reader
message_reader = MsOutlookMessageReader()

# Create a filter to limit returned messages to a max of 25, 
# those which were sent from @mydomain.com and 
# received in the last two hours
# ---
# The sender email param may not be what you expect. Sometimes it'll be a
# long OU type string. 
filter_params = MessageFilter(sender_email="@mydomain.com", 
                              received_since = (datetime.now() - timedelta(hours=2)),
                              limit=25)

# Get the message list
messages = message_reader.get_outlook_messages(filter_params)

# Do stuff with the messages
for message in messages:
    print(message.sender_name)
    print(message.body)
    print("=====================")
```