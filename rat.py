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

def installer(self):
    # Get source and unpack to $VIRTUAL_ENV/src
    os.chdir(self.src_dir)
    self.shell('svn co ' + source_url)
    os.chdir('rat')

    config_cmd = './configure'
    self.shell(config_cmd)

    # Install environment file to be used in future calls
    env_contents = 'source %s\n' % os.path.join(self.src_dir, 'rat', 'env.sh')
    self.install_env('rat.sh', contents=env_contents)

    self.shell('scons -j%d' % self.ncpu)


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
