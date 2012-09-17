from setuptools import setup
try:
    from shrinkwrap.install import AutoconfInstall
except ImportError:
    AutoconfInstall = object


class Install(AutoconfInstall):
    version = '3.3.2'
    source_url = 'http://www.fftw.org/fftw-%s.tar.gz' % version

setup(
    name='fftw',
    version=Install.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': Install},
)
