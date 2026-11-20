# Release notes

<!-- do not remove -->

## 0.0.8

### New Features

- Resolve that/who relative clauses to head noun in inert-subject rules; add act/mind verbs, drop step from runners, extend judge/rewrite examples ([#14](https://github.com/AnswerDotAI/slopometer/issues/14))


## 0.0.7

### New Features

- Add rewrite module for two-model sentence review, --ai sentence judging, --vs git revision comparison, TypeSafe Jev client, tokenizer fixes ([#12](https://github.com/AnswerDotAI/slopometer/issues/12))


## 0.0.5

### New Features

- Rename tell 1 splices to tacked-on clauses (`tacked_dash`/semi/and rules), add per-tell advice to findings, pass fd root by keyword ([#11](https://github.com/AnswerDotAI/slopometer/issues/11))


## 0.0.4

### New Features

- Add Pangram AI scoring, multi-path/directory CLI, section/and-splice/inert-subject rules, mdhtml-based segmenting, zero-weight passives ([#10](https://github.com/AnswerDotAI/slopometer/issues/10))
- Score .py module docstrings with `score_path` and the CLI, and make the CLI path argument positional ([#8](https://github.com/AnswerDotAI/slopometer/issues/8))
- Adapt corpus fetchers to rgapi Path-returning fd/ls: use stat().`st_mtime`, `relative_to`(root), and p.name ([#7](https://github.com/AnswerDotAI/slopometer/issues/7))
- rescore em dash and semicolon splices at weight 4 ([#6](https://github.com/AnswerDotAI/slopometer/issues/6))
- Score Markdown cells of .ipynb files in `score_path`, with cell-aware finding locations exposed via Result.location and JSON output ([#5](https://github.com/AnswerDotAI/slopometer/issues/5))
- Skip short inputs and remove vocabulary novelty scoring ([#4](https://github.com/AnswerDotAI/slopometer/pull/4)), thanks to [@jph00](https://github.com/jph00)


## 0.0.3

### Bugs Squashed

- Include headings and lists in scoring density ([#3](https://github.com/AnswerDotAI/slopometer/pull/3)), thanks to [@jph00](https://github.com/jph00)


## 0.0.2

### New Features

- Import APIError from fasttransport ([#2](https://github.com/AnswerDotAI/slopometer/pull/2)), thanks to [@jph00](https://github.com/jph00)


## 0.0.1

- Init release
