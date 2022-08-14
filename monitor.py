#!/usr/bin/env python
import gluster

if __name__ == '__main__':

  ret = gluster.peer.status()
  non_connected_peers = []

  if isinstance(ret['cliOutput']['peerStatus']['peer'], list):
    for peer in ret['cliOutput']['peerStatus']['peer']:
      if int(peer['connected']) != 1:
        non_connected_peers.append(peer['hostname'])
  else:
    if int(ret['cliOutput']['peerStatus']['peer']['connected']) != 1:
      non_connected_peers.append(ret['cliOutput']['peerStatus']['peer']['hostname'])

  ret = gluster.volume.info()
  non_running_volumes = []


  if isinstance(ret['cliOutput']['volInfo']['volumes']['volume'], list):
    for volume in ret['cliOutput']['volInfo']['volumes']['volume']:
      if int(volume['status']) != 1:
        non_running_volumes.append(volume['name'])
  else:
    if int(ret['cliOutput']['volInfo']['volumes']['volume']['status']) != 1:
      non_running_volumes.append(ret['cliOutput']['volInfo']['volumes']['volume']['status'])

# Output
  for peer in non_connected_peers:
    print('Peer "' + peer + '" is not connected to the pool.')

  for volume in non_running_volumes:
    print('Volume "' + volume + '" is not running.')
