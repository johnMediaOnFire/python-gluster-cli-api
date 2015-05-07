import gluster

def info():
  return gluster.xml(['volume', 'info'])
