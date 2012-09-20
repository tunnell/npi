try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install -b $VIRTUAL_ENV/build/build-shrinkwrap shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup
from distutils.version import LooseVersion

version = '7.27.0'

def skip(inst):
    try:
        output = inst.cmd_output('curl-config --version')
        name, version_str = output.split()
        system_version = LooseVersion(version_str)
        min_version = LooseVersion('7.26.0')
        if system_version > min_version:
            return True # Don't install
        else:
            return False # Version too old
    except:
        return False # install package if anything went wrong

setup(
    name='curl-check',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer='autoconf',
    shrinkwrap_skip=skip,
    shrinkwrap_source_url='http://curl.haxx.se/download/curl-%s.tar.bz2' % version,
    cmdclass={'install': ShrinkwrapInstall},
)
