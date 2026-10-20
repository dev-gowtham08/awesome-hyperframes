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

Choose the file that matches your contribution:

| Contribution | File to edit |
| --- | --- |
| A video and its creator details | [projects.json](projects.json) |
| A tutorial, skill, tool, prompt, template, or source code link | [resources.json](resources.json) |

1. Fork this repository to your GitHub account.
2. Create a new branch in your fork, such as `add-my-video` or `add-my-resource`.
3. Edit the appropriate JSON file on GitHub or in your local clone using VS Code. Add your new object at the end of the array, before the closing `]`.
4. Add a comma after the previous object. Do not add a trailing comma after your new object. Use a unique slug and check that your entry is not already listed.
5. Save and commit your changes. If working locally, push your branch to your fork.
6. Open a pull request from your branch to this repository's `main` branch. Describe what you added and credit the creator.

A maintainer reviews the pull request before merging. Merging a video entry here does not automatically publish it on the website; a maintainer must also update the private website repository.

Keep changes focused. Corrections and broken-link fixes can be submitted directly as pull requests.

### Adding a video

Follow the structure of an existing entry in `projects.json`. Include the title, a unique slug, creator name and profile URL, original video URL, tools used, category, duration, submission date, and prompt or description. Set `prompt_partial` to `true` for an excerpt or summary, and `false` only for the exact full prompt.

Preserve other creators' entries. Do not invent playback or thumbnail URLs; if you cannot supply the media details used by existing entries, mention that in the PR so a maintainer can complete them.

### Adding a learning resource

Add an object to `resources.json` using this format:

   ```json
   {
     "slug": "my-hyperframes-tutorial",
     "title": "My HyperFrames tutorial",
     "url": "https://example.com/tutorial",
     "category": "tutorial",
     "description": "A walkthrough for creating a product demo.",
     "creator": "Creator name",
     "creatorUrl": "https://example.com/creator",
     "relatedProjectSlugs": []
   }
   ```

Replace the example values and check that the links work and the description is accurate.

### Resource fields

All fields in the example are required. Use a lowercase, hyphen-separated `slug`.

Use one of these categories: `documentation`, `skill`, `tool`, `tutorial`, `workflow`, `prompt`, `template`, or `source-code`.

`relatedProjectSlugs` connects a resource to existing website videos using their exact slugs. Find them in the public [projects.json](projects.json) snapshot. Leave it as `[]` if you do not know the slug or there is no related video; a maintainer can fill it in. It does not provide access to the private website repository or publish a video.

An optional `prompt` field can contain an exact, shareable prompt. Keep summaries in `description`; do not present a summary as the creator's exact prompt. For long prompts, link to the original post.

Describe important prerequisites, costs, and reuse restrictions when known. A demonstration of a skill can be listed as a `workflow`; label it as a demo rather than implying it is downloadable source or an installation guide.

## What makes a useful resource?

- It is relevant to creating, editing, rendering, or learning about HyperFrames.
- It provides concrete instructions, reusable material, or an inspectable example.
- It credits the original creator and links to the original source.
- It states important prerequisites and costs.
- Reusable code and templates include clear license information.

Link to a creator's work instead of copying their files into this repository without permission.

## Video submissions

This repository's [projects.json](projects.json) is a public snapshot of the video directory. The private website repository's `projects.json` remains the source for website updates. Keep learning resources in `resources.json` and video records in `projects.json`.

To add a video through a pull request, fork this repository, create a branch, and append your entry to `projects.json` using the [steps above](#submit-a-pull-request).

If you prefer to suggest a video without editing files, [open a video submission](https://github.com/dev-gowtham08/awesome-hyperframes/issues/new?template=video-submission.md), or choose **Issues → New issue → Submit a video** on GitHub. Include the original X post or other public video link, creator credit, a description, and the tools used.

A maintainer reviews the submission, adds accepted videos to the private website's `projects.json`, and publishes the website update. An issue or a resource pull request does not automatically publish a video.

If you already opened a pull request to suggest a video, maintainers can review the suggestion there; there is no need to resubmit it as an issue.

Maintainers should transfer approved changes between the public catalog and the private website data before refreshing this snapshot, so contributions are preserved. Until syncing is configured, a change to one copy does not update the other.

## Future resource syncing

`resources.json` in this public repository is the source for learning resources. Submit new resources there; you do not need to duplicate them in the README.

The website does not consume this file yet, and README resource lists are not generated yet. A future integration can read the approved catalog to populate a website Resources page and generate README lists. Video syncing is also not configured.
