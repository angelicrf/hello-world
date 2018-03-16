print("Sales Report\n\n")
print("{:15} {:>9} {:>9} {:>9} {:>9}".format("Reqion", "Q1","Q2","Q3","Q4"))
print ("{:15}{:10,.2f}{:10,.2f}{:10,.2f}{:10,.2f}".format ( "1" ,1540,2010,2450,1845 ) )
print ("{:15}{:10,.2f}{:10,.2f}{:10,.2f}{:10,.2f}".format ( "2" ,1130,1680,18470,1491 ) )
print ("{:15}{:10,.2f}{:10,.2f}{:10,.2f}{:10,.2f}".format ( "3" ,1580,2305,2710,1284 ) )
print ("{:15}{:10,.2f}{:10,.2f}{:10,.2f}{:10,.2f}".format ( "4" ,1105,4102,2391,1576 ) )

array=[
    [1540,2010,2450,1845],
    [1130,1168,1847,1491],
    [1580,2305,2710,1284],
    [1105,4102,2391,1576]
        ]

columnSums = [0] * len(array[0])
rowSums = [0] * len(array)

row_index = 0
for row in array:
    c_index = 0
    rowSums[row_index] = sum(row)
    for column in row:
        columnSums[c_index] += column
        c_index +=1
    row_index += 1

print("\nSales by region: ")
for r in range(len(rowSums)):
    print("Region",r+1,": ","{:10,.2f}".format(rowSums[r]))
print()
print("\nSales by quarters: ")
for v in range (len(columnSums)):
    print("Q",v+1,": ","{:10,.2f}".format(columnSums[v]))

total_sum= sum(map(sum,array))
print("\nTotal annual sales, all the regions: ","{:10,.2f}".format(total_sum))