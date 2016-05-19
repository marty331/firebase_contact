# firebase_contact
What you will need -
A firebase account
An alterlative gmail account (less secure login enabled) and credentials

To use this method you will need an email address that is not your primary and that you are not storing valuable data.  Enable 'less secure login' for this account, which will allow you login with a plain text password.

The script is self explainatory and simple.  It reads the /contacts node on your firebase url and then gathers the data and marks the node as read (to prevent duplicate email notifications), then sends an email to alert you that a new customer would like more information.

I have this script running on spare raspberry pi, it runs every 5 minutes so if a new customer enters their contact information then I am notified within 5 minutes or less.
