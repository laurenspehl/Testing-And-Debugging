import pytest
from leaderboard import Leaderboard


def test_add_player():
    lb = Leaderboard()
    lb.add_player("Alice")
    assert len(lb) == 1


def test_add_player_with_initial_score():
    lb = Leaderboard()
    lb.add_player("Alice", initial_score=500)
    assert lb.get_top_n(1) == [("Alice", 500)]

def test_add_player_with_negative_initial_score():
    lb = Leaderboard()
    with pytest.raises(ValueError):
        lb.add_player("Alice", initial_score=-500)

def test_get_top_n_negative():
    lb = Leaderboard()
    with pytest.raises(ValueError):
        lb.get_top_n(-1)

def test_add_duplicate_player():
    lb = Leaderboard()
    lb.add_player("Alice", initial_score=500)
    with pytest.raises(ValueError):
        lb.add_player("Alice", initial_score=500)

def test_record_match_updates_scores():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 100)
    lb.record_match("Alice", "Bob")
    assert lb.get_top_n(2) == [("Alice", 110), ("Bob", 90)]

def test_record_match_no_winner():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 100)
    with pytest.raises(KeyError):
        lb.record_match("Alicee", "Bob")

def test_record_match_no_loser():
    lb = Leaderboard()
    lb.add_player("Alice", 100)
    lb.add_player("Bob", 100)
    with pytest.raises(KeyError):
        lb.record_match("Alice", "Bobb")

def test_record_match_zero_points():
    lb = Leaderboard()
    lb.add_player("Alice", 10)
    lb.add_player("Bob", 10)
    with pytest.raises(ValueError):
        lb.record_match("Alice", "Bob", 0)


def test_get_rank_key_error():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    lb.add_player("Carol", 200)
    assert lb.get_rank("Alice") == 1
    assert lb.get_rank("Carol") == 2
    with pytest.raises(KeyError):
        assert lb.get_rank("Bobb") == 3

def test_get_rank():
    lb = Leaderboard()
    lb.add_player("Alice", 300)
    lb.add_player("Bob", 100)
    lb.add_player("Carol", 200)
    assert lb.get_rank("Alice") == 1
    assert lb.get_rank("Carol") == 2
    assert lb.get_rank("Bob") == 3

def test_get_percentile():
    lb = Leaderboard()
    lb.add_player("Alice")
    assert lb.get_percentile("Alice") == 100.0

def test_get_percentile_error():
    lb = Leaderboard()
    lb.add_player("Alice")
    with pytest.raises(KeyError):
        lb.get_percentile("Alicee")

def test_get_win_rate_error():
    lb = Leaderboard()
    lb.add_player("Alice")
    with pytest.raises(KeyError):
        lb.get_win_rate("Alicee")

def test_apply_bonus_error():
    lb = Leaderboard()
    lb.add_player("Alice")
    with pytest.raises(KeyError):
        lb.apply_bonus("Alicee", 1.0)

def test_get_multi_percentile():
    lb = Leaderboard()
    lb.add_player("Alice")
    lb.add_player("Bob")
    assert lb.get_percentile("Alice") == 0.0
