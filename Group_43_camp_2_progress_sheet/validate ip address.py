class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        one, two, three = 'IPv4', 'IPv6', 'Neither'
        if '.' in queryIP:
            ip = queryIP.split('.')
            if len(ip) != 4:
                return three
            
            for chunk in ip:
                if not chunk.isdecimal() or (chunk[0] == '0' and len(chunk) > 1) or (not 0 <= int(chunk) <= 255):
                    return three
            
            return one

        elif ':' in queryIP:
            ip = queryIP.split(':')
            if len(ip) != 8:
                return three
            
            allowed = {'a','b','c','d','e','f','A','B','C','D','E','F','0','9','8','7','6','5','4','3','2','1'}
            for chunk in ip:
                if not 1 <= len(chunk) <= 4:
                    return three
                
                for char in chunk:
                    if char not in allowed:
                        return three
            
            return two                

        return three
