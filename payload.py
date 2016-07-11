"""
################################################################################
#                                                                              #
# payload example                                                              #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a monitor payload example.                                   #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

name    = "payload"
version = "2016-07-11T1828Z"

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

global messages_warning
messages_warning = []

global messages
messages = []

################################################################################

message = MIMEMultipart("alternative")
message["Subject"] = "timeout: automatic warning message from monitor"
message["From"]    = "monitor@localhost"
message["To"]      = "user@home.pr0"
text = """
Hi there

This is an automatic warning message. The interaction time limit is near. Please interact with monitor.

monitor
"""
message.attach(MIMEText(text, "plain"))
messages_warning.append(message)

################################################################################

message = MIMEMultipart("alternative")
message["Subject"] = "timeout: automatic message from monitor"
message["From"]    = "monitor@localhost"
message["To"]      = "mulder@fbi.g0v"
text = """
Hi there

This is an automatic message that is designed to be sent should certain
conditions arise; they have. Please standby for further messages.

monitor
"""
message.attach(MIMEText(text, "plain"))
messages.append(message)

################################################################################

message = MIMEMultipart("alternative")
message["Subject"] = "monitor: instructions"
message["From"]    = "monitor@localhost"
message["To"]      = "scully@fbi.g0v"
text = """
Please do the following things:

- a
- b
- c

monitor
"""
message.attach(MIMEText(text, "plain"))
messages.append(message)

################################################################################
