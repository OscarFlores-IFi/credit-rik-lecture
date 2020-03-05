#!/usr/bin/env bash

target_file="exam-0${1}"
printf "rmarkdown::render('%s.Rmd', output_format='pdf_document')" "${target_file}" | R --vanilla --quiet
