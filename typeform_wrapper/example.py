import lib


class Application(object):
    pass


tf = lib.TypeForm(api_key="TYPEFORM_API_KEY")
tf.use_form(form_id="TYPEFORM_FORM_ID")
form = tf.form
foo = form.complete_entries()
ques = form.get_questions()

import pdb; pdb.set_trace()
