import web
import view, config
from view import render
from web import form

import index

urls = (
  '/', 'index',
  '/register', 'register',
  '/login', 'login',
  '/profile', 'profile',
  '/demo', 'demo',
  '/entropy', 'entropy',
)

### Templates
t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)

# This may not be the best place for this. Maybe in forms.py or something?
# Put the button in the form. I'm totally putting this in a separate file.
# Along with the register button, which I'm assuming is slightly different.

registration_form = form.Form (
    form.Textbox("Email"),
    form.Password("Password", form.notnull),
    form.Password("Again", form.notnull),
    form.Button("submit", type="submit"),
    validators = [form.Validator("Passwords didn't match",lambda x:x.Password == x.Again),
                  form.Validator('Must be more than five characters.', lambda x:len(x) > 5)])

class index:
    def GET(self):
        return render.index()

class register:
    def GET(self):
        reg_form = registration_form()
        return render.register(reg_form)

    def POST(self):
        reg_form = registration_form()
        if not reg_form.validates():
            return render.register(reg_form)
        else:
            web.insert('user_table', **reg_form.d)
            return render.index()

class login:
    def GET(self):
        return render.login()

class profile:
    def GET(self):
        return render.profile()

class demo:
    def GET(self):
        return render.demo()

class entropy:
    def GET(self):
        return render.entropy()

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.internalerror = web.debugerror
  app.run()
