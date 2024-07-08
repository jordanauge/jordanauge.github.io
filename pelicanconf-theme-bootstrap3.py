# BEGIN https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites']

# Uncomment only if default language is not english
#I18N_TEMPLATES_LANG = 'en'

# See https://bootswatch.com/
BOOTSTRAP_THEME = 'simplex'

# Article info
SHOW_ARTICLE_AUTHOR = 'false'
SHOW_ARTICLE_CATEGORY = 'true'
SHOW_DATE_MODIFIED = 'true'

# Custom CSS/JS
#CUSTOM_CSS = 'static/css/custom.css'
#CUSTOM_JS = 'static/js/custom.js'

STATIC_PATHS = [
    'static',
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    #'extra/custom.css': {'path': 'static/css/custom.css'},
    #'extra/custom.js': {'path': 'static/js/custom.js'}
    'extra/htaccess-NoIndexes': {'path': 'drafts/.htaccess'},
    'extra/favicon.ico': {'path': ''}
}

# Breadcrumbs
DISPLAY_BREADCRUMB = 'true'
DISPLAY_CATEGORY_IN_BREADCRUMBS = 'false'

# Navbar
BOOTSTRAP_NAVBAR_INVERSE = 'false'

# Series
DISPLAY_SERIES_ON_SIDEBAR = 'true'
SHOW_SERIES = 'true'

# Favicon
FAVICON = 'images/favicon.png'

ABOUT_ME = open('data/bio.md')

# Sidebar options

# - Social links
SOCIAL = (
    ('github', 'https://github.com/jordanauge/'),
    ('linkedin', 'https://www.linkedin.com/in/jordan-aug%C3%A9-763ba4a8/'),
)

# - Tags
DISPLAY_TAGS_ON_SIDEBAR = 'true'
DISPLAY_TAGS_INLINE = 'true'
TAGS_URL = 'tags.html'

# - Categories
DISPLAY_CATEGORIES_ON_SIDEBAR = 'true'

# - Recent posts
DISPLAY_RECENT_POSTS_ON_SIDEBAR = 'true'
# RECENT_POST_COUNT = 5

# - Archive
DISPLAY_ARCHIVE_ON_SIDEBAR = 'true'
MONTH_ARCHIVE_SAVE_AS = ''

# - Authors
DISPLAY_AUTHORS_ON_SIDEBAR = 'false'

# - Other
#HIDE_SIDEBAR
#SIDEBAR_ON_LEFT
#DISABLE_SIDEBAR_TITLE_ICONS

# - License
CC_LICENSE = "CC-BY-NC-SA"
# END

