# Valheims.com Biomes Hub Schema & SEO Specification v1.0

Version:

v1.0


Project:

Valheims.com Biomes Hub


Target URL:

/biomes/


Document Purpose:

Define SEO metadata, structured data, schema implementation, and technical SEO requirements for the Valheim Biomes Hub page.


---

# 1. SEO Positioning


## Page Type


Primary:



Collection Hub Page



Secondary:



Guide Landing Page



This page is NOT:


- A single article
- A news page
- A wiki entry


---

# 2. Search Engine Understanding Goal


Google should understand:



Valheims.com

owns a structured Valheim Biomes knowledge collection

containing:

- biome order
- biome progression
- biome resources
- biome guides
- biome preparation information


---

# 3. URL Specification


Final URL:



https://valheims.com/biomes/



Requirements:


- Clean URL
- No .html extension
- Permanent URL


---

# 4. Title Tag Specification


## Recommended Title



Valheim Biomes Guide - Complete Biome Order & Progression



Length:


Approx:

58-62 characters


---

## SEO Reason


Contains:


Primary:


Valheim Biomes



Secondary:


Biome Order
Biome Progression



---

# 5. Meta Description Specification


Recommended:



Explore every Valheim biome in the correct order. Learn biome progression, resources, enemies, bosses, and gear requirements from Meadows to Ashlands.



Length:


150-160 characters


---

# 6. H1 Specification


Required:



Valheim Biomes Guide



Rules:


- Exact primary keyword
- One H1 only
- Visible above fold


---

# 7. Heading Structure


Recommended:



H1
Valheim Biomes Guide

H2
Valheim Biomes Explained

H2
Valheim Biome Order and Progression

H2
Valheim Biomes by Difficulty

H2
Complete Biome Guides

H2
What To Bring Before Entering Each Biome

H2
Important Resources Found In Each Biome

H2
Frequently Asked Questions



---

# 8. Structured Data Strategy


Required Schema:


1. BreadcrumbList

2. CollectionPage

3. ItemList

4. FAQPage


Optional:


5. WebSite reference


---

# 9. BreadcrumbList Schema


Purpose:


Help Google understand hierarchy.


Structure:



Home

Biomes



JSON-LD:


```json
{
 "@context": "https://schema.org",
 "@type": "BreadcrumbList",
 "itemListElement": [
  {
   "@type": "ListItem",
   "position": 1,
   "name": "Home",
   "item": "https://valheims.com/"
  },
  {
   "@type": "ListItem",
   "position": 2,
   "name": "Biomes",
   "item": "https://valheims.com/biomes/"
  }
 ]
}
10. CollectionPage Schema

Purpose:

Tell Google this is a content collection.

JSON-LD:

{
 "@context":"https://schema.org",
 "@type":"CollectionPage",

 "name":
 "Valheim Biomes Guide",

 "description":
 "Complete Valheim biome guide covering biome order, progression, resources, enemies, bosses and preparation.",

 "url":
 "https://valheims.com/biomes/"
}
11. ItemList Schema

Purpose:

Represent biome collection.

Items:

Meadows
Black Forest
Swamp
Mountains
Plains
Mistlands
Ashlands
Deep North

JSON-LD:

{
 "@context":"https://schema.org",
 "@type":"ItemList",

 "name":
 "Valheim Biome Progression Order",

 "itemListElement":[

 {
 "@type":"ListItem",
 "position":1,
 "name":"Meadows"
 },

 {
 "@type":"ListItem",
 "position":2,
 "name":"Black Forest"
 },

 {
 "@type":"ListItem",
 "position":3,
 "name":"Swamp"
 },

 {
 "@type":"ListItem",
 "position":4,
 "name":"Mountains"
 },

 {
 "@type":"ListItem",
 "position":5,
 "name":"Plains"
 },

 {
 "@type":"ListItem",
 "position":6,
 "name":"Mistlands"
 },

 {
 "@type":"ListItem",
 "position":7,
 "name":"Ashlands"
 }

 ]

}
12. FAQPage Schema

Purpose:

Support long-tail queries.

Questions:

FAQ 1

Question:

What is the biome order in Valheim?

Answer:

The recommended Valheim biome progression starts with Meadows, followed by Black Forest, Swamp, Mountains, Plains, Mistlands and Ashlands.
FAQ 2

Question:

What biome comes after Swamp in Valheim?

Answer:

Mountains is the next major biome after Swamp, where players begin searching for silver and preparing for Moder.
FAQ 3

Question:

What is the hardest biome in Valheim?

Answer:

Mistlands and Ashlands are currently among the most challenging Valheim biomes because they introduce stronger enemies and advanced progression systems.
FAQ 4

Question:

When should you enter Mistlands?

Answer:

Players should enter Mistlands after completing Plains progression and preparing stronger weapons, armor and food.
13. Canonical Specification

Required:

<link rel="canonical" href="https://valheims.com/biomes/">
14. Robots Specification

Allowed:

index, follow

Example:

<meta name="robots" content="index,follow">
15. Open Graph Metadata

Required:

<meta property="og:title"
content="Valheim Biomes Guide - Complete Biome Order & Progression">


<meta property="og:description"
content="Explore every Valheim biome with progression order, resources, enemies and preparation tips.">


<meta property="og:type"
content="website">


<meta property="og:url"
content="https://valheims.com/biomes/">
16. Twitter Card

Recommended:

<meta name="twitter:card"
content="summary_large_image">


<meta name="twitter:title"
content="Valheim Biomes Guide">


<meta name="twitter:description"
content="Complete biome progression guide from Meadows to Ashlands.">
17. Internal Link SEO Requirements

The page must contain links to:

Priority
/progression/


Anchor:

Valheim Progression Guide
Biome Pages

Examples:

/ashlands-guide.html

/deep-north-guide.html
Related Authority Pages
/boss-order.html

/best-weapons.html

/armor-guide.html

/food-recipes.html
18. Image SEO Requirements

Required images:

Hero Image

Example:

Valheim biome progression map

ALT:

Valheim biome progression map showing Meadows to Ashlands
Biome Cards

Each biome image:

ALT example:

Valheim Black Forest biome guide
19. Performance Requirements

Target:

Core Web Vitals friendly.

Requirements:

WebP images
Lazy loading below fold
Minimal JavaScript
Reuse shared.css
20. SEO Acceptance Checklist
Metadata

PASS:

[ ] Title optimized

[ ] Meta description optimized

[ ] Canonical added

[ ] Open Graph added

Schema

PASS:

[ ] BreadcrumbList

[ ] CollectionPage

[ ] ItemList

[ ] FAQPage

Content Signals

PASS:

[ ] Primary keyword in H1

[ ] Keyword supported by sections

[ ] Internal links implemented

Final SEO Goal

After implementation:

Google should classify:

/biomes/

as:

A comprehensive Valheim biome authority hub.


The page should compete for:

Valheim Biomes

Valheim biome order

Valheim biome progression


END