#!/usr/bin/env python

"""
################################################################################
#                                                                              #
# monitor                                                                      #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program is a monitor that performs contact actions should certain       #
# conditions, such as non-interaction, arise.                                  #
#                                                                              #
# copyright (C) 2016 William Breaden Madden                                    #
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

usage:
    program [options]

options:
    -h, --help               display help message
    --version                display version and exit
    -v, --verbose            verbose logging
    -s, --silent             silent
    -u, --username=USERNAME  username
"""
#   --payload=FILENAME       payload file [default: payload.py]

name    = "monitor"
version = "2016-07-11T1827Z"
logo    = None

import docopt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

import payload
import propyte

def main(options):

    global program
    program = propyte.Program(
        options = options,
        name    = name,
        version = version,
        logo    = logo
    )
    global log
    from propyte import log

    timeout_main    = 604800 # 1 week
    timeout_warning = 3600   # 1 hour

    log.info("")

    """
    |human time representation|time in seconds|
    |-------------------------|---------------|
    |10 minutes               |600            |
    |30 minutes               |1800           |
    |1 hour                   |3600           |
    |8 hours                  |28800          |
    |10 hours                 |36000          |
    |1 day                    |86400          |
    |2 days                   |172800         |
    |3 days                   |259200         |
    |4 days                   |345600         |
    |1 week                   |604800         |
    |1 month                  |2629740        |
    |1 year                   |31556900       |
    """

    response = ""
    while response is not None:
        response = propyte.get_input_time_limited(
            prompt  = "Enter some text to restart the interaction loop: ",
            timeout = timeout_main
        )

    log.info("\nstart warning procedures\n")

    # warning messages

    send_messages(messages = payload.messages_warning)

    log.info("")

    response = ""
    while response is not None:
        response = propyte.get_input_time_limited(
            prompt  = "WARNING: {timeout} seconds remaining -- Enter some text to restart the interaction loop (then reset monitor): ".format(
                timeout = timeout_warning
            ),
            timeout = timeout_warning
        )

    log.info("\nstart non-response procedures\n")

    # messages

    send_messages(messages = payload.messages)

    log.info("\ngoodbye\n")

    program.terminate()

def send_messages(
    messages = None
    ):

    if messages:
        for index, message in enumerate(messages):
            try:
                log.info("send message to {to}".format(
                    to = message["To"]
                ))
                server = smtplib.SMTP("localhost")
                server.sendmail(
                    message["From"],
                    message["To"],
                    message.as_string()
                )
                server.quit()
            except smtplib.SMTPException:
               print("e-mail send error")
            time.sleep(5)

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
