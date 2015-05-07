import os,sys
import subprocess
import json
import xmltodict
from types import ListType

class GlusterError(Exception):
    def __init__(self,value):
        self.value = value
    def _str_(self):
        return repr(self.value)

class GlusterWarning(Warning):
    def __init__(self,value):
        self.value = value
    def _str_(self):
        return repr(self.value)

if not os.geteuid()==0:
    raise GlusterError("Gluster commands require root permissions.")

def _command(args):
  out = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
  (stdout, stderr) = out.communicate()
  return stdout, stderr, out.returncode

def print_json(d):
  print(json.dumps(d, indent=2))

def _gluster_exists(gluster_path):
  return os.path.isfile(gluster_path)

def xml(args):
  assert type(args) is ListType, "args is not a list: %r" % args
  gluster_path = '/usr/sbin/gluster'
  cmd = [gluster_path]
  #TODO: check argument input, then append; else fail.
  cmd.extend(args)
  cmd.append('--xml')
  if _gluster_exists(cmd[0]):
    # Stripping because of bug: https://bugzilla.redhat.com/show_bug.cgi?id=1218732
    xml = _command(cmd)[0].strip('No snapshots present')
    xml = os.linesep.join([s for s in xml.splitlines() if s])
    return xmltodict.parse(xml)
  else:
    return -1


import peer
import volume
import snapshot
import pool
