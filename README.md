**DRL Enabled AI Factorio Player**
============
Wenyu Jing, Shivam Duhan, Chengming Zhang, Mingqi Li

**Python Package**
================
`import numpy as np`

`import cv2`

`from mss import mss`

`from PIL import Image`

`import time`

`import wx`

`from pyzbar import pyzbar`


Introduction
============

We are creating a reinforcement learning agent to play the optimization
game Factorio, a game in which you build and maintain factories. The
agent will be mining resources, researching technologies, building
infrastructure, automating production and fighting enemies.

Why Factorio
============

<img src = "https://github.com/cmz97/FactorioAI/raw/master/Documents/47900.png">

Factory optimization is typically carried out using Linear programming.
Neural Networks can probably do a better job but require a lot of data
which is not feasible in current factories. Using Reinforcement learning
to train an agent to manage a factory simulation and then transferring
that learning to the real world is our best bet to dramatically increase
efficiency and productivity and enable everyone in the world to afford
high quality manufactured goods. Factorio provides us with the perfect
environment to create such an agent. It includes all the activities
typically associated with the CEO of a company and more, with immediate
reward signals that can be optimized. It allows for extensive
modification using the in-game debugging mode and the Lua programming
language which will allow us to insert our agent and interface it with
the game effortlessly. The challenge is that it is an incredibly complex
games, at least an order of magnitude more difficult than games (eg.
Atari games ) typically targeted by reinforcement learning agents. A
reinforcement learning agent who can play Factorio well can make
factories, run companies, and design supply chains much better than
humans and will help us make everything cheaper. The agent can also
control Energy production.

Optimization scope
==================

There are 5 main things that can be optimized using our reinforcement
learning agent:

-   resource acquisition,

-   technology research,

-   infrastructure projects,

-   production automation, and

-   military might

To keep the agent manageable, we will not focus on the military aspects
by making a custom mod with no enemies. We will also not focus on doing
research to build rockets. All of our efforts will be focused on
maximizing production and logistical efficiency.

Factorio Gameplay Experience
============================

One of our team members, Chengming Zhang, has played Factorio for 62
hours. He found the game to be very difficult because of the amount of
freedom that the game offers. To achieve the final goal of the game
which is to build a rocket ship, one must keep the factory production
line efficient yet productive. Chengming had to spend a good amount of
time on the official game wiki page to learn critical information like
how to boost production efficiency, make a particular part, etc. To run
an efficient factory, one of the most important things is to have the
machines arranged so that all machines can run non-stop, meaning the
throughput and latency are perfect. A healthy production rate is key.

Work Load Assignment
====================

There are 4 main parts of the project, the yellow marking blocks will be
programmed using python, and the purple marked block will be programmed
using lua.

-   Controller - In charge of the game via modding capability. The
    controller follows the commands issued by the agent. - Mingqi

-   Agent - Takes input from the observer, outputs to the controller,
    and adjusts behavior according to the reward.- Shivam

-   Observer - Reads key metrics from the game engine using the Factorio
    API, written in Lua. - Wenyu

-   Reward - Specifies key metrics and how to optimize them, sets limits
    on the agent's scope. - Chengming
    
<img src = "https://raw.githubusercontent.com/cmz97/FactorioAI/master/Documents/download.png?token=AZbM8WkhsfiNar0i00RoTnhm_hAwLgFyks5cbJd_wA%3D%3D">

Project Milestones
==================

-   Week 5: Submit Project Proposal and collect data for human game play
    for latter comparison and also to gain a better understanding of the
    game.

-   Week 6: Come up with Controller, Agent, Observer, and Reward design
    framework. Do small scale testing in the game. Define reward
    function. Define small scale testing to limit the game play
    initially for testing. Define success. Create virtual machine on
    server to run training program.

-   Week 7: Submit Midterm Evaluation and peer evaluation forms.
    Re-think current strategy.

-   Week 8: Training and Evaluation model for **Navigation in game**

-   Week 9: Training and Evaluation model for **Finding resources**

-   Week 10: Training and Evaluation model for **Mining resource**

-   Week 11: Second Midterm Evaluation. Re-think current strategic.

-   Week 12: Training and Evaluation model for **Autonomous Crafting and
    picking resource**

-   Week 13: Training and Evaluation model for be able to manufacture
    **item \"circuit I\"**

-   Week 14: Training and Evaluation model for be able to manufacture
    **item \"circuit II\"**

-   Week 15: Training and Evaluation model for be able to manufacture
    **item \"circuit III\"**

-   Week 16: Submit finial report, present result in class, and present
    in conference.

Definition of success
=====================

An agent will able to create a **self-sustaining** factory.

Lua For Programmers Part 1: Language Essentials,\
`http://ebens.me/post/lua-for-programmers-part-1/`

Programming in Lua (first edition),\
`http://www.lua.org/pil/contents.html`

Learn X in Y Minutes Where X=lua,\
`https://learnxinyminutes.com/docs/lua/`

Lua Documentation,\
`https://www.lua.org/docs.html`

Factorio Modding,\
`https://wiki.factorio.com/index.php?title=Modding`

Factorio API,\
`https://lua-api.factorio.com/latest/`
