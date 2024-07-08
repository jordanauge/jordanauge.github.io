## Installation

This repository relies on submodules for some themes and plugins (which are not
otherwise available through pip).

The following instructions are indicative and fit a debian distribution which
restricts the installation of python packages through pip. Adapt accordingly.

```
git clone git@github.com:jordanauge/website.git --recurse-submodules
pip install -r requirements.txt --break-system-packages
make
```

## Usage

### New blog post

```
./www news create
```

File will be created, named after the slug, and the whole site will be rebuilt
This opens the vim editor with a template

## Files and folders

 - '''cache''': build cache
 - '''content''': written content including pages, blog posts, static files, etc
 - '''data''': data content (in a separate folder to avoid being processed by pelican)
 - '''Makefile''': build and serve shortcuts
 - '''output''': generated content
 - '''patches''': own patches against plugins : currently btex
 - '''pelicanconf.py''': main configuration file
 - '''plugins''': installed plugins (either cloned here as submodules, or symlinked from plugins.all)
 - '''plugins.all''': former plugin repository from which we symlink selected ones (submodule)
 - '''publishconf.py''': publish configuration file
 - '''sources''': misc source files
 - '''static''': static files (must be there for some plugins, eg Z.)
 - '''tasks.py''': build helpers
 - '''templates''': misc templates for CV, home page news (TODO: detail)
 - '''themes''': theme repository (submodule)


## Technical notes

Installing dependencies
- preferences for debian packages
- sudo pip install pelican-page-hierarchy --break-system-packages

## Updates

- plugins
- font-awesome : https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/fontawesome.min.css
