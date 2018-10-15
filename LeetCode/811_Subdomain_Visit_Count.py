class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count_map = dict()
        for pair in cpdomains:
            c = int(pair.split(' ')[0])
            domain = pair.split(' ')[1]
            domain_names = domain.split('.')
            l = ['.'.join(domain_names[i:]) for i in range(0, len(domain_names))]
            for i in l:
                count_map[i] = c if i not in count_map else count_map[i] + c
        return [str(count_map[key]) + ' ' + key for key in count_map]