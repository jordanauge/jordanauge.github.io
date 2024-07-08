#
# Global settings
#

AUTHOR = 'Jordan Augé'
SITENAME = 'Jordan Augé'
# XXX This default should be handled in theme when empty
SITEURL = '' #"http://jordan.auge.free.fr"

PATH = "content"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = 'true'

# Article info
SHOW_ARTICLE_AUTHOR = 'false'
SHOW_ARTICLE_CATEGORY = 'true'
SHOW_DATE_MODIFIED = 'true'

# Plugins
#
# If you leave the PLUGINS setting as default (None), Pelican will automatically
# discover namespace plugins and register them. If, on the other hand, you
# specify a PLUGINS setting as a list of plugins, this auto-discovery will be
# disabled. At that point, only the plugins you specify will be registered, and
# you must explicitly list any namespace plugins as well.
#
# See: https://docs.getpelican.com/en/latest/plugins.html 
#
PLUGIN_PATHS = ["plugins"]
PLUGINS = [
     'pelican-page-hierarchy',
     'i18n_subsites',
     'jinja2content', # liquid tags not compatible
     'liquid_tags',
     'pelican-btex',#
     'webassets',
]

MENUITEMS = (
    ('Home', '/'),
    #('CV', '/cv'),
    ('Research', '/research'),
    ('Publications', '/research/publications'),
    ('Blog', '/blog'),
    #('Projects', '/projects'),
#    ('Misc', '/misc'),
#    ('Links', '/links'),
    #('About', '/about')
)

#a Without this line:
# CRITICAL: UndefinedError: '_' is undefined
# see. https://github.com/getpelican/pelican-themes/issues/482#issuecomment-346653264

JINJA_ENVIRONMENT = {
# XXX i need this to make the blog posts appear under blog
    'extensions': ['jinja2.ext.i18n'],
}

# cf https://jackdewinter.github.io/2019/10/16/fine-tuning-pelican-markdown-configuration/
# XXX https://python-markdown.github.io/extensions/smarty/
#'markdown.extensions.admonition': {},
#'markdown.extensions.meta': {},
#'markdown.extensions.extra': {},
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight'
        },
        'smarty' : {
            'smart_angled_quotes' : 'true'
        },
        'markdown.extensions.toc': {
            'permalink': 'true',
        },
        'fontawesome_markdown': {},
    }
}

# This allows to populated the blog index, which is replaced by blog/ in this
# configuration (we specified a index.md)
INDEX_SAVE_AS = 'blog/index.html'

# Make articles appear under blog
ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{slug}/index.html'
# XXX # ARTICLE_LANG_URL ('{slug}-{lang}.html')	
# XXX # ARTICLE_LANG_SAVE_AS ('{slug}-{lang}.html')	


# Archive
ARCHIVES_URL='blog/archives'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'
YEAR_ARCHIVE_URL = 'blog/{date:%Y}'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_URL = 'blog/{date:%Y}/{date:%b}'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/index.html'
DAY_ARCHIVE_URL = ''
DAY_ARCHIVE_SAVE_AS = ''

AUTHOR_URL=''
AUTHOR_SAVE_AS = ''
AUTHORS_URL=''
AUTHORS_SAVE_AS = ''

CATEGORY_URL = 'blog/category/{slug}'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
CATEGORIES_URL = 'blog/category'
CATEGORIES_SAVE_AS = 'blog/category/index.html'

TAG_URL='blog/tag/{slug}'
TAG_SAVE_AS='blog/tag/{slug}/index.html'
TAGS_URL='blog/tags.html'
TAGS_SAVE_AS = 'blog/tags/index.html'

# XXX # <DIRECT_TEMPLATE_NAME>_SAVE_AS	


# Feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# This allow pages to be referencd like xxx/about, while the file is
# xxx/about/index.html
# Don't we do too many subdirs like that ?
#PAGE_URL = '{slug}.html'
#PAGE_SAVE_AS = '{slug}.html'

# FIXME This requires to list all subfolders 
PAGE_PATHS = ['pages', 'pages/research']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
# XXX # PAGE_LANG_URL ('pages/{slug}-{lang}.html')
# XXX # PAGE_LANG_SAVE_AS ('pages/{slug}-{lang}.html')	

