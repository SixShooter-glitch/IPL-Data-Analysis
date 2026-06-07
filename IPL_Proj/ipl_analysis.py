import pandas as pd
import matplotlib.pyplot as plt

ipl = pd.read_csv("IPL.csv")

# One row per match
matches = ipl.drop_duplicates(subset="match_id")

# Team name standardization
team_mapping = {
    "Royal Challengers Bangalore": "Royal Challengers Bengaluru",
    "Delhi Daredevils": "Delhi Capitals",
    "Rising Pune Supergiants": "Rising Pune Supergiant",
    "Kings XI Punjab": "Punjab Kings"
}

team_columns = [
    "batting_team",
    "bowling_team",
    "toss_winner",
    "match_won_by"
]

for col in team_columns:
    matches[col] = matches[col].replace(team_mapping)



# Remove matches with no valid winner
matches_clean = matches[matches["match_won_by"] != "Unknown"].copy()

print("Original matches:", len(matches))
print("Clean matches:", len(matches_clean))

# Removing duplicates present for venues in the dataset
venue_mapping = {
    "Wankhede Stadium, Mumbai": "Wankhede Stadium",

    "M Chinnaswamy Stadium, Bengaluru":
        "M Chinnaswamy Stadium",

    "MA Chidambaram Stadium, Chepauk":
        "MA Chidambaram Stadium",

    "MA Chidambaram Stadium, Chepauk, Chennai":
        "MA Chidambaram Stadium",

    "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh":
        "Punjab Cricket Association IS Bindra Stadium, Mohali",

    "Rajiv Gandhi International Stadium, Uppal":
        "Rajiv Gandhi International Stadium",

    "Rajiv Gandhi International Stadium, Uppal, Hyderabad":
        "Rajiv Gandhi International Stadium",

    "Arun Jaitley Stadium, Delhi":
        "Arun Jaitley Stadium",
    "Feroz Shah Kotla":"Arun Jaitley Stadium",
    "Eden Gardens, Kolkata": "Eden Gardens",
    "Brabourne Stadium, Mumbai": "Brabourne Stadium",
    "Dr DY Patil Sports Academy, Mumbai": "Dr DY Patil Sports Academy",
    "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam":
        "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium",
    "Himachal Pradesh Cricket Association Stadium, Dharamsala":
        "Himachal Pradesh Cricket Association Stadium",

    "M.Chinnaswamy Stadium":
        "M Chinnaswamy Stadium",

    "Maharaja Yadavindra Singh International Cricket Stadium, New Chandigarh":
        "Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur",


    "Sawai Mansingh Stadium, Jaipur":
        "Sawai Mansingh Stadium",

    "Newlands":
        "Newlands, Cape Town",

    "Sardar Patel Stadium, Motera":
        "Narendra Modi Stadium, Ahmedabad",
    "Punjab Cricket Association IS Bindra Stadium":
        "Punjab Cricket Association Stadium, Mohali",

    "Punjab Cricket Association IS Bindra Stadium, Mohali":
      "Punjab Cricket Association Stadium, Mohali",

    "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh":
       "Punjab Cricket Association Stadium, Mohali",   



    "Maharashtra Cricket Association Stadium, Pune":
        "Maharashtra Cricket Association Stadium"
}

matches_clean["venue"] = (
    matches_clean["venue"].replace(venue_mapping)
)

#IPL MATCHES WON BY TEAMS 1 ANALYSES

matches_clean["match_won_by"].value_counts().plot(kind="bar",figsize=(12,6))
plt.title("IPL Match wins by Teams")
plt.xlabel("Teams")
plt.ylabel("No of wins")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




matches_clean["player_of_match"].value_counts().head(10).plot(
    kind="bar",
    figsize=(10,5)
)

# Top 10 Player of the match winners Analysis Part 2

plt.title("Top 10 Player of the Match Winners")
plt.xlabel("Players")
plt.ylabel("Awards")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Does winning the toss actually help win the match Analysis part 3

matches_clean["match_won_by"] = matches_clean["match_won_by"].replace(team_mapping)

