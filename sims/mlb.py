
def simulate_game(team_a, team_b, prop):
    if prop == "ml":
        return {"type": "Moneyline", "winner": team_b, "score": "5-3"}
    elif prop == "ou":
        return {"type": "Over/Under", "total": "Over 8.5"}
    elif prop == "first":
        return {"type": "First Inning", "result": "No Runs"}
    elif prop == "hr":
        return {"type": "Home Run", "players": ["Soto", "Judge"]}
    elif prop == "tb":
        return {"type": "2+ Total Bases", "players": ["Alonso", "Tucker"]}
    elif prop == "k":
        return {"type": "Strikeouts", "pitcher": "Cole", "ks": 7}
    else:
        return {"type": "Unknown", "detail": "Invalid sim"}
