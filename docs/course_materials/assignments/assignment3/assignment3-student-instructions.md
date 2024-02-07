# Assignment 3 - Your Space



### Background 
- You now have a category in the server dedicated you and your capstone project!
- It is named something like `#FF00FF` 
  - i.e. the unique hex code you made when you signed up
  - Botto should've probably DM'd your ID to you if you forgot it 
- You have full control within your category to make channels and configure them as you like!
   - NOTE - If I have configured this correctly, 
      - You should have full control within your category, but OTHER students will only have 'view' access, not 'write' access
- When you make a new /chat, the bot is configured to follow certain instructions that guides its behavior/personality
- Every chat in the server will follow the instructions in the [`#bot-instructions🔝`](https://discord.com/channels/1194766712680222800/1194766713267433554) channel
  - Specifically, every message tagged with a `🤖` reaction/emoji is added to the bots' 'System Prompt'
    - The 'System Prompt' is (roughly speaking) a set of instructions that is stuffed into the bot's head to define its behavior
- In this assignment you will be adding new system prompts to your category so that you can have conversations with the bot that a pre-configured to your project plans

### Task - set up your space   
#### Step 1 - Setting up the Bot Prompt channel (#🤖-prompt-settings)
 - Go into the `🤖-prompt-settings`
 - Send a message to that channel that includes:
   - **A brief description of what you intend to do for your capstone project**
     - If you aren't sure about your topic yet, just say so in the message!
       - Like, "I'm not totally sure yet, but it will be realted to [something something something]"
   - **#topic-tags representing topic areas related to your project**
     - These should be written with a leading # and `kebab-case` formatting (i.e. lowercase words separated by hypens)
     - The tag itself should be 2-3 words long
     - Include: 
       - 3-5 very general topic tags, e.g. `#neuroscience` or `#genetics` or `#oncology`
       - 3-5 more specific topic tags e.g. `#perceptuomotor-control` or `#CRISPR` or `#glioblastoma`
  - Your message should follow roughly this schema:
```
# Brief project description (note there is a SPACE between the # and the text, denoting an `H1 heading`)
{1-2 sentences about what you want to focus on for your capstone project}

## Topic tags (note that there are TWO ##, denoting `H2 heading`)

#general-topic-tag1 (note there is NO SPACE between the # and the text, denoting `#tag`)
#general-topic-tag2
#general-topic-tag3

#specific-topic-tag1
#specific-topic-tag2
#specific-topic-tag3
```

#### 👉 IMPORTANT DON'T SKIP THIS STEP 👈
- ONCE YOU HAVE SENT THE MESSAGE TO THE CHANNEL, ADD A 🤖 REACTION SO THE BOT WILL USE THAT MESSAGE IN ITS SYSTEM PROMPT


NOTES - 
- You can and will be changing this message regularly, so don't over think it! You're not getting married to it, so just get something down and you can and will  tweak/hone/improve continuously moving forward
- By the way, this practice of changing the bot's behavior by changing its system prompt is called [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)

---
#### Step 2 - Pick your favorite topic tag, and make a channel conifigured for discussion of that topic
1.  Make a new channel in your category 
      1. Click the + sign next to the Category Name
      1. Select `# TEXT` channel
      1. Name the channel after the major topic
      1. Click the Edit Channel button and add some more detail about the topic and how it relates to your project/intests
          - Use the `#general-chat` channel to have conversations outside of any of these topics
          - Use that area to draft and hone text you are using in the different categories
1.  Change the channel description to provide the bot with context about what you plan to discuss in this channel 
    1.  Click the `Edit Channel` 

---
##### Option 1 - Use the bot
- Go back and extract summaries from your previous conversations about the topics you want to do your capstone about (or ignore them and start from scratch if you want - truly doesn't matter).
  - Extract a short summary of your project. It should fit within a single discord message (so ~2000 characters) and be of the form

##### Option 2 - Do it yourself, manually
- Just, like, write yourself
  - Pro: You get to write exactly the words you want
  - Cons: You have the words yourself. 

##### Option 3 (aka the smart move) - Do both 
- Use the bot to help you get started, and then edit the text it produces so it ACTUALLY fits what you want it to say
