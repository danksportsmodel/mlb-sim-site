
from flask import Flask, render_template, request
from sims import mlb

app = Flask(__name__)

daily_games = [
    {"team_a": "Yankees", "team_b": "Mets", "time": "7:05 PM", "weather": "72°F, Wind out to LF"},
    {"team_a": "Braves", "team_b": "Phillies", "time": "6:40 PM", "weather": "68°F, Slight breeze in"},
    {"team_a": "Dodgers", "team_b": "Padres", "time": "9:10 PM", "weather": "70°F, Neutral"}
]

@app.route('/')
def index():
    return render_template("mlb.html", games=daily_games, result=None)

@app.route('/simulate', methods=['POST'])
def simulate():
    team_a = request.form['team_a']
    team_b = request.form['team_b']
    prop = request.form['prop']
    result = mlb.simulate_game(team_a, team_b, prop)
    return render_template("mlb.html", games=daily_games, result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
