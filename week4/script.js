function findMiddleName (...data) {
    const middle_names = [];
    const original = {};

    for (let name of data) {
        let middle_name;
        if (name.length === 2) {
            middle_name = name[1];
        } else if (name.length === 3) {
            middle_name = name[1];
        } else if (name.length === 4) {
            middle_name = name[2];
        } else if (name.length === 5) {
            middle_name = name[2];
        }
        middle_names.push(middle_name);
        original[name] = middle_name;
    }

    const count = {};
    for (let middle_name of middle_names) {
        if (count[middle_name]) {
            count[middle_name] += 1;
        } else {
            count[middle_name] = 1;
        }
    }


    // Find names with unique middle names
    const uniqueNames = [];
    for (const name in original) {
        if (counts[original[name]] === 1) {
            uniqueNames.push(name);
        }
    }

    return 
}



// def find_and_print(messages, current_station):
// # your code here
//     green_line = {
//         "Songshan": 0, "Nanjing Sanmin": 1, "Taipei Arena": 2, "Nanjing Fuxing": 3,
//         "Songjiang Nanjing": 4, "Zhongshan": 5, "Beimen": 6, "Ximen": 7, "Xiaonanmen": 8,
//         "Chiang Kai-Shek Memorial Hall": 9, "Guting": 10, "Taipower Building": 11,
//         "Gongguan": 12, "Wanlong": 13, "Jingmei": 14, "Dapinglin": 15, "Qizhang": 16,
//         "Xindian City Hall": 17, "Xindian": 18, "Xiaobitan": 16  # Xiaobitan requires transfer
//     }
//     friend_location = {}
//     for friend, location_tip in messages.items():
//         for station, index in green_line.items():
//             if station in location_tip:
//                 friend_location[friend] = station
    

//     distance_to_friend = {}
//     for friend, station in friend_location.items():
//         if station == 'Xiaobitan':
//             distance_to_friend[friend] = abs(green_line[current_station] - green_line["Qizhang"] + 1)
//         else:
//             distance_to_friend[friend] = abs(green_line[current_station] - green_line[station])

//     compare = [distance for distance in distance_to_friend.values()]
//     compare.sort()

//     for friend, distance in distance_to_friend.items():
//         if compare[0] == distance:
//             closest = friend
//     print(closest)
const messages = {
  Leslie: "I'm at home near Xiaobitan station.",
  Bob: "I'm at Ximen MRT station.",
  Mary: "I have a drink near Jingmei MRT station.",
  Copper: "I just saw a concert at Taipei Arena.",
  Vivian: "I'm at Xindian station waiting for you.",
};

function findAndPrint(messages, currentStation) {
    const green_line = {
      "Songshan": 0,
      "Nanjing Sanmin": 1,
      "Taipei Arena": 2,
      "Nanjing Fuxing": 3,
      "Songjiang Nanjing": 4,
      "Zhongshan": 5,
      "Beimen": 6,
      "Ximen": 7,
      "Xiaonanmen": 8,
      "Chiang Kai-Shek Memorial Hall": 9,
      "Guting": 10,
      "Taipower Building": 11,
      "Gongguan": 12,
      "Wanlong": 13,
      "Jingmei": 14,
      "Dapinglin": 15,
      "Qizhang": 16,
      "Xindian City Hall": 17,
      "Xindian": 18,
      "Xiaobitan": 16
    };

    const friend_location = {}
    
}
