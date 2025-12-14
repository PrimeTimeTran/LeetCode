class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res, parent, email_to_name, components = [], {}, {}, defaultdict(list)
        def union(x, y):
            parent[find(x)] = find(y)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Build the parent list using the accounts
        for account in accounts:
            name, emails = account[0], account[1:]
            
            # If the email isn't in the parent list, then set it as it's own parent.
            for email in emails:
                if email not in parent:
                    parent[email] = email
                    email_to_name[email] = name
            for i in range(1, len(emails)):
                union(emails[0], emails[i])

        for email in parent:
            root = find(email)
            components[root].append(email)
        for root, emails in components.items():
            res.append([email_to_name[root]] + sorted(emails))
        return res