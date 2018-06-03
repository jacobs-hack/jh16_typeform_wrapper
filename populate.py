if __name__ == '__main__':
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeform_viz.settings")

    import django
    django.setup()

    from typeform_viz.models import JHAPP, _QUESTIONS
    from typeform_wrapper import lib

    tf = lib.TypeForm(api_key="TYPEFORM_API_KEY")
    tf.use_form(form_id="TYPEFORM_FORM_ID")
    form = tf.form
    complete_entries = form.complete_entries()

    for entry in complete_entries:
        ans = entry["answers"]

        def getfield(name):
            fieldname = _QUESTIONS[name]

            try:
                if isinstance(fieldname, tuple):
                    try:
                        retval = ans[fieldname[0]]
                    except KeyError:
                        retval = None

                    if retval is None:
                        retval = ans[fieldname[1]]
                else:
                    retval = ans[fieldname]
            except KeyError:
                retval = None

            return retval if retval is not None else ''

        proper_field = {}

        for field in _QUESTIONS.keys():
            proper_field[field] = getfield(field)

        if JHAPP.objects.filter(email=proper_field["email"]).count() == 0:
            JHAPP.objects.create(**proper_field)
            print("Populated user %s" % (proper_field["email"]))
        else:
            print("User %s already exists" % (proper_field["email"]))