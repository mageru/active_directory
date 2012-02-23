from distutils.core import setup

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Environment :: Win32 (MS Windows)',
  'Intended Audience :: Developers',
  'Intended Audience :: System Administrators',
  'Programming Language :: Python :: 2',
  'License :: PSF',
  'Natural Language :: English',
  'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
  'Topic :: System :: Systems Administration'
]

setup (
  name = "active_directory",
  version = "0.7-2.x",
  description = "Active Directory",
  long_description = open ("readme.txt").read (),
  author = "Tim Golden",
  author_email = "mail@timgolden.me.uk",
  url = "http://timgolden.me.uk/python/active_directory.html",
  license = "http://www.opensource.org/licenses/mit-license.php",
  py_modules = ["active_directory"]
)

