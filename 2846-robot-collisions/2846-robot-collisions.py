class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        # https://leetcode.com/problems/robot-collisions/solutions/5468704/explanations-no-one-will-give-you-very-detailed-approach-extremely-simple-and-effective/
        n = len(positions)
        robots = [[positions[ind], healths[ind], directions[ind], ind] for ind in range(n)]
        robots.sort()
        stack = []

        for robot in robots:
            if robot[2] == "R" or not stack or stack[-1][2] == "L":
                stack.append(robot)
                continue

            if robot[2] == "L":
                add = True
                while stack and stack[-1][2] == "R" and add:
                    last_health = stack[-1][1]
                    if robot[1] > last_health:
                        stack.pop()
                        robot[1] -= 1
                    elif robot[1] < last_health:
                        stack[-1][1] -= 1
                        add = False
                    else:
                        stack.pop()
                        add = False

                if add:
                    stack.append(robot)

        return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]