matches_clean["toss_winner"] = matches_clean["toss_winner"].replace(team_mapping)

matches_clean["toss_match_win"] = (
    matches_clean["toss_winner"] == matches_clean["match_won_by"]
)

print(matches_clean["toss_match_win"].value_counts())

toss_win_percentage = matches_clean["toss_match_win"].mean() * 100

print(round(toss_win_percentage, 2))

#Does batting first or chasing win more IPL matches Analysis 3
field_matches = matches_clean[
    matches_clean["toss_decision"] == "field"
]

bat_matches = matches_clean[
    matches_clean["toss_decision"] == "bat"
]

field_win_pct = (
    (field_matches["toss_winner"] ==
     field_matches["match_won_by"]).mean() * 100
)

bat_win_pct = (
    (bat_matches["toss_winner"] ==
     bat_matches["match_won_by"]).mean() * 100
)

print("Field First Win %:", round(field_win_pct, 2))
print("Bat First Win %:", round(bat_win_pct, 2))
# Top IPL Venues by no of matches Analysis part 4
print(matches_clean["venue"].value_counts().head(10))
matches_clean["venue"].value_counts().head(10).plot(
    kind="bar", figsize=(12,6)
)

plt.title("Top 10 IPL Venues by number of Matches")
plt.xlabel("Venue")
plt.ylabel("No of matches")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Kings of IPL Stadiums (top Player of the Match winners at each major venue Analysis 5

venue_kings = (
    matches_clean.groupby("venue")["player_of_match"]
    .agg(lambda x: x.value_counts().index[0])
)

print(venue_kings)

# Analysis 6 - Venue Kings (Teams)

venue_team_kings = (
    matches_clean.groupby("venue")["match_won_by"]
    .agg(lambda x: x.value_counts().index[0])
)

print(venue_team_kings)

# Analysis 7 - Fortress Analysis

venue_matches = (
    matches_clean["venue"].value_counts()
)

fortress_data = []

for venue in venue_team_kings.index:

    king_team = venue_team_kings[venue]

    wins = len(
        matches_clean[
            (matches_clean["venue"] == venue) &
            (matches_clean["match_won_by"] == king_team)
        ]
    )

    total_matches = venue_matches[venue]

    fortress_pct = (
        wins / total_matches
    ) * 100

    fortress_data.append(
        [
            venue,
            king_team,
            wins,
            total_matches,
            round(fortress_pct, 2)
        ]
    )

fortress_df = pd.DataFrame(
    fortress_data,
    columns=[
        "Venue",
        "King Team",
        "Wins",
        "Total Matches",
        "Fortress %"
    ]
)

fortress_df = fortress_df.sort_values(
    "Fortress %",
    ascending=False
)



fortress_df = fortress_df[
    fortress_df["Total Matches"]>=50
]

print(fortress_df.head(10))

#Season wise-trends ANALYSIS 8

matches_clean["season"]=(
    matches_clean["season"]
    .astype(str)
    .str.strip()
)

season_matches = (
    matches_clean["season"]
    .value_counts()
    .sort_index()
)

season_matches_plot = season_matches.drop("2026")
season_matches_plot.plot(
    kind="line",
    figsize=(12,6),
    marker="o"
)

plt.title("IPL Matches Played Per Season")
plt.xlabel("Season")
plt.ylabel("Number of Matches")

plt.xticks(
    range(len(season_matches_plot.index)),
    season_matches_plot.index,
    rotation=45
)

plt.grid(True)
plt.tight_layout()
plt.show()

matches_clean.to_csv(
    "IPL_Cleaned.csv",
    index=False
)


team_wins=(
    matches_clean["match_won_by"]
    .value_counts()
)

team_wins.to_csv(
    "Team_Wins.csv"
)

venue_kings.to_csv(
    "Venue_Player_Kings.csv"
)

venue_team_kings.to_csv(
    "Venue_Team_Kings.csv"
)

fortress_df.to_csv(
    "Fortress_Analysis.csv",
    index=False
)

season_matches.to_csv(
    "Season_Trends.csv"
)



print(
    matches_clean["player_of_match"]
    .value_counts()
    .head(10)
)



