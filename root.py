try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install -b $VIRTUAL_ENV/build/build-shrinkwrap shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
import os
from setuptools import setup


version = '5.34.01'
source_url = 'ftp://root.cern.ch/root/root_v%s.source.tar.gz' % version


def installer(inst):
    # Get source and unpack to $VIRTUAL_ENV/src
    inst.download_and_unpack_tarball(source_url, to_src_dir=True)

    # Fix source directory name
    os.chdir(inst.src_dir)
    root_dir = 'root-v' + version
    os.rename('root', root_dir)

    # Configure and compile in place
    os.chdir(root_dir)
    config_options = '--enable-minuit2 --enable-roofit --with-python-libdir=%s' % inst.python_libdir
    inst.shell('./configure ' + config_options)
    inst.make()

    # Setup environment
    env_contents = 'source %s' % os.path.join(inst.src_dir, root_dir, 'bin', 'thisroot.sh')
    inst.install_env('root.sh', contents=env_contents)


setup(
    name='root',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer=installer,
    shrinkwrap_requires=['fftw'],
    cmdclass={'install': ShrinkwrapInstall},
)
