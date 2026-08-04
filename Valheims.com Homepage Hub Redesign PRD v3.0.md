# Valheims.com Homepage Hub Redesign PRD v3.0

Version:
v3.0 Final

Project:
Valheims.com Homepage Hub Upgrade

Target File:

/index.html


---

# 1. Project Overview


## Background

Valheims.com currently contains multiple Valheim guide pages:

- Boss guides
- Equipment guides
- Biome guides
- Survival guides
- Technical guides


However, the current homepage does not clearly communicate:

- The site's complete Valheim knowledge structure
- The relationship between different guide categories
- The recommended player journey
- The importance of the Progression Hub


The homepage currently behaves like a directory.

The goal is to transform it into:

> A Valheim player's starting point and a topic authority navigation layer.


---

# 2. Main Objective


After redesign, users should understand within 5 seconds:


"Valheims.com helps me progress through Valheim from my first shelter to endgame."


The homepage should answer:


1. What is this website?

2. Where should I start?

3. What should I do next?

4. Which guide should I read?


---

# 3. Important Constraints


## DO NOT


Do NOT:

- Change homepage URL
- Create a new homepage file
- Remove existing valuable content
- Delete existing internal links
- Break current SEO metadata
- Remove existing guide pages


## ONLY MODIFY


Allowed:

- Homepage HTML structure
- Homepage sections
- Internal linking structure
- Visual hierarchy
- Hero section
- Navigation cards
- SEO copy improvements


---

# 4. SEO Positioning


## Primary Keyword


Primary:

Valheim Guide


## Secondary Keywords


- Valheim progression
- Valheim bosses
- Valheim biomes
- Valheim weapons
- Valheim armor
- Valheim survival guide


## Search Intent


Homepage should satisfy:

"I need a complete Valheim guide resource."


Not:

"I need one specific answer."


---

# 5. Homepage Role In Information Architecture


The homepage becomes:



Homepage

|
|
+-- Progression Hub

|
|
+-- Boss Guides

|
|
+-- Biome Guides

|
|
+-- Equipment Guides

|
|
+-- Survival Guides


The homepage distributes authority to important hubs.


---

# 6. Page Structure


# Section 1: Hero


## Goal


Immediately communicate:

- Valheim expertise
- Complete journey coverage
- Clear next action


---

## H1


Recommended:



Valheim Guide: Progression, Bosses & Survival



Requirements:

- Must contain "Valheim Guide"
- Must communicate gameplay journey


---

## Hero Subtitle


Recommended:



Complete guides for Valheim progression,
boss strategies, biomes, gear upgrades,
building and survival.



Requirements:

- Maximum 3 lines
- Benefit focused
- No keyword stuffing


---

## Primary CTA


Button:



Start Progression Guide



Link:



/progression/



Purpose:

Guide new players into the strongest Hub.


---

## Hero Value Pills


Add four benefit indicators:



✓ Complete Adventure Roadmap

✓ Bosses In Order

✓ Gear Progression

✓ Beginner Friendly



Design:

- Capsule style
- Easy scanning
- Mobile friendly


---

# Section 2: Start Your Valheim Journey


## Purpose


This is the most important homepage section.


It introduces:

/progression/


---

## Content


Title:



Start Your Valheim Journey



Subtitle:



Not sure what to do next?
Follow the complete progression path.



---

## Visual Roadmap


Display:



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



---

CTA:



Explore Progression Guide



Link:


/progression/



---

# Section 3: Player Stage Navigation


## Purpose


Match different user situations.


Title:



Where Are You In Your Journey?



Create four cards.


---

## Card 1


Title:


Just Started



Description:


Learn basic survival,
tools, food and first shelter.



Link:


/beginner-guide.html



---

## Card 2


Title:


Preparing For Bosses



Description:


Find boss order,
summons and strategies.



Link:


/boss-order.html



---

## Card 3


Title:


Mid Game



Description:


Explore new biomes,
resources and upgrades.



Link:


/biome-guide.html



---

## Card 4


Title:


End Game



Description:


Prepare for Mistlands,
Ashlands and final challenges.



Link:


/ashlands-guide.html



---

# Section 4: Core Guide Areas


## Purpose


Create main topic authority structure.


Display six cards.


---

## Card List


### Progression

Link:


/progression/



Description:


Follow the complete Valheim journey.



---

### Bosses


Link:

existing boss hub


Description:


Boss order, strategies and rewards.



---

### Biomes


Link:

existing biome guide


Description:


Explore every biome and discover resources.



---

### Weapons & Armor


Link:

existing equipment pages


Description:


Find the best gear and upgrades.



---

### Food & Crafting


Link:

existing food/crafting pages


Description:


Recipes, unlocks and crafting systems.



---

### Building


Link:

existing building guide


Description:


Create stronger and better bases.



---

# Section 5: Popular Guides


## Purpose


Transfer homepage authority to existing pages.


Recommended links:



Boss Order

Best Weapons

Armor Guide

Biome Guide

Food Recipes

Building Guide



---

# Section 6: Latest Guides


Purpose:

Freshness signal.


Content examples:



Ashlands Guide

Deep North Guide

Mods Guide

Server Setup Guide



---

# Section 7: Trust / Experience Section


## Purpose


Improve E-E-A-T signals.


Do NOT claim:

- official wiki
- developer affiliation


Use:



Practical Valheim guides built around:

✓ Clear progression paths

✓ Boss strategies

✓ Biome exploration

✓ Survival systems



---

# Section 8: FAQ


Add:


## FAQ 1

Question:


What order should you play Valheim?



Answer:

Link to:


/progression/



---

## FAQ 2

Question:


What boss should I fight first?



Answer:

Link to:


/boss-order.html



---

## FAQ 3

Question:


What biome comes after Swamp?



Answer:

Link to:


/biome-guide.html



---

## FAQ 4

Question:


What are the best weapons in Valheim?



Answer:

Link to:


/best-weapons.html



---

# 7. Internal Linking Strategy


Homepage priority:


Highest:


/progression/



Medium:


/boss-order.html

/biome-guide.html

/best-weapons.html

/armor-guide.html



Secondary:


/mods-guide.html

/server-setup.html

/building-guide.html



---

# 8. UX Requirements


## Typography


Increase readability.


Requirements:


Hero H1:

Desktop:

48-56px


Body:

18px minimum


Line height:

1.6+


---

## Spacing


Avoid dense layout.


Each section requires:

- clear whitespace
- visual separation
- strong hierarchy


---

# 9. Mobile Requirements


Test:


375px width


Requirements:


- Hero fits naturally
- CTA visible
- Cards stack vertically
- Text remains readable
- No horizontal overflow


---

# 10. SEO Technical Requirements


Maintain:


- Existing canonical
- Existing title structure
- Existing metadata
- Existing schema


Recommended additions:


- WebSite schema
- Organization schema
- Breadcrumb schema


---

# 11. Acceptance Criteria


## User Experience


PASS:


[ ] User understands website purpose in 5 seconds

[ ] Progression is obvious starting point

[ ] Homepage does not feel like article archive

[ ] Typography feels premium


---

## SEO


PASS:


[ ] "Valheim Guide" clearly targeted

[ ] Progression Hub receives strongest internal link

[ ] Existing guide pages receive authority


---

## Technical


PASS:


[ ] Existing URLs unchanged

[ ] No broken links

[ ] Mobile responsive


---

# Final Goal


After implementation:


Valheims.com should be understood as:



A complete Valheim adventure guide hub

where players can start,
progress,
upgrade,
explore,
and finish their journey.



END