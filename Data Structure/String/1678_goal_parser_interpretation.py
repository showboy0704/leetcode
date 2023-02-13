class Solution:
    def interpret(self, command: str) -> str:
        parsed = ''
        for i in range(len(command)):
            if command[i] == 'G':
                parsed += 'G'
            elif command[i:i+2] == '()':
                parsed += 'o'
            elif command[i:i+4] == '(al)':
                parsed += 'al'
        return parsed


if __name__ == '__main__':
    command = "G()(al)"
    print(f"{command}")
    print('----------Answer Below----------')
    print(Solution().interpret(command))
