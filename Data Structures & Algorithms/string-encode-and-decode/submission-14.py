class Solution:

    def encode(self, strs: List[str]) -> str:
        if (not strs):
            return ""
        sizes = []
        for i in strs:
            sizes.append(len(i))
        string = ""
        for i in sizes:
            string += str(i)
            string += ","
        string += "#"
        for i in strs:
            string += i
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        result = []
        value = str()
        i = 0
        # Get sizes list
        while (s[i] != "#"):
            while (s[i] != ","):
                value += s[i]
                i+=1
            if (value.isdigit()):
                sizes.append(int(value))
            else:
                sizes.append(len(value))
            value = str()
            i+=1
        start = s.index("#")
        print(sizes)
        count = 0
        for i in sizes:
            print(i)
            string = s[start+1+count:start+i+1+count]
            count+= i
            print(string)
            result.append(string)
        return result
            

            
