#!/usr/bin/env python
import gluster

if __name__ == '__main__':

  ret = gluster.peer.status()

  non_connected_peers = []

  for peer in ret['cliOutput']['peerStatus']['peer']:
    if not peer['connected']:
       non_connected_peers.append(peer['hostname'])
