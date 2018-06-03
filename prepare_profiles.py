import os
import django
import csv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeform_viz.settings")
django.setup()
from typeform_viz.models import JHAPP

all_apps = JHAPP.objects.all()
# showed_up = JHAPP.apps.showed_up()

applicants = ["Name", "University", "Email", 'Github', 'LinkedIn',
              'Personal', 'Devpost', 'CV']
attended = ["Name", "University", "Email", 'Github', 'LinkedIn',
            'Personal', 'Devpost', 'CV']

for app in all_apps:
    applicants.append(
            ["{} {}".format(app.first_name, app.last_name), app.university,
             app.email, app.github, app.linkedin, app.personal_site,
             app.devpost, app.cv])

# for app in showed_up:
#     attended.append(
#             ["{} {}".format(app.first_name, app.last_name), app.university,
#              app.email, app.github, app.linkedin, app.personal_site,
#              app.devpost, app.cv])

with open('all_applicants.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(applicants)

# with open('all_showed_up.csv', 'w', newline='') as fp:
#     a = csv.writer(fp, delimiter=',')
#     a.writerows(accepted)
