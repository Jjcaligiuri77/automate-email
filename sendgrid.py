import os
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail

sg = sendgrid.SendGridAPIClient(
    apikey=os.environ.get("SENDGRID_API_KEY")
)
from_email = Email("my@gmail.com")
to_email = Email("your@gmail.com")
subject = "A test email from Sendgrid"
content = Content(
    "text/plain", "Here's a test email sent through Python"
)
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())

# The statements below can be included for debugging purposes
print(response.status_code)
print(response.body)
print(response.headers)

#In order to run-> sign up for a sendgrid account, request API key for user validation, add your key by typing setx SENDGRID_API_KEY "YOUR_API_KEY" in Command Prompt (to store this API key permanently) or set SENDGRID_API_KEY YOUR_API_KEY to store it only for the current client session