# ADS_2021
Portfolio for applied data science minor

Name: Björn Appehl <br>
Student ID: 21087024
Group: Team Dialogue

<h1> Introduction </h1>
This is the reader's guide for my portfolio created for the Applied Data Science minor at The Hague University of Applied Sciences.   <br>
Below are the criteria from the scoring matrix with detailed information about each criteria.   <br>
The reader's guide is numbered for easier reading. <br>
A big thank you to Team Dialogue, and also to Jeroen, Tony, Ruud and Hani for guiding us.

<h2> Datacamp </h2>
All datacamp courses except for one were completed. The one that was not completed was **Joining Data with Pandas**, since it seemed like one with least in common with our project work.<br>
Outside of the assigned datacamp courses, roughly 1/4 of another course, **Spoken Language Processing in Python**, was also completed.<br>
Here is a link to a screenshot with the completed courses: https://i.imgur.com/YT92ZKs.png
  


<h2> 1. Reflection and evaluation </h2>

<details>
<summary> 1.1 Reflection on own contribution to the project </summary>

- Situation:  Our project group consisted of 6 members, and we worked with audio data to detect conversation for the Smart Teddy Bear project. We all worked together to ensure everyone would get hands-on experience with every aspect of the project work, although this was hard to realize and in the end some work ended up being unevenly distributed. Since I don't have a great deal of experience writing code, I was a little out of the loop at the end of the project when the code we had for our CNN's became more and more complex. However, at that point I took on other duties which helped the group as a whole but did not give me as much programming experience as some others.

- Task: My tasks in the group varied, early on there was a lot of hands-on with coding simple models. One example is creating a model together with David that ended up being the first real algorithm the group used, since it had the best results at that stage. Later on I started exploring different datasets and drew up some requirements and comparisons for the datasets we ended up using. As the groups priorities shifted, I found myself taking on a lot of presentations and other communication duties along with writing the paper, since we had other people who were simply better at crunching code and it became a matter of time in the final stages. I also helped David & Maria who gave the learning lab feedback and suggestions for topics for them to cover, however I didn't end up taking part in presenting our learning lab. 
  
- Activities: The first model I created in the minor was a Logistic Regression model which was based on transcripts from a TV show. The models purpose was to estimate which line was most likely being said by which speaker. On top of this, I was also splicing audio, normalizing sound levels and transforming our datasets to be more difficult. I helped streamline our data pipeline, unfortunately I finished it right when we shifted to using numpy arrays instead of image data, so it was in the end not necessary. These are only some examples of what I did and you can read more about it below.

- Result: For the presentations I was a part of, I created a lot of the slides along with the overall layout of the powerpoints. I helped other group members in taking care of the Scrum board on Taiga, and during the period in which I was scrummaster I took care of this mostly single-handedly. The code I wrote early on was a simple logistic regression model that was later converted to take audio data as input, however at that point the model also had to change since RFC gave better accuracy. My work on the dataset helped us get good data quite early on the project, which I see as a great benefit for our neural networks.

- Reflect: The contributions I made to the project gave me a much better understanding of data science as a whole. While I am not ready to explore a career in the field, I have a strong feeling that the techniques and methods used in this minor will be of use to me in a professional setting. I regret not being a bigger part of the learning lab our group gave, since it would have been a good chance to expand my own knowledge in the domain. 
 
</details>
  
  

<details>
<summary> 1.2 Reflection on own learning objectives</summary>
  
- 
  
</details>

<details>
<summary> 1.3 Evaluation on the group project as a whole</summary>
  
- Situation:Right from the start, our group contained a lot of different skill sets and this showed during our project. Some were better at writing code, while some had more experience in working with Scrum or other benefitial traits. The cohesion was always quite high in my opinion, and there was never any conflict in the group. Early on, we made it clear what we expect from eachother in terms of workload (i.e not scheduling project work on weekends or after 5pm), punctuality, etc, which helped us work more effectively and better as a group.

- Task: For the duration of the entire project, the workload of all members shifted depending on what stage the project was in. Despite this, some ended up doing a lot more coding than some others, but everyone still partook in presentations and communication along with participating on writing the paper. While everyone did get a little bit of experience in all areas, the workload could have been changed to avoid this. However we wanted to avoid a set schedule with responsibilities in order to not have a member doing something they would rather not do. An unmotivated member working on a task just because it has been assigned to them is not always optimal, in our case we instead focused on everyone doing what they wanted to do based on the current workload at the time.

