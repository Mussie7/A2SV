class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dic = defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            domain = domain.split('.')
            
            for i in range(len(domain)):
                domain_dic[".".join(domain[i:])] += int(count)
        
        return [str(item[1]) + " " + item[0] for item in domain_dic.items()]
