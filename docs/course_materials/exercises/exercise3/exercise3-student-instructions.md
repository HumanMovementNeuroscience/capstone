# Exercise 3 - Setting Up Your Space

## Background 
- I have set each of you up with a category in the server dedicated you and your capstone project!
- It is named something like `#FF00FF` 
  - i.e. the unique hex code you made when you signed up
  - I will refer to this as your "student ID"

- You have full control within your category to make channels and configure them as you like!
  - I have also created "Role" for each student ID, which is used to control write access to the category
    - You should have full control within your category, but OTHER students will only have 'view' access, not 'write' access
  
- When you make a new /chat, the bot is configured to follow certain instructions that guides its behavior/personality
  
  
- Every chat in the server will follow the instructions in the [`#bot-instructions🔝`](https://discord.com/channels/1194766712680222800/1194766713267433554) channel
  - Specifically, every message tagged with a `🤖` reaction/emoji is added to the bots' 'System Prompt'
    - The 'System Prompt' is (roughly speaking) a set of instructions that is stuffed into the bot's head to define its behavior
- In this Exercise you will be adding new system prompts to your category so that you can have conversations with the bot that a pre-configured to your project plans
---
## Step-by-Step Guide

### Step 1 - Setting up the Bot Prompt channel (#🤖-prompt-settings)
 - Go into the `🤖-prompt-settings`
 - Send a message to that channel that follows this schema: 
 ```
My Capstone is about:

>  [1-2 sentences about your project]

The major topics I want to discuss are:

#topic-channel-1
#topic-channel-2
#topic-channel-3
```
### Example Bot Prompt:
```
My Capstone is about:
> I wanna study kangaroo bouncing! Whats's up with their achilles and stuff. What can we learn about ACL injuries from that. 

#biomechanics
#animals
#physiology 
#clinical

```


** ‼️ 👉 IMPORTANT DON'T SKIP THIS STEP 👈‼️ **
- ONCE YOU HAVE SENT THE MESSAGE TO THE CHANNEL, ADD A 🤖 REACTION SO THE BOT WILL USE THAT MESSAGE IN ITS SYSTEM PROMPT

---
### Step 2 - Create a channel for each major topic
- The name of the channel should match the `#topic-channel` tag from your bot prompt
  - i.e. if you have a `#topic-channel-1` tag in your bot prompt, you should make a channel called `topic-channel-1`
  


## Note, Tips, Gotchas
- Don't overthink it!!
  - You can and will be changing these prompts a lot, so don't get too hung up on "getting it right" the first time
  - Just get something do  wn, and then expect that you've be honing and altering these prompts continuously throughout this class
- This practice of changing the bot's behavior by changing its system prompt is called [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- When generating text in this course, you will always have at least 3 options
  **-  Option 1 - Use the bot**
     - e.g. in this case: 
       - Go back and extract summaries from your previous conversations about the topics you want to do your capstone about (or ignore them and start from scratch if you want - truly doesn't matter).
       - Extract a short summary of your project. It should fit within a single discord message (so ~2000 characters) and be of the form

  **- Option 2 - Do it yourself, manually**
    - Just, like, write it all youself
      - Pro: You get to write exactly the words you want
      - Cons: You have the words yourself. 

  **- Option 3 (aka the smart move) - Do both**
    - Use the bot to help you get started, and then edit the text it produces so it ACTUALLY fits what you want it to say

## Additional Resources 
- [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [SkellyBot Documentation](https://freemocap.github.io/skellybot/skellybot-server-setup-guide.html)
  - NOTE - these docs are a bit sloppy, disorganized, and incomplete, but hopefully better than nothing if you're willing to dig through them 

## Technical instructions
### How to to make a new channel in your category 
  1. Click the + sign next to the Category Name
  2. Select `# TEXT` channel
  3. Name the channel after the major topic
  4. Click the `Edit Channel` button and add some more detail about the topic and how it relates to your project/intests
      - Use the `#general-chat` channel to have conversations outside of any of these topics
      - Use that area to draft and hone text you are using in the different categories

### How to change a channel description             
1.  Change the channel description to provide the bot with context about what you plan to discuss in this channel 
    1.  Click the `Edit Channel` and add some text to the 'Channel Topic' box with additional instructions for the bot
    2.  The Channel Topic should be written as if you were giving instructions to a person (or person-like-object) about what to expect about  conversations in this channel
        1.  i.e. for a channel called `oculomotor-control`, the description might be: 
            -   "In this channel, the student will talk to you about concepts, research, and methods related to oculomotor control and eye movements, with a particular focus on the neural bases of eye movements and tools for measuring eye movements in real-world settings" 

