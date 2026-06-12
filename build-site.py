#!/usr/bin/env python3
"""Generate the NWAI site mockup pages (shared styles + linked pages).
Output: Brain/_files/concepts/website-reposition-2026/site/
"""
import os, re

SRC = "/sessions/lucid-focused-carson/mnt/Claude/Brain/_files/concepts/website-reposition-2026"
OUT = os.path.join(SRC, "site")
os.makedirs(OUT, exist_ok=True)

# ---------- shared CSS: take v3's inline styles, add subpage styles ----------
v3 = open(os.path.join(SRC, "nwai-homepage-mockup-v3.html")).read()
base_css = re.search(r"<style>(.*?)</style>", v3, re.S).group(1)

extra_css = """
  /* ---- subpage additions ---- */
  .page-hero { padding: 90px 0 70px; border-top: none; }
  .page-hero h1 { font-size: clamp(36px, 5vw, 62px); max-width: 880px; margin-bottom: 24px; }
  .page-hero .lede { font-size: clamp(17px, 2vw, 20px); color: var(--ink-soft); max-width: 660px; }
  .page-hero .lede strong { color: var(--ink); }
  .prose { max-width: 720px; }
  .prose h2 { font-size: clamp(26px, 3.4vw, 38px); margin: 48px 0 18px; }
  .prose h2:first-child { margin-top: 0; }
  .prose p { font-size: 17px; color: var(--ink-soft); margin-bottom: 18px; }
  .prose p strong { color: var(--ink); }
  .prose ul { margin: 0 0 18px 22px; color: var(--ink-soft); font-size: 17px; }
  .prose li { margin-bottom: 8px; }
  .stat-strip { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0; border-top: 1px solid var(--hairline); border-bottom: 1px solid var(--hairline); margin: 40px 0; }
  @media (max-width: 720px) { .stat-strip { grid-template-columns: 1fr; } }
  .stat-cell { padding: 28px 24px 28px 0; border-right: 1px solid var(--hairline-soft); }
  .stat-cell:last-child { border-right: none; }
  .stat-cell + .stat-cell { padding-left: 24px; }
  @media (max-width: 720px) { .stat-cell { border-right: none; padding-left: 0 !important; } }
  .stat-cell .n { font-family: "Fraunces", Georgia, serif; font-size: 30px; font-weight: 600; color: var(--terra); }
  .stat-cell .l { font-size: 13px; color: var(--ink-soft); margin-top: 4px; }
  .legal { max-width: 760px; }
  .legal h1 { font-size: clamp(32px, 4vw, 48px); margin-bottom: 10px; }
  .legal .updated { color: var(--ink-soft); font-size: 14px; margin-bottom: 40px; }
  .legal h2 { font-size: 22px; margin: 38px 0 12px; }
  .legal p, .legal li { font-size: 15.5px; color: var(--ink-soft); margin-bottom: 12px; }
  .legal ul { margin: 0 0 14px 22px; }
  .cta-band { background: var(--ink); color: var(--paper); border-radius: 16px; padding: 56px 48px; margin-top: 80px; }
  .cta-band h2 { color: var(--paper); font-size: clamp(26px, 3.4vw, 38px); max-width: 640px; margin-bottom: 14px; }
  .cta-band p { color: rgba(250,247,241,0.65); max-width: 540px; margin-bottom: 28px; font-size: 16.5px; }
  .cta-band em.acc { color: #E8916F; }
  .crumb { font-size: 13px; color: var(--ink-soft); margin-bottom: 20px; }
  .crumb a { color: var(--ink-soft); text-decoration: none; }
  .crumb a:hover { color: var(--ink); }
  .perm-grid { background: #fff; border: 1px solid var(--hairline); border-radius: 14px; overflow: hidden; margin: 36px 0; }
  .perm-head, .perm-row { display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; }
  .perm-head { background: var(--paper); border-bottom: 1px solid var(--hairline); }
  .perm-head div { padding: 14px 18px; font-size: 12px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--ink-soft); }
  .perm-row { border-bottom: 1px solid var(--hairline-soft); }
  .perm-row:last-child { border-bottom: none; }
  .perm-row div { padding: 13px 18px; font-size: 14.5px; color: var(--ink-soft); }
  .perm-row div:first-child { font-family: "IBM Plex Mono", monospace; font-size: 13px; color: var(--ink); }
  .yes { color: #4F9D6F; font-weight: 700; }
  .no { color: var(--terra); font-weight: 700; }
  .note-flag { background: rgba(194,91,54,0.08); border: 1px dashed rgba(194,91,54,0.4); border-radius: 10px; padding: 18px 22px; font-size: 15px; color: var(--ink-soft); margin: 24px 0; }
  .note-flag strong { color: var(--terra); }
  .steps-vert { border-top: 1px solid var(--hairline); margin-top: 36px; }
  .step-v { display: grid; grid-template-columns: 90px 220px 1fr; gap: 28px; padding: 28px 0; border-bottom: 1px solid var(--hairline-soft); }
  @media (max-width: 760px) { .step-v { grid-template-columns: 1fr; gap: 6px; } }
  .step-v .num { font-family: "IBM Plex Mono", monospace; font-size: 13px; color: var(--terra); padding-top: 6px; }
  .step-v h3 { font-family: "Fraunces", Georgia, serif; font-size: 21px; font-weight: 600; }
  .step-v p { font-size: 15.5px; color: var(--ink-soft); max-width: 560px; }

  /* ---- nav dropdowns ---- */
  .menu-item { position: relative; }
  .menu-item > a.top {
    color: var(--ink-soft); text-decoration: none; font-size: 14.5px; font-weight: 500;
    display: inline-flex; align-items: center; gap: 5px; padding: 8px 0;
  }
  .menu-item > a.top:hover { color: var(--ink); }
  .menu-item > a.top .car { font-size: 9px; opacity: 0.6; transform: translateY(1px); }
  .dropdown {
    position: absolute; top: 100%; left: -18px; min-width: 280px;
    background: #fff; border: 1px solid var(--hairline); border-radius: 12px;
    box-shadow: 0 18px 44px -18px rgba(32, 40, 58, 0.28);
    padding: 10px; display: none; z-index: 60;
  }
  .menu-item:hover .dropdown, .menu-item:focus-within .dropdown { display: block; }
  .dropdown a {
    display: block; padding: 11px 14px; border-radius: 8px; text-decoration: none;
    color: var(--ink) !important; font-size: 14.5px !important; font-weight: 600;
  }
  .dropdown a .d { display: block; font-weight: 400; font-size: 12.5px; color: var(--ink-soft); margin-top: 2px; }
  .dropdown a:hover { background: var(--paper); }
  .dropdown .dd-label {
    padding: 8px 14px 4px; font-size: 10.5px; font-weight: 700; letter-spacing: 0.14em;
    text-transform: uppercase; color: var(--ink-soft);
  }
  .dropdown hr { border: none; border-top: 1px solid var(--hairline-soft); margin: 8px 6px; }

  /* ---- product mock (Company Brain page) ---- */
  .pmock { background: #0F1512; border: 1px solid rgba(255,255,255,0.08); border-radius: 14px; overflow: hidden; box-shadow: 0 28px 64px -28px rgba(15,21,18,0.6); font-family: "Inter", sans-serif; }
  .pmock-nav { display: flex; align-items: center; gap: 18px; padding: 13px 18px; border-bottom: 1px solid rgba(255,255,255,0.07); }
  .pmock-logo { display: flex; align-items: center; gap: 8px; color: #EDEFEA; font-weight: 700; font-size: 13.5px; }
  .pmock-logo .ic { width: 20px; height: 20px; border-radius: 5px; background: #4F9D6F; display: inline-block; }
  .pmock-tabs { display: flex; gap: 6px; }
  .pmock-tab { font-size: 12px; color: #9BA8A0; padding: 5px 11px; border-radius: 6px; }
  .pmock-tab.act { background: rgba(79,157,111,0.18); color: #7BC79A; font-weight: 600; }
  .pmock-flow { display: grid; grid-template-columns: 1fr 24px 1fr 24px 1fr 24px 1fr; align-items: stretch; gap: 0; padding: 18px; border-bottom: 1px solid rgba(255,255,255,0.07); }
  @media (max-width: 760px) { .pmock-flow { grid-template-columns: 1fr; } .pmock-arrow { display: none; } }
  .pmock-step { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 12px 14px; }
  .pmock-step .s-t { color: #EDEFEA; font-size: 12.5px; font-weight: 700; }
  .pmock-step .s-k { color: #7BC79A; font-size: 9.5px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin: 3px 0; }
  .pmock-step .s-d { color: #9BA8A0; font-size: 11px; }
  .pmock-arrow { display: flex; align-items: center; justify-content: center; color: #5C6B62; font-size: 14px; }
  .pmock-treehead { display: flex; justify-content: space-between; align-items: center; padding: 12px 18px 4px; color: #EDEFEA; font-size: 12.5px; font-weight: 600; }
  .pmock-treehead .vt { font-size: 10.5px; color: #9BA8A0; border: 1px solid rgba(255,255,255,0.12); border-radius: 6px; padding: 3px 9px; }
  .ptree { padding: 6px 10px 14px; }
  .pt-row { display: flex; align-items: center; gap: 8px; padding: 7px 8px; border-bottom: 1px solid rgba(255,255,255,0.04); font-size: 12px; }
  .pt-row:last-child { border-bottom: none; }
  .pt-row .fn { color: #D8DDD6; font-family: "IBM Plex Mono", monospace; font-size: 11.5px; }
  .pt-row.fold .fn { color: #7BC79A; font-weight: 600; }
  .pt-ind1 { padding-left: 26px; } .pt-ind2 { padding-left: 46px; }
  .badge { font-size: 8.5px; font-weight: 800; letter-spacing: 0.08em; padding: 2px 6px; border-radius: 4px; }
  .b-know { background: rgba(212,160,60,0.18); color: #D4A03C; }
  .b-do { background: rgba(79,157,111,0.18); color: #7BC79A; }
  .b-nav { background: rgba(90,130,200,0.2); color: #8FAEDC; }
  .b-perm { background: rgba(255,255,255,0.08); color: #9BA8A0; }
  .srcpill { font-size: 9.5px; color: #9BA8A0; border: 1px solid rgba(255,255,255,0.13); border-radius: 999px; padding: 2px 8px; }
  .sync-ok { color: #7BC79A; font-size: 10px; margin-left: auto; }
  .pt-toggle { font-size: 9px; color: #7BC79A; border: 1px solid rgba(123,199,154,0.35); border-radius: 4px; padding: 1.5px 7px; margin-left: 8px; }
  .pmock-foot { padding: 11px 18px; border-top: 1px solid rgba(255,255,255,0.07); display: flex; gap: 8px; flex-wrap: wrap; }
  .chip { font-size: 10px; color: #7BC79A; background: rgba(79,157,111,0.12); border: 1px solid rgba(79,157,111,0.3); border-radius: 6px; padding: 3px 9px; }
  .mock-note { font-size: 12px; color: var(--ink-soft); margin-top: 12px; opacity: 0.8; }
"""

