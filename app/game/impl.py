
from app.board.impl import Board
from app.board_space.abstract import BoardSpace
from app.board_space.chance.impl import ChanceSpace
from app.chance_card.deck import ChanceCardDeck
from app.dice.dices import Dices
from app.player.impl import Player
from app.position_manager.impl import PositionManager
from app.turn_manager.impl import TurnManager
import csv


class Game:
    _board: Board
    _players: list[Player]
    _turn_manager: TurnManager
    _position_manager: PositionManager
    _dices: Dices
    _card_deck: ChanceCardDeck

    def __init__(self, players: list[Player]):
        self._board = self._create_board_from_file()
        self._players = players
        self._turn_manager = TurnManager(self._players)
        self._position_manager = PositionManager(self._board, self._players)
        self._dices = Dices(count=2)
        self._card_deck = ChanceCardDeck()
        for space in self._board.get_spaces():
            if isinstance(space, ChanceSpace):
                space.set_deck(self)

    def _create_board_from_file(self) -> Board:
        spaces_data = []
        with open('board_space_data.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            spaces_data = list(csv_reader)
        return Board.create_from_data(spaces_data)

    def get_players(self) -> list[Player]:
        return self._players

    def get_turn_manager(self) -> TurnManager:
        return self._turn_manager

    def get_current_player(self) -> Player:
        return self._turn_manager.get_current_player()

    def get_position_by_player(self, player: Player) -> BoardSpace:
        return self._position_manager.get_location(player)

    def get_board(self) -> Board:
        return self._board

    def get_position_manager(self) -> PositionManager:
        return self._position_manager

    def roll_dices(self) -> list[int]:
        return self._dices.roll()

    def draw_board(self) -> None:
        pass

    def get_card_deck(self) -> ChanceCardDeck:
        return self._card_deck

    def set_card_deck(self, deck: ChanceCardDeck) -> None:
        self._card_deck = deck