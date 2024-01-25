Using the text in this conversation, please come up with a document following the schema (at the bottom) which contains sections described below. Wrap [[key terms]] in double brackets to create wiki style links: 

BEGIN SECTION DESCRIPTIONS:

title:  "The title of the research article"
author_year:  "The author and year of the research article (e.g. 'Smith et al. 2020')"
citation:  "The citation to the research article"

detailed_summary:  "A detailed summary/overview of the major points of the paper in a bulleted outline format ( with * to denote bullet points) with 1-2 sentence top level bullet points and second-level bullet points"
short_summary:  "A short (2-3 sentence) summary of the paper"
very_short_summary:  "A very short one sentence summary of the research article"
extremely_short_summary:  "An extremely short 6-10 word summary of the research article"
basic_methodology: "A basic description of the methodology used in the research article (e.g. information about tools used, species studied, analytical techniques, etc.)"
summary_title:      "A summary title made by combining the `author_year` field with the `extremely_short_summary` field, like this: ['author_year'] - ['extremely_short_summary']")
tags:  "A list of tags formatted using #kebab-case-lowercase")

END SECTION DESCRIPTIONS

BEGIN DOCUMENT SCHEMA EXAMPLE:
# {summary_title}\n
## Title\n
{title}\n\n
## Citation:\n
{citation}\n\n
## Basic Methodology\n
{basic_methodology}\n\n
## Detailed Summary\n
{detailed_summary}\n\n
## Paper summaries
### Short Summary\n
{short_summary}\n\n
### Very Short Summary\n
{very_short_summary}\n\n
### Extremely Short Summary\n
{extremely_short_summary}\n\n

### Tags\n
{tags}\n\n

END DOCUMENT SCHEMA EXAMPLE


Remember! Your job is to use the text in this conversation, please come up with a document following the schema (at the bottom) which contains sections described below. Wrap [[key terms]] in double brackets to create wiki style links

DO NOT MAKE THINGS UP! If you do not have enough information to complete your task, just put `MORE INFORMATION NEEDED` in that section and then ask the human to provide the necessary information.
