## Template structure

### Base templates

This template is common to all pages on the website:
  - header with navbar : although the content page change on some pages ?
  - content with or without sidebar
  - footer

Structure:

- header
  - BLOCK head
    - BLOCK title
  - BLOCK opengraph
- body
  - INCLUDE navbar
  - BLOCK container
    - INCLUDE sidebar
    - BLOCK breadcrums
    - BLOCK content
  - INCLUDE footer

Features:

- Bootstrap v5
- Themes : light/dark
- Font awesome
- Translations


TODO:

- Rework CSS
- SEO
- minimize assets
- RSS feeds

#### Common template : base.html

#### Extended template : index.html

### Child templates

#### article.html

- EXTENDS base
  - BLOCK title: article title
  - BLOCK head = base + article metadata
  - BLOCK header = page header WARNING : not in parent
  - BLOCK content
    - COND INCLUDE sidebar WARNING duplicate

#### page.html

- EXTENDS base
  - BLOCK title: article title
  - BLOCK header = page header WARNING : not in parent
  - BLOCK content

NOTES:

 - research/publications is not using template

### Special templates

#### fullpage.html


### Features

#### Translations

includes/translations, borrowed from pelican-bootstrap3 theme
