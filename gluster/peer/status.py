import gluster

def status():
  return gluster.xml(['peer', 'status'])
