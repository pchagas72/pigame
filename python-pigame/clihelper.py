import sys


class Cli_Helper:
    def __init__(self):
        pass

    def pass_error_message(
            self,
            error_message):
        sys.exit(f"ERROR: {error_message}")

    def print_warning_message(
            self,
            warning_message: str,
            ):
        print(f'WARNING: {warning_message}')
        print('Ignore warning?')
        ignore_warning = ''
        while (
                ignore_warning != 'y'
                and ignore_warning != 'n'
                and ignore_warning != 'yes'
                and ignore_warning != 'no'
                ):
            ignore_warning = input('Yes/No: ').strip().lower()
        if ignore_warning == 'yes' or ignore_warning == 'y':
            print('The program will just ignore it then, errors may happen.')
            return 0
        else:
            self.pass_error_message(warning_message)
            return 1

    def print_greetings(self) -> int:
        print('Now, you can type pi.')
        print('Type all digits you can remember.')
        print('Non-numeric characters will be ignored.')
        print('You can have multiple input lines, when done, just type "done"')
        print('')
        return 0

    def print_all_correct_sequence_message(
            self,
            correct_sequence_size: int
            ) -> int:
        print('Congratulations!')
        print(
                f'All your {correct_sequence_size} digits were in the correct sequence.'
                )
        return 0

    def print_wrong_digit_in_sequence_message(
            self,
            wrong_digit_position: int,
            wrong_digit: int,
            correct_digit: int,
            right_sequence_size: int,
            user_pi_input: int,
            correct_sequence: int,
            ) -> int:
        print(
                f"""
                Your {wrong_digit_position+1}th digit was wrong.
                You typed {wrong_digit} when it was supposed to be {correct_digit}.
                You rightfully wrote {right_sequence_size} digits.

                Your sequence was:

                {user_pi_input}

                The correct sequence is:

                {correct_sequence}

                """
                )
        return 0

    def warning_non_digit_character_in_pi_list(self) -> int:
        return self.print_warning_message(
                'Non digit character found in pi input file.'
                )
