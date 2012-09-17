from setuptools import setup
try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    ShrinkwrapInstall = object
import os
import platform

class Install(ShrinkwrapInstall):
    version = '4.9.5.p01'
    source_url = 'https://bitbucket.org/seibert/g4py#geant4.9.5.p01'

    def run(self):
        # Get source and unpack to $VIRTUAL_ENV/src
        os.chdir(self.src_dir)
        self.shell('hg clone ' + self.source_url)
        os.chdir('g4py')
        os.environ['CLHEP_BASE_DIR'] = self.virtualenv
        system = platform.system()
        bits = platform.architecture()[0]
        
        if system == 'Linux' and bits == '64bit':
            platform_string = 'linux64'
        elif system == 'Linux':
            platform_string = 'linux'
        elif system == 'Darwin':
            platform_string = 'macosx'

        python_version = '.'.join(platform.python_version_tuple()[:2])
        config_cmd = './configure %s --prefix=%s --with-g4-incdir=%s --with-g4-libdir=%s --libdir=%s --with-python-incdir=%s --with-python-libdir=%s --with-boost-incdir=%s --with-boost-libdir=%s' % \
            (platform_string, 
             self.virtualenv,
             os.path.join(self.virtualenv, 'include', 'Geant4'), 
             os.path.join(self.virtualenv, 'lib'),
             os.path.join(self.virtualenv, 'lib', 'python'+python_version, 'site-packages'),
             os.path.join(self.virtualenv, 'include', 'python'+python_version),
             self.python_libdir,
             os.path.join(self.virtualenv, 'include'),
             os.path.join(self.virtualenv, 'lib'))
        self.shell(config_cmd)
        self.make(extra_opts=['install'])


setup(
    name='g4py_chroma',
    version=Install.version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    install_requires=['shrinkwrap'],
    cmdclass={'install': Install},
)
