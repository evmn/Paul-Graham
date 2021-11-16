#!/bin/bash
ebook-convert "Essays of Paul Graham.recipe" .mobi \
        --authors="Paul Graham" \
        --title="Essays of Paul Graham" \
        --pubdate="2021-10-24" \
        --output-profile=kindle_pw3 \
        --mobi-file-type=new \
        -vv
