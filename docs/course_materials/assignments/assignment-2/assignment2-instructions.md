Using the text in this conversation, please come up with a document 
class PaperSummary(BaseModel):
    title: str = Field("", description="The title of the research article")
    author_year: str = Field("", description="The author and year of the research article (e.g. 'Smith et al. 2020')")
    citation: str = Field("", description="The citation to the research article")
    abstract: str = Field("", description="A copy-paste of the abstract of the research article")
    detailed_summary: str = Field("",
                                  description="A detailed summary/overview of the major points of the paper in a bulleted outline format ( with * to denote bullet points) with 1-2 sentence top level bullet points and second-level bullet points")
    short_summary: str = Field("", description="A short (2-3 sentence) summary of the paper")
    very_short_summary: str = Field("", description="A very short one sentence summary of the research article")
    extremely_short_summary: str = Field("", description="An extremely short 6-10 word summary of the research article")
    basic_methodology: str = Field("",
                                   description="A basic description of the methodology used in the research article (e.g. information about tools used, species studied, analytical techniques, etc.)")
    summary_title: str = Field("",
                               description="A summary title made by combining the `author_year` field with the `extremely_short_summary` field, like this: ['author_year'] - ['extremely_short_summary']")
    tags: str = Field("", description="A list of tags formatted using #kebab-case-lowercase")
    backlinks: str = Field("",
                           description="The same as the 'tags' field, but with double brackets around the tag name and without the # symbol, so '#tag-name' becomes '[[tag-name]]'")

    def __str__(self):
        tags = "\n".join(self.tags.split(" "))
        backlinks = "\n".join(self.backlinks.split(" "))
        return f"""
# {self.summary_title}\n
## Title\n
{self.title}\n\n
## Citation:\n
{self.citation}\n\n
## Abstract\n
{self.abstract}\n\n
## Basic Methodology\n
{self.basic_methodology}\n\n
## Detailed Summary\n
{self.detailed_summary}\n\n
## Short Summary\n
{self.short_summary}\n\n
## Very Short Summary\n
{self.very_short_summary}\n\n
## Extremely Short Summary\n
{self.extremely_short_summary}\n\n
## Tags\n
{tags}\n\n
## Backlinks\n
{backlinks}
"""
