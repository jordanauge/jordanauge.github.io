Code is ugly (repetitions, etc.) and not well documented but it does the job.

Possible templates are: default, fancy_minimal, fancy_minimal_no_bibtex, fancy_minimal_keynote
publications, latest, supervisions, minimal, news
empty if wrong default template

  data-item=None ??
  data-scholar-cite-counts=no/yes
  data-scholar-link=None
  data-target-page=None
  data-citations=btex_citation_cache.yaml

btex vs btex-item div

we have settings for grouping

possibility to have statistics

i need some instructions on how to maintain my bibtex file

item
    _award
    _pdf
    _demo
    _demo_external
    etc..

parse... returns a set of items.

What's inside a template... let's look at default

1. reverse sort by year
2. inside, a set of items sorted by year
  a. 
3. finally Modal for pop ups


ANd how it is rendered... seems grouping is static

            div_html = BeautifulSoup(template.render(publications=publications,
                                                     meta=meta,
                                                     publication_grouping=btex_publication_grouping,
                                                     first_visible_year=options['first_visible_year'],
                                                     item_count=options['item_count'],
                                                     target_page=options['target_page']
                                                     ), "html.parser")

template.render( item=item_data, meta=meta, target_page=options['target_page'], uuid=options['uuid'])