open(os.path.join(OUT, "styles.css"), "w").write(base_css + extra_css)

# ---------- shared nav / footer ----------
NAV = """<nav>
  <div class="wrap nav-inner">
    <a class="logo" href="index.html">Northwest AI<span class="dot">.</span></a>
    <div class="nav-links">
      <div class="menu-item">
        <a class="top" href="#">What we do <span class="car">&#9660;</span></a>
        <div class="dropdown">
          <div class="dd-label">Programs</div>
          <a href="fractional-caio.html">Fractional Chief AI Officer<span class="d">Your embedded AI department, run for you</span></a>
          <a href="claude-deployment.html">Claude Deployment Program<span class="d">Company-wide rollout in 16 weeks</span></a>
          <a href="#">Embedded Engineering<span class="d">Dedicated build capacity that scales</span></a>
          <hr>
          <div class="dd-label">Product</div>
          <a href="company-brain.html">Company Brain<span class="d">The context system behind everything we deploy</span></a>
        </div>
      </div>
      <div class="menu-item">
        <a class="top" href="index.html#results">Results <span class="car">&#9660;</span></a>
        <div class="dropdown">
          <a href="case-study-referrals.html">Insurance referrals: hours to minutes<span class="d">Healthcare</span></a>
          <a href="case-study-phone-agent.html">A phone agent for 500 daily calls<span class="d">Towing &amp; logistics</span></a>
          <a href="case-study-safety-reports.html">Safety reports: 80% late to 80% on time<span class="d">Construction</span></a>
          <hr>
          <a href="index.html#results">All results &rarr;</a>
        </div>
      </div>
      <div class="menu-item">
        <a class="top" href="about.html">Company <span class="car">&#9660;</span></a>
        <div class="dropdown">
          <a href="about.html">About<span class="d">Who we are and what we believe</span></a>
          <a href="careers.html">Careers<span class="d">AI consultants, trainers, and engineers</span></a>
          <a href="index.html#book">Contact<span class="d">Book a call or reach the team</span></a>
        </div>
      </div>
      <a class="btn" href="index.html#book">Book a call</a>
    </div>
  </div>
</nav>"""

FOOTER = """<footer>
  <div class="wrap foot-rule">
    <div class="foot-inner">
      <div>
        <div class="foot-logo">Northwest AI<span class="dot">.</span></div>
        <div style="margin-top: 10px;">830 NE Holladay St, Suite 1325, Portland, OR 97232<br>
        <a href="mailto:wyatt@nwai.co">wyatt@nwai.co</a> &middot; <a href="tel:+15032984673">503-298-4673</a></div>
      </div>
      <div class="foot-links" style="flex-direction: column; gap: 8px;">
        <strong style="color: rgba(250,247,241,0.8); font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase;">Programs</strong>
        <a href="fractional-caio.html">Fractional Chief AI Officer</a>
        <a href="claude-deployment.html">Claude Deployment Program</a>
        <a href="company-brain.html">Company Brain</a>
      </div>
      <div class="foot-links" style="flex-direction: column; gap: 8px;">
        <strong style="color: rgba(250,247,241,0.8); font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase;">Case studies</strong>
        <a href="case-study-referrals.html">Insurance referrals: hours to minutes</a>
        <a href="case-study-phone-agent.html">A phone agent for 500 daily calls</a>
        <a href="case-study-safety-reports.html">Safety reports: 80% late to 80% on time</a>
      </div>
      <div class="foot-links" style="flex-direction: column; gap: 8px;">
        <strong style="color: rgba(250,247,241,0.8); font-size: 13px; letter-spacing: 0.1em; text-transform: uppercase;">Company</strong>
        <a href="about.html">About</a>
        <a href="careers.html">Careers</a>
        <a href="privacy.html">Privacy</a>
        <a href="terms.html">Terms</a>
      </div>
    </div>
    <div style="margin-top: 30px; font-size: 12.5px; opacity: 0.5;">&copy; 2026 Northwest AI. All rights reserved.</div>
  </div>
</footer>"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500;1,9..144,600&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
<!-- iClosed popup widget begin -->
<script type="text/javascript" src="https://app.iclosed.io/assets/widget.js" async></script>
<!-- iClosed popup widget end -->
</head>
<body>
"""

# Every booking CTA opens the iClosed popup (element-click embed)
ICLOSED = 'href="javascript:void(0)" data-iclosed-link="https://app.iclosed.io/e/nwai/book-a-call" data-embed-type="popup"'
def wire_booking(html):
    html = html.replace('href="index.html#book"', ICLOSED)
    html = html.replace('href="#book"', ICLOSED)
    html = html.replace('<a class="btn terra" href="#">Book a discovery call</a>',
                        '<a class="btn terra" ' + ICLOSED + '>Book a discovery call</a>')
    return html

