#! python
import sys
import getopt
import os
import smtplib
from smtplib import SMTP_SSL as SMTP
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

import sys

def main(argv):
    reportdir = ''
    print 'argv'
    print argv[1]

    body = "The test execution reports from an automated batch run are attached. \n There may be a delay before the reports are archived. \n When archived the reports will be stored in the following directories:"
    
    msg = MIMEMultipart()
   
    recipients = ['rafikhan.p@tenxlabs.com']

    me = 'rafikhan.p@tenxlabs.com'
    subject = 'The number of critical tests that failed are '
    msg['From'] = me
    msg['To'] = COMMASPACE.join(recipients)
    msg['Date'] = formatdate(localtime = True)

    try:
        for arg in argv[1:]:       
            reportdir = arg
            part = MIMEBase('application', "octet-stream")
            print "Attaching the report in directory " + reportdir
            part.set_payload(open("results\\" + reportdir + "\\report.html", "r").read())
            Encoders.encode_base64(part)
            attachment = 'attachment; filename=' + reportdir + '\\report.html'
            part.add_header('Content-Disposition', attachment)
            msg.attach(part)
            subject += ' ' + reportdir
            body += '\nportal01.prv.sjc1.fatspaniel.net/Robot-Results/' + reportdir

    except IOError:
        print "error: Can not open the directory %s" % reportdir

    # Send the message via the SDT server.

    msg['Subject'] = subject
    msg.attach(MIMEText(body))
    s = SMTP('smtp.zoho.com')
    s.login('rafikhan.p@tenxlabs.com', 'R@f!10x')
    s.sendmail(me, recipients, msg.as_string())
    s.close()
    print('The email subject is "' + msg['Subject'] +'"')

main(sys.argv)






