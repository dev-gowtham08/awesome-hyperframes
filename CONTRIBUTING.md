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
2. Add an object to the array in `resources.json`.
3. Follow this format:

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

4. Replace the example values, use a unique slug, and keep the JSON valid (separate objects with commas, with no trailing comma after the last object).
5. Check that the link works, the description is accurate, and the resource is not already listed.
6. Open a pull request explaining why the addition is useful. A maintainer reviews it before merging.

Keep changes focused. Corrections and broken-link fixes can be submitted directly as pull requests.

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

To suggest a video, [open a video submission](https://github.com/dev-gowtham08/awesome-hyperframes/issues/new?template=video-submission.md), or choose **Issues → New issue → Submit a video** on GitHub. Include the original X post or other public video link, creator credit, a description, and the tools used. No fork or file edit is needed.

A maintainer reviews the submission, adds accepted videos to the private website's `projects.json`, and publishes the website update. An issue or a resource pull request does not automatically publish a video.

If you already opened a pull request to suggest a video, maintainers can review the suggestion there; there is no need to resubmit it as an issue.

Maintainers can refresh the public snapshot after updating the website data. Until syncing is configured, a change to one copy does not update the other.

## Future resource syncing

`resources.json` in this public repository is the source for learning resources. Submit new resources there; you do not need to duplicate them in the README.

The website does not consume this file yet, and README resource lists are not generated yet. A future integration can read the approved catalog to populate a website Resources page and generate README lists. Video syncing is also not configured.
