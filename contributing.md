# Contributing

Thanks for considering a contribution. Before opening a pull request, please check:

1. **Open source.** The project must have a public repository and an open source license. Commercial or closed source software does not belong here, use [awesome-civil-engineering](https://github.com/QuantumNovice/awesome-civil-engineering) for that. A project whose source or content is public under a more restrictive license (for example noncommercial terms) can be listed when it is a field standard or has no open alternative. State the restriction in the entry, as the OpenSees entry does.
2. **Relevant.** The project must be directly relevant to civil or infrastructure engineering, or to a discipline this list already covers (structural analysis, design code and calculation tools, earthquake engineering, geotechnical engineering, structural health monitoring, BIM, CAD and parametric modeling, digital twins, point clouds and photogrammetry, geospatial analysis, water and hydraulics, urban and infrastructure analytics, construction focused AI and ML, climate and resilience, open datasets used in these fields, or open learning resources for them).
3. **Documented and usable.** At minimum, the README must explain what the project does and how to install or run it. A research code dump with no explanation will not be merged.
4. **Not a duplicate.** Search the existing list first. If a very similar project already exists, explain in the PR description why the new one is a better fit or a meaningful addition.
5. **Maintained, or clearly still useful.** Actively maintained projects are preferred. An unmaintained project can still be included if it remains the best or only open source option for its niche, note this in your PR description.

## Evidence for proposed entries

Include these links or notes in the pull request description so reviewers
can check the proposal efficiently:

- Link directly to the project's license file or official license statement.
- Link to documentation that explains the project's purpose and how to use it.
- Note a recent release or maintenance activity. If the project is no longer
  maintained, explain why it remains useful for this list.
- Confirm that you checked the existing list for duplicates.

These checks support human review. They do not replace a review of the
license terms or guarantee that a project is legally compatible.

## Format

Add your entry to the correct section, in this format:

```markdown
- [Project Name](https://github.com/owner/repo#readme) - One or two sentences describing what it does and why it belongs in this list, written in your own words rather than copied from the project's README. Python, MIT.
```

End the entry with a short tag sentence that gives the main language and the license as an SPDX identifier, for example `Python, MIT.` or `C++, GPL-3.0.`. Entries in Open Datasets and Learning Resources carry the license only, entries that are not hosted on GitHub carry no tag. The monthly health check compares each tag with what GitHub reports. If GitHub cannot classify the license, add the value you read from the license file to `.github/tag-overrides.txt`. Maintainers can rewrite all tags with `python3 scripts/update_tags.py`.

Keep descriptions factual and neutral. Do not use marketing language.

Add new entries to `README.md` only. The Turkish translation in `README.tr.md` is kept in sync by the maintainers.

## Adding a new section

If your project does not fit any existing section and you believe there are enough related projects to justify a new one, open an issue first to discuss scope before submitting a pull request.

## Checking your changes before opening a pull request

CI runs [awesome-lint](https://github.com/sindresorhus/awesome-lint) on pushes and pull requests. Run the style check before submitting:

```bash
npm ci
npm run lint
```

The link checker runs separately on pull requests and every Tuesday.

On a branch that has not been pushed yet, the lint run can fail with `Awesome list must reside in a valid git repository`. The check looks up the remote of the current branch, which is only set after the first push. Push the branch with `git push -u origin <branch>`, or set the remote yourself, and run the lint again:

```bash
git config branch.<branch>.remote origin
```

If you change anything under `scripts/` or the health check files under `.github/`, run the tests as well:

```bash
python3 -m unittest discover -s tests -v
```

## License

The list itself (the selection, arrangement and descriptions in this repository) is released under [CC0 1.0](LICENSE). This does not extend to the third party projects it links to, each of which remains under its own license.
