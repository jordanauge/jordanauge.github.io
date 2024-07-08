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

## They need to be pip installed since they don't seem to be loaded
#PLUGIN_PATHS = ['plugins']
#PLUGINS = [
#    'ii18n_subsites',
#    'liquid-tags',
#    'webassets',
#]

# wk
