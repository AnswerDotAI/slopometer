"""Score prose for simplicity and precision against plain-English reference rules

Modules:

- `slopometer.ai`: Ask a language model which sentences have a subject that does not do what its verb says
- `slopometer.cli`: The command line: score a file or stdin, warm
- `slopometer.core`: Tells, findings, the rule registry, and what the meter cannot see
- `slopometer.corpus`: Build the labeled corpus: weak positives from scored replies, mixed human negatives
- `slopometer.features`: Continuous measurements for learned scoring
- `slopometer.lexicon`: Word and phrase rules: banned vocabulary, hedges, fillers, and tacked-on clauses
- `slopometer.pangram`: Score prose with Pangram's AI detector, as an alternative to the rules
- `slopometer.para`: Paragraph rules: restatement, elegant variation, forced symmetry, and length
- `slopometer.rewrite`: Number the sentences of a Markdown file, a notebook or a Python file's docstrings for language models, compare the rewrites they suggest, and put rewrites into the file
- `slopometer.score`: Run every rule, weigh the findings, and report worst first
- `slopometer.segment`: Markdown becomes typed blocks that keep their file positions
- `slopometer.syntax`: The spaCy rules: sentences, clauses, passives, and the patterns anchored to them
- `slopometer.typesafe`: Ask TypeSafe's Jev model yes/no questions about text"""

__version__ = "0.0.8"
