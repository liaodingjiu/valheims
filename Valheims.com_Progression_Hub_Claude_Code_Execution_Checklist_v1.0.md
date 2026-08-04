# Valheims.com Progression Hub Claude Code Execution Checklist v1.0

Version: 1.0

Target URL:

    https://valheims.com/progression/

Project Type:

Static HTML + CSS + JS website

Goal:

Create a new SEO Hub page without replacing existing HTML pages.

------------------------------------------------------------------------

# 1. Implementation Rules

## Additive Upgrade Only

DO NOT:

-   Delete existing pages
-   Rename existing URLs
-   Replace existing guides
-   Change existing URL structure

DO:

-   Create new `/progression/`
-   Add internal links
-   Improve site architecture
-   Preserve existing SEO assets

------------------------------------------------------------------------

# 2. New Page Creation

Create:

    /progression/index.html

Page type:

SEO Hub Page

Purpose:

Central Valheim progression navigation hub.

------------------------------------------------------------------------

# 3. Required HTML Structure

Implement:

    Header

    Hero Section

    Progression Roadmap

    Progression Chart

    Progression Checklist

    Biome Progression Cards

    Boss Progression

    Gear Progression

    Crafting Progression

    FAQ

    Related Guides

    Footer

------------------------------------------------------------------------

# 4. SEO Metadata

## Title

    Valheim Progression Guide - Complete Biome, Boss & Gear Order

## Meta Description

    Complete Valheim progression guide covering biome order, boss sequence, gear upgrades, crafting unlocks, and what to do next from Meadows to Ashlands.

## Canonical

``` html
<link rel="canonical" href="https://valheims.com/progression/">
```

## Robots

``` html
<meta name="robots" content="index, follow">
```

------------------------------------------------------------------------

# 5. Schema Implementation

Add JSON-LD:

Required:

-   BreadcrumbList
-   FAQPage
-   Article

Validate with Google Rich Results Test.

------------------------------------------------------------------------

# 6. Content Requirements

Minimum:

2500 words.

Must cover:

-   biome order
-   boss order
-   gear progression
-   crafting progression
-   survival milestones

Avoid:

-   copied wiki content
-   generic AI filler
-   keyword stuffing

------------------------------------------------------------------------

# 7. Internal Links From Progression Hub

## Boss Cluster

    /boss-order.html
    /eikthyr-guide.html
    /elder-guide.html
    /bonemass-guide.html
    /moder-guide.html
    /yagluth-guide.html
    /queen-guide.html
    /fader-guide.html

## Biome Cluster

    /biome-guide.html
    /ashlands-guide.html
    /deep-north-guide.html

## Equipment Cluster

    /best-weapons.html
    /armor-guide.html
    /food-recipes.html

## Survival Cluster

    /beginner-guide.html
    /building-guide.html
    /base-defense.html
    /taming-guide.html

------------------------------------------------------------------------

# 8. Existing Page Updates

Update:

## Homepage

    index.html

Add a Valheim Progression Guide section linking to:

    /progression/

------------------------------------------------------------------------

## Category Hubs

Update:

    guides-bosses.html
    guides-equipment.html
    guides-world.html
    guides-survival.html
    guides-technical.html

Add contextual links to the progression hub.

------------------------------------------------------------------------

## Boss Pages

Update:

    boss-order.html
    eikthyr-guide.html
    elder-guide.html
    bonemass-guide.html
    moder-guide.html
    yagluth-guide.html
    queen-guide.html
    fader-guide.html

Add:

    See the complete Valheim progression order.

Link:

    /progression/

------------------------------------------------------------------------

## Equipment Pages

Update:

    best-weapons.html
    armor-guide.html
    food-recipes.html

Add progression context links.

------------------------------------------------------------------------

# 9. Sitemap Update

Update:

    sitemap.xml

Add:

    https://valheims.com/progression/

Recommended:

    priority: 0.9

    changefreq: weekly

------------------------------------------------------------------------

# 10. CSS Requirements

Reuse:

    shared.css

Avoid duplicate CSS.

Required components:

-   Hero section
-   Timeline roadmap
-   Progression cards
-   Responsive tables
-   FAQ accordion

------------------------------------------------------------------------

# 11. Mobile Requirements

Support:

-   320px
-   375px
-   768px
-   1024px

Check:

-   tables
-   cards
-   navigation
-   images
-   schema rendering

------------------------------------------------------------------------

# 12. Image Requirements

Recommended WebP images:

    valheim-progression-chart.webp

    valheim-biome-progression.webp

    valheim-gear-progression.webp

Requirements:

-   descriptive filenames
-   alt text
-   compressed size

------------------------------------------------------------------------

# 13. Performance Requirements

Target:

Good Core Web Vitals.

Avoid:

-   heavy JavaScript
-   unnecessary libraries
-   oversized images

------------------------------------------------------------------------

# 14. QA Checklist

## HTML

\[ \] Valid HTML

\[ \] One H1

\[ \] Correct heading hierarchy

## SEO

\[ \] Title correct

\[ \] Description correct

\[ \] Canonical correct

\[ \] Schema valid

## Links

\[ \] No broken links

\[ \] Internal links added

## Mobile

\[ \] Responsive tested

\[ \] Tables usable

## Indexing

\[ \] Sitemap updated

\[ \] Robots checked

------------------------------------------------------------------------

# 15. Deployment Checklist

Before publishing:

\[ \] Local test completed

\[ \] Mobile test completed

\[ \] Rich Results validation completed

\[ \] Sitemap submitted

\[ \] Search Console inspection requested

------------------------------------------------------------------------

# 16. Expected SEO Outcome

Google should understand:

    Valheims.com

        |

    Valheim Progression Hub

        |

    Complete Valheim Guide Ecosystem

The page should become the authority page for:

    valheim progression

and distribute authority to:

-   Boss guides
-   Biome guides
-   Equipment guides
-   Survival guides
