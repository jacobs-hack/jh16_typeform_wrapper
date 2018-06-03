from django.db import models

_QUESTIONS = {
    "first_name": "textfield_28990631",
    "last_name": "textfield_28990632",
    "email": "email_28990633",
    "coming_from": "dropdown_28990634",
    "nationality": "dropdown_28990808",
    "degree": ("list_28990901_choice", "list_28990901_other"),
    "graduation": "date_28991016",
    "major": "dropdown_28991305",
    "university": "textfield_28991659",
    "_18yo": "yesno_28991894",
    "needs_reimbursement": "yesno_29001580",
    "needs_visa": "yesno_29005061",
    "github": "website_28991933",
    "devpost": "website_28991936",
    "linkedin": "website_28991941",
    "personal_site": "website_28991950",
    "first_hackathon": "yesno_28991972",
    "why_jacobshack": "textarea_29001709",
    "previous_projects": "textarea_29001343",
    "tshirt_size": "list_29001632_choice",
    "dietary_requirements": ("list_29001860_choice", "list_29001860_other"),
    "has_team": "yesno_29001866",
    "names_of_teammates": "textarea_29001868",
    "cv": "fileupload_29001894"
}


class JHAPPManager(models.Manager):
    def get_queryset(self):
        return super(JHAPPManager, self).get_queryset().all()

    def get_accepted(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                accepted=True)

    def get_not_accepted(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                accepted=False)

    def get_accepted_but_not_emailed(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                accepted=True, sentmail=False)

    def get_accepted_and_emailed(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                accepted=True, sentmail=True)

    def get_accepted_but_not_slacked(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                accepted=True, slack_invite=False)

    def get_18yos(self):
        return super(JHAPPManager, self).get_queryset().all().filter(_18yo=1)

    def get_underaged(self):
        return super(JHAPPManager, self).get_queryset().all().filter(_18yo=0)

    def get_visa_needed(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                needs_visa=1)

    def get_visa_not_needed(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                needs_visa=0)

    def get_money_needed(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                needs_reimbursement=1)

    def get_money_not_needed(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                needs_reimbursement=0)

    def get_ze_germans(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
                nationality="Germany")

    def get_le_coders(self):
        return super(JHAPPManager, self).get_queryset().all().filter(
            github != "http://")


class JHAPP(models.Model):
    apps = JHAPPManager()
    objects = models.Manager()

    first_name = models.TextField()
    last_name = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    coming_from = models.TextField()
    nationality = models.TextField()
    degree = models.TextField()
    graduation = models.TextField()
    major = models.TextField()
    university = models.TextField()
    _18yo = models.TextField()
    needs_reimbursement = models.TextField()
    needs_visa = models.TextField()
    github = models.TextField(null=True, blank=True)
    devpost = models.TextField(null=True, blank=True)
    linkedin = models.TextField(null=True, blank=True)
    personal_site = models.TextField(null=True, blank=True)
    first_hackathon = models.TextField()
    why_jacobshack = models.TextField(null=True, blank=True)
    previous_projects = models.TextField()
    tshirt_size = models.TextField()
    dietary_requirements = models.TextField(null=True, blank=True)
    has_team = models.TextField()
    names_of_teammates = models.TextField(null=True, blank=True)
    cv = models.TextField(null=True, blank=True)
    agree_to_policy = models.TextField(null=True, blank=True)
    agree_to_coc = models.TextField(null=True, blank=True)

    accepted = models.BooleanField(default=False)
    sentmail = models.BooleanField(default=False)
    slack_invite = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s <%s> %s' % (self.first_name, self.last_name, self.email,
                                  '' if not self.accepted else '✓')
