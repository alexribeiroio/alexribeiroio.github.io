{{- $slug := replaceRE "^[0-9]{2}-" "" .Name -}}
+++
title = '{{ replace $slug "-" " " | humanize }}'
description = ''
date = '{{ .Date }}'
lastmod = '{{ .Date }}'
slug = '{{ $slug }}'
postId = '{{ crypto.SHA256 (printf "%s-%s" .Path .Date) }}'
draft = true
categorias = []
tags = []
comments = true
+++

Escreva sua introdução aqui.

## Desenvolvimento

Desenvolva o assunto e inclua links para suas fontes.
