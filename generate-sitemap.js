#!/usr/bin/env node
/**
 * Deploy-time sitemap generator for nwai-site.
 * Runs as the Vercel buildCommand on every deploy. Scans the repo root for
 * *.html and includes every page EXCEPT those that declare a noindex robots
 * meta (claude.html ads LP, 404/403 error pages, any noindex source file).
 * No hardcoded page list, so new pages appear automatically.
 */
const fs = require("fs");
const path = require("path");

const BASE = "https://nwai.co";
const ROOT = __dirname;

function isIndexable(file) {
  let html;
  try { html = fs.readFileSync(path.join(ROOT, file), "utf8"); }
  catch { return false; }
  const metas = html.match(/<meta[^>]*>/gi) || [];
  // exclude if any robots meta on the page contains noindex (order-agnostic)
  const noindex = metas.some(m => /name=["']robots["']/i.test(m) && /noindex/i.test(m));
  return !noindex;
}

function loc(file) {
  return file === "index.html" ? BASE + "/" : BASE + "/" + file.slice(0, -5) + "/";
}

const pages = fs.readdirSync(ROOT)
  .filter(f => f.toLowerCase().endsWith(".html") && isIndexable(f));

const ordered = [];
if (pages.includes("index.html")) ordered.push("index.html");
for (const f of pages.filter(f => f !== "index.html").sort()) ordered.push(f);

const today = new Date().toISOString().slice(0, 10);
const urls = ordered
  .map(f => `  <url>\n    <loc>${loc(f)}</loc>\n    <lastmod>${today}</lastmod>\n  </url>`)
  .join("\n");

const xml =
  '<?xml version="1.0" encoding="UTF-8"?>\n' +
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  urls + "\n</urlset>\n";

fs.writeFileSync(path.join(ROOT, "sitemap.xml"), xml);
console.log("generate-sitemap: wrote sitemap.xml with " + ordered.length + " urls");
