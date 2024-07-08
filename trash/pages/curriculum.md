---
title: Curriculum
slug: curriculum
---

_This curriculum vitae is an extended version (compared to the PDF
version_

__Jordan AUGE__
![/static/img/mail.png]() 22, rue d'Estienne d'Orves

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;92120, Montrouge, France
![/static/img/cellular.png]() +33 6 82 39 27 76
![/static/img/phone.png']() +33 1 42 09 11 03<br/>
<img src='../img/email.png' alt=''/> <a href='mailto:jordan.nospam.auge@free.fr'>jordan.nospam.auge@free.fr</a><br/>
<br/>
French citizen, born on sept. the 6th, 1980<br/><br/>
<!--  Permis B, possède une voiture<br/><br>-->
</p>

### Career history

{% for experience in EXPERIENCE(lang) %}
- __{{experience.year}}__ : {{experience.position}}, in {{experience.lab}}<br/>
{{experience.description}}

{% endfor %}

### Internships

{% for internship in INTERNSHIP(lang) %}
- __{{internship.year}}__ : {{internship.type}}, in {{internship.lab}}<br/>
{{internship.description}}

{% endfor %}

### Education

{% for formation in FORMATION(lang) %}
- __{{formation.year}}__ : {{formation.position}}, in {{formation.lab}}<br/>
{{formation.description}}

{% endfor %}

### Knowledge and skills

Download:<br/>
[![](/static/img/pdf.png)](/static/files/cv.pdf)

See also:<br/>
[![](/static/img/link.png)My research page](/static/img/link.png)
[![](/static/img/link.png)My personal projects](/static/img/link.png)
