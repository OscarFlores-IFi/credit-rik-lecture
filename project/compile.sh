#!/usr/bin/env bash

target_file="projects"
printf "rmarkdown::render('%s.Rmd', output_format='pdf_document')" "${target_file}" | R --vanilla --quiet
