import imaplib
import email
import os
import Mailconf

svdir = '/Documents/Amazon/mailattach/'

print 'Starting Mail Check'
print 'Begin set up info'
print 'Server setup'
mail=imaplib.IMAP4_SSL(Mailconf.server, 993)

print 'Begin login user'
mail.login(Mailconf.login,Mailconf.pw)

print 'Select Mailbox'
mail.select("Inbox")
print 'Imap stuff begins'

while True:
    imap = imaplib.IMAP4_SSL(Mailconf.server)
    r, d = imap.login(Mailconf.login, Mailconf.pw)
    assert r == 'OK', 'login failed'
    try:
        print 'HELLOWORLD'
    # do things with imap
    except imap.abort, e:
        continue
    imap.logout()
    break

print 'Initial setup complete'
print 'Starting Search'

typ, msgs = mail.search(None, '(SUBJECT "Test")')
msgs = msgs[0].split()

print 'End search'

for emailid in msgs:
    resp, data = mail.fetch(emailid, "(RFC822)")
    email_body = data[0][1] 
    m = email.message_from_string(email_body)
    print 'Found ID'

    if m.get_content_maintype() != 'multipart':
        continue

    for part in m.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename=part.get_filename()
        if filename is not None:
            sv_path = os.path.join(svdir, filename)
            if not os.path.isfile(sv_path):
                print sv_path       
                fp = open(sv_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
