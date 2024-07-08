---
title: Publications
slug: publications
status: published
---

<div class='btex'
     data-source='data/bibliography.bib'
     data-template='publications'
     data-scholar-link='https://scholar.google.fr/citations?user=-itbwwIAAAAJ'
     data-stats='yes'
     data-scholar-cite-counts='yes'>
        <div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
            {% for year, year_group in publications|groupby('year')|sort(reverse=True) %}
                <h3>{{year}}</h3>
                {% for item in year_group|sort(attribute='year') %}
                    <div class="panel publication-item" id="{{ item.key }}" style="box-shadow: none">
                        <div class="panel-heading" role="tab" id="heading{{ item.key }}">
                            <div class="row">
                                <div class="col-md-1">
                                    <span class="{{ item.type_label_css }}">{{ item.type_label_short }}</span>
                                </div>
                                <div class="col-xs-8">
                                    <p style="text-align:left">
                                    {{item.text}}
                                    {% if item.award %}<span class="label label-success">{{item.award}}</span>{% endif %}
                                    {% if item.cites %}
                                    <span style="padding-left:5px">
                                    <span title="Number of citations" class="badge">{{ item.cites }} {% if item.cites==1 %}cite{% else %}cites{% endif %}</span>
                                    </span>
                                    {% endif %}
                                    </p>
                                    <button type="button" class="btn btn-default btn-xs" data-toggle="collapse" data-parent="#accordion" href="#collapse{{ item.key }}" aria-expanded="true" aria-controls="collapse{{ item.key }}">
                                    <i class="fa fa-caret-down"></i> Read more...</button>
                                </div>
                                <div class="col-xs-3">
                                    <div class="btn-group">
                                        <button type="button" class="btn btn-xs btn-danger" data-toggle="modal" data-target="#bibtex{{ item.key }}"><i class="fa fa-file-text-o"></i> Bib</button>
                                        {% if item.pdf %}
                                            <a href="{{item.pdf}}" class="btn btn-xs btn-warning btn-btex" rel="tooltip" title="Download pdf" data-placement="bottom"><i class="fa fa-file-pdf-o fa-1x"></i> PDF</a>
                                        {% endif %}
                                        {% if item.demo %}
                                            <a href="{{item.demo}}" class="btn btn-xs btn-primary iframe-demo btn-btex" rel="tooltip" title="Demo" data-placement="bottom"><i class="fa fa-headphones"></i> Demo</a>
                                        {% endif %}
                                        {% if item.demo_external %}
                                            <a href="{{item.demo_external}}" target="_blank" class="btn btn-xs btn-primary btn-btex" rel="tooltip" title="Demo" data-placement="bottom"><i class="fa fa-headphones"></i> Demo</a>
                                        {% endif %}
                                        {% if item.toolbox %}
                                            <a href="{{item.toolbox}}" class="btn btn-xs btn-success btn-btex" rel="tooltip" title="Toolbox" data-placement="bottom"><i class="fa fa-file-code-o"></i> Toolbox</a>
                                        {% endif %}
                                        {% if item.data1 %}
                                            <a href="{{item.data1.url}}" class="btn btn-xs btn-info btn-btex" rel="tooltip" title="{{item.data1.title}}" data-placement="bottom"><i class="fa fa-database"></i></a>
                                        {% endif %}
                                        {% if item.data2 %}
                                            <a href="{{item.data2.url}}" class="btn btn-xs btn-info btn-btex" rel="tooltip" title="{{item.data2.title}}" data-placement="bottom"><i class="fa fa-database"></i></a>
                                        {% endif %}
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div id="collapse{{ item.key }}" class="panel-collapse collapse" role="tabpanel" aria-labelledby="heading{{ item.key }}">
                            <div class="panel-body well well-sm">
                                <h4>{{item.title}}</h4>
                                {% if item.abstract %}
                                    <h5>Abstract</h5>
                                    <p class="text-justify">{{item.abstract}}</p>
                                {% endif %}
                                {% if item.keywords %}
                                    <h5>Keywords</h5>
                                    <p class="text-justify">{{item.keywords}}</p>
                                {% endif %}
                                {% if item.award %}
                                    <p><strong>Awards:</strong> {{item.award}}</p>
                                {% endif %}
                                {% if item.cites %}
                                    <p><strong>Cites:</strong> {{item.cites}} (<a href="{{ item.citation_url }}" target="_blank">see at Google Scholar</a>)</p>
                                {% endif %}
                                <div class="btn-group">
                                    <button type="button" class="btn btn-sm btn-danger" data-toggle="modal" data-target="#bibtex{{ item.key }}"><i class="fa fa-file-text-o"></i> Bibtex</button>
                                    {% if item.pdf %}
                                        <a href="{{item.pdf}}" class="btn btn-sm btn-warning btn-btex2" rel="tooltip" title="Download pdf" data-placement="bottom"><i class="fa fa-file-pdf-o fa-1x"></i> PDF</a>
                                    {% endif %}
                                    {% if item.slides %}
                                        <a href="{{item.slides}}" class="btn btn-sm btn-info btn-btex2" rel="tooltip" title="Download slides" data-placement="bottom"><i class="fa fa-file-powerpoint-o"></i> Slides</a>
                                    {% endif %}
                                    {% if item.poster %}
                                        <a href="{{item.poster}}" class="btn btn-sm btn-info btn-btex2" rel="tooltip" title="Download poster" data-placement="bottom"><i class="fa fa-picture-o"></i> Poster</a>
                                    {% endif %}
                                    {% if item.webpublication %}
                                        <a href="{{item.webpublication.url}}" class="btn btn-sm btn-info btn-btex2" title="{{item.webpublication.title}}"><i class="fa fa-book"></i> Web publication</a>
                                    {% endif %}
                                </div>
                                <div class="btn-group">
                                    {% if item.toolbox %}
                                        <a href="{{item.toolbox}}" class="btn btn-sm btn-success btn-btex2" rel="tooltip" title="Toolbox" data-placement="bottom"><i class="fa fa-file-code-o"></i> Toolbox</a>
                                    {% endif %}
                                    {% if item.data1 %}
                                        <a href="{{item.data1.url}}" class="btn btn-sm btn-info btn-btex2" rel="tooltip" title="Toolbox" data-placement="bottom"><i class="fa fa-database"></i> {{item.data1.title}}</a>
                                    {% endif %}
                                    {% if item.data2 %}
                                        <a href="{{item.data2.url}}" class="btn btn-sm btn-info btn-btex2" rel="tooltip" title="Toolbox" data-placement="bottom"><i class="fa fa-database"></i> {{item.data2.title}}</a>
                                    {% endif %}
                                    {% if item.code1 %}
                                        <a href="{{item.code1.url}}" class="btn btn-sm btn-success btn-btex2" title="{{item.code1.title}}"><i class="fa fa-file-code-o"></i> {{item.code1.title}}</a>
                                    {% endif %}
                                    {% if item.code2 %}
                                        <a href="{{item.code2.url}}" class="btn btn-sm btn-success btn-btex2" title="{{item.code2.title}}"><i class="fa fa-file-code-o"></i> {{item.code2.title}}</a>
                                    {% endif %}
                                    {% if item.demo %}
                                        <a href="{{item.demo}}" class="btn btn-sm btn-primary iframe-demo btn-btex2" rel="tooltip" title="Demo" data-placement="bottom"><i class="fa fa-headphones"></i> Demo</a>
                                    {% endif %}
                                    {% if item.demo_external %}
                                        <a href="{{item.demo_external}}" target="_blank" class="btn btn-sm btn-primary btn-btex2" rel="tooltip" title="Demo" data-placement="bottom"><i class="fa fa-headphones"></i> Demo</a>
                                    {% endif %}
                                    {% if item.link1 %}
                                        <a href="{{item.link1.url}}" class="btn btn-sm btn-info btn-btex2" title="{{item.link1.title}}"><i class="fa fa-external-link-square"></i> {{item.link1.title}}</a>
                                    {% endif %}
                                    {% if item.link2 %}
                                        <a href="{{item.link2.url}}" class="btn btn-sm btn-info btn-btex2" title="{{item.link2.title}}"><i class="fa fa-external-link-square"></i> {{item.link2.title}}</a>
                                    {% endif %}
                                    {% if item.link3 %}
                                        <a href="{{item.link3.url}}" class="btn btn-sm btn-info btn-btex2" title="{{item.link3.title}}"><i class="fa fa-external-link-square"></i> {{item.link3.title}}</a>
                                    {% endif %}
                                    {% if item.link4 %}
                                        <a href="{{item.link4.url}}" class="btn btn-sm btn-info btn-btex2" title="{{item.link4.title}}"><i class="fa fa-external-link-square"></i> {{item.link4.title}}</a>
                                    {% endif %}
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Modal -->
                    <div class="modal fade" id="bibtex{{item.key}}" tabindex="-1" role="dialog" aria-labelledby="bibtex{{item.key}}label" aria-hidden="true">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <button type="button" class="close" data-dismiss="modal"><span class="glyphicon glyphicon-remove-sign" aria-hidden="true"></span><span class="sr-only">Close</span></button>
                                    <h4 class="modal-title" id="bibtex{{item.key}}label">{{item.title}}</h4>
                                </div>
                                <div class="modal-body">
                                    <pre>{{item.bibtex}}</pre>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                </div>
                            </div>
                        </div>
                    </div>
                {% endfor %}
            {% endfor %}
        </div>
