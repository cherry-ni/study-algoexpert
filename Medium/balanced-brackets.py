# O(n) time | O(n) space
def balancedBrackets(string):
    # Write your code here.
    strings = list(string)
    stacks = []
    cases = ['(', ')', '[', ']', '{', '}']

    for s in strings:
        if s not in cases:
            continue

        if stacks:
            if stacks[-1] == '(' and  s == ')':
                stacks.pop()
            elif stacks[-1] == '[' and s == ']':
                stacks.pop()
            elif stacks[-1] == '{' and s == '}':
                stacks.pop()
            else:
                stacks.append(s)

        else:
            stacks.append(s)

    return not stacks

if __name__ == '__main__':
    print(balancedBrackets("(141[])(){waga}((51afaw))()hh()"))