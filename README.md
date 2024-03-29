# 1. Enumerates the headers in a markdown file
Enumerate headers in markdown file.

## 1.1 Usage:
Run from the command line
```bash
markdown-enum inputFile.md outputFile.md
```
The script will parse `someFile.md`, add an enumeration to each header and output
the result to the file named `outputFile.md`.
All previously existing headers will be overriden. So a useful scenario is
```bash
markdown-enum inputFile.md inputFile.md
```

## 1.2 Install:
Requires python 3.

```bash
pip install enumerate-markdown
```

## 1.3 Assumed markdown syntax:

The markdown syntax assumed is the one used by mistune, called "Sane CommonMark"

https://mistune.readthedocs.io/en/latest/intro.html#sane-commonmark

But, with a fine twist: headings defined by a single `-` or single `=` are considered too.  For example:

```markdown
This is a heading
-
This is also a heading
=
``` 