CTA_BAND = """<div class="wrap"><div class="cta-band">
  <h2>Find out what this looks like <em class="acc">in your company.</em></h2>
  <p>One call. We'll tell you exactly what AI can and can't do for your business, and what it would take. If it's not a fit, we'll say so.</p>
  <a class="btn terra" href="index.html#book">Book a discovery call</a>
</div></div>
"""

def page(filename, title, body, include_cta=True):
    html = HEAD.replace("{{TITLE}}", title) + NAV + body
    if include_cta:
        html += CTA_BAND
    html += "\n<div style='height:80px'></div>\n" + FOOTER + "\n</body>\n</html>\n"
    html = wire_booking(html)
    html = html.replace("wyatt@nwai.co", "consulting@nwai.co")
    open(os.path.join(OUT, filename), "w").write(html)
    print("wrote", filename)

# ============================================================ COMPANY BRAIN
company_brain = """
<header class="page-hero">
  <div class="wrap">
    <div class="kicker">Our product &middot; Company Brain</div>
    <h1>AI gives generic answers until it <em class="acc">knows your company.</em></h1>
    <p class="lede">Company Brain is our context management system. It holds everything AI needs to know about your business, defined once, deployed to every employee, and kept current. <strong>We run it. You own it.</strong></p>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="kicker">The problem it solves</div>
    <div class="prose">
      <h2>Watch any company's AI usage and you'll see the same pattern.</h2>
      <p>The people most skeptical of change open AI, ask a question about their work, and get a generic answer, because the AI knows nothing about the company. They quit using it within the week. That's where most rollouts die.</p>
      <p>The standard fix is to make every employee load company context themselves: build folder structures, learn what an index file is, decide what the AI should know. <strong>Nobody in estimating, underwriting, or operations wants a course on folder structures.</strong> So instead, people mount everything, burn through usage on noise, still get generic answers, and give up.</p>
      <p>The companies that get AI working solve context once, centrally, for everyone. That's what Company Brain does.</p>
    </div>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">What it is</div>
    <h2 style="max-width: 800px;">One governed structure for everything your <em class="acc">AI needs to know.</em></h2>
    <div class="brain-grid" style="margin-top: 48px;">
      <div class="brain-copy">
        <p><strong>Your company's knowledge, mapped to where it actually lives.</strong> SharePoint, Google Drive, GitHub, Notion, your data warehouse. Company Brain doesn't move your files. It builds one clean structure on top of them and keeps the two in sync.</p>
        <p><strong>Pushed to every employee.</strong> When your people open Claude, the right context for their role is already there. Nobody sets up anything. Nobody learns anything technical.</p>
        <p><strong>Centrally controlled.</strong> Your admin or AI champion edits in one place and it updates for the whole company. Core facts about the business stay locked so the source of truth stays true.</p>
      </div>
      <div>
      <div class="pmock">
        <div class="pmock-nav">
          <span class="pmock-logo"><span class="ic"></span>Company Brain</span>
          <div class="pmock-tabs"><span class="pmock-tab">Brain</span><span class="pmock-tab">Departments</span><span class="pmock-tab act">Mappings</span></div>
        </div>
        <div class="pmock-flow">
          <div class="pmock-step"><div class="s-t">Your sources</div><div class="s-k">Source of truth</div><div class="s-d">SharePoint, Drive, GitHub, Notion</div></div>
          <div class="pmock-arrow">&rarr;</div>
          <div class="pmock-step"><div class="s-t">Company Brain</div><div class="s-k">Mapping + sync</div><div class="s-d">One governed structure</div></div>
          <div class="pmock-arrow">&rarr;</div>
          <div class="pmock-step"><div class="s-t">File share</div><div class="s-k">Source of use</div><div class="s-d">Per department, governed</div></div>
          <div class="pmock-arrow">&rarr;</div>
          <div class="pmock-step"><div class="s-t">Every employee's Claude</div><div class="s-k">Reads files</div><div class="s-d">Right context, by role</div></div>
        </div>
        <div class="pmock-treehead"><span>Mappings &mdash; where this team's context comes from</span><span class="vt">Tree</span></div>
        <div class="ptree">
          <div class="pt-row fold"><span class="fn">02_Estimating</span><span class="srcpill">12 files</span></div>
          <div class="pt-row pt-ind1"><span class="fn">CLAUDE.md</span><span class="badge b-nav">NAV</span><span class="badge b-perm">R</span><span class="srcpill">github</span><span class="sync-ok">&#10003; synced</span><span class="pt-toggle">on</span></div>
          <div class="pt-row pt-ind1"><span class="fn">bid_history.md</span><span class="badge b-know">KNOW</span><span class="badge b-perm">R</span><span class="srcpill">sharepoint</span><span class="sync-ok">&#10003; synced</span><span class="pt-toggle">on</span></div>
          <div class="pt-row pt-ind1"><span class="fn">subcontractors.md</span><span class="badge b-know">KNOW</span><span class="badge b-perm">R</span><span class="srcpill">notion</span><span class="sync-ok">&#10003; synced</span><span class="pt-toggle">on</span></div>
          <div class="pt-row pt-ind1"><span class="fn">takeoff-workflow</span><span class="badge b-do">DO</span><span class="badge b-perm">P</span><span class="srcpill">github</span><span class="sync-ok">&#10003; synced</span><span class="pt-toggle">on</span></div>
          <div class="pt-row pt-ind1"><span class="fn">job_costs/</span><span class="badge b-know">KNOW</span><span class="badge b-perm">R</span><span class="srcpill">databricks</span><span class="sync-ok">&#10003; synced</span><span class="pt-toggle">on</span></div>
          <div class="pt-row fold"><span class="fn">03_Field_Ops</span><span class="srcpill">9 files</span></div>
          <div class="pt-row pt-ind1"><span class="fn">safety-reporting</span><span class="badge b-do">DO</span><span class="badge b-perm">P</span><span class="srcpill">sharepoint</span><span class="sync-ok">&#10003; synced</span><span class="pt-toggle">on</span></div>
        </div>
        <div class="pmock-foot"><span class="chip">8 departments</span><span class="chip">120+ mappings</span><span class="chip">5 sources</span><span class="chip">synced nightly</span></div>
      </div>
      <p class="mock-note">Product view shown with example data.</p>
      </div>
    </div>
    <div class="cards" style="margin-top: 56px;">
      <div class="card"><h3>L1 &middot; Company</h3><p>Who you are, what you build, who you sell to, what's confidential, voice and house rules. The always-true layer, locked so the source of truth stays true.</p></div>
      <div class="card"><h3>L2 &middot; Department</h3><p>SOPs, data sources, tools, repeating outputs. The way finance actually closes the books, the way estimating actually bids.</p></div>
      <div class="card"><h3>L3 &middot; Individual</h3><p>Role-specific files, recurring tasks, personal voice, the workflows each operator owns. The layer that makes Claude feel like it works for them.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kicker">Access by role</div>
    <h2 style="max-width: 760px;">Everyone gets the context they need. <em class="acc">Nothing they shouldn't have.</em></h2>
    <p style="color: var(--ink-soft); max-width: 640px; margin-top: 16px; font-size: 17px;">Executives see the whole company. A project manager sees their projects, not the finance folders. Leadership decides who sees what, once, and Company Brain enforces it everywhere.</p>
    <div class="perm-grid">
      <div class="perm-head"><div>Context</div><div>Executive</div><div>Estimating</div><div>Project Mgmt</div></div>
      <div class="perm-row"><div>company-overview/</div><div class="yes">&#10003;</div><div class="yes">&#10003;</div><div class="yes">&#10003;</div></div>
      <div class="perm-row"><div>estimating/</div><div class="yes">&#10003;</div><div class="yes">&#10003;</div><div class="no">&#10007;</div></div>
      <div class="perm-row"><div>projects/</div><div class="yes">&#10003;</div><div class="no">&#10007;</div><div class="yes">&#10003;</div></div>
      <div class="perm-row"><div>finance/</div><div class="yes">&#10003;</div><div class="no">&#10007;</div><div class="no">&#10007;</div></div>
    </div>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">How it gets built</div>
    <h2>You never think about it. <em class="acc">That's the point.</em></h2>
    <div class="steps-vert">
      <div class="step-v"><div class="num">01</div><h3>Define</h3><p>Week one, we sit with your leadership and the people who run each department. We pull the 20% of context that drives 80% of the value out of their heads and systems. Your team doesn't interview 500 people. We talk to the few who know.</p></div>
      <div class="step-v"><div class="num">02</div><h3>Map</h3><p>We connect the structure to where your knowledge actually lives: SharePoint, Google Drive, GitHub, Notion, your databases. Big datasets pipe in from the warehouse. Nothing gets migrated.</p></div>
      <div class="step-v"><div class="num">03</div><h3>Deploy</h3><p>The right context lands on every employee's Claude, matched to their role, along with pre-built skills for their actual workflows. Day one, the AI already knows the business.</p></div>
      <div class="step-v"><div class="num">04</div><h3>Run</h3><p>We keep it current as your business changes. Your admins edit anything, anytime, in one place. New skills and updates push to the whole company without anyone lifting a finger.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="prose">
      <h2>Why this is the part that <em class="acc">compounds.</em></h2>
      <p>Custom agents are powerful. Training sticks. But context is what makes every single AI interaction in your company better, for every employee, on day one. It's the difference between AI as a toy and AI as how work gets done.</p>
      <p>And it's yours. The structure, the content, the source mappings all live in your environment. We run it while we're engaged. If you ever leave, it stays.</p>
    </div>
  </div>
</section>
"""
page("company-brain.html", "Company Brain — Northwest AI", company_brain)

