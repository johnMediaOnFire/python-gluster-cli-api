#!/usr/bin/env python

import gluster

gluster.print_json(gluster.peer.status())

gluster.print_json(gluster.volume.list())
gluster.print_json(gluster.volume.status())
gluster.print_json(gluster.volume.info())

gluster.print_json(gluster.snapshot.list())
gluster.print_json(gluster.snapshot.status())
gluster.print_json(gluster.snapshot.info())


volumes = [ volume for volume in gluster.volume.list()['cliOutput']['volList']['volume'] ]

for m in volumes:
  gluster.print_json(gluster.volume.status(m))

for m in volumes:
  gluster.print_json(gluster.snapshot.status(m))
