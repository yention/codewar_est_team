# https://leetcode.com/discuss/interview-question/982488/bettercom-phone-interview-badge-access
'''
    We are working on a security system for a badged-access room in our company's building.
    Given an ordered list of employees who used their badge to enter or exit the room, write
    a function that returns two collections:
    All employees who didnt use their badge while exiting the room - they recorded an enter
    without a matching exit. (All employees are required to leave the room before the log ends.)
    All employees who didnt use their badge while entering the room - they recorded an exit
    without a matching enter. (The room is empty when the log begins.)
    Each collection should contain no duplicates, regardless of how many times a given employee
    matches the criteria for belonging to it.

    badge_records_1 = [
    ["Martha", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "enter"],
    ["Paul", "enter"],
    ["Curtis", "exit"],
    ["Curtis", "enter"],
    ["Paul", "exit"],
    ["Martha", "enter"],
    ["Martha", "exit"],
    ["Jennifer", "exit"],
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Martha", "exit"],
    ]

    Expected output: ["Curtis", "Paul"], ["Martha", "Curtis"]
'''

badge_system = dict()
enter_error = []
exit_error = []

def security_updating(name:str, act: str):

    # if act == 'exit' and badge_system[name][-1] == 'enter' or act == 'enter' and badge_system[name][-1] == 'exit':
    #     pass
    if act == 'exit' and badge_system[name][-1] != 'enter':
        exit_error.append(name)
        # badge_system[name].append('enter')
    elif act == 'enter' and badge_system[name][-1] != 'exit':
        enter_error.append(name)

    badge_system[name].append(act)


def checking_system(name:str, acts:str):
    if name not in list(badge_system.keys()):
        badge_system[name] = ['enter', 'exit']
    security_updating(name, acts)


def find_out_list(ls:list):
    for check_point in ls:
        name = check_point[0]
        acts = check_point[1]
        checking_system(name, acts)


badge_records_1 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
]

if __name__ == '__main__':
    find_out_list(badge_records_1)
    print(badge_system)
    print(f'enter_error = {list(set(enter_error))}')
    print(f'exit_error = {list(set(exit_error))}')