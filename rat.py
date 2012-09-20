try:
    from shrinkwrap.install import ShrinkwrapInstall
except ImportError:
    import subprocess; subprocess.check_call('pip install -b $VIRTUAL_ENV/build/build-shrinkwrap shrinkwrap', shell=True)
    from shrinkwrap.install import ShrinkwrapInstall
from setuptools import setup
import os
import platform


version = '0.1'
source_url = 'https://deapclean.org/svn/priv/rat'

def installer(inst):
    # Get source and unpack to $VIRTUAL_ENV/src
    os.chdir(inst.src_dir)
    inst.shell('svn co ' + source_url)
    os.chdir('rat')

    config_cmd = './configure'
    inst.shell(config_cmd)

    # Install environment file to be used in future calls
    env_contents = 'source %s\n' % os.path.join(inst.src_dir, 'rat', 'env.sh')
    inst.install_env('rat.sh', contents=env_contents)

    inst.shell('scons -j%d' % inst.ncpu)


setup(
    name='deapclean-rat',
    version=version,
    author='Stan Seibert',
    author_email='stan@mtrr.org',
    setup_requires=['shrinkwrap'],
    shrinkwrap_installer=installer,
    shrinkwrap_requires=['geant4', 'root', 'curl'],
    cmdclass={'install': ShrinkwrapInstall},
)
