# Valheims.com Progression Hub HTML Wireframe v1.0

## 1. Page Overview

**URL**

    https://valheims.com/progression/

**Page Type**

SEO Hub Page

Purpose:

Create the central navigation page for Valheim player progression.

Primary user question:

> What should I do next in Valheim?

------------------------------------------------------------------------

# 2. Overall Page Layout

    HEADER

    Breadcrumb

    Hero Section

    Quick Progression Overview

    Progression Chart

    Progression Checklist

    Biome Stage Cards

    Boss Progression

    Gear Progression

    Related Guides

    FAQ

    Footer

------------------------------------------------------------------------

# 3. HTML Structure

Recommended structure:

    progression/
    │
    ├── index.html
    │
    └── assets/
        └── images/

Main structure:

``` html
<body>

<header>
    Site Navigation
</header>

<main>

<section class="breadcrumb">
</section>

<section class="hero">
</section>

<section class="progression-summary">
</section>

<section class="progression-chart">
</section>

<section class="progression-checklist">
</section>

<section class="stage-cards">
</section>

<section class="boss-progression">
</section>

<section class="gear-progression">
</section>

<section class="related-guides">
</section>

<section class="faq">
</section>

</main>

<footer>
</footer>

</body>
```

------------------------------------------------------------------------

# 4. Component Design

## Hero Section

Purpose:

Capture primary keyword.

H1:

    Valheim Progression Guide

Description:

    Complete Valheim progression roadmap covering biome order,
    bosses, gear upgrades, crafting unlocks, and survival milestones.

------------------------------------------------------------------------

## Quick Progression Overview

Purpose:

Featured snippet opportunity.

Example:

    Meadows
    ↓
    Black Forest
    ↓
    Swamp
    ↓
    Mountain
    ↓
    Plains
    ↓
    Mistlands
    ↓
    Ashlands
    ↓
    Deep North

------------------------------------------------------------------------

## Progression Chart

Target keyword:

    valheim progression chart

Required fields:

  Stage   Biome   Boss   Unlocks
  ------- ------- ------ ---------

Desktop:

Use table.

Mobile:

Convert to cards.

------------------------------------------------------------------------

## Progression Checklist

Target keyword:

    valheim progression checklist

Example:

    ☐ Defeat Eikthyr
    ☐ Build Forge
    ☐ Collect Bronze
    ☐ Enter Swamp
    ☐ Upgrade Iron Gear

------------------------------------------------------------------------

## Stage Cards

Each biome card contains:

-   Biome name
-   Difficulty
-   Boss
-   Objectives
-   Required resources
-   Unlocks
-   Related guides

Example:

    Meadows

    Boss:
    Eikthyr

    Objectives:
    - Build first base
    - Craft tools
    - Prepare food

    Related:
    Beginner Guide
    Boss Guide

------------------------------------------------------------------------

# 5. CSS Component Requirements

Reuse:

    shared.css

Add progression-specific components.

Required classes:

    .container
    .section
    .grid
    .flex

    .hero
    .hero-title
    .hero-description

    .progression-flow
    .flow-item
    .flow-arrow

    .stage-card
    .stage-title
    .stage-meta
    .stage-links

    .checklist-item
    .checkbox

------------------------------------------------------------------------

# 6. Responsive Mobile Layout

## Breakpoints

Desktop:

    >1024px

Tablet:

    768px-1024px

Mobile:

    <768px

------------------------------------------------------------------------

## Mobile Rules

### Progression Flow

Desktop:

    Meadows → Forest → Swamp

Mobile:

    Meadows

    ↓

    Forest

    ↓

    Swamp

------------------------------------------------------------------------

### Tables

Never allow horizontal scrolling.

Convert tables into stacked cards.

------------------------------------------------------------------------

### Stage Cards

Desktop:

3 columns

Mobile:

1 column

------------------------------------------------------------------------

# 7. SEO HTML Requirements

Required:

-   Unique title
-   Meta description
-   Canonical URL
-   BreadcrumbList schema
-   FAQPage schema
-   Article schema

Title:

    Valheim Progression Guide - Complete Biome, Boss & Gear Order

Description:

    Complete Valheim progression guide covering biome order, boss sequence, gear upgrades, crafting unlocks, and what to do next from Meadows to Ashlands.

------------------------------------------------------------------------

# 8. Image Requirements

Required:

1.  Progression roadmap visualization
2.  Biome progression visualization
3.  Gear progression diagram

Format:

-   WebP
-   Optimized size
-   Descriptive filenames
-   Accurate alt text

Example:

    valheim-progression-chart.webp

Alt:

    Valheim progression chart showing biome and boss order

------------------------------------------------------------------------

# 9. Performance Requirements

Technology:

-   Static HTML
-   CSS
-   Minimal JavaScript

Do not introduce:

-   React
-   CMS
-   Database
-   Heavy JS framework

------------------------------------------------------------------------

# 10. Development Principle

DO:

-   Extend existing website
-   Reuse shared.css
-   Maintain static architecture

DO NOT:

-   Replace existing pages
-   Change existing URL structure
-   Build database system in MVP
