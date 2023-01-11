# Getting 72/100 from Judge because Judge is being Judge ...

list_tickets = input().split(", ")
winning_chars = ["@", "#", "$"]

for index in range(len(list_tickets)):
    invalid_ticket = False
    winning_ticket = False
    current_ticket = list_tickets[index].strip()
    jackpot = False

    if len(current_ticket) != 20:
        invalid_ticket = True

    else:
        ticket_left_part = current_ticket[:10]
        ticket_right_part = current_ticket[10:]
        lp_winning = False
        rp_winning = False
        winning_ch = ""
        count_win_ch = 0
        max_count_win_chr_left_part = 0
        max_count_win_chr_right_part = 0

        for character in winning_chars:
            if current_ticket.count(character) == 20:
                count_win_ch = len(current_ticket) / 2
                winning_ch = character
                jackpot = True
                break
            else:
                winning_ch_accum = 0
                for symbol in ticket_left_part:
                    if symbol == character:
                        winning_ch_accum += 1
                        if winning_ch_accum >= 6:
                            lp_winning = True
                            winning_ch = character
                            if max_count_win_chr_left_part < winning_ch_accum:
                                max_count_win_chr_left_part = winning_ch_accum
                    else:
                        if max_count_win_chr_left_part < winning_ch_accum:
                            max_count_win_chr_left_part = winning_ch_accum
                        winning_ch_accum = 0

                winning_ch_accum = 0
                for symbol in ticket_right_part:
                    if symbol == character:
                        winning_ch_accum += 1
                        if winning_ch_accum >= 6:
                            rp_winning = True
                            winning_ch = character
                            if max_count_win_chr_right_part < winning_ch_accum:
                                max_count_win_chr_right_part = winning_ch_accum
                    else:
                        if max_count_win_chr_right_part < winning_ch_accum:
                            max_count_win_chr_right_part = winning_ch_accum
                        winning_ch_accum = 0

            if lp_winning is True and rp_winning is True:
                winning_ticket = True
                if max_count_win_chr_left_part > max_count_win_chr_right_part:
                    count_win_ch = max_count_win_chr_right_part
                else:
                    count_win_ch = max_count_win_chr_left_part

    if jackpot == True:
        print(f'ticket "{current_ticket}" - {int(count_win_ch)}{winning_ch} Jackpot!')
    elif jackpot == False and winning_ticket == True:
        print(f'ticket "{current_ticket}" - {count_win_ch}{winning_ch}')
    elif invalid_ticket == True:
        print(f"invalid ticket")
    else:
        print(f'ticket "{current_ticket}" - no match')

# ------------------------------------------------------------#
# input_1: Cash$$$$$$Ca$$$$$$sh
# output_1: ticket "Cash$$$$$$Ca$$$$$$sh" - 6$
# ------------------------------------------------------------#
# input_2: $$$$$$$$$$$$$$$$$$$$, aabb , th@@@@@@eemo@@@@@@ey
# output_2:
#           ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!
#           invalid ticket
#           ticket "th@@@@@@eemo@@@@@@ey" - 6@
# ------------------------------------------------------------#
# input_3: validticketnomatch:(, Cas$$$$$$$Ca$$$$$$s$
# output_3:
#           ticket "validticketnomatch:(" - no match
#           ticket "Cas$$$$$$$Ca$$$$$$s$" - 6$
# ------------------------------------------------------------#

