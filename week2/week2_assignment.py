print("===Task 1===")

def find_and_print(messages, current_station):
    # Define the green line stations and their positions
    green_line = {
        "Songshan": 0, "Nanjing Sanmin": 1, "Taipei Arena": 2, "Nanjing Fuxing": 3,
        "Songjiang Nanjing": 4, "Zhongshan": 5, "Beimen": 6, "Ximen": 7, "Xiaonanmen": 8,
        "Chiang Kai-Shek Memorial Hall": 9, "Guting": 10, "Taipower Building": 11,
        "Gongguan": 12, "Wanlong": 13, "Jingmei": 14, "Dapinglin": 15, "Qizhang": 16,
        "Xindian City Hall": 17, "Xindian": 18, "Xiaobitan": 16  # Xiaobitan requires transfer
    }
    # Find friend's stations
    friend_stations = {}
    for friend in messages:  
        message = messages[friend]
        for station in green_line:  
            if station in message:
                friend_stations[friend] = station
                break  

    # Find the current station's position
    current_station_value = green_line[current_station]

    # Calculate the nearest friend
    nearest_friend = None
    min_distance = float('inf')  # Start with a very large distance

    for friend in friend_stations:  # Check each friend's station
        station = friend_stations[friend]
        station_value = green_line[station]

        # Calculate distance
        if station == "Xiaobitan": 
            distance = abs(current_station_value - green_line["Qizhang"]) + 1
        else:
            distance = abs(current_station_value - station_value)

        # Check if this friend is closer
        if distance < min_distance:
            min_distance = distance
            nearest_friend = friend

    # Print the name of the nearest friend
    if nearest_friend:
        print(nearest_friend)

messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong")
find_and_print(messages, "Songshan")
find_and_print(messages, "Qizhang")
find_and_print(messages, "Ximen")
find_and_print(messages, "Xindian City Hall")

# Task 2
print("===Task 2===")

def book(consultants, hour, duration, criteria):
    # Initialize booked slots for consultants
    for consultant in consultants:
        if "booked_slots" not in consultant:
            consultant["booked_slots"] = []

    # Calculate the requested booking time range
    request_start = hour
    request_end = hour + duration

    # Find available consultants
    available_consultants = []
    for consultant in consultants:
        is_available = True
        for slot in consultant["booked_slots"]:
            if not (request_end <= slot["start"] or request_start >= slot["end"]):
                is_available = False
                break
        if is_available:
            available_consultants.append(consultant)

    # Find the best consultant based on criteria
    best_consultant = None
    if criteria == "price":
        best_price = None
        for consultant in available_consultants:
            if best_price is None or consultant["price"] < best_price:
                best_price = consultant["price"]
                best_consultant = consultant
    elif criteria == "rate":
        best_rate = None
        for consultant in available_consultants:
            if best_rate is None or consultant["rate"] > best_rate:
                best_rate = consultant["rate"]
                best_consultant = consultant


    # Book the consultant or print "No Service"
    if best_consultant is not None:
        best_consultant["booked_slots"].append({"start": request_start, "end": request_end})
        print(best_consultant["name"])
    else:
        print("No Service")

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800},
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John

# Task 3
print("===Task 3===")

def func(*data):
    # Extract middle names and map to the original names
    middle_names = []
    original = {}  

    for name in data:
        length = len(name)
        if length == 2:  
            middle_name = name[1]
        elif length == 4:  
            middle_name = name[2]
        elif length == 3:  
            middle_name = name[1]
        elif length == 5:
            middle_name = name[2]
        

        middle_names.append(middle_name)
        original[name] = middle_name

    # Count occurrences of each middle name
    counts = {}
    for middle_name in middle_names:
        if middle_name in counts:
            counts[middle_name] += 1
        else:
            counts[middle_name] = 1

    # Find names with unique middle names
    unique_names = [name for name, middle_name in original.items() if counts[middle_name] == 1]


    if unique_names:
        print(",".join(unique_names))
    else:
        print("沒有")  


func("彭大牆","陳王明雅","吳明") # print 彭大牆
func("郭靜雅","王立強","郭林靜宜","郭立恆","林花花") # print 林花花
func("郭宣雅","林靜宜","郭宣恆","林靜花") # print 沒有
func("郭宣雅","夏曼藍波安","郭宣恆") # print 夏曼藍波安

print("===Task 4===")
def get_number(index):
    ans = 0
    if index == 0:
        ans = 0
    elif index % 3 == 1:
        ans = 4+(index//3)*7
    elif index % 3 == 2:
        ans = 8+(index//3)*7
    elif index % 3 == 0:
        ans = (index//3)*7
    print(ans)

get_number(1)
get_number(5)
get_number(10)
get_number(30)
    
