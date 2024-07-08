# pybtex style for pelican-btex
# based on plain style of pybtex

import re
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.formatting import BaseStyle, toplevel
from pybtex.style.template import (
    join, words, field, optional, first_of,
    names, sentence, tag, optional_field, href
)
from pybtex.richtext import Text, Symbol

# jordan

from pybtex.style.template import node, FieldIsMissing

MAP_NAME_URL = {
    u'Jordan Aug\xe9': '#',
    u'Sandrine Avakian': 'http://fr.viadeo.com/fr/profile/avakian.sandrine',
    u'Thomas Bourgeau': 'http://scholar.google.fr/citations?user=u1aoKZYAAAAJ',
    u'Marc-Olivier Buob': 'http://marcolivier.buob.pagesperso-orange.fr/',
    u'Giovanna Carofiglio': 'https://scholar.google.com/citations?user=fvP_U2MAAAAJ',
    u'Danilo Cicalese': 'https://fr.linkedin.com/in/danilocicalese',
    u'Alberto Compagno': 'https://scholar.google.com/citations?user=jzZfJrMAAAAJ', # https://sites.google.com/a/di.uniroma1.it/compagno/
    u'Marcel Enguehard': 'https://enguehard.org/',
    # https://scholar.google.com/citations?authorid=1zxXbsgAAAAJ
    # https://github.com/marceleng
    # https://www.linkedin.com/in/marceleng
    # https://twitter.com/menguehard
    u'Serge Fdida': 'https://www-npa.lip6.fr/~sf/',
    # https://scholar.google.com/citations?user=XL6CnCwAAAAJ
    u'Timur Friedman': 'https://www-npa.lip6.fr/~timur/',
    u'Giulio Grassi': 'http://scholar.google.com/citations?user=DzaE5C4AAAAJ',
    u'Luca Muscariello': 'https://sites.google.com/view/lucamuscariello/',
    u'Sara Oueslati': 'https://fr.linkedin.com/in/sara-oueslati-68b47716',
    u'Michele Papalini': 'https://scholar.google.com/citations?user=sEIjNiYAAAAJ',
    u'Giovanni Pau': 'scholar.google.com/citations?user=jLEgvnsAAAAJ',
    u'James Roberts': 'https://scholar.google.fr/citations?user=ebkV47UAAAAJ',
    u'Dario Rossi': 'http://perso.telecom-paristech.fr/~drossi/',
    u'Jacques Samain': 'https://jaqu.eu/',
    # https://twitter.com/LeJackSamain
    # https://www.linkedin.com/in/jacques-samain-25138694/
    u'Mauro Sardara': 'https://fr.linkedin.com/in/mauro-sardara-584100a7',
    u'Nicolas Turro': 'http://sed.inrialpes.fr/people/turro/',
    u'Xuan Zeng': 'https://www.linkedin.com/in/xuan-zeng-56a2968b/',
    u'': '#',
}

def make_url(person):
    #person_text = person.text
    #name = person_text.format().plaintext()
    name = str(person)
    url = MAP_NAME_URL.get(name, None)
    if not url:
        pass#print("MISSING", name)
    return href() [ url, name ] if url else name

@node
def names(children, data, role, **kwargs):
    """Return formatted names."""

    assert not children
    data = data['entry']
    try:
        persons = data.persons[role]
    except KeyError:
        # role is a bibtex field so it makes sense
        # to raise FieldIsMissing; optional will catch it
        raise FieldIsMissing(role, data)

    # person.text is set by pybtex.style.formatting.BaseStyle.format_entries()
    # TODO: do something about it, because it is confusing
    #import pdb; pdb.set_trace()
    return join(**kwargs) [[ make_url(person) for person in persons]].format_data(data)

    #return join(**kwargs) [[ person.text for person in persons]].format_data(data)


# end jordan

def dashify(text):
    dash_re = re.compile(r'-+')
    return Text(Symbol('ndash')).join(dash_re.split(text.plaintext()))

pages = field('pages', apply_func=dashify)

date = words[optional_field('month'), field('year')]


