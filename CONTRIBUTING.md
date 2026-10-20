# Contributing

Help people learn HyperFrames and find resources they can use in their own projects.

## Suggest a resource

[Open a resource submission](https://github.com/dev-gowtham08/awesome-hyperframes/issues/new?template=resource-submission.md). You do not need to clone the repository or edit code.

Include:

- The resource title and a direct URL.
- A category: documentation, skill, tool, tutorial, workflow, prompt, template, or source code.
- A short explanation of what someone can learn or do with it.
- The creator's name and profile or website.
- Any cost, account requirements, dependencies, or reuse restrictions.
- An example video or source repository, if available.

If you created or maintain the resource, mention that. Self-submissions are welcome.

## Submit a pull request

1. Fork this repository and create a branch.
2. Add your resource to the appropriate section in `README.md`.
3. Follow this format:

   ```markdown
   - [Resource title](https://example.com/resource) by [Creator](https://example.com/creator) — A short description of what it helps people do.
   ```

4. Check that the link works, the description is accurate, and the resource is not already listed.
5. Open a pull request explaining why the addition is useful.

Keep changes focused. Corrections and broken-link fixes can be submitted directly as pull requests.

## What makes a useful resource?

- It is relevant to creating, editing, rendering, or learning about HyperFrames.
- It provides concrete instructions, reusable material, or an inspectable example.
- It credits the original creator and links to the original source.
- It states important prerequisites and costs.
- Reusable code and templates include clear license information.

Link to a creator's work instead of copying their files into this repository without permission.

## Video submissions

Video entries and creator details live in the website's `projects.json`. Do not create a second video directory here.

To suggest a video, use the resource submission template, choose **Video suggestion**, and include the original X post or other source, creator credit, and the video page on [madewithhyperframes.com](https://madewithhyperframes.com) if one exists. A maintainer can review it for the website.

Submitting an issue here does not automatically publish a video. README syncing from `projects.json` is planned but is not configured yet.

## Future resource syncing

For this initial setup, resource links are maintained in `README.md`. A shared `resources.json` alongside the website's `projects.json` is planned to supply a website Resources page and generate this README's resource lists. That automation will be set up separately.
