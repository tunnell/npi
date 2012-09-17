from setuptools import setup
try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    ShrinkwrapInstall = object
import os

class Install(ShrinkwrapInstall):
    version = '2.8.9'
    source_url = "http://www.cmake.org/files/v2.8/cmake-%s.tar.gz" % version

    def run(self):
        self.download_and_unpack_tarball(self.source_url)
        # Remove .tar and .gz
        basename, ext = os.path.splitext(os.path.basename(self.source_url))
        basename, ext = os.path.splitext(basename)
        self.build_dir = basename

        os.chdir(self.build_dir)
        self.shell('./bootstrap --prefix=' + self.virtualenv)
        self.make()
        self.make(extra_opts=['install'])

setup(
    name='cmake',
    version=Install.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': Install},
)