# ============================================================ FRACTIONAL CAIO
fcaio = """
<header class="page-hero">
  <div class="wrap">
    <div class="kicker">Programs &middot; Fractional Chief AI Officer</div>
    <h1>An executive owns your AI strategy. Engineers build it. <em class="acc">Your team actually uses it.</em></h1>
    <p class="lede">The Fractional CAIO is our core partnership: a hands-on AI department embedded in your company, every month. <strong>Strategy, builds, and training, run for you.</strong> For companies doing $10M to $500M.</p>
    <div class="hero-cta" style="margin-top: 32px;"><a class="btn terra" href="index.html#book">Book a discovery call</a></div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="kicker">What you get</div>
    <h2 style="max-width: 800px;">It's not a workshop. It's not a course. <em class="acc">It's your AI department.</em></h2>
    <div class="steps-vert">
      <div class="step-v"><div class="num">01</div><h3>An executive who owns it</h3><p>Your fractional Chief AI Officer leads strategy, decides what gets built and in what order, and answers for results. AI stops being everyone's side project and becomes someone's job.</p></div>
      <div class="step-v"><div class="num">02</div><h3>A real engineering team</h3><p>A 20+ engineer team led by our CTO, who built the Thursday Night Football backend at Amazon, and our head of engineering out of Microsoft. They ship the builds, then maintain them, and you own every line.</p></div>
      <div class="step-v"><div class="num">03</div><h3>Your team, fluent in Claude</h3><p>Not a generic webinar. Every person gets hands-on, role-specific help on their actual work, so adoption sticks instead of stalling like most rollouts.</p></div>
      <div class="step-v"><div class="num">04</div><h3>Company Brain</h3><p>We pull your data and knowledge out of scattered tools and people's heads into one clean source of truth, the operating system your AI runs on. <a href="company-brain.html" style="color: var(--terra);">How it works &rarr;</a></p></div>
    </div>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">How the engagement runs</div>
    <h2>Month one has a deliverable. <em class="acc">Then it just runs.</em></h2>
    <div class="prose" style="margin-top: 28px;">
      <p><strong>Month 1: the 80/20 Report.</strong> We map every workflow in your company and hand you a written report: exactly where AI pays off fastest, ranked, with a build roadmap for the year. It becomes the input for everything that gets built. No guessing, no pilot purgatory.</p>
      <p><strong>Every month after:</strong> two tracks run in parallel. Our engineers ship the builds the roadmap calls for, anything from agents and automations to data pipelines that pull your operational data into one warehouse. Your team gets trained, role by role, with access to our consultants by scheduled calls and a shared Slack channel. And you get a weekly strategy call with your CAIO, so AI stays someone's job, not everyone's side project.</p>
      <p><strong>Build credits work simply:</strong> we write a one-page scope for each build with the objective, hours, and expected outcome. You approve it in writing. We ship it. You can see your credit balance anytime.</p>
      <p><strong>The structure:</strong> an annual partnership that flexes by depth, from a few builds a quarter to running your whole AI org. Backed by a 60-day money-back guarantee. If you want a one-time project with a finish line, that's the <a href="claude-deployment.html" style="color: var(--terra);">Deployment Program</a>. If you want AI owned, this is it.</p>
    </div>
    <div class="stat-strip">
      <div class="stat-cell"><div class="n">Week 1</div><div class="l">Your team is live</div></div>
      <div class="stat-cell"><div class="n">Month 1</div><div class="l">80/20 Report in hand</div></div>
      <div class="stat-cell"><div class="n">60-day</div><div class="l">Money-back guarantee</div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kicker">Who it's for</div>
    <div class="prose">
      <h2>Built for the companies the big firms <em class="acc">can't serve.</em></h2>
      <p><strong>Size:</strong> $10M to $500M a year in revenue. Under $10M, the math doesn't pay back yet; start with our free content and come back when it does.</p>
      <p><strong>Industry:</strong> we've recently shipped in construction, insurance, energy, CPG, fintech, financial services, manufacturing, healthcare, professional services, and B2B software. The less digitally native the industry, the bigger the head start.</p>
      <p><strong>The alternative:</strong> hiring this team yourself runs $1M+ a year in salaries, if you can find the people. Most can't, because big tech hires them first. <a href="index.html#how" style="color: var(--terra);">See the math &rarr;</a></p>
    </div>
  </div>
</section>
"""
page("fractional-caio.html", "Fractional Chief AI Officer — Northwest AI", fcaio)