#
# We add both pages and article (blog) content to the list of static paths to
# allow static content to be attached to pages
#
# see: https://docs.getpelican.com/en/3.6.2/content.html#attaching-static-files
# tags: #static-content
#
# Static files should be stored in two types of locations:
#  - /static/TYPE/FILE for css, js, img, etc

#
STATIC_PATHS = [
    'pages',
    'blog',
    'extra', #wk-1
]

EXTRA_PATH_METADATA = {
    # Don't allow to list draft folder
    'extra/htaccess-NoIndexes': {'path': 'drafts/.htaccess'},
    # Favicon
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# Same for static


# Articles  are automatically published as drafts, unless marked as published.
DEFAULT_METADATA = {
    'Status': 'draft',
}

THEME_TEMPLATES_OVERRIDES = ['templates']

DISPLAY_BREADCRUMBS = True

# Incremental rebuild
# https://docs.getpelican.com/en/latest/settings.html#reading-only-modified-content

CACHE_CONTENT=True
#LOAD_CONTENT_CACHE=True
CHECK_MODIFIED_METHOD='md5' # mtime
CONTENT_CACHING_LAYER='reader' # generator
GZIP_CACHE=True

SUMMARY_MAX_LENGTH=0


################################################################################
#
# Theme settings
#

THEME = 'themes/jordan'

# theme: jordan

# GOOGLE_SITE_VERIFICATION
# BING_SITE_VERIFICATION
# LOCALE
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

DESCRIPTION="Jordan Augé's homepage"

# See: https://github.com/mpaglia0/Z?tab=readme-ov-file#translation-for-templates-strings

# custom Jinja2 filter for localizing theme
def gettext(string, lang):
    if lang == "en":
        return string
    elif lang == "fr":
        if string == "Archives": return "Archivi"
        elif string == "Archives for": return "Archivi per"
        elif string == "Posted by": return "Pubblicato da"
        else:
            return string

JINJA_FILTERS = {
    'gettext': gettext,
}

# theme: pelican-bootstrap

#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
#
#PLUGIN_PATHS = ['plugins']
#PLUGINS = ['i18n_subsites']
#
## Uncomment only if default language is not english
##I18N_TEMPLATES_LANG = 'en'
#
## See https://bootswatch.com/
#BOOTSTRAP_THEME = 'simplex'
#
## Article info
#SHOW_ARTICLE_AUTHOR = 'false'
#SHOW_ARTICLE_CATEGORY = 'true'
#SHOW_DATE_MODIFIED = 'true'
#
## Custom CSS/JS
##CUSTOM_CSS = 'static/css/custom.css'
##CUSTOM_JS = 'static/js/custom.js'
#
#STATIC_PATHS = [
#    'static',
#    'images',
#    'extra',
#]
#
#EXTRA_PATH_METADATA = {
#    #'extra/custom.css': {'path': 'static/css/custom.css'},
#    #'extra/custom.js': {'path': 'static/js/custom.js'}
#    'extra/htaccess-NoIndexes': {'path': 'drafts/.htaccess'},
#    'extra/favicon.ico': {'path': ''}
#}
#
## Breadcrumbs
#DISPLAY_BREADCRUMB = 'true'
#DISPLAY_CATEGORY_IN_BREADCRUMBS = 'false'
#
## Navbar
#BOOTSTRAP_NAVBAR_INVERSE = 'false'
#
## Series
#DISPLAY_SERIES_ON_SIDEBAR = 'true'
#SHOW_SERIES = 'true'
#
## Favicon
#FAVICON = 'images/favicon.png'
#
#ABOUT_ME = open('data/bio.md')
#
## Sidebar options
#
## - Social links
#SOCIAL = (
#    ('github', 'https://github.com/jordanauge/'),
#    ('linkedin', 'https://www.linkedin.com/in/jordan-aug%C3%A9-763ba4a8/'),
#)
#
## - Tags
#DISPLAY_TAGS_ON_SIDEBAR = 'true'
#DISPLAY_TAGS_INLINE = 'true'
#TAGS_URL = 'tags.html'
#
## - Categories
#DISPLAY_CATEGORIES_ON_SIDEBAR = 'true'
#
## - Recent posts
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = 'true'
## RECENT_POST_COUNT = 5
#
## - Archive
#DISPLAY_ARCHIVE_ON_SIDEBAR = 'true'
#MONTH_ARCHIVE_SAVE_AS = ''
#
## - Authors
#DISPLAY_AUTHORS_ON_SIDEBAR = 'false'
#
## - Other
##HIDE_SIDEBAR
##SIDEBAR_ON_LEFT
##DISABLE_SIDEBAR_TITLE_ICONS
#
## - License
#CC_LICENSE = "CC-BY-NC-SA"
## END





################################################################################
#
# Plugin settings
#

# --- plugin: pelican-page-hierarchy -------------------------------------------

# This allows the page hierarchy to be preserved
#
# see: https://github.com/akhayyat/pelican-page-hierarchy
# tags: #static-content
#
# TODO : this should not be the case for static files we want to land in the
# same folder as the content
#
SLUGIFY_SOURCE = 'basename'

# --- plugin: i18n_subsites ----------------------------------------------------

I18N_UNTRANSLATED_ARTICLES='keep'
I18N_UNTRANSLATED_PAGES='keep'

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'fr': {
        }
    }

