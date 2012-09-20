try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install -b $VIRTUAL_ENV/build/build-shrinkwrap shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup
import os

version = '1.51.0'
version_alt = version.replace('.', '_')
source_url = 'http://sourceforge.net/projects/boost/files/boost/%s/boost_%s.tar.bz2' % (version, version_alt)

def installer(inst):
    inst.download_and_unpack_tarball(source_url)
    # Remove .tar and .gz
    basename, ext = os.path.splitext(os.path.basename(source_url))
    basename, ext = os.path.splitext(basename)
    inst.build_dir = basename

    os.chdir(inst.build_dir)
    inst.shell('./bootstrap.sh --prefix=' + inst.virtualenv)
    inst.shell('./b2 install')

setup(
    name='boost',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer=installer,
    cmdclass={'install': ShrinkwrapInstall},
)
