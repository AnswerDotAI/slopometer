"""Score prose for simplicity and precision against plain-English reference rules

Modules:

- `slopometer.cli`: The command line: score a file or stdin, warm
- `slopometer.core`: Tells, findings, the rule registry, and what the meter cannot see
- `slopometer.corpus`: Build the labeled corpus: weak positives from scored replies, mixed human negatives
- `slopometer.features`: Continuous measurements for learned scoring
- `slopometer.lexicon`: Word and phrase rules: banned vocabulary, hedges, fillers, and splices
- `slopometer.para`: Paragraph rules: restatement, elegant variation, forced symmetry, and coinage
- `slopometer.score`: Run every rule, weigh the findings, and report worst first
- `slopometer.segment`: Markdown becomes typed blocks that keep their file positions
- `slopometer.syntax`: The spaCy rules: sentences, clauses, passives, and the patterns anchored to them"""

__version__ = "0.0.2"
