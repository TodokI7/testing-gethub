from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4


class Wallet:
    def __init__(self, owner_id: str):
        self.balance = 0.0
        self.deposit = 0.0
        self.owner_id = owner_id


class User:
    def __init__(self, id: str, username: str, password: str, birthday: datetime):
        self.id = id
        self.username = username
        self.password = password
        self.birthday = birthday

    @property
    def wallet(self) -> Optional[Wallet]:
        for w in database["wallets"]:
            if w.owner_id == self.id:
                return w
        return None


class Transaction:
    def __init__(
        self,
        from_id: str,
        to_id: str,
        amount: float,
        transfer_datetime: datetime,
        description: str,
    ):
        self.from_id = from_id
        self.to_id = to_id
        self.amount = amount
        self.transfer_datetime = transfer_datetime
        self.description = description


class BankService:
    def __init__(self):
        self.__current_user: User = None

    def create_transaction(self):
        from_id = self.__current_user.id
        to_id = input("Введите ID пользователя: ")
        amount = float(input("Введите сумму для перевода: "))
        transfer_datetime = datetime.now(tz=timezone.utc)
        description = input("Оставьте сообщение к переводу: ")

        new_transaction = Transaction(
            from_id=from_id,
            to_id=to_id,
            amount=amount,
            transfer_datetime=transfer_datetime,
            description=description,
        )

        to_user: User = None
        for user in database["users"]:
            if user.id == to_id:
                to_user = user

        if to_user is None:
            print("Пользователь не найден!")
            return

        if to_user.wallet is None:
            print("У получателя нет кошелька")
            return

        if self.__current_user.wallet is None:
            print("У вас нет кошелька")
            return

        if self.__current_user.wallet.balance < amount:
            print("Недостаточно денег для перевода")
            return

        self.__current_user.wallet.balance -= amount
        to_user.wallet.balance += amount
        database["transactions"].append(new_transaction)
        print("Транзакция выполнена")

    def put_deposit(self):
        pass

    def take_deposit(self):
        pass

    def get_balance(self):
        if self.__current_user is None:
            print("Сначала войдите в аккаунт!")
        else:
            for wallet in database["wallets"]:
                if wallet.owner_id == self.__current_user.id:
                    print("Ник вашего аккаунта:", self.__current_user.username)
                    print("Ваш баланс:", wallet.balance, "KZT")
                    print("На депозите:", wallet.deposit, "KZT")

    def create_user(self):
        user_id = str(uuid4())
        username = input("Введите ник пользователя: ")
        password = input("Введите пароль пользователя: ")
        birthday = input("Введите ДР пользователя в формате - мм.дд.гггг : ")
        try:
            birthday = datetime.strptime(birthday, "%m.%d.%Y")

            user = User(
                id=user_id,
                username=username,
                password=password,
                birthday=birthday,
            )
            wallet = Wallet(owner_id=user_id)

            database["users"].append(user)
            database["wallets"].append(wallet)

            print("Вы успешно зарегистрированы!")
        except ValueError:
            print("Вы ввели день рождения в неправильном формате")

    def logout(self):
        pass

    def login(self):
        print("*" * 10)
        username = input("Введите ник: ")
        password = input("Введите пароль: ")
        for user in database["users"]:
            if username == user.username and password == user.password:
                self.__current_user = user

                print("Вы успешно зашли!")
                print("*" * 10)
                return
        print("Неправильные данные!")

    def get_transactions(self):
        pass


database = {
    "users": [
        User(
            id="1",
            username="teacher",
            password="123",
            birthday=datetime(1999, 10, 10),
        ),
        User(
            id="2",
            username="test_user",
            password="123",
            birthday=datetime(1999, 10, 10),
        ),
        User(str(uuid4()), "second", "123", datetime(1999, 10, 10)),
        User(str(uuid4()), "third", "123", datetime(1999, 10, 10)),
        User(str(uuid4()), "fourth", "123", datetime(1999, 10, 10)),
    ],
    "wallets": [
        Wallet(owner_id="1"),
        Wallet(owner_id="2"),
    ],
    "transactions": [],
}

bank_service = BankService()  # создание объекта класса BankService


commands = {
    "Войти": bank_service.login,
    "Зарегистрироваться": bank_service.create_user,
    "Выйти": bank_service.logout,
    "Положить деньги на депозит": bank_service.put_deposit,
    "Взять деньги с депозита": bank_service.take_deposit,
    "Посмотреть баланс": bank_service.get_balance,
    "Перевести деньги на другой счет": bank_service.create_transaction,
    "Посмотреть историю переводов": bank_service.get_transactions,
}

while True:
    keys = list(commands.keys())
    for index in range(len(keys) - 1):
        print(f"{index + 1}. {keys[index]}")
    command_index = int(input("Выберите номер комманды: "))
    try:
        command_key = keys[command_index - 1]
        commands[command_key]()
    except IndexError:
        print("Такой комманды нету")