# ============================================================ CLAUDE DEPLOYMENT
cdp = """
<header class="page-hero">
  <div class="wrap">
    <div class="kicker">Programs &middot; Claude Deployment Program</div>
    <h1>Your whole company on Claude, doing real work, <em class="acc">in 16 weeks.</em></h1>
    <p class="lede">A fixed-scope, fixed-fee program built on three pillars: <strong>executive training, department-by-department rollout with matched consultants, and the context architecture that makes adoption stick.</strong> It ends with your people demoing real automations they built.</p>
    <div class="hero-cta" style="margin-top: 32px;"><a class="btn terra" href="index.html#book">Book a discovery call</a></div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="kicker">The three pillars</div>
    <h2 style="max-width: 820px;">Three pillars. <em class="acc">One cadence.</em></h2>
    <div class="cards" style="margin-top: 44px;">
      <div class="card"><h3>1. Executives first</h3><p>Your exec team trains alongside the org, with a consultant who has worked on exec teams, in the language of budgets and board updates, not prompt theory. We used to make this optional. We don't anymore: adoption only sticks when the workforce sees leadership using it first.</p></div>
      <div class="card"><h3>2. Matched consultants</h3><p>Each department pairs with a consultant who actually did that job: finance with a finance veteran, sales with a sales veteran, ops with an ops veteran. They speak the operators' language and know where Claude breaks in practice, not in theory.</p></div>
      <div class="card"><h3>3. Context architecture</h3><p>Company, department, and individual-level knowledge wired into Claude, built as its own parallel workstream so we never burn a training session on troubleshooting someone's folder sync. <a href="company-brain.html" style="color: var(--terra);">This is Company Brain &rarr;</a></p></div>
    </div>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">The 16 weeks</div>
    <h2>Foundations, capability, possibility, <em class="acc">builds.</em></h2>
    <div class="steps-vert">
      <div class="step-v"><div class="num">Weeks 0&ndash;3</div><h3>Foundations</h3><p>Everyone gets to the same baseline: procurement and settings, then Claude 101 and 102. Nobody starts department work behind.</p></div>
      <div class="step-v"><div class="num">Weeks 4&ndash;9</div><h3>Context + capability</h3><p>The context substrate goes in, then weekly tool mastery: Excel, documents and decks, artifacts, skills. Your people stop chatting with AI and start working with it.</p></div>
      <div class="step-v"><div class="num">Weeks 10&ndash;11</div><h3>What's possible</h3><p>Show, then ask. Curated examples from past clients in your industry, walked through end to end, so your team sees the bar before they're asked to clear it.</p></div>
      <div class="step-v"><div class="num">Weeks 12&ndash;16</div><h3>Pod builds + demo day</h3><p>Pair-programming with the matched consultant. By week 16 your people ship real automations they own, demoed at a final readout with ROI. An invite-only advanced group runs in parallel for the top users: Claude Code, MCP, agentic workflows.</p></div>
    </div>
    <div class="stat-strip" style="margin-top: 44px;">
      <div class="stat-cell"><div class="n">60+</div><div class="l">Named deliverables across 16 weeks</div></div>
      <div class="stat-cell"><div class="n">3&ndash;5</div><div class="l">Departments, scoped by headcount</div></div>
      <div class="stat-cell"><div class="n">Demo day</div><div class="l">Your people present what they built</div></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kicker">The honest part</div>
    <h2 style="max-width: 800px;">We're going to ask something <em class="acc">of your team.</em></h2>
    <div class="prose" style="margin-top: 24px;">
      <p>Real workforce adoption isn't free, and we put this in writing before kickoff. Your people commit <strong>4 to 6 hours a month</strong> of workshop time, pair-programming, and homework on their own files. The first three weeks feel like learning a new operating system. And around weeks 5 through 8, throughput dips, because they're doing the same work two ways: once their way, once with Claude. Plan for it.</p>
      <p><strong>They come out the other side feeling like they have superpowers.</strong> That's not a metaphor we use lightly. It's what demo day exists to prove.</p>
    </div>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">Scope &amp; fit</div>
    <div class="prose">
      <h2>Scoped to your headcount. <em class="acc">Fixed fee, clear finish line.</em></h2>
      <p>The program scales from 2 to 3 departments for smaller companies up to 5 departments with an expanded champions network for larger ones. Above ~300 employees we scope custom. Every tier includes the pre-engagement diagnostic, the exec cohort, matched consultants, full context architecture, pair-programmed builds, and an exit handoff. We'll give you a real number on the first call.</p>
      <h2>Deployment or partnership? <em class="acc">How to choose.</em></h2>
      <p>The Deployment Program has a finish line: 16 weeks, your company live on Claude, your people shipping their own automations. It's the right fit when you want a defined transformation with a defined end, and your team is self-sufficient at exit.</p>
      <p>The <a href="fractional-caio.html" style="color: var(--terra);">Fractional Chief AI Officer</a> is the ongoing version: an executive owning your AI strategy, engineers shipping every month, training that never goes stale. Most deployment clients graduate into it, because the companies pulling ahead never stop building.</p>
    </div>
  </div>
</section>
"""
page("claude-deployment.html", "Claude Deployment Program — Northwest AI", cdp)

# ============================================================ CASE STUDIES
def case_study(filename, kicker, h1, lede, stats, problem, built, result):
    body = """
<header class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="index.html">Home</a> / <a href="index.html#results">Results</a> / Case study</div>
    <div class="kicker">{K}</div>
    <h1>{H1}</h1>
    <p class="lede">{LEDE}</p>
  </div>
</header>
<section style="padding-top: 0; border-top: none;">
  <div class="wrap">
    <div class="stat-strip">{STATS}</div>
    <div class="prose">
      <h2>The problem</h2>
      {PROBLEM}
      <h2>What we built</h2>
      {BUILT}
      <h2>The result</h2>
      {RESULT}
    </div>
  </div>
</section>
""".replace("{K}", kicker).replace("{H1}", h1).replace("{LEDE}", lede).replace("{STATS}", stats).replace("{PROBLEM}", problem).replace("{BUILT}", built).replace("{RESULT}", result)
    page(filename, h1.replace('<em class="acc">', '').replace('</em>', '') + " — Northwest AI", body)

case_study(
  "case-study-referrals.html",
  "Case study &middot; Healthcare",
  'Insurance referrals: from hours of sorting to <em class="acc">minutes.</em>',
  "A healthcare provider's staff hand-sorted hundreds of insurance referrals. We automated the whole process.",
  """<div class="stat-cell"><div class="n">Hundreds</div><div class="l">of referrals processed</div></div>
     <div class="stat-cell"><div class="n">Hours &rarr; minutes</div><div class="l">processing time</div></div>
     <div class="stat-cell"><div class="n">Healthcare</div><div class="l">industry</div></div>""",
  """<p>Every referral that came in had to be read, classified, and routed by a person. Insurance referrals don't arrive in a tidy format: they show up as faxes, PDFs, and portal exports, each one different. Staff spent hours every day just sorting, before any actual care coordination happened.</p>
     <p>That's skilled people doing work a machine should do, and a queue that grows every time the practice grows.</p>""",
  """<p>We built an automated referral pipeline: incoming referrals get read, key details extracted, classified by type and urgency, and routed to the right queue, with a human reviewing the output instead of producing it.</p>
     <p>It runs inside the team's existing workflow. Nobody learned new software. The work just shows up sorted.</p>""",
  """<p><strong>What took hours every day now takes minutes.</strong> The team reviews and handles exceptions instead of sorting from scratch, and referral volume can grow without the sorting burden growing with it.</p>"""
)

case_study(
  "case-study-phone-agent.html",
  "Case study &middot; Towing &amp; logistics",
  'A phone agent that answers <em class="acc">90% of 500 daily calls.</em>',
  "A towing company staffed a full call team to answer 500 calls a day. Our phone agent picks up almost all of them.",
  """<div class="stat-cell"><div class="n">500</div><div class="l">calls per day</div></div>
     <div class="stat-cell"><div class="n">90%</div><div class="l">answered by the agent</div></div>
     <div class="stat-cell"><div class="n">Towing</div><div class="l">industry</div></div>""",
  """<p>Five hundred calls a day, every day, answered by a human call team. Dispatch requests, status checks, the same questions on repeat. Staffing it meant constant hiring and training for high-turnover seats, and every missed call was potentially lost business.</p>""",
  """<p>We built a phone agent that answers the line, handles the routine calls end to end, and hands the unusual ones to a person with full context of the conversation so far.</p>
     <p>It picks up instantly, around the clock, and it doesn't have a bad day.</p>""",
  """<p><strong>The agent now picks up 90% of the company's 500 daily calls.</strong> The human team handles the calls that actually need a human, and the phone never rings out.</p>"""
)

