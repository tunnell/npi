from setuptools import setup
try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    ShrinkwrapInstall = object
import os

class Geant4Install(ShrinkwrapInstall):
    version = '4.9.5.p01'
    source_url = 'http://geant4.cern.ch/support/source/geant%s.tar.gz' % version

    def run(self):
        # Get source and unpack to $VIRTUAL_ENV/src
        self.download_and_unpack_tarball(self.source_url, to_src_dir=True)

        # Create build directory
        os.chdir(self.src_dir)
        g4src_dir = os.path.realpath('geant' + self.version)
        build_dir = g4src_dir + '-build'
        if not os.path.exists(build_dir):
            os.mkdir(build_dir)
        os.chdir(build_dir)

        # Configure and compile in place
        config_cmd = 'cmake -DCMAKE_INSTALL_PREFIX=%s -DGEANT4_INSTALL_DATA=ON -DGEANT4_USE_RAYTRACER_X11=ON %s' % (self.virtualenv, g4src_dir)
        self.shell(config_cmd)

        self.make(extra_opts=['install'])

        # Setup environment
        env_contents = 'source %s' % os.path.join(self.virtualenv, 'bin', 'geant4.sh')
        self.install_env('geant4.sh', contents=env_contents)

setup(
    name='geant4',
    version=Geant4Install.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': Geant4Install},
)
