#!/usr/bin/python
import gluster

if __name__ == '__main__':
  status = gluster.peer.status()         # retrieve peer status from all servers
  volumes = gluster.volume.info()         # retrieve all volumes on this server

  # are all the peers connected?
  for key, value in status['host'].items():
    for i in value['state'].items():
      print i
      if i[1] not in ['Peer in Cluster (Connected)']:
        print i[0] + ' ' + i[1]

  # are all the volumes running?
  for key, value in volumes.items():
    if value['status'] not in ['Created', 'Started']:
      print key + ' is ' + value['status']
