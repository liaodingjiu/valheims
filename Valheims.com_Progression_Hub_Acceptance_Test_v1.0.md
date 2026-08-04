# Valheims.com Progression Hub Acceptance Test v1.0

Version: 1.0

Target URL:

    https://valheims.com/progression/

Project:

Valheims.com Progression Hub

Page Type:

SEO Topic Authority Hub

------------------------------------------------------------------------

# 1. Acceptance Goal

Verify that the Progression Hub implementation satisfies:

-   SEO requirements
-   Technical requirements
-   Content requirements
-   Internal linking requirements
-   User experience requirements

Expected architecture:

    Valheims.com

            |

    Valheim Progression Hub

            |

    Complete Valheim Guide Ecosystem

------------------------------------------------------------------------

# 2. URL Validation

Required URL:

    /progression/

Checklist:

-   [ ] HTTP 200 status
-   [ ] No redirect issues
-   [ ] Canonical URL correct
-   [ ] All assets load correctly

------------------------------------------------------------------------

# 3. Existing Page Safety

This is an additive upgrade.

Existing pages must remain:

    /boss-order.html
    /biome-guide.html
    /best-weapons.html
    /armor-guide.html
    /beginner-guide.html

Checklist:

-   [ ] Existing URLs unchanged
-   [ ] Existing pages accessible
-   [ ] No HTML files removed

------------------------------------------------------------------------

# 4. SEO Metadata Test

## Title

Expected:

    Valheim Progression Guide - Complete Biome, Boss & Gear Order

Checklist:

-   [ ] Exists
-   [ ] Unique
-   [ ] Matches search intent

------------------------------------------------------------------------

## Meta Description

Expected:

    Complete Valheim progression guide covering biome order, boss sequence, gear upgrades, crafting unlocks, and what to do next from Meadows to Ashlands.

Checklist:

-   [ ] Exists
-   [ ] Relevant
-   [ ] Not duplicated

------------------------------------------------------------------------

## Canonical

Required:

``` html
<link rel="canonical" href="https://valheims.com/progression/">
```

Checklist:

-   [ ] Correct canonical
-   [ ] Only one canonical tag

------------------------------------------------------------------------

# 5. Heading Structure

## H1

Required:

    Valheim Progression Guide

Checklist:

-   [ ] One H1 only
-   [ ] Contains primary keyword

------------------------------------------------------------------------

## Required H2 Sections

    Valheim Progression Roadmap

    Valheim Progression Chart

    Valheim Progression Checklist

    Biome Progression Guide

    Boss Progression Order

    Gear Progression

    Frequently Asked Questions

Checklist:

-   [ ] Logical hierarchy
-   [ ] No skipped heading levels

------------------------------------------------------------------------

# 6. Content Quality Test

Minimum:

    2500+ words

Required coverage:

## Progression System

-   Explain how Valheim progression works
-   Explain unlock dependencies

## Biomes

Required:

    Meadows
    Black Forest
    Swamp
    Mountain
    Plains
    Mistlands
    Ashlands
    Deep North

Checklist:

-   [ ] Correct order
-   [ ] Difficulty explained
-   [ ] Resources explained

------------------------------------------------------------------------

## Boss Progression

Required:

    Eikthyr
    The Elder
    Bonemass
    Moder
    Yagluth
    The Queen
    Fader

Checklist:

-   [ ] Correct sequence
-   [ ] Connection to progression explained

------------------------------------------------------------------------

## Gear Progression

Must cover:

    Tools
    Weapons
    Armor
    Food
    Crafting upgrades

Checklist:

-   [ ] Upgrade logic explained
-   [ ] Not only item lists

------------------------------------------------------------------------

# 7. Search Intent Coverage

Primary:

    valheim progression

Must answer:

    How do I progress in Valheim?

Secondary:

## Checklist Intent

Keyword:

    valheim progression checklist

Requirement:

-   [ ] Checklist section exists

## Chart Intent

Keyword:

    valheim progression chart

Requirement:

-   [ ] Visual roadmap exists

## Order Intent

Keyword:

    valheim progression order

Requirement:

-   [ ] Clear progression sequence exists

------------------------------------------------------------------------

# 8. Internal Linking Test

The page must link to:

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

Checklist:

-   [ ] Links work
-   [ ] No 404 errors
-   [ ] Anchor text descriptive

------------------------------------------------------------------------

# 9. Schema Validation

Required:

-   Article Schema
-   BreadcrumbList Schema
-   FAQPage Schema

Checklist:

-   [ ] JSON-LD valid
-   [ ] Rich Results Test passed
-   [ ] FAQ matches visible content

------------------------------------------------------------------------

# 10. Image SEO

Required:

    valheim-progression-chart.webp

    valheim-biome-progression.webp

    valheim-gear-progression.webp

Checklist:

-   [ ] WebP format
-   [ ] Proper filenames
-   [ ] Alt attributes
-   [ ] Compressed images

------------------------------------------------------------------------

# 11. Mobile UX Test

Test:

    320px
    375px
    768px
    1024px

Checklist:

-   [ ] Navigation works
-   [ ] Cards responsive
-   [ ] Tables usable
-   [ ] Images responsive
-   [ ] Text readable

------------------------------------------------------------------------

# 12. Performance Test

Checklist:

-   [ ] No unnecessary JavaScript
-   [ ] Images optimized
-   [ ] No layout shift issues
-   [ ] Fast loading

------------------------------------------------------------------------

# 13. Sitemap Test

Update:

    sitemap.xml

Required:

    https://valheims.com/progression/

Checklist:

-   [ ] Added
-   [ ] Sitemap valid
-   [ ] Submitted

------------------------------------------------------------------------

# 14. Final Approval

Status:

    PASS / FAIL

Approved by:

    SEO:

    Developer:

    Date:

------------------------------------------------------------------------

# Expected Result

Google should identify:

    Valheims.com

    as a complete Valheim knowledge hub

    with Progression as the central topic authority page.
