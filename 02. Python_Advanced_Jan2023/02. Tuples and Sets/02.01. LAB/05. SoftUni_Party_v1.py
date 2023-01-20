guests_total_number = int(input())
vip_guests_list = []
regular_guests_list = []
for guest_codes in range(guests_total_number):
    guest_res_code = input()
    if guest_res_code[0].isnumeric():
        vip_guests_list.append(guest_res_code)
    elif guest_res_code[0].isalpha():
        regular_guests_list.append(guest_res_code)
#
vip_guests_set = set(sorted(vip_guests_list))
regular_guests_set = set(sorted(regular_guests_list))

attendees_set = set()
attendee = input()
while attendee != "END":
    attendees_set.add(attendee)
    attendee = input()

guests_not_attending_set = set()
[guests_not_attending_set.add(x) for x in vip_guests_set.difference(attendees_set)]
[guests_not_attending_set.add(x) for x in regular_guests_set.difference(attendees_set)]
print(len(guests_not_attending_set))
print('\n'.join(sorted(guests_not_attending_set)))

# ############
# Input_1:
# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END
# -------------
# Output_1:
# 2
# 7IK9Yo0h
# tSzE5t0p
# ############
# Input_2:
# 6
# m8rfQBvl
# fc1oZCE0
# UgffRkOn
# 7ugX7bm0
# 9CQBGUeJ
# 2FQZT3uC
# 2FQZT3uC
# 9CQBGUeJ
# fc1oZCE0
# END
# -------------
# Output_2:
# 3
# 7ugX7bm0
# UgffRkOn
# m8rfQBvl
# ############
