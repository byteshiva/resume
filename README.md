# Resume

This is where I host *[my personal resume](latest.pdf)*.

## Generating File Formats

This reads the asciidoc latest.adoc file, and generates html and pdf files.

```{r, engine='bash', count_lines}
sh generate.bash
```

Github action pull the code and generates html and pdf and publish to gh-pages.