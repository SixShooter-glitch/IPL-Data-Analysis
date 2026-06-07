# IPL Data Analysis Project

## Dashboard Preview

![Dashboard](Screenshots/Dashboard.png)




IPL Data Analysis Project
Project Overview

This project analyses historical Indian Premier League (IPL) match data to uncover trends and insights related to team performance, player achievements, venue dominance, toss impact, home-ground advantage, and the growth of the IPL over time.

The objective of this project is to demonstrate data cleaning, exploratory data analysis (EDA), visualization, and dashboard development skills using real-world cricket data.


Dataset: IPL.csv

Original Records: 1193 matches

Clean Records: 1169 matches



Tools Used:
Python
Tableau


Python Libraries Used:
Pandas
Matplotlib


Data Cleaning Performed



Team Standardization
Several IPL franchises changed names over the years. To ensure accurate analysis, franchise names were standardized.
Examples:

Delhi Daredevils → Delhi Capitals
Kings XI Punjab → Punjab Kings
Royal Challengers Bangalore → Royal Challengers Bengaluru
Rising Pune Supergiants → Rising Pune Supergiant
Venue Standardization


Duplicate venue names were consolidated into a single standard format.

Examples:

Wankhede Stadium, Mumbai → Wankhede Stadium
Eden Gardens, Kolkata → Eden Gardens
M Chinnaswamy Stadium, Bengaluru → M Chinnaswamy Stadium
This ensured that venue-based analyses were not affected by naming inconsistencies.

Removed Invalid Records
Records containing invalid or missing match winner information were removed.
Example:

Match Won By = Unknown
Total Records Removed: 24 matches


Season Standardization
The Season column contained mixed formats such as:

2007/08
2009
2010

These values were standardized to maintain consistency during trend analysis.


Analyses Performed
Analysis 1: Match Wins by Team
Finding

Mumbai Indians emerged as the most successful IPL franchise with 152 match victories, followed by:

Chennai Super Kings – 144 wins
Royal Challengers Bengaluru – 136 wins
Kolkata Knight Riders – 135 wins
Insight

Mumbai Indians have maintained consistent performance throughout IPL history, making them the most successful team in the dataset.



Analysis 2: Player of the Match Leaders
Finding

AB de Villiers recorded the highest number of Player of the Match awards in the dataset.

Top performers:

AB de Villiers – 24 awards
Chris Gayle – 22 awards
Rohit Sharma – 21 awards
David Warner – 18 awards
Virat Kohli – 18 awards
Insight

The rankings highlight the consistent impact of elite players across multiple IPL seasons.



Analysis 3: Toss Impact Analysis
Finding

Teams winning the toss went on to win the match approximately 51.84% of the time.

Conclusion

While toss advantage exists, the impact is relatively small. Team quality and match performance appear to play a much larger role in determining match outcomes.




Analysis 4: Most Frequently Used IPL Venues
Finding

The venues hosting the highest number of IPL matches were:

Wankhede Stadium – 127 matches
Eden Gardens – 101 matches
M Chinnaswamy Stadium – 98 matches
Arun Jaitley Stadium – 96 matches
Insight

These stadiums have been major IPL venues and have consistently hosted a large number of matches across seasons.



Analysis 5: Venue Kings (Players)
Finding

Different venues have different dominant performers based on Player of the Match awards.

Examples:

Wankhede Stadium → Rohit Sharma
MA Chidambaram Stadium → Michael Hussey
Eden Gardens → Andre Russell
Insight

Certain players consistently perform exceptionally well at specific venues, making them "Venue Kings."



Analysis 6: Venue Kings (Teams)
Finding

Most teams recorded their highest number of victories at their traditional home grounds.

Examples:

Chennai Super Kings → MA Chidambaram Stadium
Mumbai Indians → Wankhede Stadium
Rajasthan Royals → Sawai Mansingh Stadium
Insight

Home-ground familiarity plays an important role in team performance and success.



Analysis 7: Fortress Analysis
Finding

The strongest home-ground advantages in the IPL were:

Venue	Team	Win Percentage
Sawai Mansingh Stadium	Rajasthan Royals	59.38%
MA Chidambaram Stadium	Chennai Super Kings	57.61%
Eden Gardens	Kolkata Knight Riders	53.47%
Insight

These venues can be considered true IPL fortresses where home teams have historically performed exceptionally well.



Analysis 8: IPL Growth Through the Years
Finding

The IPL has expanded significantly since its inception.

Early seasons contained approximately 56–60 matches.
Peak seasons featured more than 70 matches.
Recent seasons continue to maintain a larger tournament structure.
Insight

The increasing number of matches reflects the league's growth, popularity, and commercial success over time.

Key Insights
Mumbai Indians are the most successful IPL franchise with 152 victories.
AB de Villiers leads the Player of the Match rankings with 24 awards.
Wankhede Stadium is the most frequently used IPL venue.
Toss winners won approximately 51.84% of matches, indicating only a slight toss advantage.
Rajasthan Royals possess the strongest home-ground advantage at Sawai Mansingh Stadium.
IPL has expanded significantly, growing from around 58 matches per season to more than 70 matches in recent years.
Tableau Dashboard

An interactive Tableau dashboard was developed to visualize the major insights from the project.

The dashboard includes:

Team Win Analysis
Player of the Match Analysis
Venue Analysis
Toss Impact Analysis
IPL Growth Trend Analysis
Fortress Analysis
Venue Kings (Players)
Venue Kings (Teams)

The dashboard enables users to quickly explore historical IPL trends and performance metrics.

Skills Demonstrated

Through this project, the following skills were demonstrated:

Data Cleaning
Data Transformation
Exploratory Data Analysis (EDA)
Data Visualization
Tableau Dashboard Development
Business Insight Generation
Pandas
Matplotlib
Data Storytelling
Conclusion

This project demonstrates how raw sports data can be transformed into meaningful insights through data cleaning, analysis, and visualization. The findings highlight team dominance, player excellence, venue influence, home-ground advantage, and the evolution of the IPL over nearly two decades.