</div>

## IETF drafts

<ul>
  <li>
    <b>MAP-Me : Managing Anchorless Mobility in Content Centric Networking</b><br/>
    Jordan Augé, Giovanna Carofiglio, Luca Muscariello, Michele Papalini<br/>
    <i><a href='https://datatracker.ietf.org/doc/draft-irtf-icnrg-mapme/'>draft-irtf-icnrg-mapme-00</a>, IRTF, ICNRG, 2018</i>
  </li>
</ul>

## Patents

<ul>
  <li>
    <b>Low-Overhead Anchorless Managing of Producer Mobility in Information-Centric Networking</b><br/>
    Giovanna Carofiglio, Jordan Augé, Pascal Thubert - Cisco Technology Inc.<br/>
    <i><a href='https://patents.google.com/patent/US20170034041A1/'>US20170034041A1</a> - Priority 2015-07-30 • Filing 2016-03-03 • Publication 2017-02-02</i>
  </li>￼
  <li>
    <b>System and method to facilitate integration of information-centric networking into internet protocol networks</b><br/>
    Luca MUSCARIELLO, Giovanna Carofiglio, Jordan Augé - Cisco Technology Inc.<br/>
    <i><a href='https://patents.google.com/patent/US20180103128A1/'>US20180103128A1</a> - Filing 2017-07-25 • Publication 2018-04-12 • Issued 2020-08-18</i>
  </li>￼
