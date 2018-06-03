import os
import django
import csv


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeform_viz.settings")
django.setup()
from typeform_viz.models import JHAPP

apps = JHAPP.apps.get_accepted()

accepted = ["Name", "Nationality", "University", "Email"]

for app in apps:
    accepted.append(["{} {}".format(app.first_name, app.last_name), app.nationality, app.university, app.email])
with open('accepted_list.csv', 'w', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(accepted)
