from setuptools import setup
try:
    from shrinkwrap.install import AutoconfInstall
except ImportError:
    AutoconfInstall = object


class Install(AutoconfInstall):
    version = '7.27.0'
    source_url = 'http://curl.haxx.se/download/curl-%s.tar.bz2' % version

setup(
    name='curl',
    version=Install.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': Install},
)
