try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup


version = '2012.08.22'
date = version.replace('.', '')

setup(
    name='gnu_parallel',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer='autoconf',
    shrinkwrap_source_url="http://ftp.gnu.org/gnu/parallel/parallel-%s.tar.bz2" % date,
    cmdclass={'install': ShrinkwrapInstall},
)
