# Emailer
Email and SMS alerts using google cloud

# Install
1. Fork/clone this repository
2. Create a new google cloud project
3. Update app.yaml to reflect your apps name
3. Mirror your repository or start new repository by going to <code>console -> development -> repositories</code> in Google cloud.
4. Navigate to https://[your_emailer_app].appspot.com/_ah/api/explorer to test your API

# Send Email
Google API (recommended): <br /><code>emailer.rest.send_email(args)</code><br /><br />
Request: <br /><code>POST https://[your_emailer_app].appspot.com/_ah/api/emailer/v1/send-email?message=Read+this+email+message.&recipient=someonesemail%40mail.com&subject=Urgent+Message</code>
