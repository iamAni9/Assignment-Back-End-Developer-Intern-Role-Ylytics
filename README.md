# Assignment-Back-End-Developer-Intern-Role-Ylytics
The Rest API fetch the video data comprising the 5 fields: at, author, like, reply, and text.
![image](https://github.com/iamAni9/Assignment-Back-End-Developer-Intern-Role-Ylytics/assets/108063755/0d688fa2-f640-4b68-ac41-6867d2bd1763)

<h4>Results of my search API</h4>

http://127.0.0.1:4000/search?author=Anthony%20English
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

http://127.0.0.1:4000/search?like=1&reply=1
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
    }
................................................................

