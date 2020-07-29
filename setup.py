from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        name='localstack-python-demo',
        version='1.0.0',
        packages=find_packages(),
        install_requires=['dataclasses', 'pytest', 'boto3'],
        author='anthony blanchflower',
        url='https://github.com/anthonyblanchflower',
        description='Demonstrating pytest and localstack',
        long_description=open('README.md').read(),
        classifiers=[
            'Environment :: MacOS X',
            'Environment :: Win32 (MS Windows)',
            'Environment :: X11 Applications',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3']
    )
