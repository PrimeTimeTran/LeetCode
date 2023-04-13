class Solution:
    def simplifyPath(self, path: str) -> str:
        result = []
        for part in path.split('/'):
            print(part)
            if part == '..':
                if len(result):
                    result.pop()
            elif len(part) and part != '.':
                result.append(part)
        return '/' + '/'.join(result)