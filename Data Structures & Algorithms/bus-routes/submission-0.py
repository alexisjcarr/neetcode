class Solution:
        def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
            if source == target:
                return 0

            adj_list, q = defaultdict(set), deque([(source, 0)])
            visited_stops, visited_buses = set(), set()

            for bus, route in enumerate(routes):
                for stop in route:
                    adj_list[stop].add(bus)

            while q:
                stop, route_len = q.popleft()

                if stop == target:
                    return route_len

                for bus in adj_list[stop]:
                    if bus not in visited_buses:
                        visited_buses.add(bus)

                        for stop in routes[bus]:
                            if stop not in visited_stops:
                                visited_stops.add(stop)
                                q.append((stop, route_len + 1))

            return -1

        