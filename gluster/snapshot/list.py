import gluster

def list(volume_name = None):
  if volume_name:
    return gluster.xml(['snapshot', 'list', volume_name])
  else:
    return gluster.xml(['snapshot', 'list'])

