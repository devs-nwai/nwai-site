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

ALSO in here: `claude.html` — the Facebook ads landing page, to be stood up at
nwai.co/claude. Rules for this one page: keep its meta noindex,nofollow, keep it OUT of
the nav and OUT of sitemap.xml, and rebuild it byte-faithful (the layout is matched to
the converting live page). Its video embeds (Vidalytics) and inline booking widget
(iClosed) are live third-party embeds and must be carried over exactly. Known pre-launch
items on this page: the Google-style review cards are placeholders pending real
permission-cleared reviews, and the top-bar scarcity line must be literally true.

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

- [ ] **Tracking first.** The ads are the business; verify everything below fires BEFORE
      pointing the domain. Pulled from the live site source 2026-06-10:

      1. **GTM container `GTM-56W2P5N8`** (on every live page incl. /claude). Put the two
         standard snippets on EVERY new page:

         In `<head>`, as high as possible:
         ```
         <!-- Google Tag Manager -->
         <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
         new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
         j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
         'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
         })(window,document,'script','dataLayer','GTM-56W2P5N8');</script>
         <!-- End Google Tag Manager -->
         ```
         Immediately after `<body>`:
         ```
         <!-- Google Tag Manager (noscript) -->
         <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-56W2P5N8"
         height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
         <!-- End Google Tag Manager (noscript) -->
         ```

      2. **Facebook domain verification** in every `<head>` (ads account breaks without it):
         `<meta name="facebook-domain-verification" content="uvurknwfoozz7aou0s49waz7rdd54y" />`

      3. **The Meta Pixel + booking conversion live INSIDE the GTM container**, not on the
         page. Awais needs GTM access. After cutover, check the container's triggers: if any
         conversion fires on an Elementor-specific selector or old URL, remap it. The new
         pages keep `#book` anchors + the same iClosed embeds.

      4. **View-source check on nwai.co and nwai.co/claude** for anything loaded OUTSIDE
         GTM; copy any hits verbatim: `fbq(`, `connect.facebook.net`, `gtag(`, `G-`,
         `retention` (privacy policy has a retention.com opt-out clause, so it's likely
         live; keeping it is a business decision, it's an email-identity tracker),
         `hs-scripts` (HubSpot), `hotjar`, `clarity`, `iclosed`, `vidalytics`.

      5. **Favicon:** grab `https://nwai.co/wp-content/uploads/2025/07/favicon.png` before
         WP dies. Do NOT migrate the live og:images (homepage uses a headshot, /claude uses
         a fabricated review screenshot); make a proper og:image fresh.
- [ ] **iClosed popup.** Already wired on every Book a call button
      (`data-iclosed-link="https://app.iclosed.io/e/nwai/book-a-call"` +
      `data-embed-type="popup"` + widget.js in head). Test over http. If it refuses on
      the real domain, add the domain in iClosed's embed/allowlist settings.
- [ ] **Client logos.** REMOVED from the site entirely (Wyatt, 2026-06-10) pending client
      permission. Do NOT re-add any client names or logos until Wyatt confirms clearance
      per client. When cleared, the band goes back in the homepage results section
      (the build script has the removal as a tagged transform, easy to revert).

- [ ] **Images.** Team headshots currently hotlink to nwai.co/wp-content uploads. Copy
      the image files into the new host before WP ever goes away.
- [ ] **Redirects.** All old /solutions/*, /industries/*, /locations/* pages 301 to the
      new homepage or closest relevant page. Pull HubSpot attribution first and keep any
      page that has ever sourced a booked call. Blog is removed from nav for now
      (deliberate, decision later), don't delete the posts yet.
- [x] **SEO basics (added 2026-06-10, generated by build-site.py).** Every page now has a
      unique meta description, a self-referencing canonical, OG/Twitter tags, and an
      em-dash-free title. `sitemap.xml` (14 URLs) and `robots.txt` are generated by the
      build. RULES FOR THE DEV: (1) page slugs MUST match the canonicals exactly
      (`nwai.co/fractional-caio/` etc., extensionless, trailing slash) or fix canonicals +
      sitemap to the real URLs; (2) do NOT Disallow /claude in robots.txt, it relies on its
      meta noindex,nofollow and is deliberately excluded from the sitemap; (3) after DNS
      cutover, submit https://nwai.co/sitemap.xml in Search Console (Wyatt does this);
      (4) WordPress/Yoast must not emit a second title/description/canonical set, use these.
- [ ] **Still pending: favicon + og:image.** Neither asset exists yet. Add both before
      launch (og:image is what makes shared links show a card in Slack/LinkedIn).
- [ ] **Email.** Public contact is consulting@nwai.co everywhere (incl. careers mailtos).
      No wyatt@ on the public site.
- [ ] **Press ticker.** The "As covered in" marquee above the footer uses typographic
      wordmarks as placeholders. Swap in official press logos (greyscale) at build. BEFORE
      launch: verify each outlet's actual article from the Ahrefs backlink URLs and save
      PDFs. CIO confirmed by Wyatt (landed Feb 2026; no link in the Ahrefs export, so get the
      article URL from him). Dates in the captions come from Ahrefs first-seen and
      should be checked against the real articles.
- [ ] **Final read.** Wyatt signs off on: the founding story (mom + Ubiquify mentions),
      the case-study numbers, and the About page before it goes live.

Questions on copy or design intent: ask Wyatt. Regenerating pages: edit build-site.py and run it.
