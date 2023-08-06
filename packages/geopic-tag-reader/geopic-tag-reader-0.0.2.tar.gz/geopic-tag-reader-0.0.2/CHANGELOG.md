# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.2] - 2023-05-10

### Added
- EXIF tag `UserComment` is now read and available in raw `exif` tags
- If not set, `GPSLatitudeRef` defaults to North and `GPSLongitudeRef` defaults to East
- A new `tag_reader:warning` property lists non-blocking warnings raised while reading EXIF tags


## [0.0.1] - 2023-03-31

### Added
- EXIF tag reading methods extracted from [GeoVisio API](https://gitlab.com/geovisio/api)


[Unreleased]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.0.2...main
[0.0.2]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.0.1...0.0.2
[0.0.1]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/commits/0.0.1
