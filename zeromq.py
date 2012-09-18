try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install -b $VIRTUAL_ENV/build/build-shrinkwrap shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup


version = '2.2.0'

setup(
    name='zeromq',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer='autoconf',
    shrinkwrap_source_url='http://download.zeromq.org/zeromq-%s.tar.gz' % version,
    cmdclass={'install': ShrinkwrapInstall},
)
