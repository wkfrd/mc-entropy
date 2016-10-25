import web
import view, config
from view import render


import index

urls = (
  '/', 'index',
  '/register', 'register'
  '/login', 'login'
  '/profile', 'profile'
  '/demo', 'demo'
)

class index:
  def GET(self):
    return render.index()

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.internalerror = web.debugerror
  app.run()
