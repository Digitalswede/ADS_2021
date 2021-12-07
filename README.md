# ADS_2021
Portfolio for applied data science minor

Name: Björn Appehl <br>
Student ID: 21087024

<h1> Introduction </h1>
This is the reader's guide for my portfolio created for the Applied Data Science minor at The Hague University of Applied Sciences.
Below are the criteria from the scoring matrix with detailed information about each criteria.

<h2> Datacamp </h2>
All datacamp courses except for one were completed. The one that was not completed was *Time Series Analysis with Python*.
Outside of the assigned datacamp courses, roughly 1/4 of another course, *Spoken Language Processing in Python*, was also completed.

Insert that image here (in a dropdown)


<h2> Reflection and evaluation </h2>

<details>
<summary> Reflection on own contribution to the project </summary>

- Situation:  Our project group consisted of 6 members, and we worked with audio data to detect conversation for the Smart Teddy Bear project. We all worked together to ensure everyone would get hands-on experience with every aspect of the project work, although this was hard to realize and in the end some work ended up being unevenly distributed. Since I don't have a great deal of experience writing code, I was a little out of the loop at the end of the project when the code we had for our CNN's became more and more complex. However, at that point I took on other duties which helped the group as a whole but did give me as much programming experience as some others.

- Task: My tasks in the group varied, early on there was a lot of hands-on with coding simple models. One example is creating a model together with David that ended up being the first real algorithm the group used, since it had the best results at that stage. Later on I started exploring different datasets and drew up some requirements and comparisons for the datasets we ended up using. As the groups priorities shifted, I found myself taking on a lot of presentations and other communication duties along with writing the paper, since we had other people who were simply better at crunching code and it became a matter of time in the final stages. I also helped David & Maria who gave the learning lab feedback and suggestions for topics for them to cover, however I didn't end up taking part in presenting our learning lab. 
  
- Activities: The first model I created in the minor was a Logistic Regression model which was based on transcripts from a TV show. The models purpose was to estimate which line was most likely being said by which speaker. On top of this, I was also splicing audio, normalizing sound levels and transforming our datasets to be more difficult. I helped streamline our data pipeline, unfortunately I finished it right when we shifted to using numpy arrays instead of image data, so it was in the end not necessary. These are only some examples of what I did.

- Result: For the presentations I was a part of, I created a lot of the slides along with the overall layout of the powerpoints. I helped other group members in taking care of the Scrum board on Taiga, and during the period in which I was scrummaster I took care of this mostly single-handedly. The code I wrote early on was a simple logistic regression model that was later converted to take audio data as input, however at that point the model also had to change since RFC gave better accuracy. My work on the dataset helped us get good data quite early on the project, which I see as a great benefit for our neural networks.

- Reflect: The contributions I made to the project gave me a much better understanding of data science as a whole. While I am not ready to explore a career in the field, I have a strong feeling that the techniques and methods used in this minor will be of use to me in a professional setting. I regret not being a bigger part of the learning lab our group gave, since it would have been a good chance to expand my own knowledge in the domain. 
</details>
  
  

<details>
<summary>Reflection on own learning objectives</summary>
  
- I learnt'd many objectives
  
</details>

<details>
<summary>Evaluation on the group project as a whole</summary>
  
- Situation:Right from the start, our group contained a lot of different skill sets and this showed during our project. Some were better at writing code, while some had more experience in working with Scrum or other benefitial traits. The cohesion was always quite high in my opinion, and there was never any conflict in the group. Early on, we made it clear what we expect from eachother in terms of punctuality / being late for scheduled meetings, which helped us work more effectively and focus on the important things. 

- Task: For the duration of the entire project, the workload of all members shifted depending on what stage the project was in. Despite this, some were doing a lot more coding than some others, but everyone still partook in presentations and communication along with participating on writing the paper. While everyone did get a little bit of experience in all areas, the workload could have been changed to avoid this. However we wanted to avoid a set schedule with responsibilities in order to not have a member doing something they would rather not do. An unmotivated member working on a task just because it has been assigned to them is not always optimal, in our case we instead focused on everyone doing what they wanted to do based on the current workload at the time.

- Activities: Our application of Scrum consisted of daily online standups, which we had mostly every weekday for the minor unless something else was said. We still had physical standup meetings on days where we were all gathering to work at campus. These 'working days' on campus became quite central in our work, and 2-3 days every week was spent on campus. 

- Results: I, and I belive all other group members, are happy with the results we achieved. Not only are we happy with the algoithm, which gives great results as far as we can see, we also achieved the results working in a sustainable and reasonable pace with little conflict or unnecessary stress. 

- Reflection: I'm sure none of our group members are finishing this minor without having learned something. The distribution of workload in retrospect was, according to me, a very good way to make sure noone is understimulated or has too much to do. While it took a few weeks to get this running smoothly, mostly due to all members getting to know eachother and their skill sets, it ended up being very benefitial for us. If I were to do this project again, I would happily work with the same group in the same manner as we did. The working days on campus was, according to me, a big factor in our projects success and helped us work better together and make social connections.

  
</details>



<h2> Research Project </h2>

<details>
<summary>Task Definition</summary>
  
I was mostly working on our datasets when our first drafts of the research paper was created, so as soon as I finished work on the dataset I helped out with the paper. I gave feedback and discussed with the group members (David & Maria) who had created the initial draft about which research questions we should keep, and which questions we should move forward with. Below are some examples of questions that made it, and those that did not:
    
 - How can we detect multiple voices from audio data? 
This question was central in the project, since the context for our project consists of defining when conversation is happening. Detecting multiple voices makes the difference between a monologue and an actual conversation and is very important for the end result.
  
 - Which characteristics make a conversation?
This question has a lot to do with the one above it. We ultimately decided that a minimum grade of participation from at least two speakers is necessary to constitute a conversation. We had to discuss this with the problem owner several times, as we didn't want to make assumptions ourselves. If we simply regarded any dialogue between people regardless of speech duration per speaker, this could have given different results.
  
 - Can we detect if the dementia patient is speaking on the phone?
This questions was considered to be out of scope. There are probably easier ways to determine when an elderly person is using their phone than only listening to them speak, and we wanted to focus on specifically conversation in a physical setting.

- Can we detect if the person speaking is physically present?
This question was ultimately decided to be out of scope, but it did come up for discussion a few times. Essentially, a voice being played from a speaker will most likely not have the same range as a human speaking. This makes it possible - in theory, we never got far enough to actually work on it - to determine when a voice is "fake" or "real".



<details>
<summary>Evaluation</summary>
  
</details>
  
  
<details>
<summary>Conclusions</summary>
  
</details>
  
  
<details>
<summary>Planning</summary>
  
</details>
