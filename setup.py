from distutils.core import setup

setup(name='python-gluster-cli-api',
        version='0.1',
        package_dir={'gluster': 'gluster'},
        packages=[
            'gluster',
            'gluster.peer',
            'gluster.volume',
            'gluster.snapshot',
            ],
        )