- Activities: Our application of Scrum consisted of daily online standups, which we had mostly every weekday for the minor unless something else was said. We still had physical standup meetings on days where we were all gathering to work at campus. These 'working days' on campus became quite central in our work, and 2-3 days every week was spent on campus. 

- Results: I, and I belive all other group members, are happy with the results we achieved. Not only are we happy with the algoithm, which gives great results as far as we can see, we also achieved the results working in a sustainable and reasonable pace with little conflict or unnecessary stress. 

- Reflection: I'm sure none of our group members are finishing this minor without having learned something. The distribution of workload in retrospect was, according to me, a very good way to make sure noone is understimulated or has too much to do. While it took a few weeks to get this running smoothly, mostly due to all members getting to know eachother and their skill sets, it ended up being very benefitial for us. If I were to do this project again, I would happily work with the same group in the same manner as we did. The working days on campus was, according to me, a big factor in our projects success and helped us work better together and make social connections.

  
</details>



<h2> 2. Research Project </h2>

<details>
<summary> 2.1 Task Definition</summary>
  
My contribution: I gave feedback and discussed with the group members (David & Maria, who had created the initial draft) about which research questions we should keep, and which questions we should move forward with. Here is a link to a very early draft of our paper with the questions still in there, the "answers" to each question on page 2 is typed by me and was used for reference later on in the project. 
  https://drive.google.com/file/d/1tm8MRCr17ix6i32tT9nXcVKYS6k9HhKh/view?usp=sharing <br>
  
  I was mostly working on our datasets when our first drafts of the research paper was created, so as soon as I finished work on the dataset I helped out with the questions. Below are some examples of questions that made it, and those that did not (along with our reasoning):
  
 - How can we detect multiple voices from audio data? <br>
This question was central in the project, since the context for our project consists of defining when conversation is happening. Detecting multiple voices makes the difference between a monologue and an actual conversation and is very important for the end result.
  
 - Which characteristics make a conversation?<br>
This question has a lot to do with the one above it. We ultimately decided that a minimum grade of participation from at least two speakers is necessary to constitute a conversation. We had to discuss this with the problem owner several times, as we didn't want to make assumptions ourselves. If we simply regarded any dialogue between people regardless of speech duration per speaker, this could have given different results.
  
 - Can we detect if the dementia patient is speaking on the phone?<br>
This question was considered to be out of scope. There are probably easier ways to determine when an elderly person is using their phone than only listening to them speak, and we wanted to focus on specifically conversation in a physical setting.

- Can we detect if the person speaking is physically present?<br>
This question was ultimately decided to be out of scope, but it did come up for discussion a few times. Essentially, a voice being played from a speaker will most likely not have the same range as a human speaking. This makes it possible - in theory, we never got far enough to actually work on it - to determine when a voice is "fake" or "real". This is a suitable area for further research in my opinion, since we never had time to try it out the results would be very interesting.
</details>


<details>
<summary> 2.2 Evaluation</summary>
My contribution: For the paper, I gave some ideas for future work with our prototype. I put this in the paper so other group members could also put ideas in, and build off mine if they agree. 
  Here is an early draft of our paper where on page 5, my first ideas for future work are listed: https://drive.google.com/file/d/1_IV_NqUBWdRstXnUaXdXFCy66YA4UpWQ/view?usp=sharing
  
  A few of them include:
  
  - Comparing the accuracy of our speaker differentiation model with human results. This could be done by a study where correspondants listen to short clips of speech and asses whether all clips are said by the same speaker or not. It would be very interesting to see if humans or the model perform better if voices are very similar for instance. Since our research has only measured the accuracy of our model,  a "human" accuracy score would be an interesting metric to consider. 
  Link to this 
  
  - Since the model for speaker differentation came to be quite complex, it would be interesting to see new projects which aims to identify the elderly person's voice. Samples might be collected over a period of time and eventually could be used to compare all detected speech to the patient themselves, instead of always comparing every segment.
</details>
  
  
<details>
<summary> 2.3 Conclusions</summary>
  My conclusions from this project are that it is indeed possible to use data science techniques (in our case, convolutional neural networks) to detect conversation to some degree. By converting audio data to MFCC's, and feeding them through two neural networks, we can with 89% (for detecting speech) and 94% (for detecting changes in speaker) accuracy determine if a conversation is happening. Of course, our algorithm is not perfect, and there will be many situations where it does not work properly. For instance, if the other half of the conversation is taking place over the phone. With the final product, that combines the first and second model, I would say we have results that support our research problem "”How can data science techniques detect if there is a conversation between at least two people by analyzing audio files?”" and can now state that by using CNNs, MFCC data format and measuring speaker activity & speech duration, data science techniques can detect conversation.
  
