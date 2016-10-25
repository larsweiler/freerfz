from setuptools import setup

setup(
        name='freerfz_dl',
        version='1.5',
        py_modules=['freerfz_dl'],
        install_requires=[
            'click',
        ],
        entry_points='''
            [console_scripts]
            freerfz_dl=freerfz_dl:freerfz
        ''',
)
