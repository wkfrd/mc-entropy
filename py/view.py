import web
import db
import config

# t as in temp?
t_globals = dict (
    datestr = web.datestr,
)

render = web.template.render('~/Documents/prog/mc-entropy/py/templates/', base='templates/base', cache = config.cache, globals = t_globals)
render._keywords['globals']['render'] = render

def listing(**k):
    l = db.listing(**k)
    return render.listing(l)