</details>
  
  
<details>
<summary> 2.4 Planning</summary>
 My contribution: I, along with Leander Loomans, were in charge of documentation. This included taking notes whenever important information was recieved from teachers or the problem owner (or internal meetings). It also included making documents (internal and external, such as found papers) available for other group members to take part in. <br/>  
  On top of this, every group member was equally involved in updating the Scrumboard on Taiga and making sure it was up to date.<br/>  
  
  
  A screenshot from Taiga with almost everyone's activity: https://i.imgur.com/Q91fnWq.png (It's difficult to get a really descriptive image)
  
  A screenshot of some of the notes that were taken: https://i.imgur.com/YU2HRXk.png  (Since not every meeting leads to notes having to be taken, there are some gaps.)
  
  In our group, efficiency was quite important, and led to us having daily stand up meetings so we could all keep up with the progress happening. This worked very well, and I attended these meetings to increase our group cohesion and keep the others informed about my part in the project. 
  
  
</details>


<h2> 3. Predictive Analysis </h2>

<details>
<summary> 3.1 Selecting a Model</summary>
  To help select a model, I 
</details>

<details>
<summary> 3.2 Configuring a Model</summary>
  Early on, i configured a neural network (with some help from Jeroen in handling errors). The code can be found here: https://gpuserver.hhs.nl:8888/user/21087024/notebooks/dialogue/Bj%C3%A4rn/ye%20olde%20cnn%20stuff/NN%20Take%201.ipynb
My contribution: All of what you see in the notebook, some of the values were changed in accordance with feedback from Jeroen to get things working.
  I also configured a simple Logistic Regression model early in the course as a first test of machine learning models, using one of the example notebooks provided as the foundation. This file is available here: https://datascience.hhs.nl:8888/user/21087024/notebooks/dialogue/Bj%C3%B6rn/L6.7%20Text.ipynb
</details>

<details>
<summary> 3.3 Training a Model</summary>
  
  
</details>

<details>
<summary> 3.4 Evaluating a Model</summary>
  
</details>

<details>
<summary> 3.5 Visualising the outcome of a model</summary>
  
</details>


<h2> 4. Domain Knowledge </h2>  

<details>
<summary> 4.1 Introduction to the subject field </summary>
  Our subject field came to be audio signal processing. This meant we had to use recordings of audio to be read by an algorithm in order to make predictions on the audio itself. In order to do this, we transformed the audio data into MFCC data, since MFCCs are good at representing a lot of features useful in voice recognition.This process can be seen here: https://gpuserver.hhs.nl:8888/user/21087024/notebooks/dialogue/Bj%C3%A4rn/make%20npy%20array%20of%20audio.ipynb 
Sound data can also be represented with spectrograms, and other image representations of sound (such as oscillograms/waveforms). In our study, we got the best results from working with only mfcc data. The sample rate of recordings is also an important factor to consider, since it is a measure of how many samples are recorded over a period of time. A high sample rate will contain a lot of samples, but might be computationally expensive or contain unnecessarily many samples. While a low sample rate has some information loss, but can be faster to process.
  
</details>


<details>
<summary> 4.2 Literature Research </summary>
  
</details>


<details>
<summary> 4.3 Explaination of Terminology, jargon and definitions </summary>
  
  Below follows an explaination for all terms or definition that are viewed as important:
  - MFC: Mel-Frequency Cepstrum, an aggregation of several MFCC's (components).
  - MFCC : A coefficient to MFC's, meaning one MFC is made up of many MFCCs. MFCCs are a method of displaying features on audio data, and is heavily related to feature extraction.
  - Epoch : An iteration over the entire dataset during the training process for a neural network.
  - Learning Rate : The rate at which a neural network adapts to the data. A learning rate that's too big will generally "jump over" the optimal solution and might never reach a good result. While a learning rate that's too small might take very long to train as the "jumps" it makes are very small.
  - Dataset : A set of data that can be split into train, test and validation parts. Datasets generally consist of negative data (data that is not correct, in our case background noise) and some positive data (in our case speech). Negative and positive data should generally be balanced to avoid algorithms being biased towards one or the other. 
  - Overfitting : Overfitting might occur when a model is trained on a limited data set, and only predicts in accordance with training data instead of adapting to validation or other 'non-training' data.
  - Spectrogram : A visualisation of audio data which highlights changes to sound over time. A spectrogram is generated from a collection of Fourier Transforms, thus creating a more detailed representation of the data.
  - (Machine learning) model: A program that is trained to detect certain patterns in data.
  - Confusion Matrix: A form of evaluation on a model, where the amount of false negatives, false positives and correct estimations are displayed.
  - Sample Rate: An attribute of audio describing the amount of samples over a period of time. A high sample rate is generally good, but might be more computationally expensive. While a low sample rate generally means less samples over time, but easier to process.
  - Loss function: A function that is able to determine how the performance of a model relates to the dataset used. 
  - Neural Network: A type of algorithm that works by using layers containing nodes/neurons that recieve and pass on weighted data in order to make predictions on it. 
  
