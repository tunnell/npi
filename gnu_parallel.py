from setuptools import setup
try:
    from shrinkwrap.install import AutoconfInstall
except ImportError:
    AutoconfInstall = object


class Install(AutoconfInstall):
    version = '2012.08.22'
    date = version.replace('.', '')
    source_url = "http://ftp.gnu.org/gnu/parallel/parallel-%s.tar.bz2" % date

setup(
    name='gnu_parallel',
    version=Install.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': Install},
)
