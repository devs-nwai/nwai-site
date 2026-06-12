# nwai.co reposition — handoff

This folder is the complete spec for the new nwai.co. 14 linked pages plus a shared
`styles.css`. Everything is plain HTML/CSS, no build tools, no dependencies.

## What's in here

| File | What it is |
|---|---|
| index.html | Homepage |
| fractional-caio.html | Fractional Chief AI Officer program |
| claude-deployment.html | 16-week Claude Deployment Program (matches the DSA briefing structure) |
| company-brain.html | Company Brain product page (anonymized NovaBrain-style mock) |
| case-study-*.html | 3 anonymized case studies |
| about.html | About + founding story + team |
| careers.html + role-*.html | Careers hub + 3 always-open roles |
| privacy.html / terms.html | Ported from the live site verbatim |
| styles.css | Shared design system (paper/ink/terracotta, Fraunces + Inter) |
| build-site.py | Regenerates every page. `python3 build-site.py` (edit, run, done) |

NOT in here: /claude. That page is the live Facebook ads LP and stays exactly as it is.
It's deliberately not in the nav.

## Viewing locally

The iClosed booking popup refuses to render on `file://` origins. Serve it:

    cd site && python3 -m http.server 8080   →   http://localhost:8080

## Two ways to ship

1. **Rebuild in Elementor (current plan).** These files are the pixel spec. Match them,
   don't reinterpret. Fonts: Fraunces (headlines), Inter (body), IBM Plex Mono (data bits),
   all on Google Fonts. Colors are CSS variables at the top of styles.css.
2. **Host static.** The files are production-grade as-is. Cloudflare Pages or any static
   host works. If we go this route, WP stays alive only until the blog decision is made.

## Launch checklist

- [ ] **Tracking first.** Paste the GTM / Meta Pixel snippet into every page `<head>`
      (there's a TODO comment slot). Verify the pixel fires and the booking conversion
      event tracks BEFORE pointing the domain. The ads are the business.
- [ ] **iClosed popup.** Already wired on every Book a call button
      (`data-iclosed-link="https://app.iclosed.io/e/nwai/book-a-call"` +
      `data-embed-type="popup"` + widget.js in head). Test over http. If it refuses on
      the real domain, add the domain in iClosed's embed/allowlist settings.
- [ ] **Client logos.** The trusted-by band uses styled wordmarks. Replace with real logo
      files: Novacore, Delphi Construction, Jacobsen Construction (CONFIRM spelling
      Jacobsen vs Jacobson against their actual logo), Keeley Construction. A possible
      5th logo is unresolved (Wyatt's list said "Cloude", unclear).
- [ ] **Images.** Team headshots currently hotlink to nwai.co/wp-content uploads. Copy
      the image files into the new host before WP ever goes away.
- [ ] **Redirects.** All old /solutions/*, /industries/*, /locations/* pages 301 to the
      new homepage or closest relevant page. Pull HubSpot attribution first and keep any
      page that has ever sourced a booked call. Blog is removed from nav for now
      (deliberate, decision later), don't delete the posts yet.
- [ ] **Meta/OG.** Add favicon, og:image, and meta descriptions per page. Site pages are
      indexable; /claude keeps noindex,nofollow.
- [ ] **Email.** Public contact is consulting@nwai.co everywhere (incl. careers mailtos).
      No wyatt@ on the public site.
- [ ] **Final read.** Wyatt signs off on: the founding story (mom + Ubiquify mentions),
      the case-study numbers, and the About page before it goes live.

Questions on copy or design intent: ask Wyatt. Regenerating pages: edit build-site.py and run it.