class Style(UnsrtStyle):
    name = 'btex'

    def format_btitle(self, e, which_field, as_sentence=True):
        formatted_title = field(which_field)
#        if as_sentence:
#            return tag('emph') [sentence(capfirst=False) [ formatted_title ]]
#        else:
#            return tag('emph') [formatted_title]
        return tag('b') [formatted_title]

    def format_title(self, e, which_field, as_sentence=True):

        def protected_capitalize(x):
            """Capitalize string, but protect {...} parts."""
            return x.capitalize().plaintext()

        formatted_title = field(which_field, apply_func=protected_capitalize)

        if as_sentence:
            return tag('emph') [sentence(capfirst=False) [ formatted_title ]]
        else:
            return tag('emph') [formatted_title]

    def format_names(self, role, as_sentence=True):
        formatted_names = names(role, sep=', ', sep2 = ' and ', last_sep=', and ')
        if as_sentence:
            return sentence(capfirst=False) [formatted_names]
        else:
            return formatted_names

    def format_article(self, e):
        volume_and_pages = first_of[
            # volume and pages, with optional issue number
            optional[
                join[
                    field('volume'),
                    optional['(', field('number'), ')'],
                    ':', pages
                ],
            ],
            # pages only
            words['pp', pages],
        ]
        template = toplevel[
            self.format_names('author'),
            self.format_title(e, 'title'),
            sentence(capfirst=False)[
                field('journal'),
                optional[volume_and_pages],
                date],
            sentence(capfirst=False)[optional_field('note')],
            #self.format_web_refs(e),
        ]

        return template.format_data(e)

    def format_book(self, e):
        template = toplevel [
            words[sentence [self.format_names('author')], '(Eds.)'],
            self.format_title(e, 'title'),
            sentence[date],
            words['ISBN: ', sentence(capfirst=False) [ optional_field('isbn') ]],
        ]
        return template.format_data(e)

    def format_incollection(self, e):
        template = toplevel [
            self.format_names('author'),
            sentence(capfirst=False) [
                self.format_title(e, 'title'),
            ],
            sentence(capfirst=False) [
                field('booktitle'),
                field('series'),
                optional[
                    words['pp', field('pages')],
                ],
                date,
            ],
        ]
        return template.format_data(e)

    def format_inproceedings(self, e):
        template = toplevel[
            sentence[self.format_names('author')],
            self.format_title(e, 'title'),
            words[
                'In',
                sentence(capfirst=False)[
                    optional[self.format_editor(e, as_sentence=False)],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    optional[
                        words['pp', field('pages')],
                    ],
                ],
                self.format_address_organization_publisher_date(e),
            ],
            sentence(capfirst=False)[optional_field('note')],
            #self.format_web_refs(e),
        ]
        return template.format_data(e)

    def format_patent(self, e):
        template = toplevel[
            sentence[self.format_names('author')],
            self.format_title(e, 'title'),
            sentence(capfirst=False)[
                tag('emph')[field('number')],
                date],
        ]
        return template.format_data(e)

    def format_mastersthesis(self, e):
        template = toplevel[
            sentence[self.format_names('author')],
            self.format_title(e, 'title'),
            sentence[
                "Master's thesis",
                field('school'),
                optional_field('address'),
                date,
            ],
            sentence(capfirst=False)[optional_field('note')],
            #self.format_web_refs(e),
        ]
        return template.format_data(e)

    def format_misc(self, e):
        if '_subtype' in e.fields and e.fields['_subtype'] == 'studentproject':
            template = toplevel [
                sentence [self.format_names('author')],
                self.format_title(e, 'title'),
                sentence[
                    field('_school'),
                    field('_course'),
                    date,
                ],
                sentence(capfirst=False) [ optional_field('note') ],
                #self.format_web_refs(e),
            ]
        else:
            template = toplevel [
                sentence [self.format_names('author')],
                self.format_title(e, 'title'),
                sentence[
                    date,
                ],
                sentence(capfirst=False) [ optional_field('note') ],
                #self.format_web_refs(e),
            ]
        return template.format_data(e)
