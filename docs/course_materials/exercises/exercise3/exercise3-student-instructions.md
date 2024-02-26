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
___
## Step-by-Step Guide

### Step 1 - Setting up the Bot Prompt channel (#🤖-prompt-settings)
 - Go into the `🤖-prompt-settings`
 #### Capstone Bot Prompt schema
 ```
My Capstone is about:

>  [1-2 sentences about your project]

The major topics I want to discuss are:

#topic-channel-1
#topic-channel-2
#topic-channel-3
```

#### Example Bot Prompt:
```
My Capstone is about:

> I wanna study kangaroo bouncing! Whats's up with their achilles and stuff. What can we learn about ACL injuries from that. 

#biomechanics
#animals
#physiology 
```


#### **‼️ 👉 IMPORTANT DON'T SKIP THIS STEP 👈‼️**
- ONCE YOU HAVE SENT THE MESSAGE TO THE CHANNEL, ADD A 🤖 REACTION SO THE BOT WILL USE THAT MESSAGE IN ITS SYSTEM PROMPT
---
### Step 2 - Setting up the channels

#### Step 2a - Make the channels
  - [How to make a new channel in your category](#how-to-to-make-a-new-channel-in-your-category)
  - Make a channel for each of the `#topic-channel` tags in your bot prompt
    - i.e. if you have a `#topic-channel-1` tag in your bot prompt, you should make a channel called `topic-channel-1`
  - NOTE: You can only make channels in YOUR category
    - i.e. if your Student ID / assigned role is `#FF00FF`, you can only make channels in the `#FF00FF` category

#### Step 2b - Add a description to the each of the topic channels to hone the discussion to your interests
 - [How to change a channel description](#how-to-change-a-channel-description)
1.  Change the channel description to provide the bot with context about what you plan to discuss in this channel 
    1.  The Channel Topic should be written as if you were giving instructions to a person (or person-like-object) about what to expect about  conversations in this channel
        1.  i.e. for a channel called `oculomotor-control`, the description might be: 
            -   "In this channel, the student will talk to you about concepts, research, and methods related to oculomotor control and eye movements, with a particular focus on the neural bases of eye movements and tools for measuring eye movements in real-world settings" 
     - NOTE: 
       - The bot will already be able to see the channel name
       - Less is more! This description will be automatically added to the prompt of each /chat that happens in that channel, so you don't want to say TOO much
         - Better to be terse with it, and then add details in the /chat itself

---

### Step 3 - High level chat with the bot

Have a high level convestation wtih the bot about the overall structure of your project

1. Open a `/chat` in the `#general-chat` channel of your server
2. Confirm that the bot can see your prompt by asking it to give you an overview of your own capstone project
  - e.g. "Can you give me a summary of my capstone project?"
  - Continue the conversation for a few exchanges to see if the bot 'understands' what you meant in your prompt message. 
  - If you don't like the response, go edit the message, **open a new /chat** and try again
  - Iterate until the bot is describing your project in a way that aligns with your vision of it

---

### Step 4 - Have topic-specific chats with the bot

Have 3 more directed conversations with the bot in each of the channels you made in Step 2  

1. Open a new `/chat` in each of the channels you made in Step 2
2. Have a conversation, specifically about that sub-area of your project
3. If the vibes are off, iteratively edit the relevant sub-prompt components until they are back on again:
   1. Channel description
   2. Bot prompt
   3. Open a new /chat and try again

---
### Step 5 - Iterate iterate iterate

You are not being evaluated! You cannot make mistakes that will hurt your grade! Do a bunch, screw it up, tweak, tune, fix, and try again!

The only determiniant of skill is Time On Task 

Feel free to discuss papers, ideas, or anything else that is relevant to your project in any of these channels.

Edit and tweak all your prompts and channel descriptions as you go as your vision for what your project could/should/will be evolves

Focus on what YOU want your project to be! The bot will always have a infinite number of suggestions on hand, so its up to YOU to CHOOSE which ones you want to pursue!

Try to balance between: 
- Broad level "project wide" conversations about the overall structure of your project
- Specific, focused conversations about the details of the sub-areas of your project (aka, rabbit holes!)
- Conversations about specific papers 
  - Use the [prompt from Exercise 2](https://discord.com/channels/1194766712680222800/1200118663043371088/1200119626491768853) to help you chew up research articles 
    - DO NOT JUST GIVE THE BOT THE CITATION AND ASK QUESTIONS ABOUT THE FULL papers
    - IT WILL JUST BE GUESSING BASED ON THE WORDS IN THE Title
    - COPY-PASTE THE FULL ABSTRACT
    - THE BOT ONLY SEES WHAT YOU SHOW IT

___
## Completion Criteria (aka "Definition of Done")
### Bot Prompt
  - You have a bot prompt in the `🤖-prompt-settings` channel that matches the [defined schema](#capstone-bot-prompt-schema)
### Channels
  - You have made a channel for each of the `#topic-channel` tags in your bot prompt
  - You have added a description to each of the channels that hones the discussion to your interests
### Chats
  - You have had a high level conversation with the bot about the overall structure of your project in your `#general-chat` channel
  - You have had 3 more directed conversations with the bot in each of the `#topic-channel` channels you made in Step 2

___
## Additional Resources 
- [Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [SkellyBot Documentation](https://freemocap.github.io/skellybot/skellybot-server-setup-guide.html)
  - NOTE - these docs are a bit sloppy, disorganized, and incomplete, but hopefully better than nothing if you're willing to dig through them 

___
## Technical instructions
### How to to make a new channel in your category 
  1. Click the + sign next to the Category Name
  2. Select `# TEXT` channel
  3. Name the channel after the major topic
  4. Click the `Edit Channel` button and add some more detail about the topic and how it relates to your project/intests
      - Use the `#general-chat` channel to have conversations outside of any of these topics
      - Use that area to draft and hone text you are using in the different categories

### How to change a channel description             
  1.  Click the `Edit Channel` and add some text to the 'Channel Topic' box with additional instructions for the bot
      1.  Alternatively, right click the channel name and select `Edit Channel` 
  1. Enter text into the 'Channel Topic' box
  


