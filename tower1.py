def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return

    tower_of_hanoi(n-1, source, target, auxiliary)
    print("Move disk", n, "from", source, "to", target)
    tower_of_hanoi(n-1, auxiliary, source, target)

n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'B', 'C')
