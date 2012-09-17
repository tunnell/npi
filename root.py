from setuptools import setup
try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    ShrinkwrapInstall = object
import os

class RootInstall(ShrinkwrapInstall):
    version = '5.34.01'
    source_url = 'ftp://root.cern.ch/root/root_v%s.source.tar.gz' % version

    def run(self):
        # Get source and unpack to $VIRTUAL_ENV/src
        self.download_and_unpack_tarball(self.source_url, to_src_dir=True)

        # Fix source directory name
        os.chdir(self.src_dir)
        root_dir = 'root-v'+self.version
        os.rename('root', root_dir)

        # Configure and compile in place
        os.chdir(root_dir)
        config_options = '--enable-minuit2 --enable-roofit --with-python-libdir=%s' % self.python_libdir
        self.shell('./configure ' + config_options)
        self.make()

        # Setup environment
        env_contents = 'source %s' % os.path.join(self.src_dir, root_dir, 'bin', 'thisroot.sh')
        self.install_env('root.sh', contents=env_contents)

setup(
    name='root',
    version=RootInstall.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': RootInstall},
)
