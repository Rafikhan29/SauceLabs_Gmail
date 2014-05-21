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
    body = "Please find the attached batch run test execution results:"
    
    msg = MIMEMultipart()
   
    recipients = ['rafikhan.p@tenxlabs.com','vijaykumar.madishetty@tenxlabs.com']

    me = 'rafikhan.p@tenxlabs.com'
    #subject = 'The number of critical tests that failed are '
    subject = 'Summary Reports of Wizard Applicaton:'
    msg['From'] = me
    msg['To'] = COMMASPACE.join(recipients)
    msg['Date'] = formatdate(localtime = True)

    try:
        for arg in argv[1:]:       
            reportdir = arg
            part = MIMEBase('application', "octet-stream")
            print "Attaching the report in directory " + reportdir
            part.set_payload(open(reportdir+'results.zip', "r").read())
            Encoders.encode_base64(part)
            attachment = 'attachment; filename=' + reportdir+'results.zip'
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






