date = input("Please enter date in MM/DD/YYYY format: ")

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

if len(date) == 10:
    month = int(date[0:2]) - 1
    newDate = "Here is the formatted date: " + months[month] + ' ' + date[3:5] + ',' + ' ' + date[6:10]
    print(newDate)

elif len(date) == 9 and date[2] != '/':
    month = int(date[0]) -1
    newDate = "Here is the formatted date: " + months[month] + ' ' + date[2:4] + ',' + ' ' + date[5:9]
    print(newDate)

elif len(date) == 9 and date[1] != '/':
    month = int(date[0:2]) - 1
    newDate = "Here is the formatted date: " + months[month] + ' 0' + date[3] + ', ' + date[5:9]
    print(newDate)

else:
    month = int(date[0]) - 1
    newDate = "Here is the formatted date: " + months[month] + ' 0' + date[2] + ', ' + date[4:8]
    print(newDate)

