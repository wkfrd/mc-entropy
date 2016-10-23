import config

def listing(**k):
  return config.mc_database.select('items', **k)
