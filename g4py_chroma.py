try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install -b $VIRTUAL_ENV/build/build-shrinkwrap shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup
import os
import platform


version = '4.9.5.p01'
source_url = 'https://bitbucket.org/seibert/g4py#geant4.9.5.p01'

def installer(inst):
    # Get source and unpack to $VIRTUAL_ENV/src
    os.chdir(inst.src_dir)
    inst.shell('hg clone ' + source_url)
    os.chdir('g4py')
    os.environ['CLHEP_BASE_DIR'] = inst.virtualenv
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
         inst.virtualenv,
         os.path.join(inst.virtualenv, 'include', 'Geant4'), 
         os.path.join(inst.virtualenv, 'lib'),
         os.path.join(inst.virtualenv, 'lib', 'python'+python_version, 'site-packages'),
         os.path.join(inst.virtualenv, 'include', 'python'+python_version),
         inst.python_libdir,
         os.path.join(inst.virtualenv, 'include'),
         os.path.join(inst.virtualenv, 'lib'))
    inst.shell(config_cmd)
    inst.make(extra_opts=['install'])


setup(
    name='g4py_chroma',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    shrinkwrap_installer=installer,
    shrinkwrap_requires=['boost', 'geant4'],
    cmdclass={'install': ShrinkwrapInstall},
)
