# Contributing

Thanks for considering a contribution. Before opening a pull request, please check:

1. **Open source.** The project must have a public repository and an open source license. Commercial or closed source software does not belong here, use [awesome-civil-engineering](https://github.com/QuantumNovice/awesome-civil-engineering) for that.
2. **Relevant.** The project must be directly relevant to civil or infrastructure engineering, or to a discipline this list already covers (structural analysis, earthquake engineering, structural health monitoring, BIM, digital twins, geospatial analysis, urban and infrastructure analytics, construction focused AI and ML, climate and resilience, or open datasets used in these fields).
3. **Documented and usable.** At minimum, the README must explain what the project does and how to install or run it. A research code dump with no explanation will not be merged.
4. **Not a duplicate.** Search the existing list first. If a very similar project already exists, explain in the PR description why the new one is a better fit or a meaningful addition.
5. **Maintained, or clearly still useful.** Actively maintained projects are preferred. An unmaintained project can still be included if it remains the best or only open source option for its niche, note this in your PR description.

## Format

Add your entry to the correct section, in this format:

```markdown
- [Project Name](https://github.com/owner/repo#readme) - One or two sentences describing what it does and why it belongs in this list, written in your own words rather than copied from the project's README.
```

Keep descriptions factual and neutral. Do not use marketing language.

## Adding a new section

If your project does not fit any existing section and you believe there are enough related projects to justify a new one, open an issue first to discuss scope before submitting a pull request.

## Checking your changes before opening a pull request

This repository runs [awesome-lint](https://github.com/sindresorhus/awesome-lint) in CI to catch structural and formatting issues (table of contents, heading order, duplicate links, entry format) on every push and pull request. Run it locally before submitting:

```bash
npm install
npm run lint
```

Also check that every link you added actually resolves; the link checker workflow in this repository does this automatically on pull requests too.
