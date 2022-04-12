class Player:
    def __init__(self, player_name) -> None:
        self.player_name = player_name


class Negative(Player):
    def __init__(self, player_name) -> None:
        self.lier = False
        super().__init__(player_name)


class LotusCarrier(Player):
    def __init__(self, player_name) -> None:
        self.lier = False
        super().__init__(player_name)

    def protect(self):
        pass


class Positive(Player):
    def __init__(self, player_name) -> None:
        self.lier = True
        super().__init__(player_name)

    def infect(self, target):
        target = Positive(target)


class Otaku(Player):
    def __init__(self, player_name) -> None:
        self.room = 
        self.lier = False
        super().__init__(player_name)

    def confirm(self, target):
        if type(target) == Otaku and target.room == self.room:
            return type(self), type(target)
        else:
            return 'Target is not Otaku'


class Volunteer(Player):
    def __init__(self, player_name) -> None:
        self.lier = False
        super().__init__(player_name)

    def check(self, target):
        return type(target)


class Spreadism(Player):
    def __init__(self, player_name) -> None:
        self.lier = True
        super().__init__(player_name)


class Doctor(Player):
    def __init__(self, player_name) -> None:
        self.lier = False
        super().__init__(player_name)
    
    def check(self, target):
        return type(target)


class Hunger(Player):
    def __init__(self, player_name) -> None:
        self.lier = False
        super().__init__(player_name)