</details>




<h2> 5. Data Preprocessing </h2>  

<details>
<summary> 5.1 Data Exploration</summary>
  
  In order to familiarize myself with the data we were using, I had to inspect the data to be able to work with it as best as possible.
  One of the data explorations I did is in this notebook: https://datascience.hhs.nl:8888/user/21087024/notebooks/dialogue/Bj%C3%B6rn/audiodata%20test/wav%20data%20filter%2Bexploration.ipynb. Here, I started experimenting with using attributes from the data (such as sample rates) while also looking at the labels for our data, and making sure the labels add up with the speech. It was helpful in order to learn about the format of our data, and what our data can be used for.
  
  
  
</details>

<details>
<summary> 5.2 Data Cleansing</summary>
  
  Some of the data cleansing I did can be found in this notebook, in block [6]: https://datascience.hhs.nl:8888/user/21087024/notebooks/dialogue/Bj%C3%B6rn/negativesamples/dataset%20incl%20neg%20data.ipynb
 Here, I filter out some specific columns (the ones that will be of use to us) from the 'negativedf' dataframe (this dataframe contains all negative samples). Afterwards, I concatenate this dataframe with our positive data, resulting in a cleaned up version of the negative data being concatenated to the positive data.  
  
</details>

<details>
<summary> 5.3 Data Preparation</summary>
While the project was still using images as input data, I created a dataloader to speed up the data processing times for the group. Unfortunately this never really came to be used since, shortly after I finished it, we switched to not using images anymore.
A overview of my work on data prep can be found in this notebook: https://gpuserver.hhs.nl:8888/user/21087024/notebooks/dialogue/Bj%C3%A4rn/Standardized%20Image%20Generator%20Multi-Assistant%20-%20SIGMA.ipynb
  
After the dataloader for images ended up being scrapped, I helped Leander and Olaf create a new version. 
  It can be found here: https://gpuserver.hhs.nl:8888/user/21087024/notebooks/dialogue/Bj%C3%A4rn/make%20npy%20array%20of%20audio.ipynb
  For that notebook, I would estimate my contribution is around 25-30%.
  
  
  
</details>

<details>
<summary> 5.4 Data Explaination</summary>
  
</details>

<details>
<summary> 5.5 Data visualisation</summary>
  
</details>

<h2> 6. Communication </h2>


<details>
<summary> 6.1 Presentations </summary>
  The presentations where I partook are the following:
  
  External Presentation:
  - #1 (helped create presentation, gave the presentation together with the rest of the group) 
  
  - #2 (created presentation, gave the presentation together with 1 other member)
  
  - #3 (created presentation, gave the presentation together with 1 other member)
  
  Internal Presentation: 
  - #2 (created presentation, gave the presentation together with 1 other member)
  
  - #4 (created presentation, gave the presentation together with 1 other member)
  
  - #5 (created presentation, gave the presentation together with 1 other member)
  
  - #8 (gave the presentation together with 2 others)
  
  - #9 (created the presentation) 
  
</details>


<details>
<summary> 6.2 Writing paper </summary>
  
  I helped write the paper as much as possible. Before the writing started, I gave a detailed overview of our subquestions and answered them, which helped form the base for our paper. Of course the structure changed a lot since then, but it was a start. I worked a lot on the introduction part, including background and research problem of the paper. I also wrote content in other sections, but my primary focus (since we divided it up) was the introduction. The introduction was the first section of the paper I started writing, and I put a lot of effort in to make it as good as possible. I hope the introduction properly showcases our domain and the purpose of our work, since I put a lot of time into it. 
  
 I also helped other group members writing the paper by giving constructive feedback, always being mindful of other people's work and not criticizing. I ended up making quite a few corrections to the paper in most sections, an effort that I hope changed our paper for the better since I feel it's important to deliver a strong paper. 
  
  It is difficult to give examples here, since writing the paper is a continuous process and quite hard to measure in terms of contribution.
</details>


