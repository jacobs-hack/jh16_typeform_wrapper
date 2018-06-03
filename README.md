# typeform_appviz
This is a utility to send invititations for JacobsHack. It makes use of:

* the `typeform` API to manage applications
* the `sendgrid` API to send emails to participants
* Django Admin as UI to accept or reject applications

**WARNING:** This is a complete and utter hack, do not use unless there is no other solution. 

Please run on a test dataset before doing anything, or you may mess up and make JacobsHack seem unprofessional. 
**Repeat:** Do not use live data on the first try. 

Last year, typeform [did some weird stuff with their API](https://twitter.com/thunderboltsid/status/779791930783834112) and it probably has changed again. 
None of this may be working. 

NOTE: Replace typeform_viz.settings.EMAIL_HOST_PASSWORD and typeform_viz.settings.SECRET_KEY with real keys


## Installation & Setup
It is recommended to run in a `virtualenv`. Then do the normal thing of:

```bash
# Install deps
pip install -r requirements.txt

# Migrations (if there are any)
python manage.py migrate

# Create a user account to login
python manage.py createsuperuser
```

## Step 1: Importing applications from typeform

* Update API key and form ID in https://github.com/thunderboltsid/typeform_appviz/blob/master/populate.py#L11-L12
* update field names in https://github.com/thunderboltsid/typeform_appviz/blob/master/typeform_viz/models.py#L3-L28
* run ```python populate.py```
* repeat this step every time you want to re-read data from typeform. Existing users will not be touched. 

## Step 2: Accepting people
* run a django instance with ```python manage.py runserver```
* navigate to `http://localhost:8080/admin`
* set the `accepted` to `yes` for all applications that you want to accept

## Step 3: Send emails
* In the appropriate script, edit the sendmail api key:
  * https://github.com/thunderboltsid/typeform_appviz/blob/master/send_hosting_email.py#L18
  * https://github.com/thunderboltsid/typeform_appviz/blob/master/send_slack_invite.py#L22
  * https://github.com/thunderboltsid/typeform_appviz/blob/master/send_hosting_email.py#L18
* Update the email text in the appropriate script
* Run the script

## Step 4: Generate CSV files
* run one of the scripts
  * https://github.com/thunderboltsid/typeform_appviz/blob/master/prepare_profiles.py
  * https://github.com/thunderboltsid/typeform_appviz/blob/master/participants%20coming.py