case_study(
  "case-study-safety-reports.html",
  "Case study &middot; Construction",
  'Safety reports: from 80% late to <em class="acc">80% on time.</em>',
  "A construction company chased crews by hand for safety reports. Our automated system flipped the compliance rate.",
  """<div class="stat-cell"><div class="n">80% late</div><div class="l">before</div></div>
     <div class="stat-cell"><div class="n">80% on time</div><div class="l">after</div></div>
     <div class="stat-cell"><div class="n">Construction</div><div class="l">industry</div></div>""",
  """<p>Safety reports only protect you if they exist. Site teams are busy building, so reports slipped, and someone in the office spent their time chasing crews one by one. Eighty percent of reports came in late.</p>
     <p>In construction, that's not a paperwork problem. If there's ever an incident and a lawsuit, the company's defense is the documentation. Late and missing reports are exposure.</p>""",
  """<p>We built an automated system that pings every team member when their safety reports are due, follows up on its own, and gives leadership a live view of what's outstanding, without anyone playing collections agent.</p>""",
  """<p><strong>Safety reports went from 80% late to 80% on time.</strong> The documentation exists when it matters, the office got its time back, and leadership can see compliance at a glance instead of hoping.</p>"""
)

# ============================================================ ABOUT
about = """
<header class="page-hero">
  <div class="wrap">
    <div class="kicker">About Northwest AI</div>
    <h1>We make mid-market companies <em class="acc">AI native.</em></h1>
    <p class="lede">Northwest AI embeds engineers and consultants into companies doing $10M to $500M, builds their AI agents, trains their people, and runs their AI department. Bootstrapped, profitable, and built on shipped work, not slideware.</p>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="kicker">What we believe</div>
    <div class="prose">
      <h2>The technology was never <em class="acc">the hard part.</em></h2>
      <p>MIT found that about 5% of enterprise AI pilots produce real P&amp;L impact. The other 95% spend and stall. We've watched why, from inside hundreds of engagements: AI fails on adoption, not capability. People get generic answers from a tool that doesn't know their company, and they quit.</p>
      <p>So we built the firm around the three things adoption actually takes: <strong>engineers who ship real builds, trainers who change daily behavior, and Company Brain, the context system that makes AI specific to your business from the first prompt.</strong> Most firms do one of these. Doing all three, every month, is the whole point.</p>
      <p>And we work where the big firms don't: the independent mid-market. Construction, insurance, healthcare, manufacturing. The companies that run the real economy, where the gap between AI talk and AI work is widest, and where closing it pays off fastest.</p>
    </div>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">The story</div>
    <div class="prose">
      <h2>It started with a contract manager <em class="acc">in construction.</em></h2>
      <p>Wyatt's mom manages contracts for a construction company. One day she was told she couldn't use AI. No training, no guidance, no legal help with the contracts crossing her desk every day. Just a ban.</p>
      <p>That struck Wyatt as exactly backwards. The people doing the real work in industries like construction weren't being replaced by AI. They were being locked out of it, because nobody would teach them what it could do, what it couldn't, and how to use it safely. The problem was never the tool. It was that nobody was educating the people.</p>
      <p>At the time, Wyatt was already building custom tools with Asad Malik and Awais Tariq, who ran Ubiquify Digital, a development shop built on Amazon and Microsoft engineering pedigree. He brought them a partnership: pair that engineering bench with consultants who teach in plain language, and serve the companies everyone else ignores. The rest is history. We've been building together ever since.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="kicker">The team</div>
    <h2>Built by people who've <em class="acc">done it at scale.</em></h2>
    <div class="team-rows">
      <div class="team-row">
        <img class="face" src="https://nwai.co/wp-content/uploads/2025/07/wyatt-headshot-hq-2.png" alt="Wyatt Mayham">
        <div class="name">Wyatt Mayham</div>
        <div class="role">CEO</div>
        <p>Second-time founder. Built and sold TwitchMetrics to GameSquare (NASDAQ: GAME). Leads strategy and runs the front of the house.</p>
      </div>
      <div class="team-row">
        <img class="face" src="https://nwai.co/wp-content/uploads/2025/07/asad-headshot.jpg" alt="Asad Malik">
        <div class="name">Asad Malik</div>
        <div class="role">CTO</div>
        <p>Built the Thursday Night Football backend at Amazon. Owns technical strategy and hires and trains our engineers like AWS.</p>
      </div>
      <div class="team-row">
        <img class="face" src="https://nwai.co/wp-content/uploads/2025/07/awais-headshot.jpg" alt="Awais Tariq">
        <div class="name">Awais Tariq</div>
        <div class="role">COO</div>
        <p>Ex-Microsoft, Bank of America, and Merrill Lynch. Princeton grad. Fifteen years in operations. Runs delivery.</p>
      </div>
    </div>
    <p class="bench"><strong>Behind them:</strong> US-based consultants and trainers who own your relationship, and a 20-engineer team that ships around the clock.</p>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">How we work</div>
    <div class="cards" style="margin-top: 36px;">
      <div class="card"><h3>We build, not advise</h3><p>200+ shipped projects. Strategy exists to point the building in the right direction, never to replace it. You own every line we write.</p></div>
      <div class="card"><h3>We say no</h3><p>Under $10M in revenue, we'll tell you the math doesn't work yet and point you to our free content. Turning away bad fits is how the guarantee stays easy to offer.</p></div>
      <div class="card"><h3>We stay accountable</h3><p>Every engagement is backed by a 60-day money-back guarantee, and our flagship clients have grown with us year over year.</p></div>
    </div>
  </div>
</section>
"""
page("about.html", "About — Northwest AI", about)

# ============================================================ CAREERS
careers = """
<header class="page-hero">
  <div class="wrap">
    <div class="kicker">Careers</div>
    <h1>We hire people who know tech and can <em class="acc">talk to humans.</em></h1>
    <p class="lede">That combination is rarer than either skill alone, and it's the entire reason our clients' AI rollouts stick while everyone else's stall. If that sentence describes you, we should talk. <strong>We're always hiring for three roles.</strong></p>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="kicker">Open roles</div>
    <div class="cards" style="margin-top: 36px;">
      <div class="card"><h3><a href="role-ai-consultant.html" style="color: inherit; text-decoration: none;">AI Consultant &rarr;</a></h3><p>Own client relationships and lead AI transformations inside mid-market companies. You've done a real job in a real industry, and you can teach.</p><p style="margin-top: 12px; font-size: 13px; color: var(--terra); font-weight: 600;">US-based &middot; Always open</p></div>
      <div class="card"><h3><a href="role-ai-trainer.html" style="color: inherit; text-decoration: none;">AI Trainer &rarr;</a></h3><p>Teach Claude to entire companies, role by role, from the exec cohort to the field. Adoption is behavior change, and you're the one who changes it.</p><p style="margin-top: 12px; font-size: 13px; color: var(--terra); font-weight: 600;">US-based &middot; Always open</p></div>
      <div class="card"><h3><a href="role-engineer.html" style="color: inherit; text-decoration: none;">Engineer &rarr;</a></h3><p>Ship agents, automations, and data pipelines that mid-market companies run their business on. Claude, MCP, and agentic workflows, in production.</p><p style="margin-top: 12px; font-size: 13px; color: var(--terra); font-weight: 600;">Remote &middot; Always open</p></div>
    </div>
  </div>
</section>

<section style="background: var(--paper-2);">
  <div class="wrap">
    <div class="kicker">Why here</div>
    <div class="prose">
      <h2>Real clients, real builds, <em class="acc">no bench time.</em></h2>
      <p>We're bootstrapped, profitable, and growing fast on the back of work that ships. You'll be inside real companies (construction, insurance, healthcare, manufacturing) doing work their teams use every day, not writing decks about work someone else might do someday.</p>
      <p>You'll also be early. The team is small, the surface area is huge, and the people who join now get to build the playbook everyone after them runs.</p>
    </div>
  </div>
</section>
"""
page("careers.html", "Careers — Northwest AI", careers, include_cta=False)

