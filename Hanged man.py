msg_proposal = 'Введите Буква/Слово'
msg_win = 'Вы угадали'
msg_game_over = 'Вы проиграли'
lives = 3
word = 'вишня'
###############################################
def get_lives(lives): return lives
def show_table(word): return '---'
def show_message(msg): return msg
def letter_correct(letter):return letter
def letter_incorrect(letter): lives - 1
def word_correct(word): return word
################################################
while(get_lives):
    show_table(word)
    show_message(msg_proposal)
    if letter_correct:
        show_table(word)
        show_message(msg_proposal)
    elif letter_incorrect:
        show_table(word)
        show_message(msg_proposal)
        get_lives
    if word_correct:
        show_table(word)
        show_message(msg_win)
    else:
        show_message(msg_game_over)
        get_lives
######################################


#letter = get_letter()
#table = get_table()
#word = get_word()
#score = get_score()
#while is_alive(score):
#        show_table(table)
#        show_message('')
#        answer = prompt('')
#        if is_word_correct(letter, answer):
#          create_new_table(table)
#          show_message('')
#          else

 #       elif is_letter_correct(letter):
  #        create_new_table(table)
   #       show_message('')




