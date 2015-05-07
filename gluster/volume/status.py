import gluster

def status(volume_name='all'):
  return gluster.xml(['volume', 'status', volume_name])