def role_page(filename, title, h1, lede, do_items, look_items, location):
    body = """
<header class="page-hero">
  <div class="wrap">
    <div class="crumb"><a href="careers.html">Careers</a> / {TITLE}</div>
    <div class="kicker">Open role &middot; {LOC}</div>
    <h1>{H1}</h1>
    <p class="lede">{LEDE}</p>
  </div>
</header>
<section style="padding-top: 0; border-top: none;">
  <div class="wrap">
    <div class="prose">
      <h2>What you'll do</h2>
      <ul>{DO}</ul>
      <h2>What we look for</h2>
      <ul>{LOOK}</ul>
      <h2>How to apply</h2>
      <p>Email <a href="mailto:wyatt@nwai.co?subject={SUBJ}" style="color: var(--terra);">wyatt@nwai.co</a> with the subject line "{TITLE}". Skip the formal cover letter. Send a few sentences on who you are, the most impressive thing you've built or taught, and why this role. If you've used Claude to do real work, tell us about that too.</p>
    </div>
  </div>
</section>
""".replace("{TITLE}", title).replace("{LOC}", location).replace("{H1}", h1).replace("{LEDE}", lede) \
   .replace("{DO}", "".join("<li>" + i + "</li>" for i in do_items)) \
   .replace("{LOOK}", "".join("<li>" + i + "</li>" for i in look_items)) \
   .replace("{SUBJ}", title.replace(" ", "%20"))
    page(filename, title + " — Careers — Northwest AI", body, include_cta=False)

role_page("role-ai-consultant.html", "AI Consultant",
  'You did the job for a decade. Now teach an industry <em class="acc">to do it with AI.</em>',
  "Our model pairs every client department with a consultant who actually worked in that discipline: finance with a finance veteran, ops with an ops veteran. You own client relationships, run discovery, and lead mid-market companies through becoming AI native.",
  ["Own a portfolio of client relationships as their day-to-day AI lead",
   "Run discovery and workflow mapping, and shape each client's 80/20 roadmap",
   "Pair-program real automations with client teams in your discipline",
   "Work alongside our engineers to turn what clients need into what gets built",
   "Represent NWAI in the room with executives, plainly and without jargon"],
  ["A real career in a real discipline: finance, operations, sales, estimating, supply chain, legal, or similar",
   "Daily, serious use of AI in your own work, you're the person colleagues already ask",
   "The rare combination: technical enough to be credible, human enough to be trusted",
   "Plain written and spoken communication, no consultant-speak",
   "Comfort with ambiguity, small-team pace, and being measured on client outcomes"],
  "US-based")

role_page("role-ai-trainer.html", "AI Trainer",
  "Adoption is behavior change. <em class='acc'>You're the one who changes it.</em>",
  "Most AI rollouts die because nobody actually teaches people. Our trainers run the 16-week programs that make whole companies fluent in Claude, from the executive cohort to the field, on their real work.",
  ["Deliver Claude 101/102 and role-specific training across client departments",
   "Train executive cohorts in their language: budgets, board updates, deal memos",
   "Coach individuals through the learning curve, including the weeks where it's hard",
   "Run pair-programming sessions where client teams build their own automations",
   "Feed what you learn in the room back into our programs and playbooks"],
  ["You've taught adults something hard before: training, coaching, enablement, teaching, or facilitation",
   "Deep hands-on fluency with Claude, and the ability to demystify it for a skeptical 55-year-old estimator",
   "Patience and presence in a room, in person and on Zoom",
   "Energy for repetition: the hundredth 101 session has to be as good as the first",
   "Plain language as a reflex, not an effort"],
  "US-based")

role_page("role-engineer.html", "Engineer",
  'Ship AI that companies <em class="acc">run their business on.</em>',
  "Our engineering team builds the agents, automations, and data pipelines behind every engagement: phone agents handling hundreds of calls a day, referral pipelines, safety systems, and Company Brain deployments. Real production work, shipped weekly, owned by the client.",
  ["Build and ship client automations: agents, integrations, data pipelines, and internal tools",
   "Stand up Company Brain deployments: source connectors, role mappings, sync infrastructure",
   "Work with Claude, MCP, and agentic workflows in production, not in demos",
   "Scope builds in plain language clients can approve, then deliver what was scoped",
   "Maintain what you ship: our clients stay, so your code has a long life"],
  ["Strong general software engineering: APIs, data, cloud infrastructure (AWS or Azure)",
   "Real experience building with LLMs and agentic patterns beyond toy projects",
   "Pragmatism: you ship the boring solution that works over the clever one that might",
   "Clear written communication, our team is distributed and async",
   "Comfort owning projects end to end with a small, senior team"],
  "Remote")

# ============================================================ LEGAL
privacy_body = """
<section class="page-hero" style="padding-bottom: 30px;"><div class="wrap legal">
<h1>Privacy Policy</h1>
<p class="updated">Last updated: January 2, 2025</p>
<h2>1. Information We Collect</h2>
<p>Northwest AI Consulting ("we," "us," or "our") collects information you provide directly to us, such as when you:</p>
<ul><li>Fill out contact forms or request consultations</li><li>Subscribe to our newsletters or communications</li><li>Participate in surveys or provide feedback</li><li>Contact us via email, phone, or other communication methods</li></ul>
<p>The types of information we may collect include:</p>
<ul><li>Name, email address, phone number, and company information</li><li>Project requirements and business information you choose to share</li><li>Communications between you and our team</li><li>Technical information about your AI implementation needs</li></ul>
<p>When you visit or log in to our website, cookies and similar technologies may be used by our online data partners or vendors to associate these activities with other personal information they or others have about you, including by association with your email or home address. We (or service providers on our behalf) may then send communications and marketing to these email or home addresses. You may opt out of receiving this advertising by visiting <a href="https://app.retention.com/optout">https://app.retention.com/optout</a>.</p>
<p>All the above categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.</p>
<h2>2. How We Use Your Information</h2>
<p>We use the information we collect to:</p>
<ul><li>Provide, maintain, and improve our AI consulting services</li><li>Respond to your inquiries and provide customer support</li><li>Send you technical updates, security alerts, and administrative messages</li><li>Develop custom AI solutions tailored to your business needs</li><li>Comply with legal obligations and protect our legal rights</li><li>Prevent fraud and enhance the security of our services</li></ul>
<h2>3. Information Sharing and Disclosure</h2>
<p>We do not sell, trade, or otherwise transfer your personal information to third parties except as described in this policy:</p>
<ul><li><strong>Service Providers:</strong> We may share information with trusted third-party service providers who assist us in operating our business</li><li><strong>Legal Requirements:</strong> We may disclose information if required by law or in response to valid legal requests</li><li><strong>Business Transfers:</strong> Information may be transferred in connection with mergers, acquisitions, or asset sales</li><li><strong>Consent:</strong> We may share information with your explicit consent</li></ul>
<h2>4. Data Security</h2>
<p>We implement appropriate technical and organizational security measures to protect your personal information against unauthorized access, alteration, disclosure, or destruction. These measures include:</p>
<ul><li>Encryption of data in transit and at rest</li><li>Regular security assessments and updates</li><li>Access controls and authentication mechanisms</li><li>Employee training on data protection practices</li></ul>
<h2>5. Your Rights and Choices</h2>
<p>Depending on your location, you may have certain rights regarding your personal information:</p>
<ul><li><strong>Access:</strong> Request access to the personal information we hold about you</li><li><strong>Correction:</strong> Request correction of inaccurate or incomplete information</li><li><strong>Deletion:</strong> Request deletion of your personal information</li><li><strong>Portability:</strong> Request a copy of your information in a structured format</li><li><strong>Opt-out:</strong> Unsubscribe from marketing communications</li></ul>
<p>To exercise these rights, please contact us at consulting@nwai.co.</p>
<h2>6. Cookies and Tracking</h2>
<p>Our website may use cookies and similar tracking technologies to enhance your browsing experience and analyze website usage. You can control cookies through your browser settings.</p>
<h2>7. International Data Transfers</h2>
<p>Your information may be transferred to and processed in countries other than your country of residence. We ensure appropriate safeguards are in place to protect your information during such transfers.</p>
<h2>8. Changes to This Policy</h2>
<p>We may update this privacy policy from time to time. We will notify you of any material changes by posting the new policy on this page and updating the "Last updated" date.</p>
<h2>9. Contact Us</h2>
<p>If you have any questions about this privacy policy or our data practices, please contact us:</p>
<p><strong>Northwest AI Consulting</strong><br>Email: consulting@nwai.co<br>Phone: +1 (503) 298-4673</p>
</div></section>
"""
page("privacy.html", "Privacy Policy — Northwest AI", privacy_body, include_cta=False)

