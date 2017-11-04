# IMC 2017 website template and scripts

This repository contains the scripts and templates that were used to build and maintain the ACM IMC 2017 webpage - https://conferences.sigcomm.org/imc/2017/

## Tools

The website has, among others, been built with the following tools:
* Bootstrap CSS framework - https://getbootstrap.com/docs/3.3/
* Hugo static site generator - http://gohugo.io/
* HTML Tidy - http://www.html-tidy.org/

## Implementation details

Most of the content is static, however the list of accepted posters and the program are generated dynamically from json files. The repository contains two dummy files in the data folder. There also is a script that can parse a HotCRP json export and create/ update the paper/ poster metadata for the webpage.
