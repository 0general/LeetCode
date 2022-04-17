class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        visited = [False]*n
        answer = 0
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            num = limit - people[i]
            s,e = i+1,n-1
            ans = -1
            while s <= e:
                mid = (s+e)//2
                if people[mid] <= num and not visited[mid]:
                    ans = mid
                    s = mid + 1
                else:
                    e = mid - 1
            if ans != -1:
                visited[ans] = True
            answer += 1
        return answer
            