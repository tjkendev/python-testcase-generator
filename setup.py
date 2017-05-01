from setuptools import setup, find_packages
import python_testcase_generator.setting as setting

setup(
    name='python-testcase-generator',
    description='A testcase generator that can write testcase using Python expression',
    author = 'yaketake08',
    author_email = 'jake-basu@hotmail.co.jp',
    version = setting.version,
    packages = ['python_testcase_generator'],
    install_requires = [],
    entry_points = {
        'console_scripts': [
            'python-testcase-generator=python_testcase_generator.main:entry',
            'pytcgen=python_testcase_generator.main:entry'
        ]
    },
    url = "https://github.com/tjkendev/python-testcase-generator",
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    test_suite = 'test',
)
