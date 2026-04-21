class Solution:
    def __init__(self):
        self.link_map = defaultdict()
        self.index = 0
        self.domain = 'http://tinyurl.com/'

    def encode(self, strs: List[str]) -> str:
        self.index += 1
        self.link_map[str(self.index)] = strs
        # print(f'{self.domain}{self.index}')
        return f'{self.domain}{self.index}'
        

    def decode(self, s: str) -> List[str]:
        index = s.split('/')[-1]
        return self.link_map[index]
