def main():
    print("=== Campus Transport Allocation ===")
    import math
    
    r = int(input("Enter number of routes: "))
    
    demands = []
    print(f"\nEnter demand for {r} routes:")
    for i in range(r):
        d = int(input(f"Route {i+1} demand: "))
        demands.append(d)
    
    capacity = int(input("\nEnter bus capacity: "))
    available_buses = int(input("Enter total buses available (0 for unlimited): "))
    
    buses_needed_list = []
    unserved_list = []
    total_buses_needed = 0
    
    for i in range(r):
        demand = demands[i]
        needed = math.ceil(demand / capacity) if capacity > 0 else 0
        buses_needed_list.append(needed)
        total_buses_needed += needed
        
        served = needed * capacity
        unserved = 0
        if served < demand:
            unserved = demand - served
        unserved_list.append(unserved)
    
    print("\n========== TRANSPORT ALLOCATION ==========")
    for i in range(r):
        print(f"Route {i+1}: Demand {demands[i]} -> Buses Needed {buses_needed_list[i]}, Unserved {unserved_list[i]}")
    
    print(f"\nTotal Buses Needed: {total_buses_needed}")
    
    if available_buses > 0:
        print(f"Buses Available: {available_buses}")
        if total_buses_needed > available_buses:
            extra_unserved = 0
            for i in range(r):
                extra_unserved += unserved_list[i]
            shortage = total_buses_needed - available_buses
            extra_unserved += shortage * capacity
            print(f"Bus Shortage: {shortage}")
            print(f"Total Unserved Passengers: {extra_unserved}")
        else:
            print(f"Total Unserved Passengers: {sum(unserved_list)}")
            print("All Routes Served with Available Buses")
    else:
        print(f"Total Unserved Passengers: {sum(unserved_list)}")
    
    print("\n=== Allocation Complete ===")

main()
