import random


class Person:

    def __init__(self, number: int) -> None:
        self.__number = number

    def get_number(self) -> int:
        return self.__number

    def __eq__(self, other: "Person") -> bool:
        # переопределен оператор сравнения, чтобы использовать оператор in
        return self.get_number() == other.get_number()


class GroupTest:

    def __init__(self, people: list[Person], num_tests: int) -> None:
        self.people = people
        self.num_tests = num_tests

    def run_tests_and_return_result(self) -> float:
        people_in_one_group = 0
        person_19 = self.people[-2]  # человек с номером 19
        person_20 = self.people[-1]  # человек с номером 20
        for _ in range(self.num_tests):
            group = random.sample(self.people, k=10)
            if (person_19 in group) == (person_20 in group):  # оба или в первой группе, или во второй
                people_in_one_group += 1
        return people_in_one_group / self.num_tests


def main() -> None:

    people = [Person(number=number) for number in range(1, 21)]

    group_test = GroupTest(people=people, num_tests=100_000)
    result = group_test.run_tests_and_return_result()

    print(f"Вероятность того, что люди с номерами 19 и 20 окажутся в одной группе: {result}")


if __name__ == "__main__":
    main()
