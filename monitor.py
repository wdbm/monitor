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
version = "2016-07-01T2027Z"
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

    log.info("")

    response = ""
    while response is not None:
        response = propyte.get_input_time_limited(
            prompt  = "Enter some text to restart the interaction loop: ",
            timeout = 604800 # 1 week
        )
        """
        |human time representation|time in seconds|
        |-------------------------|---------------|
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

    log.info("start non-response procedures")

    # e-mails

    for index, message in enumerate(payload.messages):

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

    log.info("goodbye")

    program.terminate()

if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--version"]:
        print(version)
        exit()
    main(options)
