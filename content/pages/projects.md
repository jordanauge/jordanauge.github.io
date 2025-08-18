---
title: Projects
slug: projects
status: published
template: fullpage
---

{% from 'project.html' import project_tpl %}

# Projects

{% for project in 'projects'|load_data %}
{{ project_tpl(project) }}
{% endfor %}
