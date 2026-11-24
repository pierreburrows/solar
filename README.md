# EVelec website

Static website for EVelec Ltd: EV charge point, Solar PV and battery storage installers in Brighton & the South East.

- `site/` is the live website (deployed by Vercel as-is, no build step; see `vercel.json`).
- `build.py` generates every page in `site/`. Edit the `CONFIG` block (phone, email, form endpoint, review count) or page content, then run:

  ```bash
  python3 build.py
  ```

- `site/assets/style.css` and `site/assets/main.js` hold the design and interactions.
- `site/assets/video/` holds the hero film and service animations (generated with Higgsfield, 1080p web versions plus lighter mobile versions of the hero clips).
- `content/reviews.md` holds the curated Google reviews; `source-photos/` holds the original installation photos.
