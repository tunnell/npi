from setuptools import setup
try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    ShrinkwrapInstall = object
import os

class Install(ShrinkwrapInstall):
    version = '1.51.0'
    version_alt = version.replace('.', '_')
    source_url = 'http://sourceforge.net/projects/boost/files/boost/%s/boost_%s.tar.bz2' % (version, version_alt)

    def run(self):
        self.download_and_unpack_tarball(self.source_url)
        # Remove .tar and .gz
        basename, ext = os.path.splitext(os.path.basename(self.source_url))
        basename, ext = os.path.splitext(basename)
        self.build_dir = basename

        os.chdir(self.build_dir)
        self.shell('./bootstrap.sh --prefix=' + self.virtualenv)
        self.shell('./b2 install')

setup(
    name='boost',
    version=Install.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': Install},
)
