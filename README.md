# Assignment-Back-End-Developer-Intern-Role-Ylytics
The Rest API fetch the video data comprising the 5 fields: at, author, like, reply, and text.
![image](https://github.com/iamAni9/Assignment-Back-End-Developer-Intern-Role-Ylytics/assets/108063755/0d688fa2-f640-4b68-ac41-6867d2bd1763)

<h4>Results of my search API</h4>
<h5>I have hosted locally on port 4000</h5>

http://127.0.0.1:4000/search?author=Anthony%20English
<pre>
{
  "comments": [
    {
      "at": "Wed, 18 Jan 2023 00:56:26 GMT",
      "author": "Anthony English",
      "like": 0,
      "reply": 4,
      "text": "I clicked Like before you asked for a boop. It was that \"and that memes / that means\" pun which got me to like."
    }
  ]
}
</pre>
http://127.0.0.1:4000/search?like=1&reply=1
<pre>
{
  "comments": [
    {
      "at": "Thu, 19 Jan 2023 09:59:46 GMT",
      "author": "Fredrick Carlos",
      "like": 1,
      "reply": 1,
      "text": "*Because of the economic crisis that always comes up the best thing to be on every wise individual\u2019s mind or list is to invest in different streams of income that\u2019s not depending on the government to generate funds.*"
    },
    {
      "at": "Wed, 18 Jan 2023 09:07:34 GMT",
      "author": "Nikita Maree",
      "like": 1,
      "reply": 1,
      "text": "The first one  \ud83d\udc4d\nI would love to know more about how much money different types of creators are making with how many views/  watchhours/ subscribers they have. Wether that's from add revenue or sponsored vids."
    },
    {
      "at": "Sat, 21 Jan 2023 02:01:36 GMT",
      "author": "KissMe",
      "like": 1,
      "reply": 1,
      "text": "Who uses patron????? Curious how it\u2019s working out for you."
    },
    {
      "at": "Thu, 19 Jan 2023 04:47:35 GMT",
      "author": "HGNext ",
      "like": 1,
      "reply": 1,
      "text": "Whats up Nate! Your channel has been so helpful. I recently started my YT channel and it\u2019s going well so far. Only thing is that I\u2019m not getting the views I\u2019d hope for. I feel like my content is too well crafted to not be seen by more people. Wondering if you can give me some advice?"
    },
    {
      "at": "Wed, 18 Jan 2023 04:03:44 GMT",
      "author": "KeSetoKaiba",
      "like": 1,
      "reply": 1,
      "text": "Howdy :D Nice video timing as my channel just got accepted for YPP and monetization about yesterday. Also, 10:28 I like both video ideas, but the 1st option piques my interest more right now. :)"
    },
    {
      "at": "Tue, 17 Jan 2023 22:06:43 GMT",
      "author": "CarsonRocks35",
      "like": 1,
      "reply": 1,
      "text": "The 5k a month would be definitely be an interesting one, but I tend to watch anything you put up. I also am curious about easier ways to study or be able to tell your channels quality with a much more popular video still effecting the direct statistics for the month. See I running a Minecraft/pokemon gaming channel where I grew up watching the two and always found lots of people liked both content types, but with no channels mixing them. Changing that was my hopes and it's really run well but I have a video from about a year ago and it's blown up. It pushed to the final stretch to monetization, but it's still going sorta which yes I'm happy about, but with all the views and revenue it's getting I haven't had a month of monetization without it, so it's hard to judge my revenue, monthly views and things since it still has effects on it currently. So I don't know my channels average monthlys are. Hope that made since sorry for the ramble as well.\ud83d\ude06"
    },
    {
      "at": "Tue, 17 Jan 2023 22:46:55 GMT",
      "author": "Chris Reed Beats",
      "like": 1,
      "reply": 1,
      "text": "I always pre-boop the like button before watching \ud83d\ude02"
    },
    {
      "at": "Tue, 17 Jan 2023 22:43:46 GMT",
      "author": "scribbledjoy",
      "like": 1,
      "reply": 1,
      "text": "I\u2019m sure option B could have a great, attention-getting title, but I also doubt every style of channel can get that kind of revenue. \n\nI\u2019d much rather see content that combines what you did here (vlog channel = sponsorship focus) with real data from real channels."
    }
  ]
}
</pre>
