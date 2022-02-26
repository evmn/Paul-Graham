#!/bin/bash
ebook-convert "calibre.recipe" .mobi \
        --authors="Paul Graham" \
        --title="Essays of Paul Graham" \
        --pubdate="2022-2-26" \
        --output-profile=kindle_pw3 \
        --mobi-file-type=new \
        -vv
