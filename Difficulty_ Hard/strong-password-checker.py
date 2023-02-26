#  https://leetcode.com/problems/strong-password-checker/
#  A password is considered strong if the below conditions are all met:
#  It has at least 6 characters and at most 20 characters.
#  It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
#  It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
#  Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.
#  In one step, you can:
#  Insert one character to password,
#  Delete one character from password, or
#  Replace one character of password with another character.


from string import ascii_lowercase, ascii_uppercase, digits


class Solution:
    def strongPasswordChecker(self, password: str):

        # function get ostatok ot delenia na 3 and number
        def get_ostatok_ot_delenia_na_3(num):
            return num % 3, num

        # function for checking lenght of the password
        def check_len_password(password):
            return True if 6 <= len(password) <= 20 else False

        # function to count deleting or adding in lenght for getting the strong password
        def get_difference_len_password(password):
            if len(password) < 6:
                return 6 - len(password)
            if len(password) > 20:
                return len(password) - 20

        # function for checking containing ascii_lowercase in the password
        def check_ascii_lowercase(password):
            count = 0
            for c in password:
                if c in ascii_lowercase:
                    count += 1
            return True if count else False

        # function for checking containing ascii_uppercase in the password
        def check_ascii_uppercase(password):
            count = 0
            for c in password:
                if c in ascii_uppercase:
                    count += 1
            return True if count else False

        # function for checking containing digits in the password
        def check_digits(password):
            count = 0
            for c in password:
                if c in digits:
                    count += 1
            return True if count else False

        # function for checking three repeat symbols in the password
        def check_three_repeat_symbol(password):
            repeat_symbol = True
            for i in range(len(password)):
                if password.count(password[i]) > 2:
                    if password[i] * 3 in password:
                        repeat_symbol = False
                        break
            return repeat_symbol

        # function to count deleting for getting strong the password
        def get_differecne_three_repeat_symbol(password):
            repeat_symbol = 0
            while len(password) > 0:
                for i in password:
                    count = 1
                    if password.count(i) < 3:
                        password = password.replace(i, '', 1)
                    elif password.count(i) > 2:
                        for j in range(1, len(password)):
                            if i == password[j]:
                                count += 1
                                continue
                            break
                        if count >= 3:
                            repeat_symbol = repeat_symbol + count - 2
                            password = password.replace(i * count, '', 1)
                        else:
                            password = password.replace(i * count, '', 1)
                    break
            return repeat_symbol

        # The function return quantity of changes if lenght of password is ok - [6; 20] letters
        def get_repeat_quantity_if_len_is_ok(password):
            quantity_changes = 0
            while len(password) > 0:
                for i in password:
                    count = 1
                    if password.count(i) < 3:
                        password = password.replace(i, '', 1)
                    elif password.count(i) > 2:
                        for j in range(1, len(password)):
                            if i == password[j]:
                                count += 1
                                continue
                            break
                        if count >= 3:
                            quantity_changes = quantity_changes + count // 3
                            password = password.replace(i * count, '', 1)
                        else:
                            password = password.replace(i * count, '', 1)
                    break
            return quantity_changes

        # func return quantity of changes if len more 20
        def get_quantity_changes_if_len_more_20_1(password):
            password_copy = password[:]
            repeat_symbol = {}
            while len(password) > 0:
                for i in range(len(password)):
                    count = 1
                    if password.count(password[i]) < 3:
                        password = password.replace(password[i], '', 1)
                    elif password.count(password[i]) > 2:
                        for j in range(1, len(password)):
                            if password[i] == password[j]:
                                count += 1
                                continue
                            break
                        if count >= 3:
                            if password[i] not in repeat_symbol.keys():
                                repeat_symbol[password[i]] = []
                                repeat_symbol[password[i]].append(count)
                            else:
                                repeat_symbol[password[i]].append(count)
                            password = password.replace(password[i] * count, '', 1)
                        else:
                            password = password.replace(password[i] * count, '', 1)
                    break
            tmp = [repeat_symbol[key] for key in repeat_symbol]
            res = []
            for x in tmp:
                res += x

            quantity_of_changes = 0
            difr = len(password_copy) - 20
            while difr > quantity_of_changes:
                res = sorted(res, key=get_ostatok_ot_delenia_na_3)
                for x in range(len(res)):
                    if res[x] % 3 == 0:
                        if quantity_of_changes == difr:
                            break
                        quantity_of_changes += 1
                        res[x] -= 1
                        continue
                    if res[x] % 3 == 1:
                        if quantity_of_changes == difr:
                            break
                        quantity_of_changes += 1
                        res[x] -= 1
                        continue
                    if res[x] % 3 == 2:
                        if quantity_of_changes == difr:
                            break
                        quantity_of_changes += 1
                        res[x] -= 1
                        continue

            answer = 0
            for y in res:
                answer += y // 3
            answer += difr

            return answer

        def get_quantity_changes_if_len_more_20_2(password):
            password_copy = password[:]
            repeat_symbol = {}
            while len(password) > 0:
                for i in range(len(password)):
                    count = 1
                    if password.count(password[i]) < 3:
                        password = password.replace(password[i], '', 1)
                    elif password.count(password[i]) > 2:
                        for j in range(1, len(password)):
                            if password[i] == password[j]:
                                count += 1
                                continue
                            break
                        if count >= 3:
                            if password[i] not in repeat_symbol.keys():
                                repeat_symbol[password[i]] = []
                                repeat_symbol[password[i]].append(count)
                            else:
                                repeat_symbol[password[i]].append(count)
                            password = password.replace(password[i] * count, '', 1)
                        else:
                            password = password.replace(password[i] * count, '', 1)
                    break
            tmp = [repeat_symbol[key] for key in repeat_symbol]
            res = []
            for x in tmp:
                res += x

            quantity_of_changes = 0
            difr = len(password_copy) - 20
            while difr > quantity_of_changes:
                for x in range(len(res)):
                    res = sorted(res, key=get_ostatok_ot_delenia_na_3, reverse=True)
                    if res[x] % 3 == 0:
                        if quantity_of_changes == difr:
                            break
                        quantity_of_changes += 1
                        res[x] -= 1
                        continue
                    if res[x] % 3 == 1:
                        if quantity_of_changes == difr:
                            break
                        quantity_of_changes += 1
                        res[x] -= 1
                        continue
                    if res[x] % 3 == 2:
                        if quantity_of_changes == difr:
                            break
                        quantity_of_changes += 1
                        res[x] -= 1
                        continue

            answer = 0
            for y in res:
                answer += y // 3
            answer += difr

            return answer

        def get_quantity_changes_if_len_more_20_3(password):
            password_copy = password[:]
            repeat_symbol = {}
            while len(password) > 0:
                for i in range(len(password)):
                    count = 1
                    if password.count(password[i]) < 3:
                        password = password.replace(password[i], '', 1)
                    elif password.count(password[i]) > 2:
                        for j in range(1, len(password)):
                            if password[i] == password[j]:
                                count += 1
                                continue
                            break
                        if count >= 3:
                            if password[i] not in repeat_symbol.keys():
                                repeat_symbol[password[i]] = []
                                repeat_symbol[password[i]].append(count)
                            else:
                                repeat_symbol[password[i]].append(count)
                            password = password.replace(password[i] * count, '', 1)
                        else:
                            password = password.replace(password[i] * count, '', 1)
                    break
            tmp = [repeat_symbol[key] for key in repeat_symbol]
            res = []
            for x in tmp:
                res += x

            quantity_of_changes = 0
            difr = len(password_copy) - 20
            while difr > quantity_of_changes:
                res = sorted(res)
                for x in range(len(res)):
                    while res[x] > 2:
                        if quantity_of_changes == difr:
                            break
                        if res[x] > 2:
                            quantity_of_changes += 1
                            res[x] -= 1
                continue

            answer = 0
            for y in res:
                answer += y // 3
            answer += difr

            return answer

        def get_quantity_changes_if_len_more_20_4(password):
            password_copy = password[:]
            repeat_symbol = {}
            while len(password) > 0:
                for i in range(len(password)):
                    count = 1
                    if password.count(password[i]) < 3:
                        password = password.replace(password[i], '', 1)
                    elif password.count(password[i]) > 2:
                        for j in range(1, len(password)):
                            if password[i] == password[j]:
                                count += 1
                                continue
                            break
                        if count >= 3:
                            if password[i] not in repeat_symbol.keys():
                                repeat_symbol[password[i]] = []
                                repeat_symbol[password[i]].append(count)
                            else:
                                repeat_symbol[password[i]].append(count)
                            password = password.replace(password[i] * count, '', 1)
                        else:
                            password = password.replace(password[i] * count, '', 1)
                    break

            tmp = [repeat_symbol[key] for key in repeat_symbol]

            res = []
            for x in tmp:
                res += x
            res = sorted(res, key=get_ostatok_ot_delenia_na_3)

            def get_kratnoe_3_0(num):
                return True if num % 3 == 0 else False

            def get_kratnoe_3_1(num):
                return True if num % 3 == 1 else False

            def get_kratnoe_3_2(num):
                return True if num % 3 == 2 else False

            def get_num_3_or_4(num):
                return True if num == 4 or num == 3 else False

            quantity_of_changes = 0
            difr = len(password_copy) - 20
            while difr > quantity_of_changes:
                if any([get_num_3_or_4(num) for num in res]) == True:
                    for x in range(len(res)):
                        if res[x] == 4 or res[x] == 3:
                            if quantity_of_changes == difr:
                                break
                            quantity_of_changes += 1
                            res[x] -= 1
                            break
                    continue

                if any([get_kratnoe_3_0(num) for num in res]) == True:
                    for x in range(len(res)):
                        if res[x] >= 3 and res[x] % 3 == 0:
                            if quantity_of_changes == difr:
                                break
                            quantity_of_changes += 1
                            res[x] -= 1
                            break
                        else:
                            continue
                    continue

                if any([get_kratnoe_3_1(num) for num in res]) == True:
                    for x in range(len(res)):
                        if res[x] >= 3 and res[x] % 3 == 1:
                            if quantity_of_changes == difr:
                                break
                            quantity_of_changes += 1
                            res[x] -= 1
                            break
                        else:
                            continue
                    continue

                if any([get_kratnoe_3_2(num) for num in res]) == True:
                    for x in range(len(res)):
                        if res[x] >= 3 and res[x] % 3 == 2:
                            if quantity_of_changes == difr:
                                break
                            quantity_of_changes += 1
                            res[x] -= 1
                            break
                        else:
                            continue
                    continue

            answer = 0
            for y in res:
                answer += y // 3
            answer += difr

            return answer

        # list with results of functions
        check_all = [check_ascii_lowercase(password),
                     check_ascii_uppercase(password),
                     check_digits(password),
                     check_len_password(password),
                     check_three_repeat_symbol(password)
                     ]

        check_all_num = []

        if check_all[0] == False:
            check_all_num.append(1)
        else:
            check_all_num.append(0)

        if check_all[1] == False:
            check_all_num.append(1)
        else:
            check_all_num.append(0)

        if check_all[2] == False:
            check_all_num.append(1)
        else:
            check_all_num.append(0)

        if check_all[3] == False:
            check_all_num.append(get_difference_len_password(password))
        else:
            check_all_num.append(0)

        if check_all[4] == False:
            check_all_num.append(get_repeat_quantity_if_len_is_ok(password))
        else:
            check_all_num.append(0)

        if all(check_all) == True:
            return 0
        elif check_all_num[3] == 0: # len is ok
            return max([check_all_num[4], sum(check_all_num[:3])])
        elif len(password) < 6:
            return max([check_all_num[3], sum(check_all_num[:3]), check_all_num[4]])
        elif len(password) > 20 and check_all_num[4] == 0: # len > 20 and repeat is ok
            return sum(check_all_num)
        elif len(password) > 20 and check_all_num[4] != 0: # len > 20 and repeat is not ok
            if get_quantity_changes_if_len_more_20_1(password) == len(password) - 20:
                return get_quantity_changes_if_len_more_20_1(password) + sum(check_all_num[:3])
            else:
                if min([get_quantity_changes_if_len_more_20_1(password),
                            get_quantity_changes_if_len_more_20_2(password),
                            get_quantity_changes_if_len_more_20_3(password)]) - len(password) + 20 < sum(check_all_num[:3]):
                    return min([get_quantity_changes_if_len_more_20_1(password),
                            get_quantity_changes_if_len_more_20_2(password),
                            get_quantity_changes_if_len_more_20_3(password)]) - len(password) + 20 + sum(check_all_num[:3])
                else:
                    return min([get_quantity_changes_if_len_more_20_1(password),
                            get_quantity_changes_if_len_more_20_2(password),
                            get_quantity_changes_if_len_more_20_3(password),
                            get_quantity_changes_if_len_more_20_4(password)])


res = Solution()

password = "aaaaaaaAAAAAA6666bbbbaaaaaaABBC" # 13 correct answer

print(res.strongPasswordChecker(password))
