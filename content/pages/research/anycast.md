---
title: Anycast enumeration and geolocation
slug: anycast
---

NOTE: The project page is hosted at [https://anycast.telecom-paristech.fr/].
This page is a personal summary, freely adapted to content published there.

## Overview

Use of anycast IP addresses has increased in the last few years: once relegated
to DNS root and top-level domain servers, anycast is now commonly used to assist
distribution of general purpose content by CDN providers. Yet, most anycast
discovery methodologies rely so far on DNS, which limits their usefulness to
this particular service. This raises the need for protocol agnostic
methodologies, that should additionally be as lightweight as possible in order
to scale up anycast service discovery. Our anycast discovery method allows for
exhaustive and accurate enumeration and city-level geolocation of anycast
replicas, with the constraints of only leverages a handful of latency
measurements from a set of known probes. The method, which exploits an iterative
workflow to enumerate (optimization problem) and geolocate (classification
problem) anycast instances, is described in [1],[2],[3]. The method is
so lightweight and protocol agnostic that we were able to perform several
censuses of the whole IPv4 Internet (during March 2015), as described in [4]. We
keep performing such censuses and making this dataset available to the
scientific community to the interactive Google maps interfaces accessible below.

Googlemaps
<https://anycast.telecom-paristech.fr/map/>
    Dataset
    Github

## Datasets, Code and Services

You can find all datasets and their description on
[https://anycast.telecom-paristech.fr/](the project website).

## About

I worked on Anycast during my Postdoc at Telecom ParisTech with Pr. Dario Rossi.
This work was part of Danilo Cicalese's Phd, and was done jointly with
Marc-Olivier Buob and Diana Joumblatt.

This work was motivated by discussion with Dario following our lab at TMA
workshop. My work has been mostly related to the measurement, analysis and the
optimization part. I wrote the initial version of the iGreedy algorithm, further
developed by Danilo.
