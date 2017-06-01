from setuptools import setup, find_packages


version = '2.0.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.scriptedredirect',
      version=version,
      description="Write redirects in Python for Plone CMS",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=["Environment :: Web Environment",
                   "Framework :: Plone",
                   "Framework :: Plone :: 4.3",
                   "Framework :: Plone :: 5.0",
                   "Framework :: Plone :: 5.1",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.7",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
      keywords='Plone Redirect Scripting Links Sysadmin',
      author='Mikko Ohtamaa',
      author_email='mikko@opensourcehacker.com',
      url='https://github.com/collective/collective.scriptedredirect',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
