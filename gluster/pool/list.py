import gluster

def list():
  return gluster.xml(['pool', 'list'])
