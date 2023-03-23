class Solution:
    def makeIp(self, index, ip):
        if len(ip) == 3:
            rem = self.s[index:]
            if rem and int(rem) <= 255 and len(str(int(rem))) == len(rem):
                self.ips.append('.'.join(ip) + '.' + rem)
            return

        cur = ''
        for i in range(index, min(index + 3, len(self.s))):
            cur += self.s[i]
            if int(cur) > 255:
                break

            if (len(self.s) - i - 1) / (4 - len(ip) - 1) <= 3:
                ip.append(cur)
                self.makeIp(i+1, ip)
                ip.pop()
            
            if int(cur) == 0:
                break

    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
            
        self.s = s
        self.ips = []
        self.makeIp(0, [])
        return self.ips
