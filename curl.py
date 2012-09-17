try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup


version = '7.27.0'

setup(
    name='curl',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer='autoconf',
    shrinkwrap_source_url='http://curl.haxx.se/download/curl-%s.tar.bz2' % version,
    cmdclass={'install': ShrinkwrapInstall},
)
