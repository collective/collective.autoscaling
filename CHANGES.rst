Changelog
=========


1.2 (2022-02-21)
----------------

- Fix resize-images view that was saving nothing because of CSRF protection
  [laulaz]

- Add support for Python 3 / Plone 6
  [marclava, laulaz]

- Add new JPEG Quality setting
  [marclava]

- Improve resizing code
  [marclava]

- Add uninstall profile
  [laulaz]


1.1.2 (2019-01-15)
------------------

- Handle special cases when we don't get a request at ObjectAddedEvent
  (example : when an object is added at Zope startup)
  [laulaz]

- Remove useless dependency on CMFDefault (#5)
  [laulaz]


1.1.1 (2016-07-28)
------------------

- Pin plone.api to avoid any errors (#2)
  [laulaz]

- Add Portuguese translation
  [laulaz]


1.1 (2016-04-13)
----------------

- Remove dependency on plone.app.imagecropping (#1)
  [laulaz]

- Translations cleanup
  [laulaz]


1.0 (2016-04-11)
----------------

- Initial release.
  [laulaz]
