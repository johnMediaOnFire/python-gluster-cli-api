Python GlusterFS CLI API
========================

## What is this?
This is a wrapper for the GlusterFS admin cli. It takes advantage of the xml output using the '--xml' flag
and returns a python dictionary of the data you need.

Currently, this library only has some of the read only functions to help with my monitoring.
This can be updated to include all functions of the CLI.


## Why was this created?
I needed a way to monitor my gluster servers and the only way I could find to get consistent and machine
parsable data out of gluster was via the CLI using the --xml flag.


### Installation
You have two options. 
 * Option 1: You can check out this repo anywhere on your gluster server and you should be able to execute ```test.py```.
 * Option 2: Check out the repo and run:

    python setup.py install

##### Usage:

    import gluster


#### Debug Methods

"Prints out the dictionary given."

    gluster.print_json(dict)


#### Get Data Methods
All of the following functions return a dictionary:

"Retrieve peer status from all servers"

    gluster.peer.status()

"Retrieve a list of gluster volumes"

    gluster.volume.list()

"Retrieve all information on all volumes"

    gluster.volume.info()

"Retrieve the status of all volumes"

    gluster.volume.status()

"Retrieve the status of a specific volume"

    gluster.volume.status('vol1')

"Retrieve a list of all snapshots"

    gluster.snapshot.list()

"Retrieve a list of snapshots of a specific volume"

    gluster.snapshot.list('vol1')

"Retrieve information about all snapshots on all volumes"

    gluster.snapshot.info()

"Retrieve information about a specific snapshot on a volume"

    gluster.snapshot.info('snap1', 'vol1')

"Retrieve the status of all snapshots"

    gluster.snapshot.status()

"Retrieve the status of a particular snapshot on a volume"

    gluster.snapshot.status('snap1', 'vol1')



#### Examples:
    status = gluster.peer.status()

    volumes = [ volume for volume in gluster.volume.list()['cliOutput']['volList']['volume'] ]
    for m in volumes:
      gluster.print_json(gluster.volume.status(m))
    for m in volumes:
      gluster.print_json(gluster.snapshot.status(m))

