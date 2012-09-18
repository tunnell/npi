try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install -b $VIRTUAL_ENV/build/build-shrinkwrap shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup
import os


version = '2.8.9'
source_url = "http://www.cmake.org/files/v2.8/cmake-%s.tar.gz" % version

def installer(self):
    self.download_and_unpack_tarball(source_url)
    # Remove .tar and .gz
    basename, ext = os.path.splitext(os.path.basename(source_url))
    basename, ext = os.path.splitext(basename)
    self.build_dir = basename

    os.chdir(self.build_dir)
    self.shell('./bootstrap --prefix=' + self.virtualenv)
    self.make()
    self.make(extra_opts=['install'])

setup(
    name='cmake',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer=installer,
    cmdclass={'install': ShrinkwrapInstall},
)
