import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("akromabdumannopov815@gmail.com", 'u r m x h f e w b l g c n k d t')
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("akromabdumannopov815@gmail.com", "akromabdumannopov802@gmail.com", message)
# terminating the session
s.quit()


import smtplib
# list of email_id to send the mail
li = ["akromabdumannopov802@gmail.com","akromabdumannopov802@gmail.com"]
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("akromabdumannopov815@gmail.com", 'u r m x h f e w b l g c n k d t')
    message = "Message_you_need_to_send"
    s.sendmail("akromabdumannopov815@gmail.com", dest, message)
    s.quit()