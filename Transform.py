import pandas as pd
import os

patharquivos = os.path.abspath("files")

arquivos = {
    "match_events": pd.read_csv(os.path.join(patharquivos, "match_events.csv")),
    "matches_detailed": pd.read_csv(os.path.join(patharquivos, "matches_detailed.csv")),
    "matches": pd.read_csv(os.path.join(patharquivos, "matches.csv")),
    "referees": pd.read_csv(os.path.join(patharquivos, "referees.csv")),
    "squads_and_players": pd.read_csv(os.path.join(patharquivos, "squads_and_players.csv")),
    "teams": pd.read_csv(os.path.join(patharquivos, "teams.csv")),
    "tournament_stages": pd.read_csv(os.path.join(patharquivos, "tournament_stages.csv")),
    "venues": pd.read_csv(os.path.join(patharquivos, "venues.csv")),
}

dfs_name = list(arquivos)

# for name in dfs_name:
#     df = arquivos[name]
#     print(name)
#     print(df)

#jogadores goals
print("jogadores goals")
df_squads_and_players = arquivos["squads_and_players"]
df_teams = arquivos["teams"]

df_squads_and_players["team_id"] = pd.to_numeric(df_squads_and_players["team_id"])
df_teams["team_id"] = pd.to_numeric(df_teams["team_id"])

df_squads_and_players = df_squads_and_players.merge(
    df_teams,
    on="team_id",
    how="left"
)
print("\n\n")

resultado_goals = df_squads_and_players[['player_name','team_name','goals']]
resultado_goals['goals'] = pd.to_numeric(resultado_goals['goals'])
resultado_goals = resultado_goals.sort_values(by="goals", ascending=False)
print(resultado_goals)

