Using our dashboard we attempted to answer the following research question:  

*Is there a relationship between cabin location of passengers and their survival rates on the Titanic which can help inform ship design and safety policies?*  

To answer this question, the first visualization of our dashboard allows users to navigate different decks of the ship and see where passengers died or survived. A cruise line designer could focus in on "death clusters" to find out if there were sub-standard safety features implemented in those areas of the ship. Our second visualization, the "survival rate by deck level" plot gives a general overview showing whether or not certain deck levels were lacking in safety features compared to others. Similarly, the "survival rate by class" plot helps show a general overview of differences in safety features between cabins of varying classes. Overall, dashboard does well in addressing our research question.

Based on TA and peer feedback, the use of the dropdown as the single interactive feature in combination with the two static horizontal bar charts for survival rates by class and deck respectively is effective at showing how passenger fates vary by these two attributes which is difficult to visualize in two dimensions on a single plot since all three classes of passenger cabins (1-3) are found on all seven decks (A-G).

In its current form, the dashboard does not consider passenger fates by other attributes such as gender, age, marital status, or port of origin which are interesting but separate research questions requiring additional visualizations. To enhance the visualization of the current research question, we could also consider using colour to encode the three classes in the deck levels legend where the area of each colour is proportional to the share of its corresponding cabins class on each deck level. A more ambitious improvement would be to create a 3D interactive visualization of the ship which would allow the user to rotate the ship about the x, y and z axes to visualize passenger fate by specific cabin class, deck and nautical location at a single glance (i.e. bow-stern, port-starboard) with tooltips providing additional passenger attributes which could be explored.

Our dashboard had several important limitations that need to be considered, especially when trying to draw conclusions to answer the research question. First, our visualization assumes that all passengers were in their cabins at the time of the disaster. Additionally, incomplete records on passenger cabin location means that we have only plotted a sample of the population of all passengers, and ss such, we were extremely cognizant about not allowing users to draw conclusions that generalize to the entire population of passengers and may not be accurate. We were also conscious of not inferring causation from correlation. For example, class may be correlated with survival, but not necessarily due to the cabin location of a particular class, but due to a confounding association between passenger class and societal status which may have led crew members giving priority access to lifeboats and lifejackets to these passengers.

We received peer feedback in milestone 3 suggesting several changes including making positional changes of interactivities, color and sizing changes for visualizations, and description additions to clarify conceptual terminologies.

We decided to implement five peer-recommended changes:

1. Repositioning the dropdown bar for deck level to be on the right side of the titanic visualization in response to peer feedback indicating this was the most natural place to look for dropdown interactivity  

2. Changing the font size of the note about adjusting the browser. We initially added a note to tell users to adjust their browser to enhance visualization experience, but some peers noted that the note was not clear enough.  

3. Changing the color of bars in the horizontal bar chart to be blue and changing the “passenger survived” bubble to the color bar. Because the amount of blue ink used in the bar chart was analogous to the amount of survival in passengers, we adhered to the principle of proportional ink by keeping the color of “passenger survival” consistent through the titanic visualization and the bar chart visualization.  

4. Changing the default deck level from B to C because deck C had more data points to visualize.  

5. Adding a note that states you can hover over data points for passenger information for additional clarity on how to fully utilize our titanic visualization. In conjunction with this change, we also enlarged the tooltip bubble for better readability. 

We decided NOT to implement four peer-recommended changes:  

1. Adding a note or label to show that the square shape in the titanic visualization represented an empty cabin. We did not go through with this change because the word “cabin” was used in our title but after reconsidering and soliciting additional feedback, we determined that it is quite obvious that a box represents a cabin.

2. Showing which cabins belong to which class on each deck level. Although this was a reasonable suggestion, this is not possible because due to data limitations as the available data indicates only where first-class cabins are located and no information on the other classes.  

3. Changing the word “location” to “deck level”. We decided against this as “location” more holistically describes all three of our plots since the word encompasses both “deck level” and “class” and we are specifically visualizing associations between these attributes and passenger survival.

4. Decreasing the size of the Titanic image at the top of the page. We did not do this because there were actually more people who gave us positive feedback on this aspect of our dashboard including Firas who said that the photo really “sets the tone of our project”. Also, there is a trade-off between maintaining the original aspect ratio of the photo while trying to shrink its height and maintaining its width to match the width of the other frames.  

Below are some general reflections on peer feedback:

- In terms of usability, it was easy for our peers to use the app because there was only one drop down bar which made the interactive element of the app obvious and easy to use, although we did not expect them to look to the right for the dropdown bar. As a result, of this observation, we repositioned the dropdown to the right just above the legend for the deck levels.  

- Two themes emerged looking at the full set of peer feedback: Descriptive clarifications and Visualization schematic adjustments. Peers asked us to either clarify descriptions or add descriptions to better under visualizations. They also often asked us to change the size, positioning, or color of visualizations. 

- The most valuable feedback received was the suggestion to put some background colour on the deck since there was an abundance of whitespace, so we now have a grey background for the cabins which allows the eye to better pick up and contrast the white and red dots denoting survival and non-survival. Although conceptually simplistic, the implications are rather meaningful since the bars and bubbles represent half of the core variable of interest -- i/e. passenger survival.  

- There was no non-valuable feedback per se, and even the somewhat frustrating first part of the exercise where we were asked to be silent and refrain from any verbal response to peer reaction was ultimately quite fruitful. From our experience as “flies-on-the-wall”, we were able to see the effectiveness of the dashboard on a standalone basis without the benefit of any guidance or pointers. Each of us took copious notes in "fly mode", many of which contributed to the dashboard improvements discussed above.

Overall, the feedback was exteremely valuable and our app is now decidedly more effective and user-friendly than it was a week ago.

Last but not least, we implemented a change based on our own experience which was to refactoring our code and performing all major data wrangling externally such that we could importing wrangled data to our plot functions. This had a significant positive impact on the speed at which our interactive plot updated and enhanced the user experience. 

We are also working on implementing audio in the form of the popular Titanic theme song playing (Top 10 song of all-time) when users land on our dashaboard page and inserting a button with an audio .gif file which allows and instructs users to click to turn off the music. This was working fine in Python but needs to be debugged for R which we hope to have done by the final submission as this idea, like our image, received overwhelmingly positive feedback when we tested it briefly in the lab.