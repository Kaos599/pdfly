# CHANGELOG

## Version 0.4.0, not released yet

### New Features (ENH)
- New  update-offsets command to adjust offsets and lengths. (#15)
- New rm command (#59)
- metadata: now also displaying CreationDate, Creator, Keywords & Subject (#73)
- Add warning for out-of-bounds page range in pdfly cat command (#58)

[Full Changelog](https://github.com/py-pdf/pdfly/compare/0.3.3...0.4.0)


## Version 0.3.3, 2024-04-14

### Developer Experience (DEV)
-  Chain workflows

[Full Changelog](https://github.com/py-pdf/pdfly/compare/0.3.2...0.3.3)


## Version 0.3.2, 2024-04-14

### Developer Experience (DEV)
-  Decouple git tag / PyPI release / Github release page (#49, #50)


[Full Changelog](https://github.com/py-pdf/pdfly/compare/0.3.1...0.3.2)

## Version 0.3.1, 2024-03-29

### Maintenance (MAINT)
-  Update pypdf usage (#48)

### Developer Experience (DEV)
-  Release via REL commit (#48)
-  Fix mypy issues
-  Add make_release.py

[Full Changelog](https://github.com/py-pdf/pdfly/compare/0.3.0...0.3.1)

## Version 0.3.0, 2023-12-17

### New Features (ENH)
-  Add x2pdf command (#25)

### Bug Fixes (BUG)
-  boxes are floats, not int
-  Add missing fpdf2 dependency (#29)

### Documentation (DOC)
-  cat command
-  More examples for the cat subcommand
-  Add cat subcommand
-  Link to readthedocs
-  Add project governance file
-  Move readthedocs config file to root
-  Add docs (#24)

### Developer Experience (DEV)
-  Checkout sample-files in CI (#30)
-  Let dependabot update Github Actions
-  Add action for automatic releases

### Maintenance (MAINT)
-  Update dependencies (#42)
-  In the cat subcommand, replace the usage of the deprecated PdfMerger by PdfWriter (#34)
-  Update .pre-commit-config.yaml
-  Adjust x2pdf syntax

### Testing (TST)
-  cat with two files (#41)
-  Test cat command with more parameters + validate result (#40)
-  Adding unit tests (#28)

### Other
- : [{'msg': 'Bump actions/setup-python from 4 to 5 (#39)', 'author': 'dependabot[bot]'}, {'msg': 'test_extract_images_monochrome() is now passing', 'author': 'CimonLucas(LCM)'}, {'msg': 'Bump actions/setup-python from 3 to 4 (#27)', 'author': 'dependabot[bot]'}, {'msg': 'Bump actions/checkout from 3 to 4 (#26)', 'author': 'dependabot[bot]'}, {'msg': 'Ensure input PDF exists for cat subcommand', 'author': 'MartinThoma'}]

[Full Changelog](https://github.com/py-pdf/pdfly/compare/0.2.14...0.3.0)