# --- plugin: pelican-bibtex ---------------------------------------------------

PUBLICATIONS_SRC = 'data/bibliography.bib'

# --- plugin: webassets --------------------------------------------------------

WEBASSETS_SOURCE_PATHS = ['static']

# It seems I have to define this... ok if there is a single ASSET_SOURCE_PATHS
ASSET_URL = 'static'
# use {{ ASSET_URL }} in templates
# i use it in my base template with fancy toc


# --- plugin: jinja2content ----------------------------------------------------

# This is relative to PATH
JINJA2CONTENT_TEMPLATES = ['../templates']

# This is not used although it would be more standard
#EXTRA_TEMPLATES_PATHS = ['macros']

################################################################################
#
# Content settings
#

## content: cv
#
#FN_FORMATION = 'data/formation.yaml'
#HF_FORMATION = ('year', 'lab', 'position', 'description', 'logo')
#FN_EXPERIENCE = 'data/experience.yaml'
#HF_EXPERIENCE = ('year', 'lab', 'position', 'description', 'advisor', 'logo')
#FN_INTERNSHIP = 'data/internship.yaml'
#HF_INTERNSHIP = ('year', 'type', 'lab', 'description')
#FN_SKILLS = 'data/skills.yaml'
#HF_SKILLS = ('group', 'items.name', 'items.level')
#FN_PROJECTS = 'data/projects.yaml'
#HF_PROJECTS = ('year', 'name', 'url', 'funding', 'description', 'comments')
#FN_SOFTWARE = 'data/software.yaml'
#HF_SOFTWARE = ('name', 'description')
#
## XXX How to retrieve the current language ?
#
#import yaml
#
#def get_dic_field(dic, field, lang):
#    if '.' in field:
#        # XXX TODO
#        l, _, r = field.rpartition('.')
#    else:
#        field_lang = '{}-{}'.format(field, lang)
#        return dic.get(field_lang, dic.get(field, None))
#
#def get_dataset(filename, field_names, lang = DEFAULT_LANG):
#    with open(filename) as f:
#        # https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
#        data = yaml.load(f, Loader=yaml.FullLoader)
#        ret = list()
#        for entry in data:
#            dic = dict()
#            for field in field_names:
#                dic[field] = get_dic_field(entry, field, lang)
#            ret.append(dic)
#    return ret
#
## I had to prefix by CV as many extensions like elegant, resume theme already use those
## I changed the meaning of those to be lambda's depending on lang
## they are used in my own CV templates
## templates/includes/projects.html
#CAREER_SUMMARY = 'todo'
#FORMATION = lambda lang : get_dataset(FN_FORMATION, HF_FORMATION, lang)
#EXPERIENCE = lambda lang: get_dataset(FN_EXPERIENCE, HF_EXPERIENCE, lang)
#INTERNSHIP = lambda lang : get_dataset(FN_INTERNSHIP, HF_INTERNSHIP, lang)
#CV_PROJECT_INTRO = ''
#CV_PROJECTS = lambda lang : get_dataset(FN_SOFTWARE, HF_SOFTWARE, lang)
#SKILLS = lambda lang : get_dataset(FN_SKILLS, HF_SKILLS, lang)

