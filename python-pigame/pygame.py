from clihelper import Cli_Helper

Cli_Helper = Cli_Helper()


class Game:
    def __init__(self, default_file_name: str):
        self.default_pi_list = self.update_pi_file(default_file_name)
        self.default_pi_string = self.return_pi_string(self.default_pi_list)

    def update_pi_file(self, filename: str) -> list[int]:
        pi_digits_list = []
        with open(filename, 'r', encoding='UTF-8') as pi_file:
            pi_digits = pi_file.read()
        for digit in pi_digits:
            if digit.isnumeric():
                pi_digits_list.append(int(digit))
            elif digit != '\n':
                Cli_Helper.warning_non_digit_character_in_pi_list()
            else:
                continue
        return pi_digits_list

    def return_pi_string(
            self,
            pi_digits_list: list[int],
            ) -> str:
        return ''.join([str(digit) for digit in pi_digits_list])

    def ask_pi(self) -> list[int]:

        Cli_Helper.print_greetings()

        new_input_pi = ''
        input_pi = ''
        while new_input_pi != 'done':
            new_input_pi = input('>> ')
            if input_pi != 'done':
                input_pi += new_input_pi
        return [int(digit) for digit in input_pi if digit.isnumeric()]

    def check_pi(
            self, user_pi_input: list[int], pi_list: list[int]
            ) -> (bool, int):
        user_pi_input_sum = sum(user_pi_input)
        sum_pi_list_adjusted = sum(pi_list[0:len(user_pi_input)])
        first_all_correct_check = user_pi_input_sum - sum_pi_list_adjusted == 0
        if first_all_correct_check:
            Cli_Helper.print_all_correct_sequence_message(len(user_pi_input))
            return (True, len(user_pi_input))
        right_sequence_size = 0
        wrong_digit_position = 0
        wrong_digit = 0
        correct_digit = 0
        for digit in range(len(user_pi_input)):
            if user_pi_input[digit] != pi_list[digit]:
                wrong_digit_position = digit
                wrong_digit = user_pi_input[digit]
                correct_digit = pi_list[digit]
                break
            right_sequence_size += 1

        Cli_Helper.print_wrong_digit_in_sequence_message(
                wrong_digit_position,
                wrong_digit,
                correct_digit,
                right_sequence_size,
                user_pi_input,
                pi_list[0:len(user_pi_input)],
                )

        return (False, right_sequence_size)

    def return_pi_in_epochs(
            self,
            pi_list: list[int],
            first_three_digits_in_the_list: bool,
            how_many_epochs: int,
            epoch_size=4,
            ) -> int:
        pi_in_epochs = []
        current_epoch = ''
        current_digit_counter = 0
        number_of_epochs = 0
        if first_three_digits_in_the_list:
            pi_list_for_iterate = pi_list[3:]
        else:
            pi_list_for_iterate = pi_list
        for digit in pi_list_for_iterate:
            if number_of_epochs == how_many_epochs:
                break
            current_epoch += (
                    str(digit)
                    if str(digit).isnumeric()
                    else Cli_Helper.warning_non_digit_character_in_pi_list()
                    )
            current_digit_counter += 1
            if current_digit_counter == epoch_size:
                pi_in_epochs.append(current_epoch)
                current_epoch = ''
                current_digit_counter = 0
                number_of_epochs += 1

        return pi_in_epochs

    def return_user_pi_input_in_epochs(
            self, user_pi_input: list[int], epoch_size: int
            ) -> int:
        user_input_remainder = (len(user_pi_input) - 3) % epoch_size
        remainder_elements_in_user_input = []
        if user_input_remainder != 0:
            remainder_elements_in_user_input = ''.join(
                    [
                        str(i)
                        for i in user_pi_input[
                            len(user_pi_input) - user_input_remainder:
                            ]
                        ]
                    )
            user_pi_input_size_fixed = user_pi_input[
                    0:len(user_pi_input)
                    -
                    len(remainder_elements_in_user_input)
                    ]
        else:
            user_pi_input_size_fixed = user_pi_input
        user_pi_in_epochs = self.return_pi_in_epochs(
                user_pi_input_size_fixed, True, -1, epoch_size
                )
        return (
                user_pi_in_epochs
                if user_input_remainder == 0
                else user_pi_in_epochs + [remainder_elements_in_user_input]
                )


game_section = Game('./one-million.txt')
default_pi_list = game_section.default_pi_list
asked_pi = game_section.ask_pi()
game_section.check_pi(asked_pi, default_pi_list)
user_pi_input_in_epochs = game_section.return_user_pi_input_in_epochs(
        asked_pi, 4
        )
pi_in_epochs_user = game_section.return_pi_in_epochs(
        default_pi_list, True, len(user_pi_input_in_epochs), 4
        )
for epoch_id in range(len(user_pi_input_in_epochs)):
    print(
            user_pi_input_in_epochs[epoch_id],
            ' - ',
            pi_in_epochs_user[epoch_id]
            )
