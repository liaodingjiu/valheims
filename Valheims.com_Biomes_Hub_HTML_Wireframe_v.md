Valheims.com_Biomes_Hub_HTML_Wireframe_v1.0.md
# Valheims.com Biomes Hub HTML Wireframe v1.0

Version:

v1.0


Project:

Valheims.com Biomes Hub


Target URL:

/biomes/


Document Purpose:

Define the HTML structure, layout system, CSS components, responsive behavior, and UX requirements for the new Biomes Hub page.


---

# 1. Page Objective


The Biomes Hub should transform Valheims.com from a collection of individual biome articles into a structured Valheim world exploration system.


The page should feel like:


- A Valheim world atlas
- A biome progression map
- A survival navigation dashboard


The page should NOT feel like:


- A traditional SEO article
- A text-heavy wiki page
- A blog post


---

# 2. Overall HTML Structure


Recommended structure:


```html
<body>

<header>
    Global Navigation
</header>


<main>


<section class="biomes-hero">
    Hero Section
</section>


<section class="biome-roadmap">
    Biome Progression Map
</section>


<section class="biome-comparison">
    Biome Comparison Table
</section>


<section class="biome-guide-grid">
    Individual Biome Cards
</section>


<section class="biome-preparation">
    Preparation Guide
</section>


<section class="biome-resources">
    Resource Navigation
</section>


<section class="biome-faq">
    FAQ Section
</section>


</main>


<footer>

</footer>


</body>
3. Hero Section Wireframe
Purpose

The first screen must immediately communicate:

"This page tells me every Valheim biome and the correct order to explore them."

Desktop Layout
--------------------------------------------------


WORLD PROGRESSION MAP


Valheim Biomes Guide


Explore every biome in the correct order,
including resources, enemies,
bosses and gear requirements.



[ View Biome Progression ]



[ All Biomes Covered ]

[ Progression Order ]

[ Resources ]

[ Gear Requirements ]


--------------------------------------------------
HTML Structure
<section class="biomes-hero">


<div class="hero-container">


<span class="hero-label">

WORLD PROGRESSION MAP

</span>



<h1>

Valheim Biomes Guide

</h1>



<p class="hero-description">

Explore every Valheim biome in the right order,
including resources, enemies, bosses and gear.

</p>



<div class="hero-pills">


<span>
All Biomes Covered
</span>


<span>
Progression Order
</span>


<span>
Resources
</span>


<span>
Gear Requirements
</span>


</div>



<a class="hero-button">

View Biome Progression

</a>



</div>


</section>
4. Biome Progression Roadmap Section
Purpose

This is the most important visual component.

It connects directly with:

/progression/

The user should understand:

"Where do I go next?"

Desktop Layout
Meadows

↓

Black Forest

↓

Swamp

↓

Mountains

↓

Plains

↓

Mistlands

↓

Ashlands

↓

Deep North
HTML Structure
<section 
id="biome-roadmap"
class="biome-roadmap">


<h2>

Valheim Biome Progression Order

</h2>



<div class="biome-map">


<div class="biome-node">

<h3>
Meadows
</h3>

<span>
Starter
</span>

</div>



<div class="biome-arrow">

↓

</div>



...

</div>


</section>
5. Biome Node Component

Each biome node should include:

Required information:

Biome Name
Difficulty Level
Progression Stage
Main Resources
Main Boss
Guide Link

Example:

<div class="biome-node">


<h3>

Black Forest

</h3>


<span class="difficulty">

Early Game

</span>


<ul>

<li>
Copper
</li>

<li>
Tin
</li>

<li>
Core Wood
</li>


</ul>


<p>

Boss:
The Elder

</p>


<a href="/black-forest-guide.html">

Read Guide

</a>


</div>
6. Biome Comparison Section
Purpose

Target search intent:

Valheim biome order
Valheim biome difficulty
Valheim biome progression
Desktop Table

Structure:

Biome	Difficulty	Boss	Resources	Recommended Gear
Meadows	Starter	Eikthyr	Wood, Flint	Leather
Black Forest	Early	Elder	Copper, Tin	Bronze
Swamp	Mid	Bonemass	Iron	Iron
Mountains	Mid-Late	Moder	Silver	Wolf Armor
Plains	Late	Yagluth	Black Metal	Padded
Mistlands	Endgame	Queen	Eitr	Magic Gear
Ashlands	Endgame	Fader	Flametal	Ashlands Gear
Mobile Behavior

Desktop table must transform into stacked cards.

Example:

Biome:

Swamp


Difficulty:

Mid Game


Boss:

Bonemass


Resources:

Iron


Gear:

Iron Armor
7. Individual Biome Guide Grid
Purpose

Transfer authority to individual biome pages.

Layout

Desktop:

4 columns

Tablet:

2 columns

Mobile:

1 column
Cards

Required biome cards:

Meadows

Beginner survival

Black Forest

Bronze progression

Swamp

Iron age

Mountains

Silver progression

Plains

Black Metal progression

Mistlands

Magic progression

Ashlands

Late game combat

Deep North

Future content

Card HTML
<div class="biome-card">


<h3>

Mistlands

</h3>


<p>

End Game

</p>


<p>

Magic, Eitr and advanced crafting.

</p>


<a>

Explore Mistlands Guide

</a>


</div>
8. Biome Preparation Section
Purpose

Answer:

"What should I bring before entering this biome?"

Components

Each preparation block:

Weapons

Recommended weapon tier

Armor

Recommended protection

Food

Recommended meals

Resistance

Required protection

Items

Essential supplies

9. Resource Navigation Section
Purpose

Capture resource-based searches.

Resource Cards

Examples:

Copper

Iron

Silver

Black Metal

Eitr

Flametal

Each resource card links to related guides.

10. FAQ Section

Structure:

<section class="biome-faq">

<h2>

Frequently Asked Questions

</h2>


</section>

Recommended questions:

Question 1

What is the biome order in Valheim?

Question 2

What biome comes after Swamp?

Question 3

What is the hardest biome in Valheim?

Question 4

When should I enter Mistlands?

11. CSS Component Requirements

Required classes:

.biomes-hero

.hero-label

.hero-container

.hero-pills

.hero-button

.biome-roadmap

.biome-map

.biome-node

.biome-arrow

.biome-comparison

.biome-table

.biome-guide-grid

.biome-card

.biome-preparation

.resource-card

.biome-faq
12. Visual Design Requirements

Design direction:

Premium Valheim guide experience.

Recommended feeling:

Dark fantasy
Adventure map
Game dashboard
World exploration

Avoid:

Dense paragraphs
Small fonts
Wikipedia layout
13. Typography Requirements

Desktop:

H1:

48px - 56px

H2:

32px - 40px

Body:

18px minimum

Line height:

1.6+

Mobile:

H1:

32px - 38px

Body:

16px - 18px

14. Responsive Requirements

Target device:

375px mobile

Requirements:

Hero
No overflow
CTA visible
Text readable
Roadmap

Desktop:

Horizontal

Mobile:

Vertical

Cards

Desktop:

Grid

Mobile:

Single column

Tables

Convert into cards.

15. Developer Implementation Notes

Do:

Create new:
/biomes/index.html
Reuse:
shared.css
Maintain existing site architecture

Do NOT:

Remove biome-guide.html
Replace old pages
Break existing links
Change global navigation without approval
16. Acceptance Criteria
UX

PASS:

User understands biome order within 5 seconds
Hero communicates page purpose
Roadmap is visually dominant
Page feels like a game guide system
SEO

PASS:

Keyword "Valheim Biomes" clearly targeted
Internal links point to biome pages
Progression relationship is clear
Technical

PASS:

Mobile responsive
No broken links
Existing pages preserved
Final Goal

After implementation:

Google should understand:

"Valheims.com provides a complete Valheim biome progression and exploration resource."

Users should understand:

"This page tells me where to go, what to find, and how to prepare."

END