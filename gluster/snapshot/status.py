import gluster

# be aware https://bugzilla.redhat.com/show_bug.cgi?id=1218732
def status(snap_name = None, volume_name = None):
  if snap_name and volume_name:
    return gluster.xml(['snapshot', 'status', snap_name, volume_name])
  else:
    return gluster.xml(['snapshot', 'status'])
