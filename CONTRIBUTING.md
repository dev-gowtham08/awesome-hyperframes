# Contributing

Share a video, credit its creator, and help others understand how it was made.

## Submit a video without editing files

Choose **Issues → New issue → Submit a video**, or [open the submission template](https://github.com/dev-gowtham08/awesome-hyperframes/issues/new?template=video-submission.md).

Include the original video link, creator name and profile, tools used, and a short description. Add the exact prompt if it is available for sharing; otherwise, say that you are providing an excerpt or summary.

You do not need to fork the repository or use VS Code. A maintainer reviews the submission before adding it.

## Submit a pull request

1. Fork this repository to your GitHub account.
2. Create a new branch, such as `add-my-video`.
3. Open `data/projects.json` on GitHub or in your local clone using VS Code.
4. Add your video object at the end of the array, before the closing `]`. Add a comma after the previous object, with no trailing comma after your new object.
5. Check that the video is not already listed and use a unique slug.
6. If working locally, run `python3 scripts/build_directory.py` to validate your entry and refresh the generated lists. Include those documentation changes in your commit. If editing on GitHub, a maintainer can run this step.
7. Commit your changes and push your branch if working locally.
8. Open a pull request from your branch to this repository’s `main` branch. Explain what you added and whether you are the creator.

Only edit video information in `data/projects.json`. The README’s counts and showcase, and all of `DIRECTORY.md`, are generated from it.

## Example entry

Replace the example values below with the real details. If the full prompt is unavailable, provide a short description and keep `prompt_partial` set to `true`.

```json
{
  "slug": "my-product-demo",
  "title": "My Product Demo",
  "creator": "Your name",
  "stack": ["Hyperframes"],
  "category": "Product Demo",
  "prompt": "A short description of the video and how it was made.",
  "prompt_partial": true,
  "videoUrl": "https://example.com/original-video",
  "creatorUrl": "https://example.com/creator",
  "duration": "0:30",
  "submittedAt": "2026-10-22T12:00:00Z"
}
```

| Field | What to provide |
| --- | --- |
| `slug` | A unique identifier using lowercase letters, numbers, and hyphens. |
| `title` | A clear video title. |
| `creator` and `creatorUrl` | The original creator’s name and public profile link. |
| `stack` | The tools actually used. Use `Hyperframes` for HyperFrames to match the existing data. |
| `category` | One of the categories below. |
| `prompt` | The shared prompt, an excerpt, or your description. |
| `prompt_partial` | `false` only for the exact full prompt; `true` for excerpts or descriptions. |
| `videoUrl` | The public original post or video page. |
| `duration` | Optional length in `m:ss` format. |
| `submittedAt` | Optional known date as an ISO timestamp with a timezone. Do not guess a date. |
| `thumbnailUrl` | Optional public image URL or existing website `/posters/` path. |
| `playbackUrl` | Optional direct media URL or existing website `/videos/` path. |
| `featured` | Optional boolean used by maintainers to prioritize showcase entries. |

Categories: `Product Demo`, `Motion`, `Marketing`, `Short Film`, `3D`, `Explainer`, `Education`, `Creative`, `Tutorial`, `Music`, or `AI`.

Do not invent media URLs or reuse another entry’s thumbnail. If you cannot supply them, omit the optional fields and mention that in your submission. The video can still appear in the complete directory without a preview image.

## Review and credit

- Link to the original source and credit the original creator.
- Label the tools accurately; do not describe an Opus-only or Remotion video as a HyperFrames creation without evidence.
- Keep summaries distinct from exact prompts. Include long prompts only when you have permission to share them or their license permits it.
- Preserve existing entries when adding yours. Corrections to existing entries are welcome; explain the change in your PR.

If you have already opened a video PR, there is no need to submit the same video through an issue.

## Updating the generated lists

Run these from the repository folder using Python 3.9 or later:

```bash
python3 scripts/build_directory.py
python3 scripts/build_directory.py --check
```

The command validates the data, rebuilds `DIRECTORY.md`, and updates only the marked sections of the README. Each category shows up to three previews, prioritizing HyperFrames entries, then featured entries, then known dates from newest to oldest. Entries without dates remain in the directory. Every video is included in the complete list.

`--check` reports invalid data or stale generated files without changing anything. These are local commands, not a scheduled job or GitHub Action.

## Website publishing

Merging a PR here updates this repository. It does not automatically update [madewithhyperframes.com](https://madewithhyperframes.com).

A maintainer transfers accepted changes to the private website repository’s `data/projects.json` and publishes the website update. Reconcile approved changes in both copies before refreshing the public copy, so community contributions are preserved.

## Corrections and removal

If you are a creator and want an entry corrected or removed, [open an issue](https://github.com/dev-gowtham08/awesome-hyperframes/issues) with the video link and requested change.
