from distutils.core import setup

setup(
    name='abqueue',
    version='0.0.1.dev1',
    description='Abaqus queue definitions',
    author='Stefano Miccoli',
    author_email='stefano.miccoli@polimi.it',
    url='https://github.com/miccoli/abqueue',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    py_modules=['mecmi', ],
)
