class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        s= set()
        for item in emails:
            local,domain = item.split("@")
            plus = local.find("+")
            if plus != -1:
                local = local[:plus]
            local = local.replace(".","")
            s.add(local + "@"+ domain)
        return len(s)