terms_body = """
<section class="page-hero" style="padding-bottom: 30px;"><div class="wrap legal">
<h1>Terms of Service</h1>
<p class="updated">Last updated: January 2, 2025</p>
<h2>1. Acceptance of Terms</h2>
<p>By accessing or using Northwest AI Consulting's website and services, you agree to be bound by these Terms of Service ("Terms"). If you do not agree to these Terms, please do not use our services.</p>
<h2>2. Description of Services</h2>
<p>Northwest AI Consulting provides artificial intelligence consulting services, including but not limited to:</p>
<ul><li>AI strategy development and roadmapping</li><li>Custom AI solution development and implementation</li><li>AI training and education programs</li><li>AI compliance and governance consulting</li><li>Managed AI services and ongoing support</li></ul>
<h2>3. User Responsibilities</h2>
<p>As a user of our services, you agree to:</p>
<ul><li>Provide accurate and complete information when requested</li><li>Maintain the confidentiality of any login credentials</li><li>Use our services only for lawful purposes</li><li>Respect intellectual property rights</li><li>Comply with all applicable laws and regulations</li><li>Not interfere with or disrupt our services</li></ul>
<h2>4. Service Availability</h2>
<p>We strive to maintain high availability of our services, but we do not guarantee uninterrupted access. We may temporarily suspend or restrict access for maintenance, updates, or other operational reasons.</p>
<h2>5. Intellectual Property</h2>
<p>All content, trademarks, and intellectual property on our website and in our services remain the property of Northwest AI Consulting or our licensors. You may not copy, modify, distribute, or create derivative works without explicit written permission.</p>
<p>Custom AI solutions developed for clients will be governed by separate consulting agreements that specify intellectual property ownership and usage rights.</p>
<h2>6. Confidentiality</h2>
<p>We understand the sensitive nature of business information shared during consulting engagements. We maintain strict confidentiality protocols and will not disclose your proprietary information without your explicit consent, except as required by law.</p>
<h2>7. Payment Terms</h2>
<p>Payment terms for consulting services will be specified in individual service agreements. General terms include:</p>
<ul><li>Fees are due according to the agreed payment schedule</li><li>Late payments may incur additional charges</li><li>All fees are non-refundable unless otherwise specified</li><li>Prices are subject to change with appropriate notice</li></ul>
<h2>8. Limitation of Liability</h2>
<p>To the fullest extent permitted by law, Northwest AI Consulting shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including but not limited to loss of profits, data, or business opportunities.</p>
<p>Our total liability for any claims arising from our services shall not exceed the amount paid by you for the specific services giving rise to the claim.</p>
<h2>9. Disclaimers</h2>
<p>Our services are provided "as is" without warranties of any kind. We make no guarantees about the accuracy, reliability, or suitability of our AI solutions for specific purposes. AI technology involves inherent uncertainties, and results may vary.</p>
<h2>10. Termination</h2>
<p>Either party may terminate consulting agreements according to the terms specified in individual service contracts. We reserve the right to suspend or terminate access to our services for violations of these Terms.</p>
<h2>11. Governing Law</h2>
<p>These Terms shall be governed by and construed in accordance with the laws of the state in which Northwest AI Consulting is incorporated, without regard to conflict of law principles.</p>
<h2>12. Changes to Terms</h2>
<p>We may modify these Terms at any time by posting updated terms on our website. Your continued use of our services after such modifications constitutes acceptance of the new Terms.</p>
<h2>13. Contact Information</h2>
<p>If you have questions about these Terms, please contact us:</p>
<p><strong>Northwest AI Consulting</strong><br>Email: consulting@nwai.co<br>Phone: +1 (503) 298-4673</p>
</div></section>
"""
page("terms.html", "Terms of Service — Northwest AI", terms_body, include_cta=False)

# ============================================================ INDEX (adapt v3)
idx = v3
# replace inline style with stylesheet link
idx = re.sub(r"<style>.*?</style>", '<link rel="stylesheet" href="styles.css">', idx, flags=re.S)
# replace nav
idx = re.sub(r"<nav>.*?</nav>", NAV, idx, flags=re.S)
# replace footer
idx = re.sub(r"<footer>.*?</footer>", FOOTER, idx, flags=re.S)
# nav anchors within page still fine; fix nav links that pointed to anchors
idx = idx.replace('href="#brain"', 'href="company-brain.html"').replace('href="#programs"', 'href="#programs"')
# link results rows to case studies: add read links
idx = idx.replace(
  "now takes minutes.</p>",
  'now takes minutes. <a href="case-study-referrals.html" style="color: var(--terra); font-weight: 600;">Read the case study &rarr;</a></p>')
idx = idx.replace(
  "now picks up 90% of them.</p>",
  'now picks up 90% of them. <a href="case-study-phone-agent.html" style="color: var(--terra); font-weight: 600;">Read the case study &rarr;</a></p>')
idx = idx.replace(
  "the paperwork exists.</strong></p>",
  'the paperwork exists.</strong> <a href="case-study-safety-reports.html" style="color: var(--terra); font-weight: 600;">Read the case study &rarr;</a></p>')
# link program cards
idx = idx.replace("<h3>Claude Deployment Program</h3>", '<h3><a href="claude-deployment.html" style="color: inherit; text-decoration: none;">Claude Deployment Program &rarr;</a></h3>')
idx = idx.replace("<h3>Fractional AI Team</h3>", '<h3><a href="fractional-caio.html" style="color: inherit; text-decoration: none;">Fractional Chief AI Officer &rarr;</a></h3>')
# company brain section link to page
idx = idx.replace("We run it. Your team just opens Claude and it already knows the business.</p>",
  'We run it. Your team just opens Claude and it already knows the business. <a href="company-brain.html" style="color: var(--terra); font-weight: 600;">How Company Brain works &rarr;</a></p>')
# headline revert per Wyatt (2026-06-09): back to the $1M payroll line
idx = idx.replace('<h1>AI doing real work, without hiring a <em class="acc">single engineer.</em></h1>',
  '<h1>Your AI department, without the <em class="acc">$1M payroll.</em></h1>')
idx = idx.replace("<title>Northwest AI — AI doing real work, without hiring a single engineer</title>",
  "<title>Northwest AI — Your AI department, without the $1M payroll</title>")
# deployment card bullet corrected per the real DSA program (no agents-by-week-4 claim)
idx = idx.replace("<li>Working agents by week four</li>", "<li>Pair-programmed builds and a demo day finish</li>")
# iClosed widget script + popup wiring on all booking CTAs
idx = idx.replace('<link rel="stylesheet" href="styles.css">',
  '<link rel="stylesheet" href="styles.css">\n<!-- iClosed popup widget begin -->\n<script type="text/javascript" src="https://app.iclosed.io/assets/widget.js" async></script>\n<!-- iClosed popup widget end -->')
idx = wire_booking(idx)
idx = idx.replace("wyatt@nwai.co", "consulting@nwai.co")
open(os.path.join(OUT, "index.html"), "w").write(idx)
print("wrote index.html")

print("DONE. Files:", sorted(os.listdir(OUT)))
