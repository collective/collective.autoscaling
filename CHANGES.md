# Changelog

<!-- towncrier release notes start -->

## 2.0.0 (unreleased)


- Breaking: replace the `pkg_resources` namespace of `collective` with a
  PEP 420 native namespace. Support Plone 6.1 and 6.2 only, on Python 3.10
  to 3.13. Use 1.x for Plone 4.3 to 6.0.
  [remdub]

- Import `IPloneSiteRoot`, `INonInstallable` and `get_installer` from
  `plone.base` instead of the aliases Plone 6.2 deprecates, and use
  `plone.testing.zope` in the test layers.
  [remdub]

- Include the CMFCore permissions in `configure.zcml`, so the package also
  loads when it is included before Plone (`zcml_package_includes`).
  [remdub]

- Run the robot scenarios on the Plone 6.2 classic UI.
  [remdub]

- Configure the package with plone.meta 2.12.0 (test matrix on Plone 6.2.3
  and 6.1), move its metadata to `pyproject.toml`, convert the documentation
  to Markdown and run the development environment on Plone 6.2.3 with uv
  instead of buildout.
  [remdub]

- Fix typos in french translations
  [remdub]


## 1.2 (2022-02-21)


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


## 1.1.2 (2019-01-15)


- Handle special cases when we don't get a request at ObjectAddedEvent
  (example: when an object is added at Zope startup)
  [laulaz]

- Remove useless dependency on CMFDefault (#5)
  [laulaz]


## 1.1.1 (2016-07-28)


- Pin plone.api to avoid any errors (#2)
  [laulaz]

- Add Portuguese translation
  [laulaz]


## 1.1 (2016-04-13)


- Remove dependency on plone.app.imagecropping (#1)
  [laulaz]

- Translations cleanup
  [laulaz]


## 1.0 (2016-04-11)


- Initial release.
  [laulaz]
