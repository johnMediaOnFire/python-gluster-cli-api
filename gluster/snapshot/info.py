import gluster

def info(snapname = None, volume_name = None):
  if snapname and volume_name:
    return gluster.xml(['snapshot', 'info', snapname, volume_name])
  else:
    return gluster.xml(['snapshot', 'info'])
