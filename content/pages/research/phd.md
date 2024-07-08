---
title: Phd thesis
slug: phd
lang: en
---
<link rel="stylesheet" href="/lib/phpBibLib/bibtex.css" type="text/css">

### Garanties de performance pour les flots IP dans l'architecture Flow-Aware

Jordan Augé _(Orange Labs, Télécom ParisTech)_

La soutenance de thèse aura lieu le jeudi 27 Novembre à 14h00 au LINCS en Salle
du Conseil, et sera traditionnellement suivie d'un pot. Les informations d'accès au laboratoire sont
disponibles sur cette page:
[http://www.lincs.fr/access-details/](http://www.lincs.fr/access-details/)

Le jury sera composé de:

- Mme. Isabelle GUERIN-LASSOUS, Professeur, ENS Lyon, LIP (rapporteur)
- M. Steve UHLIG, Professeur, Queen Mary University of London, UK (rapporteur)
- M. Tijani CHAHED, Professeur, Telecom SudParis (examinateur)
- M. Fabien MATHIEU, Ingénieur de recherche, Alcatel Lucent Bell Labs France (examinateur)
- M. Daniel KOFMAN, Professeur, Telecom ParisTech (directeur de thèse académique)
- M. James ROBERTS, Chercheur senior, IRT SystemX (directeur de thèse industriel)

---

## Resume

Les réseaux connaissent des changements fondamentaux qui ont suscité un regain
d'intêret pour les problématiques de qualité de service (QoS): accès fibre
optique, réseaux mobiles 4G, datacenters, etc. À de rares
exceptions, l'utilisation des architectures classiques de QoS est restée
marginale à cause de leur complexité de mise en oeuvre. Dans cette thèse, nous
nous intéressons à l'architecture Flow-Aware Networking (FAN), en rupture avec les
approches classiques. FAN propose de considérer la performance du trafic au
niveau des flux de données, et est ancrée sur des modèles théoriques de files
d'attente simples et robustes, permettant d'établir la relation existant entre
capacité du réseau, demande en trafic, et performance obtenue.

Nous nous intéressons particulièrement une réalisation de cette architecture
pour le coeur de réseau, qui associe un ordonnancement équitable par flot à un
contrôle d'admission, et pour lequel nous avons réalisé un prototype. Un tel
routeur, nommé Cross-Protect, permet l'assurance de garanties de performance
de bout en bout grâce à un contrôle local du trafic, sans nécessiter de marquage
ou de protocole de signalisation: il permet des délais et pertes négligeables
pour les flux streaming, et l'assurance d'un débit moyen minimum pour les transferts
élastiques.

Une partie des travaux à considéré l'impact des buffers IP sur la performance
des flots, dans un contexte de remise en cause par la communauté des règles de
dimensionnement usuelles. Nos travaux complètent les modèles fluides utilisés
dans FAN, qui considèrent des tailles de buffer infinies, afin de prendre en
compte les interactions au niveau paquet se produisant dans les buffers, dues au
contrôle de congestion effectué par TCP. Ils permettent de réconcilier
certaines hypothèses contradictoires, et d'aboutir à une règle de
dimensionnement empirique.

Nous motivons ensuite l'introduction d'un ordonnancement de type Fair Queueing
dans le réseau, qui permet d'une part l'isolation des flots élastiques et la
différenciation des flux streaming. Nous évaluons les principales propositions
TCP dans un tel contexte, et suggérons qu'un tel réseau permet la conception et
l'introduction de nouveaux protocoles plus efficaces pour exploiter les
ressources du réseau.

Nous proposons également deux déclinaisons d'un algorithme de contrôle
d'admission, qui est la seconde composante fondamentale de la proposition. Nous
les évaluons dans de nombreuses configurations réalistes de trafic, et montrons
qu'ils permettent une utilisation efficace du lien dans des conditions réalistes
où la majorité des flots ont un débit crête limité, tout en permettant la
différenciation implicite permise par le fair queueing.

Pour terminer, nous discutons une déclinaison de FAN pour le réseau d'accès, qui
complète la vision de bout en bout pour le trafic. L'équité entre les flots
n'est alors plus une solution satisfaisante, et il convient plutôt d'adapter une
solution neutre, basée sur la coopération de l'utilisateur, et lui permettant de
contrôle ses flots dans les sens montant et descendant.

## Publications liées à la thèse

### Conférences internationales

#$bib->Select(array('keywords' => 'conference,phd'));

### Workshops

#$bib->Select(array('keywords' => 'workshop,phd'));

## Manuscrit

La version finale du manuscrit de thèse est disponible en téléchargement
dans la colonne de droite sur cette page.

Download:
[![/static/img/pdf.png][Thèse (PDF)](/static/files/these-jordan-auge-submitted-20141012.pdf)
[![/static/img/pdf.png][CV (PDF)](/static/files/cv.pdf)
