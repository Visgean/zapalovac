import setuptools

setuptools.setup(
    name='Zapalovac',
    version="0.0.1",
    description='Robot co chodi zapalovat svicky na http://www.partezlin.cz/',
    author='Visgean Skeloru',
    author_email='me@visgean.me',
    url='https://github.com/Visgean/zapalovac',
    py_modules=[
      'zapalovac'
    ],
    install_requires=[
        'pyquery'
    ],
    license='MIT License',
    zip_safe=True,
    keywords='boilerplate package',
    classifiers=['Packages']
)
