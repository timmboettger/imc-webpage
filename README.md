# IMC 2017 website template and scripts

This repository contains the scripts and templates that were used to build and maintain the ACM IMC 2017 webpage - https://conferences.sigcomm.org/imc/2017/

## Tools

The website has, among others, been built with the following tools:
* Bootstrap CSS framework - https://getbootstrap.com/docs/3.3/
* Hugo static site generator - http://gohugo.io/
* HTML Tidy - http://www.html-tidy.org/

## Content

Most of the content is defined in the MarkDown files in content/. The header of each file can be used to modify title, menu placement and menu ordering.

## Generation of Accepted Papers, Accepted Posters and Program

These three pages can be generated automatically from a HotCRP JSON export. In the folder data/ two sample json files for posters and program (with accepted papers) can be found. These need to be renamed from *.json.template to *.json to be usable. There are two files, one file for the posters, and one joint file for program and papers. There are three shortcodes that use these json files to generate pages. The shortcodes are {{< accepted_posters >}}, {{< accepted_papers >}} and {{< program >}}. The first two generate a list of accepted posters and papers resp., the last one generates the full program. See content/posters.md or content/program.md for example how to use the shortcodes.

### hotcrp-json-to-json.py

This Python script converts a HotCRP export into a json file that can be used to generate pages. The script by default updates an existing program file. This is useful to propagate changes from HotCRP (likes abstracts, paper titles or author info) from HotCRP to the webpage. Either --papers or --posters has to be given as argument to specifify which output file to use. Rudimentary output files can be created with the optional --create argument. The script however does not generate a full program structure, this has to be copied from the program.json.template file.

### program.json

This file contains multiple elements:
* days: List of event days. Each day has an identifier (_id)
* timeslots: List of timeslots. Each timeslot is assigned to a specific day, the sorting over the day is defined via weights. A timeslot can have an optional page_url, which is converted into a link.
* papers: List of accepted papers, with standard paper metadata. PDF can contain a link to the paper PDF, slides can contain a link to the paper slides. If data artifacts are given, a link can be put into artifact. The timeslot parameter assignes the paper to a specific timeslot in the program, sorting of paper in a timeslot is done via weights.

### posters.json

Same format as above, but without timeslots and days.

## Layouts

The folder layouts/ contains the layouts for the page. The base layout is defined in layouts/_default/baseof.html. Partials for header, footer, menu and others are taken from the layouts/partials folder. The folder layouts/shortcodes contains useful shortcodes which can be used in the MarkDown files in content. Shortcodes are either used for convenience (papers and posters), or for consistency. Important dates are defined as shortcode, so that they always are consistent across the page, as they are generated from the same source.

## Static

The static/ folder contains static CSS, JS and fonts.

## config.toml

General website configuration like base URL, page title and definitions for sub menus.

## Makefile

The Makefile contains the following targets:
* main: Start local dev server that also shows drafts
* dev: Generate pages for dev instance (i.e., also generate drafts)
* dev-no-tidy: Generate pages for dev instance, but do not call HTML Tidy. Useful to debug HTML errors before tidy cleans the code and complains.
* tidy: Run HTML Tidy on generated HTML pages.
* dev-live: Generate live pages (i.e., no drafts), but use dev instance URL. Useful to make dev instance an exact copy of the live instance. Live pages cannot be uploaded to the dev instance because of the different URLs for embedded objects and links.
* live: Generate pages for live instance (i.e., do not generate draft pages)
