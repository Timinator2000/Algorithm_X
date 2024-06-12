from list_comprehension_ex_08 import remove_odds
import builtins


sum_builtin_used = False


def new_sum(x):
    global sum_builtin_used
    sum_builtin_used = True
    return orig_sum(x)


orig_sum = builtins.sum
builtins.sum = new_sum


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test_remove_odds():
    try:
        remove = remove_odds([1, 3, 5, 7, 9])
        assert remove == [], f'Trying remove_odds([1, 3, 5, 7, 9])... Expected [], got {remove}'
        remove = remove_odds([2, 4, 6, 8, 10])
        assert remove == [2, 4, 6, 8, 10], f'Trying remove_odds([2, 4, 6, 8, 10])... Expected [2, 4, 6, 8, 10], got {remove}'
        remove = remove_odds([])
        assert remove == [], f'Trying remove_odds([])... Expected [], got {remove}'
        remove = remove_odds([1, 2, 3, 4, 5, 6])
        assert remove == [2, 4, 6], f'Trying remove_odds([1, 2, 3, 4, 5, 6])... Expected [2, 4, 6], got {remove}'
        remove = remove_odds([25678, 435, 24, 999])
        assert remove == [25678, 24], f'Trying remove_odds([25678, 435, 24, 999])... Expected [[25678, 24]], got {remove}'
        # print('Back to boring me to death...and I had so much hope for you.  Sigh.')
     
        success()

        if sum_builtin_used:
            send_msg("My personal Yoda, you are. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
            send_msg("My personal Yoda, you are. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
            send_msg("My personal Yoda, you are. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
            send_msg("My personal Yoda, you are. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
            send_msg("My personal Yoda, you are. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
            send_msg("My personal Yoda, you are. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
            send_msg("My personal Yoda, you are. 🙏", "_)_/LI")
        else:
            send_msg("Kudos 🌟", "Back to boring me to death...and I had so much hope for you.  Sigh.")

    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)
        send_msg("Hint 💡", "Does you list expression have a condition that acts as a filter? 🤔")


if __name__ == "__main__":
    test_remove_odds()