</ul>

## Posters

<ul>
  <li>
  <img src='img/fr.png' alt=''/>
  <b>Evaluation d'une proposition de gestion de trafic au niveau flot</b>, <br/>
  Jordan Augé,<br/>
  <i>Forum CIFRE, CNIT La Défense, Paris, 21 Mars 2006</i><br/>
  <a href='/static/files/research/poster.pdf'><img src='/img/icon/pdf.png' alt=''/>PDF</a>
  <br/>
  </li>
</ul>

<ul>
  <li>
  <b>MASTS: Measurements at All Scales in Time and Space</b>, <br/>
  Jordan Augé, Richard Clayton, Andrew W. Moore<br/>
  <i>University of Cambridge, 2008</i><br/>
  <a href='/static/files/research/2008-masts-poster.pdf'><img src='/img/icon/pdf.png' alt=''/>PDF</a>
  <br/>
  </li>
</ul>

## Technical reports

<ul>
  <li>
  <b>Maquette de démonstration Cross-Protect</b> (in french),<br/>
  Jordan Augé, Nabil Benameur, Abdesselem Kortebi, Sara Oueslati, James Roberts,<br/>
  <i>Internal report, April 2005</i>.<br/>
  <a
  href='/static/files/research/200504-maquette_cross-protect.pdf'><img src='/img/icon/pdf.png' alt=''/>PDF</a>
  <br/>
  </li>
</ul>

## Selected presentations

<ul>
  <li>
    <b>Some development about the Future Internet in Europe</b>,<br/>
    Serge Fdida, Jordan Augé, Marc-Olivier Buob, Loïc Baron, Timur Friedman,
    <i><a href='http://www.cfi2013.edu.cn'>CFI'2013</a>, The 8th International Conference on Future Internet Technologies, June 5-7, 2013, Beijing, China</i>
    <a href='/static/files/research/cfi_talk_june7_2013.pdf'><img src='/img/icon/pdf.png' alt=''/>PDF</a>
  </li>
  <li>
    <b>Supporting the experiment lifecycle with MySlice</b>, <br/>
    Jordan Augé, Loïc Baron, Timur Friedman, Serge Fdida,<br/>
    <i>GENI Engineering Conference, GEC15 - Oct. 23-25, 2012 -  Houston, TX</i><br/>
  <a href='#'><img src='/img/icon/pdf.png' alt=''/>PDF</a>
  <br/>
  </li>
  <li>
  <b>A statistical bandwidth sharing perspective at buffer sizing</b>,<br/>
  Jordan Augé, James Roberts,<br/>
  <i>LIP6 seminars, December 4th, 2008</i>.<br/>
  <a
  href='/static/files/research/200812-lip6-buffer-sizing.pdf'><img src='/img/icon/pdf.png' alt=''/>PDF</a>
  <br/>
  </li>

  <li>
  <b>A brief introduction to Flow-Aware Networking</b>,<br/>
  Jordan Augé (inspired from collective work in the France Telecom team),<br/>
  <i>NETOS talklets, April 22nd, 2008</i>.<br/>
  <a
  href='/static/files/research/20080422-netos-talklet-fan.pdf'><img src='/img/icon/pdf.png' alt=''/>PDF</a>
  <a href='/static/files/research/20080422-netos-talklet-fan.tar.gz'><img src='/img/icon/tex.png' alt=''/>LaTeX source</a>
  <a href='/static/files/research/20080422-netos-talklet-fan-eps.tar.gz'><img
  src='/img/icon/tgz.png' alt=''/>EPS files</a>
  <br/>
  </li>
</ul>

## Awards

<ul>
  <li>Our paper "Characterizing IPv4 Anycast Adoption and Deployment" published
  in CoNEXT'15 " received the <a href='https://irtf.org/anrp'>Applied Networking
  Research Prize (ANRP)</a> from IETF .
  </li>
</ul>
