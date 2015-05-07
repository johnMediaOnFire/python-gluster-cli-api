import gluster

def list():
  return gluster.xml(['volume', 'list'])
