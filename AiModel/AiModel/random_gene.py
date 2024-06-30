


import random
import pandas as pd
from datetime import datetime, timedelta
# Sample data for districts and areas with latitude and longitude
districts_data = {
        "Center": [
                {"name": "Qalat", "latitude": 31.6116, "longitude": 65.7074},
                {"name": "Arghandab River", "latitude": 32.1091, "longitude": 66.9086},
                {"name": "Kandahar International Airport", "latitude": 31.5580, "longitude": 65.6625},
                {"name": "Kandahar Citadel (Arg-e-Kandahar)", "latitude": 31.5067, "longitude": 65.8472},
                {"name": "Mausoleum of Ahmad Shah Durrani", "latitude": 31.6283, "longitude": 65.7376},
                {"name": "Baba Wali Shrine", "latitude": 31.6122, "longitude": 65.7103},
                {"name": "Kandahar University", "latitude": 31.6539, "longitude": 65.6800},
                {"name": "Ziarat-e-Sakhi Baba", "latitude": 31.6231, "longitude": 65.6900},
                {"name": "Kandahar Central Mosque (Masjid-e-Kabir)", "latitude": 31.6383, "longitude": 65.6852},
                {"name": "Kandahar Museum", "latitude": 31.6100, "longitude": 65.7011},
                {"name": "Chahr Burjak", "latitude": 31.6180, "longitude": 65.7020},
                {"name": "Dahla Dam", "latitude": 31.5800, "longitude": 65.6150},
                {"name": "Spin Boldak (border town)", "latitude": 31.9500, "longitude": 65.5800},
                {"name": "Sarposa Prison", "latitude": 30.9000, "longitude": 66.2500},
                {"name": "Kandahar Stadium", "latitude": 31.6011, "longitude": 65.6967},
                {"name": "Aino Mina (residential area)", "latitude": 31.6100, "longitude": 65.6880},
                {"name": "Sarwar Khosti Mosque", "latitude": 31.5700, "longitude": 65.7090},
                {"name": "Haji Abdul Razziq Market", "latitude": 31.6250, "longitude": 65.7150},
                {"name": "Shahr-e Naw Park", "latitude": 31.6125, "longitude": 65.7070},
                {"name": "Mirwais Hospital", "latitude": 31.6120, "longitude": 65.7100},
                {"name": "Kandahar Public Library", "latitude": 31.6060, "longitude": 65.6980},
                {"name": "Shrine of Mirwais Hotak", "latitude": 31.6100, "longitude": 65.7010},
                {"name": "Mullah Omar's House", "latitude": 31.6120, "longitude": 65.7030},
                {"name": "Red Mosque (Masjid-e-Surkh)", "latitude": 31.6140, "longitude": 65.7075},
                {"name": "Provincial Governor's Office", "latitude": 31.6110, "longitude": 65.7050},
                {"name": "Shrine of Shah Agha", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Zarghona Ana High School", "latitude": 31.6150, "longitude": 65.7050},
                {"name": "Kandahar Agriculture Institute", "latitude": 31.6100, "longitude": 65.6980},
                {"name": "Kandahar City Center", "latitude": 31.6250, "longitude": 65.7150},
                {"name": "Old City (Shor Bazaar)", "latitude": 31.6160, "longitude": 65.7100},
                {"name": "Baba Sahib Shrine", "latitude": 31.6100, "longitude": 65.7080},
                {"name": "Shrine of Baba Jee", "latitude": 31.6300, "longitude": 65.6800},
                {"name": "Takht-e Safar (Hilltop park)", "latitude": 31.6350, "longitude": 65.6850},
                {"name": "Kandahar Industrial Park", "latitude": 31.6400, "longitude": 65.6750},
                {"name": "Tomb of Sher Ali Khan", "latitude": 31.5700, "longitude": 65.7450},
                {"name": "Shah Bazaar Mosque", "latitude": 31.6130, "longitude": 65.7040},
                {"name": "Baba Baba Shrine", "latitude": 31.6140, "longitude": 65.7060},
                {"name": "Juma Bazaar", "latitude": 31.6380, "longitude": 65.6820},
                {"name": "Shrine of Khoja Musafer", "latitude": 31.6130, "longitude": 65.7060},
                {"name": "Aino Mina Park", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Kandahar Central Park", "latitude": 31.5680, "longitude": 65.7120},
                {"name": "Malalai High School", "latitude": 31.6100, "longitude": 65.7010},
                {"name": "Kandahar Market Square", "latitude": 31.6140, "longitude": 65.7050},
                {"name": "Shrine of Sayyid Ali Akbar", "latitude": 31.6150, "longitude": 65.7070},
                {"name": "Mastoori High School", "latitude": 31.6150, "longitude": 65.7100},
                {"name": "Kandahar Red Crescent", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Kandahar Bank Headquarters", "latitude": 31.6180, "longitude": 65.7020},
                {"name": "Shahr-e Now Mosque", "latitude": 31.6160, "longitude": 65.7100},
                {"name": "Kandahar Fruit Market", "latitude": 31.6110, "longitude": 65.7100},
                {"name": "Kandahar Provincial Council", "latitude": 31.6130, "longitude": 65.7070},
                {"name": "Shrine of Pir Mohammad Jan", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Kandahar Police Headquarters", "latitude": 31.6150, "longitude": 65.7050},
                {"name": "Kandahar Radio Television (RTA)", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Kandahar Stadium (Sports Complex)", "latitude": 31.6180, "longitude": 65.7020},
                {"name": "Kandahar Women's Garden", "latitude": 31.6100, "longitude": 65.6880},
                {"name": "Shrine of Baba Sahib", "latitude": 31.6150, "longitude": 65.7050},
                {"name": "Kandahar School of Fine Arts", "latitude": 31.6300, "longitude": 65.6800},
                {"name": "Bibi Khadija Mosque", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Shrine of Mirwais Hotak", "latitude": 31.6100, "longitude": 65.7010},
                {"name": "Kandahar Institute of Modern Studies", "latitude": 31.6120, "longitude": 65.7030},
                {"name": "Shrine of Shah Agha", "latitude": 31.6250, "longitude": 65.7150},
                {"name": "Kandahar Public Health Directorate", "latitude": 31.6150, "longitude": 65.7050},
                {"name": "Kandahar Teacher Training College", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Regional Military Hospital", "latitude": 31.6200, "longitude": 65.7150},
                {"name": "Shrine of Baba Wali", "latitude": 31.6130, "longitude": 65.7040},
                {"name": "Kandahar Bagh-e Pul", "latitude": 31.6500, "longitude": 65.6900},
                {"name": "Kandahar Telecommunications Office", "latitude": 31.5800, "longitude": 65.7100},
                {"name": "Kandahar Vocational Training Center", "latitude": 31.6200, "longitude": 65.7150},
                {"name": "Kandahar Cultural Center", "latitude": 31.6230, "longitude": 65.7150},
                {"name": "Kandahar Agricultural Market", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Kandahar Technology Park", "latitude": 31.6100, "longitude": 65.7070},
                {"name": "Kandahar Railway Station", "latitude": 31.6300, "longitude": 65.6800},
                {"name": "Kandahar Post Office", "latitude": 31.6250, "longitude": 65.7000},
                {"name": "Kandahar Chamber of Commerce", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Fire Station", "latitude": 31.6200, "longitude": 65.7100},
                {"name": "Kandahar Electricity Department", "latitude": 31.6200, "longitude": 65.7150},
                {"name": "Kandahar Fish Market", "latitude": 31.6230, "longitude": 65.7150},
                {"name": "Kandahar Meat Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Dairy Market", "latitude": 31.6100, "longitude": 65.7070},
                {"name": "Kandahar Vegetable Market", "latitude": 31.6100, "longitude": 65.7070},
                {"name": "Kandahar Bakery Market", "latitude": 31.6130, "longitude": 65.7070},
                {"name": "Kandahar Carpet Market", "latitude": 31.6100, "longitude": 65.7070},
                {"name": "Kandahar Jewelry Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Textile Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Leather Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Handicrafts Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Furniture Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Electronics Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Auto Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Metal Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Construction Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Plastic Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Tools Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Pottery Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Book Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Flower Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Shoe Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Spice Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Kandahar Perfume Market", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Herat Gate (Herat Darwaza)", "latitude": 31.6100, "longitude": 65.7100},
                {"name": "Fruits Market Square (Meywa Mandi Chawk)", "latitude": 31.6100, "longitude": 65.6900},
                {"name": "Ghazi Square", "latitude": 31.6120, "longitude": 65.6940},
                {"name": "Shah Bazaar Square", "latitude": 31.6050, "longitude": 65.7050},
                {"name": "Khawja Bazaar Square", "latitude": 31.6090, "longitude": 65.6960},
                {"name": "Shorandam Square", "latitude": 31.6070, "longitude": 65.6990},
                {"name": "Chowk-e-Maidan", "latitude": 31.6200, "longitude": 65.6700},
                {"name": "Bazar-e-Khan Square", "latitude": 31.6080, "longitude": 65.7000},
                {"name": "Sarpoza Square", "latitude": 31.6110, "longitude": 65.6970},
                {"name": "Shaheedan Square", "latitude": 31.6130, "longitude": 65.7040},
                {"name": "Kandahar City Center Square", "latitude": 31.6050, "longitude": 65.7010},
                {"name": "Maiwand Gate Square", "latitude": 31.6100, "longitude": 65.7060},
                {"name": "Panjwayi Square", "latitude": 31.6140, "longitude": 65.7000},
                {"name": "Zhari Square", "latitude": 31.6000, "longitude": 65.7100},
                {"name": "Arghandab Square", "latitude": 31.6010, "longitude": 65.7110},
                {"name": "Daman Square", "latitude": 31.6120, "longitude": 65.6900},
                {"name": "Spin Boldak Square", "latitude": 31.6170, "longitude": 65.7020},
                {"name": "Nish Square", "latitude": 31.6050, "longitude": 65.6800},
                {"name": "Maroof Square", "latitude": 31.6100, "longitude": 65.6750},
                {"name": "Reg Square", "latitude": 31.6190, "longitude": 65.7070},
                {"name": "Ghorak Square", "latitude": 31.6220, "longitude": 65.7100},
                {"name": "Shurabak Square", "latitude": 31.6180, "longitude": 65.7120},
                {"name": "Miyan Nasheen Square", "latitude": 31.6250, "longitude": 65.7050},
                {"name": "Takht-e-Pol Square", "latitude": 31.6130, "longitude": 65.6950},
                {"name": "Maruf Square", "latitude": 31.6150, "longitude": 65.6980},
                {"name": "Mandisar Square", "latitude": 31.6200, "longitude": 65.6990},
                {"name": "Tiri Square", "latitude": 31.6160, "longitude": 65.7060},
                {"name": "Alokozai Square", "latitude": 31.6110, "longitude": 65.7020},
                {"name": "Mati Square", "latitude": 31.6090, "longitude": 65.6930},
                {"name": "Loy Wala Square", "latitude": 31.6070, "longitude": 65.7000},
                {"name": "Qalat Square", "latitude": 31.6140, "longitude": 65.6900},
                {"name": "Kash Square", "latitude": 31.6080, "longitude": 65.7050},
                {"name": "Salam Bazaar Square", "latitude": 31.6100, "longitude": 65.6960},
                {"name": "Janan Square", "latitude": 31.6130, "longitude": 65.6990},
                {"name": "Musa Square", "latitude": 31.6150, "longitude": 65.7000},
                {"name": "Barakzai Square", "latitude": 31.6070, "longitude": 65.7050},
                {"name": "Jalal Square", "latitude": 31.6080, "longitude": 65.6950},
                {"name": "Dand Square", "latitude": 31.6100, "longitude": 65.6980},
                {"name": "Shah Wali Kot Square", "latitude": 31.6140, "longitude": 65.6950},
                {"name": "Nawa Square", "latitude": 31.6050, "longitude": 65.6920},
                {"name": "Khakriz Square", "latitude": 31.6120, "longitude": 65.7040},
                {"name": "Gul Agha Square", "latitude": 31.6090, "longitude": 65.7030},
                {"name": "Mahmood Square", "latitude": 31.6170, "longitude": 65.6900},
                {"name": "Tariq Square", "latitude": 31.6180, "longitude": 65.6970},
                {"name": "Arbab Square", "latitude": 31.6100, "longitude": 65.7050},
                {"name": "Pach Square", "latitude": 31.6140, "longitude": 65.7000},
                {"name": "Farid Square", "latitude": 31.6110, "longitude": 65.6990},
                {"name": "Nasrat Square", "latitude": 31.6050, "longitude": 65.6900},
                {"name": "Latif Square", "latitude": 31.6090, "longitude": 65.7040},
                {"name": "Noor Square", "latitude": 31.6100, "longitude": 65.7020}
        ],
        "Kharkrez": [
                
            {"name": "Alam", "latitude": 31.94474, "longitude": 65.55319},
            {"name": "Aslam Kalay", "latitude": 31.96747, "longitude": 65.63512},
            {"name": "Azmat Kalay", "latitude": 32.14261, "longitude": 65.52635},
            {"name": "Baghak", "latitude": 32.0012, "longitude": 65.62588},
            {"name": "Bagh Khalil", "latitude": 31.96108, "longitude": 65.47107},
            {"name": "Baram Khail", "latitude": 32.01112, "longitude": 65.66342},
            {"name": "Barikzo", "latitude": 32.20074, "longitude": 65.47645},
            {"name": "Bay Himat", "latitude": 31.9138, "longitude": 65.47514},
            {"name": "Burna Qara", "latitude": 32.06982, "longitude": 65.46315},
            {"name": "Chahar Band", "latitude": 31.98742, "longitude": 65.63131},
            {"name": "Chahar Sang Kalan", "latitude": 31.96611, "longitude": 65.51578},
            {"name": "Chahar Sang Khurd", "latitude": 31.96442, "longitude": 65.52921},
            {"name": "Chargh Ya Charagah", "latitude": 32.08058, "longitude": 65.48347},
            {"name": "Chashma Ata", "latitude": 32.11539, "longitude": 65.50835},
            {"name": "China", "latitude": 32.02968, "longitude": 65.56344},
            {"name": "Chinar Baluch", "latitude": 31.97198, "longitude": 65.48169},
            {"name": "Chingay", "latitude": 31.97224, "longitude": 65.46578},
            {"name": "Chor Kalay", "latitude": 31.98681, "longitude": 65.64051},
            {"name": "Darwishan", "latitude": 31.99469, "longitude": 65.47597},
            {"name": "Din Mohammad Qanat", "latitude": 32.13842, "longitude": 65.52612},
            {"name": "Dokhana", "latitude": 31.87389, "longitude": 65.38022},
            {"name": "Faizullah Kalay", "latitude": 31.95067, "longitude": 65.66104},
            {"name": "Fatih Khan Kalay", "latitude": 31.95709, "longitude": 65.64925},
            {"name": "Ganda", "latitude": 31.96039, "longitude": 65.57424},
            {"name": "Ghulaman", "latitude": 31.95611, "longitude": 65.52432},
            {"name": "Ghulam Mohammad Kalay", "latitude": 31.96058, "longitude": 65.63709},
            {"name": "Haji Abad", "latitude": 32.16194, "longitude": 65.52864},
            {"name": "Haji Gul", "latitude": 31.96731, "longitude": 65.53151},
            {"name": "Karaiz Usman", "latitude": 32.18836, "longitude": 65.56612},
            {"name": "Karzalay", "latitude": 31.95919, "longitude": 65.53657},
            {"name": "Khaki", "latitude": 32.00153, "longitude": 65.57336},
            {"name": "Khosh Dar", "latitude": 31.91351, "longitude": 65.46674},
            {"name": "Khoshi", "latitude": 31.9639, "longitude": 65.53782},
            {"name": "Kido", "latitude": 31.94155, "longitude": 65.53856},
            {"name": "Lalak", "latitude": 31.80778, "longitude": 65.30309},
            {"name": "Landay", "latitude": 32.22094, "longitude": 65.54809},
            {"name": "Liti", "latitude": 31.90982, "longitude": 65.48317},
            {"name": "Loy Karaiz", "latitude": 32.19472, "longitude": 65.56704},
            {"name": "Mir Abad", "latitude": 31.90782, "longitude": 65.49371},
            {"name": "Musa Karaiz", "latitude": 31.79194, "longitude": 65.34895},
            {"name": "Nasir Karaiz", "latitude": 31.9893, "longitude": 65.5977},
            {"name": "Naw Abad", "latitude": 31.95156, "longitude": 65.56069},
            {"name": "Qanad Umari", "latitude": 32.00531, "longitude": 65.65552},
            {"name": "Sabzal Karaiz", "latitude": 31.85403, "longitude": 65.52051},
            {"name": "Sad Kalay", "latitude": 32.09321, "longitude": 65.52157},
            {"name": "Safid Khak", "latitude": 31.92918, "longitude": 65.42501},
            {"name": "Sang Riz", "latitude": 31.93868, "longitude": 65.41296},
            {"name": "Sanjid", "latitude": 32.17365, "longitude": 65.56415},
            {"name": "Saraw Karaiz", "latitude": 32.21129, "longitude": 65.52224},
            {"name": "Sar Gaw", "latitude": 31.91149, "longitude": 65.5037},
            {"name": "Sar Khar", "latitude": 32.03317, "longitude": 65.4542},
            {"name": "Sar Push", "latitude": 31.93655, "longitude": 65.46175},
            {"name": "Sayyid Karaiz", "latitude": 31.90107, "longitude": 65.4853},
            {"name": "Sayyidom", "latitude": 32.07123, "longitude": 65.46916},
            {"name": "Shabi", "latitude": 32.15496, "longitude": 65.51019},
            {"name": "Shairgha Hulya", "latitude": 31.95097, "longitude": 65.50544},
            {"name": "Shairgha Sufla", "latitude": 31.94938, "longitude": 65.51316},
            {"name": "Shams Kalay", "latitude": 31.96856, "longitude": 65.62621},
            {"name": "Shokhan Kalay", "latitude": 31.90228, "longitude": 65.49107},
            {"name": "Shutur Gardan", "latitude": 32.04817, "longitude": 65.49859},
            {"name": "Tawagay", "latitude": 32.16906, "longitude": 65.57242},
            {"name": "Tik", "latitude": 31.89078, "longitude": 65.46466},
            {"name": "Tura Namak", "latitude": 32.16985, "longitude": 65.5319},
            {"name": "Tur Kac", "latitude": 31.99158, "longitude": 65.64594},
            {"name": "Zarak", "latitude": 31.78842, "longitude": 65.25643},
            {"name": "Zil Abad", "latitude": 31.95598, "longitude": 65.51355},
            {"name": "Ziyarat Shah Maqsud Agha Markaz Woluswally", "latitude": 31.98177, "longitude": 65.47083}
    ],
        "Ghorak": [
            {"name": "Malmand", "latitude": 31.98997, "longitude": 64.98376},
            {"name": "Malmona Ya Mehran", "latitude": 32.01042, "longitude": 64.98311},
            {"name": "Shor Ab", "latitude": 32.00242, "longitude": 64.91901},
            {"name": "Tootak Junobi", "latitude": 31.98191, "longitude": 64.94008},
            {"name": "Tootak Shamaly", "latitude": 31.99964, "longitude": 64.93322}
        ],
        "Arghandab": [
            {"name": "Baba Sahib", "latitude": 31.6556, "longitude": 65.65716},
            {"name": "Baber", "latitude": 31.71417, "longitude": 65.67006},
            {"name": "Bagh Sarkari", "latitude": 31.71023, "longitude": 65.70621},
            {"name": "Barat Kalacha", "latitude": 31.68215, "longitude": 65.62052},
            {"name": "Changal", "latitude": 31.68392, "longitude": 65.67784},
            {"name": "Char Qoulba Hulya", "latitude": 31.69274, "longitude": 65.63969},
            {"name": "Char Qoulba Sufla", "latitude": 31.68034, "longitude": 65.64595},
            {"name": "Dahi Khushke", "latitude": 31.6685, "longitude": 65.67324},
            {"name": "Dahi Sabzi", "latitude": 31.63333, "longitude": 65.58941},
            {"name": "Dailawaran Kalacha", "latitude": 31.72848, "longitude": 65.71569},
            {"name": "Dorahi", "latitude": 31.6963, "longitude": 65.62724},
            {"name": "Faqeran Kalacha", "latitude": 31.62185, "longitude": 65.57887},
            {"name": "Gul Kalacha", "latitude": 31.70335, "longitude": 65.69124},
            {"name": "Haji Ali Mohammad Kalacha", "latitude": 31.62408, "longitude": 65.55323},
            {"name": "Haji Fatta Mohammad Kalacha", "latitude": 31.6679, "longitude": 65.61188},
            {"name": "Haji Malik Faiz Mohammad Kalacha", "latitude": 31.62594, "longitude": 65.56899},
            {"name": "Haji Nazar Kalacha", "latitude": 31.62807, "longitude": 65.53581},
            {"name": "Haji Noor Mohammad Kalacha", "latitude": 31.64427, "longitude": 65.61359},
            {"name": "Haji Sameh Kalacha", "latitude": 31.68513, "longitude": 65.62557},
            {"name": "Haji Satar Kalacha", "latitude": 31.71169, "longitude": 65.69652},
            {"name": "Haji Toor Kalacha", "latitude": 31.71683, "longitude": 65.69315},
            {"name": "Hajiyan Kala", "latitude": 31.64663, "longitude": 65.64577},
            {"name": "Hazera", "latitude": 31.67867, "longitude": 65.6111},
            {"name": "Jab Zar", "latitude": 31.68704, "longitude": 65.66904},
            {"name": "Jaza", "latitude": 31.75508, "longitude": 65.71737},
            {"name": "Jelawar", "latitude": 31.70137, "longitude": 65.6386},
            {"name": "Jeledan", "latitude": 31.64844, "longitude": 65.64183},
            {"name": "Khaleshak", "latitude": 31.65117, "longitude": 65.62467},
            {"name": "Khana Gerdab", "latitude": 31.78028, "longitude": 65.74407},
            {"name": "Khesrow Hulya", "latitude": 31.70335, "longitude": 65.66425},
            {"name": "Khesrow Sufla", "latitude": 31.69558, "longitude": 65.65386},
            {"name": "Khowja Malik Hulya", "latitude": 31.76676, "longitude": 65.75296},
            {"name": "Khowja Malik Sufla", "latitude": 31.75891, "longitude": 65.74816},
            {"name": "Kohak", "latitude": 31.64694, "longitude": 65.60743},
            {"name": "Landa Taben", "latitude": 31.67433, "longitude": 65.65401},
            {"name": "Langar", "latitude": 31.66075, "longitude": 65.66568},
            {"name": "Loy Menara Hulya", "latitude": 31.66441, "longitude": 65.61536},
            {"name": "Loy Menara Sufla", "latitude": 31.65905, "longitude": 65.60136},
            {"name": "Maranjan", "latitude": 31.74243, "longitude": 65.7288},
            {"name": "Mazreha", "latitude": 31.66496, "longitude": 65.67112},
            {"name": "Mazreha Habas", "latitude": 31.69734, "longitude": 65.69127},
            {"name": "Menara", "latitude": 31.66861, "longitude": 65.62871},
            {"name": "Mir Abkhoran", "latitude": 31.6756, "longitude": 65.67591},
            {"name": "Miyan Jowi", "latitude": 31.66274, "longitude": 65.65607},
            {"name": "Mohammad Yaqoub Kalacha", "latitude": 31.73288, "longitude": 65.7216},
            {"name": "Nagahan", "latitude": 31.64312, "longitude": 65.58211},
            {"name": "Nar Rowza", "latitude": 31.65052, "longitude": 65.58087},
            {"name": "Noor Mohammad Khan Kalacha", "latitude": 31.68594, "longitude": 65.63881},
            {"name": "Noorzay Karaiz", "latitude": 31.75123, "longitude": 65.79419},
            {"name": "Paitow", "latitude": 31.63077, "longitude": 65.54172},
            {"name": "Sar Dahi Hulya", "latitude": 31.72003, "longitude": 65.70941},
            {"name": "Sar Dahi Sufla", "latitude": 31.71033, "longitude": 65.68606},
            {"name": "Sayidan", "latitude": 31.62707, "longitude": 65.58788},
            {"name": "Sayidan Kalacha", "latitude": 31.720315, "longitude": 65.684435},
            {"name": "Sediqe Kalacha", "latitude": 31.76929, "longitude": 65.77257},
            {"name": "Shahtori", "latitude": 31.77378, "longitude": 65.73665},
            {"name": "Shaikh Chala Hulya", "latitude": 31.69284, "longitude": 65.68839},
            {"name": "Shaikh Chala Sufla", "latitude": 31.69213, "longitude": 65.66889},
            {"name": "Shair Ahmad", "latitude": 31.63167, "longitude": 65.58224},
            {"name": "Shewon Hulya", "latitude": 31.73886, "longitude": 65.70289},
            {"name": "Shewon Sufla", "latitude": 31.72113, "longitude": 65.67626},
            {"name": "Shewon Wasate", "latitude": 31.7294, "longitude": 65.68604},
            {"name": "Taben", "latitude": 31.67525, "longitude": 65.64002},
            {"name": "Taben Sufla", "latitude": 31.67098, "longitude": 65.63372},
            {"name": "Yatemak Hulya", "latitude": 31.76832, "longitude": 65.74838},
            {"name": "Yatemak Sufla", "latitude": 31.75975, "longitude": 65.74089}
    ],
        "Maruf": [
                
            {"name": "Abdul Qadir Isahq Ghat Kalay", "latitude": 31.51428, "longitude": 67.46256},
            {"name": "Khatni Zay", "latitude": 31.69846, "longitude": 67.22481},
            {"name": "Mullah Khel Qala Rashid", "latitude": 31.5132, "longitude": 67.50817},
            {"name": "Rab Kalay Akhund", "latitude": 31.50819, "longitude": 67.47925},
            {"name": "Sayyid Wali Kalay", "latitude": 31.70387, "longitude": 67.3064},
            {"name": "Warghar Kalay", "latitude": 31.58601, "longitude": 67.39402}

        ],
        "Spin Boldak": [
                {
            "name": "Abdul Hakim Kalay Dad Mohammad Kalay",
            "latitude": 31.09409,
            "longitude": 66.62089
        },
        {
            "name": "Abdul Karim",
            "latitude": 31.06422,
            "longitude": 66.41362
        },
        {
            "name": "Abdullah Jan",
            "latitude": 31.2949,
            "longitude": 65.95549
        },
        {
            "name": "Abdul Salam Kalay",
            "latitude": 30.98127,
            "longitude": 66.39733
        },
        {
            "name": "Abdul Wahed Kalay",
            "latitude": 30.99859,
            "longitude": 66.36053
        },
        {
            "name": "Abdul Wali Kalay",
            "latitude": 30.97748,
            "longitude": 66.51325
        },
        {
            "name": "Abdul Zai Kalay",
            "latitude": 31.22386,
            "longitude": 65.96891
        },
        {
            "name": "Aka Khail",
            "latitude": 31.33647,
            "longitude": 65.98369
        },
        {
            "name": "Akhond Kaka Kalay",
            "latitude": 31.18091,
            "longitude": 66.49625
        },
        {
            "name": "Akhond Zada Kalay",
            "latitude": 31.31511,
            "longitude": 65.94611
        },
        {
            "name": "Akhtar Mohammad Kalay",
            "latitude": 31.016725,
            "longitude": 66.277505
        },
        {
            "name": "Ali Jan",
            "latitude": 30.99404,
            "longitude": 66.16721
        },
        {
            "name": "Alki Chena",
            "latitude": 31.17538,
            "longitude": 66.63021
        },
        {
            "name": "Amir Mohammad Khan",
            "latitude": 31.05513,
            "longitude": 66.00858
        },
        {
            "name": "Amir Tana Baidak",
            "latitude": 31.22646,
            "longitude": 66.26124
        },
        {
            "name": "Anawi Kalay",
            "latitude": 31.16309,
            "longitude": 66.39033
        },
        {
            "name": "Anzer Gay",
            "latitude": 31.22137,
            "longitude": 66.65192
        },
        {
            "name": "Anzergay Kalay",
            "latitude": 31.22685,
            "longitude": 66.45107
        },
        {
            "name": "Aqa Mohammad Jalal Jabar Kalay Qahraman",
            "latitude": 30.86697,
            "longitude": 66.25399
        },
        {
            "name": "Azam Zai Kalay",
            "latitude": 31.15864,
            "longitude": 66.40648
        },
        {
            "name": "Babek Sahib",
            "latitude": 31.08772,
            "longitude": 66.23055
        },
        {
            "name": "Badam Kalay",
            "latitude": 31.01442,
            "longitude": 66.19531
        },
        {
            "name": "Badeen Zai",
            "latitude": 31.27532,
            "longitude": 66.55164
        },
        {
            "name": "Baesh Kalay",
            "latitude": 31.1921,
            "longitude": 66.63156
        },
        {
            "name": "Bahader Zai",
            "latitude": 31.07748,
            "longitude": 66.16835
        },
        {
            "name": "Bahder Zai",
            "latitude": 31.1852,
            "longitude": 66.33264
        },
        {
            "name": "Baiz Anzergay",
            "latitude": 31.20192,
            "longitude": 66.67081
        },
        {
            "name": "Bakari Kalay Khaday Rahim Kalay",
            "latitude": 30.90784,
            "longitude": 66.29385
        },
        {
            "name": "Baqi Kalay",
            "latitude": 30.991955,
            "longitude": 66.37198
        },
        {
            "name": "Barakat Kalay Mullah Dorani",
            "latitude": 31.16358,
            "longitude": 66.64855
        },
        {
            "name": "Barjan Kalay",
            "latitude": 31.2824,
            "longitude": 65.94138
        },
        {
            "name": "Beash Khala",
            "latitude": 31.18864,
            "longitude": 66.61099
        },
        {
            "name": "Belal Abad",
            "latitude": 30.97183,
            "longitude": 66.4466
        },
        {
            "name": "Burj Kalay",
            "latitude": 31.08072,
            "longitude": 66.45385
        },
        {
            "name": "Chaghri Kalay",
            "latitude": 31.33072,
            "longitude": 65.88849
        },
        {
            "name": "Chahel Gazi",
            "latitude": 31.20743,
            "longitude": 66.69027
        },
        {
            "name": "Chawdaily Pote",
            "latitude": 30.97383,
            "longitude": 66.40704
        },
        {
            "name": "Dabari",
            "latitude": 31.12811,
            "longitude": 66.24789
        },
        {
            "name": "Dabari Burj Kala",
            "latitude": 31.17881,
            "longitude": 66.35438
        },
        {
            "name": "Dadzai Kalay",
            "latitude": 31.08392,
            "longitude": 66.51004
        },
        {
            "name": "Dahi Jalat Kalay",
            "latitude": 31.07723,
            "longitude": 66.53776
        },
        {
            "name": "Dahi Wari Kalay",
            "latitude": 31.179,
            "longitude": 66.48504
        },
        {
            "name": "Daman",
            "latitude": 31.21097,
            "longitude": 66.62586
        },
        {
            "name": "Dokhuno Kalay Dost Mohammad",
            "latitude": 31.22891,
            "longitude": 66.11686
        },
        {
            "name": "Fazel Karam Kalay",
            "latitude": 31.09321,
            "longitude": 66.53949
        },
        {
            "name": "Galgari Matroka",
            "latitude": 31.26813,
            "longitude": 66.37005
        },
        {
            "name": "Galgari Tawa",
            "latitude": 31.26131,
            "longitude": 66.37363
        },
        {
            "name": "Garandi Kalay",
            "latitude": 31.06545,
            "longitude": 66.39038
        },
        {
            "name": "Ghulam Nabi",
            "latitude": 31.29748,
            "longitude": 65.94621
        },
        {
            "name": "Ghulam Sarwar",
            "latitude": 31.13903,
            "longitude": 65.97877
        },
        {
            "name": "Goranda Kalay",
            "latitude": 31.20211,
            "longitude": 66.43732
        },
        {
            "name": "Gul Kalay",
            "latitude": 31.00739,
            "longitude": 66.36702
        },
        {
            "name": "Gul Mir Jan Darman",
            "latitude": 31.05711,
            "longitude": 66.14545
        },
        {
            "name": "Gul Mohammad Ghulam Haidar Kalay",
            "latitude": 31.1167,
            "longitude": 66.59943
        },
        {
            "name": "Gul Mohammad Ya Nazar Mohammad",
            "latitude": 30.95714,
            "longitude": 66.27658
        },
        {
            "name": "Gulozai",
            "latitude": 31.14012,
            "longitude": 66.47721
        },
        {
            "name": "Haji Abdul Razaq Kalay",
            "latitude": 30.94238,
            "longitude": 66.3956
        },
        {
            "name": "Haji Abdul Wahed Kalay",
            "latitude": 30.96001,
            "longitude": 66.32956
        },
        {
            "name": "Haji Ahmad Khan Kalay Zaren",
            "latitude": 31.04864,
            "longitude": 66.33775
        },
        {
            "name": "Haji Fazil",
            "latitude": 31.18528,
            "longitude": 65.9473
        },
        {
            "name": "Haji Ghulam Haidar Khan",
            "latitude": 31.00289,
            "longitude": 66.37157
        },
        {
            "name": "Haji Habibullah Ghaows Mohammad",
            "latitude": 31.04034,
            "longitude": 66.38854
        },
        {
            "name": "Haji Ibrahim Kalay",
            "latitude": 31.1456,
            "longitude": 66.27891
        },
        {
            "name": "Haji Isahq Zai",
            "latitude": 30.97391,
            "longitude": 66.39847
        },
        {
            "name": "Haji Jalal Kalay",
            "latitude": 31.11472,
            "longitude": 66.62921
        },
        {
            "name": "Haji Jandu",
            "latitude": 31.23532,
            "longitude": 66.17175
        },
        {
            "name": "Haji Khairo",
            "latitude": 30.96154,
            "longitude": 66.46219
        },
        {
            "name": "Haji Kotan",
            "latitude": 31.04333,
            "longitude": 66.45161
        },
        {
            "name": "Haji Mandi Kalay",
            "latitude": 31.07865,
            "longitude": 66.40423
        },
        {
            "name": "Haji Mir Ahmad Khan",
            "latitude": 31.14455,
            "longitude": 65.95494
        },
        {
            "name": "Haji Mir Wali Kalay",
            "latitude": 31.02107,
            "longitude": 66.43627
        },
        {
            "name": "Haji Mir Zahe",
            "latitude": 30.84708,
            "longitude": 66.26198
        },
        {
            "name": "Haji Mohammad Ekhlas Kalay",
            "latitude": 30.83704,
            "longitude": 66.30892
        },
        {
            "name": "Haji Mohammad Fazel Mohammad Kalay",
            "latitude": 31.06793,
            "longitude": 66.41506
        },
        {
            "name": "Haji Mohammad Khan",
            "latitude": 31.11063,
            "longitude": 66.04825
        },
        {
            "name": "Haji Nasrula Kalay",
            "latitude": 31.18278,
            "longitude": 65.95872
        },
        {
            "name": "Haji Nazar Mohammad Kalay",
            "latitude": 31.24035,
            "longitude": 65.97214
        },
        {
            "name": "Haji Shah Mohammad Darman",
            "latitude": 31.04877,
            "longitude": 66.14394
        },
        {
            "name": "Haji Shahtol Kalay",
            "latitude": 31.13158,
            "longitude": 66.34369
        },
        {
            "name": "Haji Shair Jan Kalay",
            "latitude": 30.86229,
            "longitude": 66.28638
        },
        {
            "name": "Haji Shir Kalay",
            "latitude": 31.27481,
            "longitude": 65.95602
        },
        {
            "name": "Haji Wakil",
            "latitude": 31.00968,
            "longitude": 66.13851
        },
        {
            "name": "Haji Wazer Kalay",
            "latitude": 31.07272,
            "longitude": 66.24693
        },
        {
            "name": "Haji Yaqoub",
            "latitude": 30.96241,
            "longitude": 66.20556
        },
        {
            "name": "Haji Zarif Bole",
            "latitude": 31.11323,
            "longitude": 66.28196
        },
        {
            "name": "Halam Khan Zai",
            "latitude": 31.17949,
            "longitude": 66.46051
        },
        {
            "name": "Hanefi Kalay Dawod Khan Kalay",
            "latitude": 30.72177,
            "longitude": 66.15612
        },
        {
            "name": "Hanifya Kalay",
            "latitude": 31.04237,
            "longitude": 66.38145
        },
        {
            "name": "Haq Dad Kalay",
            "latitude": 31.21845,
            "longitude": 65.97121
        },
        {
            "name": "Hassan Zai Paro Karaiz",
            "latitude": 31.17073,
            "longitude": 66.34739
        },
        {
            "name": "Hassan Zay",
            "latitude": 31.18072,
            "longitude": 65.97625
        },
        {
            "name": "Hussain Zai",
            "latitude": 31.29554,
            "longitude": 66.4414
        },
        {
            "name": "Hussain Zai Namaki Kalay",
            "latitude": 31.09913,
            "longitude": 66.3798
        },
            {"name": "Iqbal Khan Kalay", "latitude": 31.06462, "longitude": 66.4286},
            {"name": "Isahq Zai", "latitude": 30.99704, "longitude": 66.13338},
            {"name": "Jangal Sar Haji Shadi Zai", "latitude": 31.03125, "longitude": 66.13897},
            {"name": "Jonobi Marsani Sangen", "latitude": 31.13068, "longitude": 66.65729},
            {"name": "Kachi Kaku Zay", "latitude": 31.0363, "longitude": 66.03235},
            {"name": "Kader Kalay", "latitude": 31.0331, "longitude": 66.23289},
            {"name": "Kala Gay", "latitude": 31.15318, "longitude": 66.33902},
            {"name": "Kamp Madena", "latitude": 30.9736, "longitude": 66.42778},
            {"name": "Kamp Mahjeren Yaro", "latitude": 31.00269, "longitude": 66.38688},
            {"name": "Kamp Nowi Hawame", "latitude": 30.99887, "longitude": 66.40164},
            {"name": "Kamp Shalo Ya Alla Dukhtar", "latitude": 30.97672, "longitude": 66.41484},
            {"name": "Kase Kalay", "latitude": 31.12503, "longitude": 66.5843},
            {"name": "Khada Nazar", "latitude": 30.97337, "longitude": 66.37629},
            {"name": "Khaday Rahem", "latitude": 30.9818, "longitude": 66.37278},
            {"name": "Khairan", "latitude": 31.02967, "longitude": 66.17315},
            {"name": "Khair Mohammad Kalay Loara Akhtar Zaye", "latitude": 31.26928, "longitude": 66.40117},
            {"name": "Khal Gay", "latitude": 31.14613, "longitude": 66.31677},
            {"name": "Khalifa Kalay", "latitude": 30.98677, "longitude": 66.50761},
            {"name": "Khal Zai", "latitude": 31.25997, "longitude": 66.51419},
            {"name": "Khan Sheren Kalay Mohammad Hawaz", "latitude": 30.89094, "longitude": 66.29415},
            {"name": "Khar Bote", "latitude": 31.11016, "longitude": 66.58012},
            {"name": "Khawaza Band Bala Kalay", "latitude": 31.18492, "longitude": 66.31868},
            {"name": "Khowja Bakhtyar Choda", "latitude": 31.14268, "longitude": 66.40046},
            {"name": "Khuday Dad", "latitude": 31.11282, "longitude": 66.02787},
            {"name": "Khuday Rahm Wecha Kola", "latitude": 31.02328, "longitude": 66.60599},
            {"name": "Kunje So Haji Ghafor", "latitude": 31.04005, "longitude": 66.57252},
            {"name": "Kushta Kano Zai", "latitude": 31.24292, "longitude": 66.37268},
            {"name": "Kushta Mil Haji Madad Kalay", "latitude": 31.08695, "longitude": 66.03967},
            {"name": "Lakari", "latitude": 31.17444, "longitude": 66.59934},
            {"name": "Landi Kalay", "latitude": 31.09204, "longitude": 66.56967},
            {"name": "Landi Karaiz", "latitude": 31.18383, "longitude": 66.43686},
            {"name": "Madeyan Kalay", "latitude": 31.12012, "longitude": 66.41196},
            {"name": "Mahbob Khan Karaiz", "latitude": 31.15088, "longitude": 66.38957},
            {"name": "Majlis Karaiz Kalay", "latitude": 31.23623, "longitude": 65.98787},
            {"name": "Malik Mohammadulldin", "latitude": 31.02924, "longitude": 65.97752},
            {"name": "Malik Zai", "latitude": 31.01695, "longitude": 66.3268},
            {"name": "Markaz Loy Karaiz", "latitude": 31.17724, "longitude": 66.49005},
            {"name": "Markaz Wolluswaly", "latitude": 31.31805, "longitude": 65.9628},
            {"name": "Markaz Woluswally", "latitude": 31.00712, "longitude": 66.40204},
            {"name": "Marsen Zai", "latitude": 31.10363, "longitude": 66.34362},
            {"name": "Masala", "latitude": 31.18195, "longitude": 66.66638},
            {"name": "Mashengazi", "latitude": 31.1128, "longitude": 66.50104},
            {"name": "Masheng Zai", "latitude": 31.08837, "longitude": 66.38918},
            {"name": "Mashi Kala", "latitude": 31.07045, "longitude": 66.32869},
            {"name": "Matan Zai", "latitude": 31.08765, "longitude": 66.48719},
            {"name": "Mawladad Kalay", "latitude": 31.03405, "longitude": 66.35722},
            {"name": "Mawla Zay Pupal Zayi Kalay", "latitude": 31.19992, "longitude": 66.15376},
            {"name": "Mese Zai Khuday Dad", "latitude": 31.02421, "longitude": 66.55551},
            {"name": "Mikhanzai", "latitude": 30.98251, "longitude": 66.28367},
            {"name": "Mil Karaiz", "latitude": 31.19463, "longitude": 66.06323},
            {"name": "Mir Geyan", "latitude": 31.04802, "longitude": 66.27583},
            {"name": "Mir Kalay", "latitude": 31.15151, "longitude": 66.36332},
            {"name": "Mohammad Ahzam Wa Abdul Jabar Kalay", "latitude": 30.97862, "longitude": 66.4039},
            {"name": "Mohammad Ayoub Kalay", "latitude": 30.98142, "longitude": 66.19782},
            {"name": "Mohammad Azam Baqi Kalay", "latitude": 30.9792, "longitude": 66.5563},
            {"name": "Mohammad Azam Kalay", "latitude": 31.03222, "longitude": 66.40838},
            {"name": "Mohammad Mir Kalay", "latitude": 31.04429, "longitude": 66.42244},
            {"name": "Mohammad Zahir Wa Gul Kalay", "latitude": 31.0095, "longitude": 66.161},
            {"name": "Momin Khan Kalay", "latitude": 31.23057, "longitude": 65.98254},
            {"name": "Mullah Abdul Razaq", "latitude": 31.03011, "longitude": 66.36376},
            {"name": "Mullah Mohammad Umar Kalay", "latitude": 31.02096, "longitude": 66.36341},
            {"name": "Mullah Nasruddin", "latitude": 31.28596, "longitude": 66.41046},
            {"name": "Mullah Wali Waled", "latitude": 31.17788, "longitude": 66.57645},
            {"name": "Mussa Khan", "latitude": 30.98597, "longitude": 66.36189},
            {"name": "Mussa Khan Kalay Taj Mohammad", "latitude": 31.04407, "longitude": 66.38796},
            {"name": "Nabi Dad Kalay", "latitude": 31.06839, "longitude": 66.37212},
            {"name": "Nader Hamid Zai", "latitude": 30.98682, "longitude": 66.24069},
            {"name": "Naido Kalay", "latitude": 31.11724, "longitude": 66.56772},
            {"name": "Nasrat Afghan Kalay", "latitude": 30.99603, "longitude": 66.43984},

    ],

        "Daman": [
            {"name": "Ahzam Kalay", "latitude": 31.64422, "longitude": 65.94175},
            {"name": "Akhund Zada Kalay", "latitude": 31.71812, "longitude": 66.18801},
            {"name": "Akhund Zada Sahib", "latitude": 31.7031, "longitude": 66.167},
            {"name": "Ali Abad", "latitude": 31.7387, "longitude": 65.92142},
            {"name": "Ali Zay", "latitude": 31.42325, "longitude": 65.92299},
            {"name": "Anzirgay", "latitude": 31.77652, "longitude": 65.97012},
            {"name": "Arhat Kalay", "latitude": 31.68236, "longitude": 66.01269},
            {"name": "Awme", "latitude": 31.76115, "longitude": 65.93248},
            {"name": "Bariki", "latitude": 31.69023, "longitude": 65.96822},
            {"name": "Bashar Kalay", "latitude": 31.42243, "longitude": 65.95309},
            {"name": "Bawary", "latitude": 31.69753, "longitude": 65.88339},
            {"name": "Baz Mohammad Khan Kalay", "latitude": 31.64663, "longitude": 65.94916},
            {"name": "Biyaban Dara", "latitude": 31.44774, "longitude": 65.92235},
            {"name": "Biyabani Kalay", "latitude": 31.62404, "longitude": 66.15417},
            {"name": "Burj", "latitude": 31.77743, "longitude": 66.03359},
            {"name": "Bustan", "latitude": 31.66082, "longitude": 65.88018},
            {"name": "Chahar Band", "latitude": 31.70889, "longitude": 65.9515},
            {"name": "Daman Markaz Wolluswaly", "latitude": 31.61877, "longitude": 65.89522},
            {"name": "Dayi Kalay", "latitude": 31.45528, "longitude": 65.92003},
            {"name": "Gari Kalay", "latitude": 31.74175, "longitude": 66.00381},
            {"name": "Ghaybi Qalacha", "latitude": 31.63002, "longitude": 65.85702},
            {"name": "Haino Kalay", "latitude": 31.6356, "longitude": 65.84224},
            {"name": "Haji Dahi", "latitude": 31.40741, "longitude": 65.88261},
            {"name": "Haji Ghafar", "latitude": 31.62136, "longitude": 65.92718},
            {"name": "Haji Lal Bik", "latitude": 31.72059, "longitude": 65.99262},
            {"name": "Haji Shir Kalay", "latitude": 31.41146, "longitude": 65.93457},
            {"name": "Hakim Kalay", "latitude": 31.4741, "longitude": 65.88325},
            {"name": "Hijran Kalay", "latitude": 31.70905, "longitude": 65.88173},
            {"name": "Hindo Karaiz", "latitude": 31.75218, "longitude": 66.23253},
            {"name": "Hudud Kalacha", "latitude": 31.64268, "longitude": 65.96854},
            {"name": "Kakaranu Kalacha", "latitude": 31.54164, "longitude": 65.90783},
            {"name": "Khairati", "latitude": 31.77808, "longitude": 65.94938},
            {"name": "Khaliq Dad", "latitude": 31.63602, "longitude": 65.89095},
            {"name": "Khan Mohammad Wa Sher Mohammad Karaiz", "latitude": 31.64266, "longitude": 66.20167},
            {"name": "Khwazhkay Kalay", "latitude": 31.63066, "longitude": 66.1333},
            {"name": "Kuchni Karaiz", "latitude": 31.72753, "longitude": 66.05611},
            {"name": "Kumana Karaiz", "latitude": 31.70117, "longitude": 66.01724},
            {"name": "Kushta Mir Sanzai Kalacha", "latitude": 31.66442, "longitude": 66.12243},
            {"name": "Kushta Mir Sanzai Kalay", "latitude": 31.62683, "longitude": 66.09825},
            {"name": "Landi Kalay", "latitude": 31.46148, "longitude": 65.91794},
            {"name": "Landi Karaiz", "latitude": 31.65167, "longitude": 65.91918},
            {"name": "Maduzay Kalay", "latitude": 31.57442, "longitude": 66.04057},
            {"name": "Makyan", "latitude": 31.41604, "longitude": 66.01852},
            {"name": "Malakhi Ghundi", "latitude": 31.43873, "longitude": 65.95446},
            {"name": "Malang Karaiz", "latitude": 31.64739, "longitude": 65.83752},
            {"name": "Mandisyar", "latitude": 31.54531, "longitude": 65.8548},
            {"name": "Mawlana Kalay", "latitude": 31.63437, "longitude": 66.15359},
            {"name": "Mishi", "latitude": 31.75823, "longitude": 65.9604},
            {"name": "Miyana Jakan", "latitude": 31.74163, "longitude": 66.13016},
            {"name": "Miyanji Kalay", "latitude": 31.68413, "longitude": 66.09146},
            {"name": "Mohammad Anwar Kalacha", "latitude": 31.57257, "longitude": 65.87464},
            {"name": "Mohmand", "latitude": 31.59001, "longitude": 65.89965},
            {"name": "Mullayan", "latitude": 31.6292, "longitude": 65.87842},
            {"name": "Murghankicha", "latitude": 31.53345, "longitude": 65.96764},
            {"name": "Najuyi", "latitude": 31.61007, "longitude": 65.9708},
            {"name": "Nawi Dahi", "latitude": 31.513855, "longitude": 65.92016},
            {"name": "Nazar Kalacha", "latitude": 31.68949, "longitude": 65.95133},
            {"name": "Paiy Jakan", "latitude": 31.73592, "longitude": 66.11234},
            {"name": "Pangay", "latitude": 31.60846, "longitude": 66.02677},
            {"name": "Popal Zay Mohammad Rafiq Kalacha", "latitude": 31.5281, "longitude": 65.85497},
            {"name": "Poul Tarank", "latitude": 31.55792, "longitude": 65.84438},
            {"name": "Sahib Zada Kalacha", "latitude": 31.6099, "longitude": 65.87459},
            {"name": "Salam Kalacha", "latitude": 31.66451, "longitude": 65.93479},
            {"name": "Samul Zay", "latitude": 31.71295, "longitude": 66.21022},
            {"name": "Sangar Ganj", "latitude": 31.67542, "longitude": 65.96808},
            {"name": "Sara Kala", "latitude": 31.64963, "longitude": 66.17465},
            {"name": "Sar Jakan", "latitude": 31.76176, "longitude": 66.1342},
            {"name": "Sar Pali Kalay", "latitude": 31.73858, "longitude": 65.95276},
            {"name": "Saydan Kalacha", "latitude": 31.62333, "longitude": 66.01452},
            {"name": "Sayid Abad", "latitude": 31.68287, "longitude": 66.16897},
            {"name": "Sayyid Akbar Shah", "latitude": 31.74483, "longitude": 66.2686},
            {"name": "Sayyidan Kalay", "latitude": 31.45397, "longitude": 65.9332},
            {"name": "Shah Dad Kalay", "latitude": 31.6763, "longitude": 65.94024},
            {"name": "Shakur Kalay", "latitude": 31.69816, "longitude": 65.82682},
            {"name": "Sher Ali Khan", "latitude": 31.73152, "longitude": 66.26586},
            {"name": "Spin Waya", "latitude": 31.63265, "longitude": 66.0132},
            {"name": "Sur Karaiz", "latitude": 31.72113, "longitude": 65.96306},
            {"name": "Taryu", "latitude": 31.63319, "longitude": 65.89752},
            {"name": "Yawari Hinayat", "latitude": 31.70244, "longitude": 65.93444},
            {"name": "Zan Abad", "latitude": 31.74922, "longitude": 65.95967},
            {"name": "Zangi", "latitude": 31.71516, "longitude": 66.22648}
        ],
        "Arghistan": [
            {"name": "Akhtar Zai Noor Mohammad Kalay", "latitude": 31.32958, "longitude": 66.16542},
            {"name": "Baba Ali", "latitude": 31.38975, "longitude": 66.2052},
            {"name": "Bagh Kalay Amir Mohammad Landay Shadi Khan", "latitude": 31.40311, "longitude": 66.08506},
            {"name": "Din Mohammad Kalay", "latitude": 31.31726, "longitude": 66.18218},
            {"name": "Fazil Karam", "latitude": 31.32627, "longitude": 66.2009},
            {"name": "Ghabarga", "latitude": 31.35377, "longitude": 66.19105},
            {"name": "Haji Akhtar Zay", "latitude": 31.36806, "longitude": 66.19948},
            {"name": "Loy Kalay", "latitude": 31.36665, "longitude": 66.28148},
            {"name": "Makh Kalay", "latitude": 31.3732, "longitude": 66.27291},
            {"name": "Patkay Hulya", "latitude": 31.38761, "longitude": 66.12366},
            {"name": "Patkay Sufla", "latitude": 31.36703, "longitude": 66.08718},
            {"name": "Payianda Kalay", "latitude": 31.78426, "longitude": 66.74429},
            {"name": "Sapar Zay Kalay", "latitude": 31.36702, "longitude": 66.26151},
            {"name": "Shah Kalay", "latitude": 31.3718, "longitude": 66.28518}
    ],
        "Panjwayi": [
            {"name": "Abdul Rashid Kalacha", "latitude": 31.50075, "longitude": 65.54991},
                {"name": "Abdul Rauf Kalacha", "latitude": 31.4873, "longitude": 65.36791},
                {"name": "Achakzo Wa Biyabanak", "latitude": 31.46564, "longitude": 65.37633},
                {"name": "Achakzo Wa Kakaran", "latitude": 31.44784, "longitude": 65.34815},
                {"name": "Achk Zai", "latitude": 31.512, "longitude": 65.46006},
                {"name": "Adam Zai", "latitude": 31.48357, "longitude": 65.5318},
                {"name": "Aleko Zaye", "latitude": 31.46675, "longitude": 65.3636},
                {"name": "Alokuzay", "latitude": 31.52348, "longitude": 65.49636},
                {"name": "Armada", "latitude": 31.53514, "longitude": 65.46742},
                {"name": "Ashraf", "latitude": 31.43175, "longitude": 65.45047},
                {"name": "Askicha", "latitude": 31.51332, "longitude": 65.42899},
                {"name": "Badizu", "latitude": 31.53088, "longitude": 65.54624},
                {"name": "Badwan", "latitude": 31.57334, "longitude": 65.48446},
                {"name": "Bahadur", "latitude": 31.50263, "longitude": 65.49707},
                {"name": "Bala Dahi Bala", "latitude": 31.53542, "longitude": 65.59568},
                {"name": "Balambi", "latitude": 31.46132, "longitude": 65.36858},
                {"name": "Baluchan", "latitude": 31.54251, "longitude": 65.49311},
                {"name": "Baluchan Kalay", "latitude": 31.45829, "longitude": 65.32607},
                {"name": "Baluchan Mushan", "latitude": 31.46436, "longitude": 65.26369},
                {"name": "Bilandi", "latitude": 31.52895, "longitude": 65.60231},
                {"name": "Biyabanak Mushan", "latitude": 31.45823, "longitude": 65.27083},
                {"name": "Chaka Naw Masum Khan", "latitude": 31.47576, "longitude": 65.33035},
                {"name": "Chirgano Kor", "latitude": 31.49749, "longitude": 65.41122},
                {"name": "Dabak", "latitude": 31.51348, "longitude": 65.42082},
                {"name": "Dahimrasi", "latitude": 31.54115, "longitude": 65.49923},
                {"name": "Do Ab", "latitude": 31.47207, "longitude": 65.23797},
                {"name": "Faqir Zai", "latitude": 31.51614, "longitude": 65.59006},
                {"name": "Farsibanan", "latitude": 31.46835, "longitude": 65.32353},
                {"name": "Fattah Khan", "latitude": 31.45198, "longitude": 65.41383},
                {"name": "Fattihullah", "latitude": 31.52492, "longitude": 65.56879},
                {"name": "Garandi", "latitude": 31.45493, "longitude": 65.36528},
                {"name": "Haji Abdul", "latitude": 31.5156, "longitude": 65.46185},
                {"name": "Haji Abdulhaq Kalacha", "latitude": 31.43711, "longitude": 65.32585},
                {"name": "Haji Abdulrahman", "latitude": 31.50798, "longitude": 65.43433},
                {"name": "Haji Baluch Kalacha", "latitude": 31.45256, "longitude": 65.33103},
                {"name": "Haji Habibullah", "latitude": 31.52429, "longitude": 65.45166},
                {"name": "Haji Kakar", "latitude": 31.4676, "longitude": 65.332},
                {"name": "Haji Khiro", "latitude": 31.47405, "longitude": 65.33886},
                {"name": "Haji Mohammad Yusuf", "latitude": 31.47329, "longitude": 65.36594},
                {"name": "Haji Obidullah", "latitude": 31.51323, "longitude": 65.43535},
                {"name": "Haji Rahmatullah", "latitude": 31.48767, "longitude": 65.35248},
                {"name": "Haji Salam Khan", "latitude": 31.49794, "longitude": 65.42544},
                {"name": "Haji Wali Mohammad", "latitude": 31.51605, "longitude": 65.44003},
                {"name": "Kakaran", "latitude": 31.50702, "longitude": 65.431005},
                {"name": "Kalacha", "latitude": 31.52065, "longitude": 65.47456},
                {"name": "Kamp Mahajerin Mando Zai", "latitude": 31.4751, "longitude": 65.19804},
                {"name": "Kamp Mahjeren", "latitude": 31.47758, "longitude": 65.27564},
                {"name": "Kano Zai", "latitude": 31.46266, "longitude": 65.23075},
                {"name": "Kharot", "latitude": 31.58953, "longitude": 65.53806},
                {"name": "Khinjigak", "latitude": 31.46977, "longitude": 65.52331},
                {"name": "Khuganyan", "latitude": 31.47566, "longitude": 65.3727},
                {"name": "Kishkak", "latitude": 31.48022, "longitude": 65.35387},
                {"name": "Kochni Chalghor", "latitude": 31.54469, "longitude": 65.56493},
                {"name": "Kuchni Sayyidan", "latitude": 31.49396, "longitude": 65.37966},
                {"name": "Kundyanu Kalay", "latitude": 31.52355, "longitude": 65.44125},
                {"name": "Kunjak Wa Azim", "latitude": 31.45666, "longitude": 65.26203},
                {"name": "Lagari", "latitude": 31.47277, "longitude": 65.38608},
                {"name": "Lahl Khan Kalay", "latitude": 31.49664, "longitude": 65.5254},
                {"name": "Lolara", "latitude": 31.49787, "longitude": 65.39119},
                {"name": "Lor Salihan", "latitude": 31.57035, "longitude": 65.54611},
                {"name": "Loy Chalghor", "latitude": 31.53483, "longitude": 65.5577},
                {"name": "Loy Sayyidan", "latitude": 31.4826, "longitude": 65.38175},
                {"name": "Madrasa", "latitude": 31.55828, "longitude": 65.4783},
                {"name": "Mahajirin", "latitude": 31.53236, "longitude": 65.52299},
                {"name": "Markaz Panjwayi", "latitude": 31.54537, "longitude": 65.45305},
                {"name": "Mazangan", "latitude": 31.50518, "longitude": 65.54598},
                {"name": "Miral Zai", "latitude": 31.50585, "longitude": 65.53197},
                {"name": "Mobin Shah Agha", "latitude": 31.49121, "longitude": 65.37282},
                {"name": "Mohammad Akram Kalay", "latitude": 31.5312, "longitude": 65.46188},
                {"name": "Mohammad Gul Kakaran", "latitude": 31.46608, "longitude": 65.31615},
                {"name": "Mohammad Koh", "latitude": 31.489, "longitude": 65.36251},
                {"name": "Mohammad Sidiq", "latitude": 31.46403, "longitude": 65.27258},
                {"name": "Mullah Abdulghani", "latitude": 31.47205, "longitude": 65.31924},
                {"name": "Mullah Abdulrahman", "latitude": 31.51788, "longitude": 65.45094},
                {"name": "Mullah Abdulrahman Akhund", "latitude": 31.50732, "longitude": 65.42772},
                {"name": "Mullah Ahmad Kalay", "latitude": 31.45838, "longitude": 65.33044},
                {"name": "Mullah Dost", "latitude": 31.43123, "longitude": 65.49685},
                {"name": "Mullah Hassan Akhund Khushkyan", "latitude": 31.48231, "longitude": 65.34703},
                {"name": "Mushan (Sayyidan)", "latitude": 31.46042, "longitude": 65.26226},
                {"name": "Mussa Kalim", "latitude": 31.46837, "longitude": 65.49584},
                {"name": "Mussa Khan", "latitude": 31.49859, "longitude": 65.43533},
                {"name": "Nachar", "latitude": 31.52993, "longitude": 65.44313},
                {"name": "Nahan Zai", "latitude": 31.48925, "longitude": 65.39425},
                {"name": "Nahr Kalay", "latitude": 31.61023, "longitude": 65.55431},
                {"name": "Nakhuni", "latitude": 31.50739, "longitude": 65.56939},
                {"name": "Naw Ruz Kalay", "latitude": 31.4971, "longitude": 65.55156},
                {"name": "Nayib Kheil", "latitude": 31.46001, "longitude": 65.30387},
                {"name": "Nowrozi", "latitude": 31.59892, "longitude": 65.54846},
                {"name": "Pay Malluk", "latitude": 31.50575, "longitude": 65.41133},
                {"name": "Qasem Rabat", "latitude": 31.4751, "longitude": 65.4635},
                {"name": "Rigi", "latitude": 31.4839, "longitude": 65.43908},
                {"name": "Rigu Hulya", "latitude": 31.45161, "longitude": 65.5095},
                {"name": "Rigu Sufla", "latitude": 31.4422, "longitude": 65.51712},
                {"name": "Salawat Hulya", "latitude": 31.51798, "longitude": 65.54286},
                {"name": "Salawat Sufla", "latitude": 31.51755, "longitude": 65.52758},
                {"name": "Salihan", "latitude": 31.55392, "longitude": 65.53928},
                {"name": "Salu Aka Kalay", "latitude": 31.45166, "longitude": 65.27233},
                {"name": "Sami Zayi", "latitude": 31.48055, "longitude": 65.37535},
                {"name": "Sardaran", "latitude": 31.53047, "longitude": 65.45554},
                {"name": "Sayyida Khan", "latitude": 31.45367, "longitude": 65.38993},
                {"name": "Sayyid Kalacha", "latitude": 31.55192, "longitude": 65.56592},
                {"name": "Sayyid Rustam", "latitude": 31.47206, "longitude": 65.29315},
                {"name": "Shaikh Qalandar Baba", "latitude": 31.51823, "longitude": 65.42728},
                {"name": "Spin Midan", "latitude": 31.52044, "longitude": 65.4178},
                {"name": "Sultan Mohammad", "latitude": 31.49448, "longitude": 65.40254},
                {"name": "Tulukan", "latitude": 31.44277, "longitude": 65.31471},
                {"name": "Wakil Rustam Kalay", "latitude": 31.44698, "longitude": 65.30395},
                {"name": "Yaru Kalay", "latitude": 31.45183, "longitude": 65.52685},
                {"name": "Zala Dahi", "latitude": 31.60595, "longitude": 65.53949},
                {"name": "Zila Khan", "latitude": 31.52881, "longitude": 65.59026}
        ],
        "Maywand": [
            {"name": "Abdullah Akhond Zada Kalay", "latitude": 31.53463, "longitude": 65.05457},
            {"name": "Abdul Salam Kalay", "latitude": 31.52085, "longitude": 65.10004},
            {"name": "Agha Khailo Kalay", "latitude": 31.57388, "longitude": 64.84946},
            {"name": "Agha Mir Karaiz", "latitude": 31.61741, "longitude": 64.88323},
            {"name": "Ahmad Jan Kalay", "latitude": 31.53054, "longitude": 64.99017},
            {"name": "Airan", "latitude": 31.82735, "longitude": 65.067},
            {"name": "Akbari Wala", "latitude": 31.49607, "longitude": 64.91044},
            {"name": "Akhtari", "latitude": 31.62486, "longitude": 64.90694},
            {"name": "Akhtar Khailo", "latitude": 31.53633, "longitude": 64.90314},
            {"name": "Ali Abad", "latitude": 31.78318, "longitude": 65.04398},
            {"name": "Amanat", "latitude": 31.76877, "longitude": 64.87837},
            {"name": "Anjeran", "latitude": 31.89422, "longitude": 64.87621},
            {"name": "Asoda Kalay", "latitude": 31.54704, "longitude": 65.0921},
            {"name": "Atta Mohammad Karaiz", "latitude": 31.53128, "longitude": 65.16159},
            {"name": "Azim Jan Karaiz", "latitude": 31.51811, "longitude": 65.23628},
            {"name": "Aziz Abad", "latitude": 31.64652, "longitude": 65.0462},
            {"name": "Babe Karaiz", "latitude": 31.5357, "longitude": 65.02913},
            {"name": "Baberan", "latitude": 31.535605, "longitude": 65.019875},
            {"name": "Bado Zai", "latitude": 31.53146, "longitude": 64.96974},
            {"name": "Bahlol Zai", "latitude": 31.53074, "longitude": 64.94358},
            {"name": "Balagh Kalay", "latitude": 31.80043, "longitude": 65.06644},
            {"name": "Barang", "latitude": 31.7453, "longitude": 64.92106},
            {"name": "Beyabanak", "latitude": 31.60501, "longitude": 64.95628},
            {"name": "Chahel Gazi", "latitude": 31.60557, "longitude": 65.04756},
            {"name": "Chashma", "latitude": 31.52784, "longitude": 65.01379},
            {"name": "China", "latitude": 31.79904, "longitude": 65.08356},
            {"name": "Choka Zai", "latitude": 31.52826, "longitude": 64.8964},
            {"name": "Cholawak", "latitude": 31.62664, "longitude": 64.88514},
            {"name": "Dab Karaiz", "latitude": 31.89854, "longitude": 64.81437},
            {"name": "Dahi Qabad", "latitude": 31.49104, "longitude": 65.23667},
            {"name": "Daka", "latitude": 31.81855, "longitude": 65.07006},
            {"name": "Dar Weza", "latitude": 31.543, "longitude": 64.98845},
            {"name": "Dewal Kala", "latitude": 31.54832, "longitude": 64.93301},
            {"name": "Doli", "latitude": 31.60418, "longitude": 64.79004},
            {"name": "Eashq Abad", "latitude": 31.64788, "longitude": 65.07148},
            {"name": "Gach Karaiz", "latitude": 31.64263, "longitude": 64.97507},
            {"name": "Gadiyan", "latitude": 31.60688, "longitude": 64.79954},
            {"name": "Garmab", "latitude": 31.80517, "longitude": 64.90333},
            {"name": "Garmabak Jonobi", "latitude": 31.76585, "longitude": 64.98494},
            {"name": "Garmabak Shamaly", "latitude": 31.76474, "longitude": 64.95428},
            {"name": "Ghona Che", "latitude": 31.65608, "longitude": 64.89673},
            {"name": "Gondi Khail", "latitude": 31.59749, "longitude": 64.8021},
            {"name": "Haji Habibullah Kalay", "latitude": 31.51705, "longitude": 65.07984},
            {"name": "Haji Honar Kas", "latitude": 31.51077, "longitude": 65.12455},
            {"name": "Haji Khail Karaiz", "latitude": 31.54848, "longitude": 64.9034},
            {"name": "Haji Mir Afzal Kalay", "latitude": 31.88216, "longitude": 64.81183},
            {"name": "Haji Mohammad Khan Kalay", "latitude": 31.5196, "longitude": 65.09464},
            {"name": "Haji Mohammad Shah Kalay", "latitude": 31.51812, "longitude": 65.11724},
            {"name": "Haji Taj Mohammad Karaiz", "latitude": 31.77092, "longitude": 64.90325},
            {"name": "Hamid Karaiz", "latitude": 31.51789, "longitude": 65.14274},
            {"name": "Hassan Abad", "latitude": 31.599, "longitude": 65.05895},
            {"name": "Hotal", "latitude": 31.61726, "longitude": 65.05987},
            {"name": "Jow Kari", "latitude": 31.51765, "longitude": 65.15115},
            {"name": "Kafer Shagay", "latitude": 31.50604, "longitude": 64.8791},
            {"name": "Kakaran", "latitude": 31.53089, "longitude": 64.95271},
            {"name": "Kala Khan Kalay", "latitude": 31.77128, "longitude": 65.00455},
            {"name": "Kalfak", "latitude": 31.7806, "longitude": 64.87943},
            {"name": "Kamo Zai", "latitude": 31.53559, "longitude": 64.9098},
            {"name": "Karaizak", "latitude": 31.63933, "longitude": 65.044907},
            {"name": "Karaizak Mohammad Azim", "latitude": 31.76227, "longitude": 64.9103},
            {"name": "Karaiz Wal", "latitude": 31.56462, "longitude": 64.85856},
            {"name": "Kari Khail", "latitude": 31.63812, "longitude": 64.86772},
            {"name": "Kazha Karaiz", "latitude": 31.70271, "longitude": 64.84218},
            {"name": "Khaig Karaiz", "latitude": 31.72946, "longitude": 65.10166},
            {"name": "Khak Chopan", "latitude": 31.67825, "longitude": 64.89637},
            {"name": "Khaly Zar", "latitude": 31.7661, "longitude": 64.86206},
            {"name": "Khano Khail", "latitude": 31.54444, "longitude": 64.87402},
            {"name": "Khazan Kalay", "latitude": 31.63093, "longitude": 65.08066},
            {"name": "Khogyani", "latitude": 31.64076, "longitude": 64.91801},
            {"name": "Khosh Khaliq", "latitude": 31.60512, "longitude": 65.06274},
            {"name": "Koriz Kalay", "latitude": 31.54684, "longitude": 64.97257},
            {"name": "Koy Kak", "latitude": 31.58108, "longitude": 64.83406},
            {"name": "Kushk Nakhod", "latitude": 31.62346, "longitude": 65.05192},
            {"name": "Lahl Mohammad Kalay", "latitude": 31.63985, "longitude": 64.82769},
            {"name": "Lala Zai", "latitude": 31.65383, "longitude": 64.85926},
            {"name": "Landi", "latitude": 31.59755, "longitude": 65.04187},
            {"name": "Landi Karaiz", "latitude": 31.60097, "longitude": 64.97707},
            {"name": "Loy Kalay", "latitude": 31.51263, "longitude": 64.91791},
            {"name": "Loy Karaiz", "latitude": 31.58014, "longitude": 65.04953},
            {"name": "Magat", "latitude": 31.51808, "longitude": 65.22628},
            {"name": "Mahmod Abad", "latitude": 31.71698, "longitude": 65.08803},
            {"name": "Mahmod Khail", "latitude": 31.53871, "longitude": 64.91727},
            {"name": "Mahsom Karaiz", "latitude": 31.8038, "longitude": 64.85774},
            {"name": "Maiwand Chashma", "latitude": 31.74664, "longitude": 65.12872},
            {"name": "Maiwand Karaiz", "latitude": 31.73147, "longitude": 65.12984},
            {"name": "Mako Kalay", "latitude": 31.61072, "longitude": 64.966},
            {"name": "Maly Khail", "latitude": 31.55863, "longitude": 64.84046},
            {"name": "Mama Karaiz", "latitude": 31.53186, "longitude": 65.18432},
            {"name": "Mando Zai", "latitude": 31.4981, "longitude": 65.20846},
            {"name": "Mansor Kalay", "latitude": 31.53786, "longitude": 64.98543},
            {"name": "Mazreha", "latitude": 31.62012, "longitude": 65.0378},
            {"name": "Meya Karaiz", "latitude": 31.52355, "longitude": 65.19408},
            {"name": "Mira Khor", "latitude": 31.50389, "longitude": 65.23208},
            {"name": "Mohammad Ayoub Karaiz", "latitude": 31.87307, "longitude": 64.81066},
            {"name": "Mohammad Halam Kalay", "latitude": 31.51552, "longitude": 65.15472},
            {"name": "Mohammad Moseh Kalay", "latitude": 31.62857, "longitude": 65.0297},
            {"name": "Mohsen Khan Kalay", "latitude": 31.63281, "longitude": 65.04142},
            {"name": "Moshak", "latitude": 31.68162, "longitude": 65.05581},
            {"name": "Murcha", "latitude": 31.61994, "longitude": 65.04399},
            {"name": "Naik Karaiz", "latitude": 31.75935, "longitude": 64.79119},
            {"name": "Naso Kalay", "latitude": 31.6413, "longitude": 65.02819},
            {"name": "Nasrullah Khan Kalay", "latitude": 31.63874, "longitude": 64.92231},
            {"name": "Nokar Khail", "latitude": 31.54026, "longitude": 64.89075},
            {"name": "Noor Zai", "latitude": 31.55397, "longitude": 64.94129},
            {"name": "Now Abad", "latitude": 31.692905, "longitude": 65.0192},
            {"name": "Now Abad Lala Zai", "latitude": 31.67834, "longitude": 64.86934},
            {"name": "Nowi Kas", "latitude": 31.51049, "longitude": 65.14467},
            {"name": "Nowi Wialay", "latitude": 31.53091, "longitude": 64.93803},
            {"name": "Pada", "latitude": 31.86694, "longitude": 64.86207},
            {"name": "Pair Zada", "latitude": 31.60908, "longitude": 65.06707},
            {"name": "Payen Kala", "latitude": 31.52014, "longitude": 65.13153},
            {"name": "Qala Gay", "latitude": 31.64368, "longitude": 64.89665},
            {"name": "Qala Khowja Mohammad Khan", "latitude": 31.53143, "longitude": 65.20372},
            {"name": "Qazi Karaiz", "latitude": 31.67452, "longitude": 64.93486},
            {"name": "Rangraizan", "latitude": 31.51132, "longitude": 65.18206},
            {"name": "Sanger", "latitude": 31.7717, "longitude": 64.87007},
            {"name": "Sar Boland", "latitude": 31.50946, "longitude": 65.04914},
            {"name": "Sar Kari Kalay", "latitude": 31.6518, "longitude": 64.94305},
            {"name": "Sarwar Karaiz", "latitude": 31.57328, "longitude": 65.0564},
            {"name": "Sayban", "latitude": 31.63929, "longitude": 65.03091},
            {"name": "Sayd Khan Kalay", "latitude": 31.86567, "longitude": 64.82609},
            {"name": "Sayid Ahmad Jan Kalay", "latitude": 31.51516, "longitude": 65.16628},
            {"name": "Shabaz", "latitude": 31.63796, "longitude": 65.05819},
            {"name": "Shado Qalat", "latitude": 31.63664, "longitude": 65.01997},
            {"name": "Shaghasi", "latitude": 31.51188, "longitude": 65.02523},
            {"name": "Shakh Ghazay", "latitude": 31.62578, "longitude": 65.08037},
            {"name": "Shakotay", "latitude": 31.63741, "longitude": 65.01008},
            {"name": "Shamali Darya", "latitude": 31.62329, "longitude": 65.02991},
            {"name": "Shari Kalay", "latitude": 31.58882, "longitude": 64.83822},
            {"name": "Sher Ali", "latitude": 31.57532, "longitude": 65.05627},
            {"name": "Sher Jan", "latitude": 31.54632, "longitude": 65.09325},
            {"name": "Sher Mohammad Zai", "latitude": 31.6118, "longitude": 65.04454},
            {"name": "Shna Ghazay", "latitude": 31.58623, "longitude": 64.96661},
            {"name": "Shor Ab", "latitude": 31.53494, "longitude": 65.01238},
            {"name": "Showa", "latitude": 31.63119, "longitude": 64.86703},
            {"name": "Shurabak", "latitude": 31.60323, "longitude": 64.81422},
            {"name": "Sia Khan", "latitude": 31.62067, "longitude": 64.93428},
            {"name": "Siah Sang", "latitude": 31.76895, "longitude": 64.92761},
            {"name": "Sir Sang", "latitude": 31.50454, "longitude": 65.17035},
            {"name": "Sorkay", "latitude": 31.61686, "longitude": 65.03924},
            {"name": "Sufla Chashma", "latitude": 31.57972, "longitude": 65.04203},
            {"name": "Taghano", "latitude": 31.53445, "longitude": 65.16541},
            {"name": "Tajaka", "latitude": 31.5708, "longitude": 64.89459},
            {"name": "Takhta Pul", "latitude": 31.6426, "longitude": 64.98658},
            {"name": "Tanai", "latitude": 31.53812, "longitude": 64.97066},
            {"name": "Tara Khail", "latitude": 31.53874, "longitude": 64.97789},
            {"name": "Taymur", "latitude": 31.5223, "longitude": 65.03232},
            {"name": "Umar", "latitude": 31.52293, "longitude": 65.09164},
            {"name": "Urak", "latitude": 31.5439, "longitude": 65.04366},
            {"name": "Wadi-e-Khan", "latitude": 31.57395, "longitude": 65.01233},
            {"name": "Wali Mohammad Ghazi", "latitude": 31.86955, "longitude": 64.82691},
            {"name": "Wasimabad", "latitude": 31.5089, "longitude": 65.10491},
            {"name": "Wosay Kalay", "latitude": 31.51283, "longitude": 65.10506},
            {"name": "Yaqub Kalay", "latitude": 31.54269, "longitude": 64.95772},
            {"name": "Yari", "latitude": 31.64505, "longitude": 65.05806},
            {"name": "Yari Khan Kalay", "latitude": 31.53166, "longitude": 65.04891},
            {"name": "Yosuf", "latitude": 31.53864, "longitude": 64.95512},
            {"name": "Yusef Kalay", "latitude": 31.79805, "longitude": 65.01161},
            {"name": "Zahida Kala", "latitude": 31.49368, "longitude": 65.04857},
            {"name": "Zahir", "latitude": 31.64299, "longitude": 65.07838},
            {"name": "Zarif", "latitude": 31.62366, "longitude": 65.0431},
            {"name": "Zinay", "latitude": 31.5196, "longitude": 65.18431},
            {"name": "Zowid Kala", "latitude": 31.48134, "longitude": 65.23974}
        ],
        "Shah Wali Kot": [
                    {
                "name": "Ahzam Kalay",
                "latitude": 31.64422,
                "longitude": 65.94175
            },
            {
                "name": "Akhund Zada Kalay",
                "latitude": 31.71812,
                "longitude": 66.18801
            },
            {
                "name": "Akhund Zada Sahib",
                "latitude": 31.7031,
                "longitude": 66.167
            },
            {
                "name": "Ali Abad",
                "latitude": 31.7387,
                "longitude": 65.92142
            },
            {
                "name": "Ali Zay",
                "latitude": 31.42325,
                "longitude": 65.92299
            },
            {
                "name": "Anzirgay",
                "latitude": 31.77652,
                "longitude": 65.97012
            },
            {
                "name": "Arhat Kalay",
                "latitude": 31.68236,
                "longitude": 66.01269
            },
            {
                "name": "Awme",
                "latitude": 31.76115,
                "longitude": 65.93248
            },
            {
                "name": "Bariki",
                "latitude": 31.69023,
                "longitude": 65.96822
            },
            {
                "name": "Bashar Kalay",
                "latitude": 31.42243,
                "longitude": 65.95309
            },
            {
                "name": "Bawary",
                "latitude": 31.69753,
                "longitude": 65.88339
            },
            {
                "name": "Baz Mohammad Khan Kalay",
                "latitude": 31.64663,
                "longitude": 65.94916
            },
            {
                "name": "Biyaban Dara",
                "latitude": 31.44774,
                "longitude": 65.92235
            },
            {
                "name": "Biyabani Kalay",
                "latitude": 31.62404,
                "longitude": 66.15417
            },
            {
                "name": "Chakaw",
                "latitude": 31.93134,
                "longitude": 65.67861
            },
            {
                "name": "Haji Qayoum Kalacha",
                "latitude": 31.77513,
                "longitude": 65.81851
            },
            {
                "name": "Mansor Abad",
                "latitude": 31.77833,
                "longitude": 65.80112
            }
        ],
        "Zhar": [
                {
            "name": "Abdul Ghani Sanzari",
            "latitude": 31.60789,
            "longitude": 65.52299
        },
        {
            "name": "Abdulhadi Sanzari",
            "latitude": 31.59751,
            "longitude": 65.52506
        },
        {
            "name": "Abdul Hakim Kalacha",
            "latitude": 31.61799,
            "longitude": 65.53494
        },
        {
            "name": "Abdul Mohammad Jatan",
            "latitude": 31.58268,
            "longitude": 65.43713
        },
        {
            "name": "Abdul Rauof",
            "latitude": 31.58513,
            "longitude": 65.44816
        },
        {
            "name": "Achekzai Gharbi",
            "latitude": 31.54318,
            "longitude": 65.29207
        },
        {
            "name": "Achekzai Sharqi",
            "latitude": 31.54991,
            "longitude": 65.34757
        },
        {
            "name": "Aghaygul",
            "latitude": 31.52957,
            "longitude": 65.40878
        },
        {
            "name": "Akhtar Mohammad",
            "latitude": 31.5647,
            "longitude": 65.42827
        },
        {
            "name": "Akhtar Mohammad Kalay",
            "latitude": 31.54062,
            "longitude": 65.30206
        },
        {
            "name": "Ali Zai",
            "latitude": 31.49672,
            "longitude": 65.3251
        },
        {
            "name": "Anezai",
            "latitude": 31.53289,
            "longitude": 65.38123
        },
        {
            "name": "Ardozai",
            "latitude": 31.53873,
            "longitude": 65.34288
        },
        {
            "name": "Asheqa",
            "latitude": 31.59488,
            "longitude": 65.5059
        },
        {
            "name": "Ayoub Zai",
            "latitude": 31.52768,
            "longitude": 65.37167
        },
        {
            "name": "Baberan",
            "latitude": 31.57354,
            "longitude": 65.44209
        },
        {
            "name": "Baboghdi",
            "latitude": 31.48022,
            "longitude": 65.27627
        },
        {
            "name": "Balochan Gharbi",
            "latitude": 31.57861,
            "longitude": 65.4157
        },
        {
            "name": "Balosan",
            "latitude": 31.549,
            "longitude": 65.32183
        },
        {
            "name": "Barik Zai",
            "latitude": 31.531295,
            "longitude": 65.349755
        },
        {
            "name": "Barik Zai Jonobi",
            "latitude": 31.50293,
            "longitude": 65.27576
        },
        {
            "name": "Barik Zai Wasate",
            "latitude": 31.5076,
            "longitude": 65.28225
        },
        {
            "name": "Beyabanak",
            "latitude": 31.51312,
            "longitude": 65.29491
        },
        {
            "name": "Bor Ahmad Umar Zai",
            "latitude": 31.54113,
            "longitude": 65.38797
        },
        {
            "name": "Char Kocha Baberan",
            "latitude": 31.55258,
            "longitude": 65.43834
        },
        {
            "name": "Char Shakha",
            "latitude": 31.48142,
            "longitude": 65.25999
        },
        {
            "name": "Dagran",
            "latitude": 31.55663,
            "longitude": 65.41379
        },
        {
            "name": "Dahi Dar",
            "latitude": 31.54919,
            "longitude": 65.37475
        },
        {
            "name": "Dahi Ghaowjak",
            "latitude": 31.5376,
            "longitude": 65.36491
        },
        {
            "name": "Dasht Balochan Gharbi",
            "latitude": 31.57218,
            "longitude": 65.32198
        },
        {
            "name": "Deewar Shamaly",
            "latitude": 31.53619,
            "longitude": 65.32733
        },
        {
            "name": "Faizullah Khan",
            "latitude": 31.56389,
            "longitude": 65.41143
        },
        {
            "name": "Ghariban",
            "latitude": 31.54808,
            "longitude": 65.39866
        },
        {
            "name": "Ghondi",
            "latitude": 31.53129,
            "longitude": 65.2993
        },
        {
            "name": "Ghondi Kalay",
            "latitude": 31.5323,
            "longitude": 65.35742
        },
        {
            "name": "Ghullam Hassan Khan",
            "latitude": 31.54048,
            "longitude": 65.30731
        },
        {
            "name": "Habibullah",
            "latitude": 31.49473,
            "longitude": 65.33523
        },
        {
            "name": "Haji Abdul Ahad",
            "latitude": 31.52562,
            "longitude": 65.33769
        },

        {
            "name": "Haji Abdullah Khan",
            "latitude": 31.50324,
            "longitude": 65.33641
        },

        {
            "name": "Haji Abdul Razaq",
            "latitude": 31.512,
            "longitude": 65.3883
        },
        {
            "name": "Haji Besmillah",
            "latitude": 31.55089,
            "longitude": 65.42467
        },
        {
            "name": "Haji Ghafar",
            "latitude": 31.55933,
            "longitude": 65.42978
        },
        {
            "name": "Haji Haidar Khan",
            "latitude": 31.52194,
            "longitude": 65.40194
        },
        {
            "name": "Haji Mahaiuldin",
            "latitude": 31.56816,
            "longitude": 65.41244
        },
        {
            "name": "Haji Mohammad Hewaz Khawari",
            "latitude": 31.54649,
            "longitude": 65.40363
        },
        {
            "name": "Haji Mohammad Hewaz Yasen Zai",
            "latitude": 31.53885,
            "longitude": 65.41609
        },
        {
            "name": "Haji Mohammad Umar Wa Sayyidan",
            "latitude": 31.59126,
            "longitude": 65.49394
        },
        {
            "name": "Haji Mussa Khan",
            "latitude": 31.54166,
            "longitude": 65.42243
        },
        {
            "name": "Haji Nader Kalay",
            "latitude": 31.50157,
            "longitude": 65.33159
        },
        {
            "name": "Haji Naserullah Khan",
            "latitude": 31.53774,
            "longitude": 65.37531
        },
        {
            "name": "Haji Nehmatullah Kalay",
            "latitude": 31.53487,
            "longitude": 65.31069
        },
        {
            "name": "Haji Pour Dail",
            "latitude": 31.53634,
            "longitude": 65.35911
        },
        {
            "name": "Haji Shahabudin Kalacha",
            "latitude": 31.61662,
            "longitude": 65.54251
        },
        {
            "name": "Haji Zarif Wa Haji Ibrahim",
            "latitude": 31.54586,
            "longitude": 65.33481
        },
        {
            "name": "Kadhel",
            "latitude": 31.50627,
            "longitude": 65.36926
        },
        {
            "name": "Kadi Zai",
            "latitude": 31.53186,
            "longitude": 65.35466
        },
        {
            "name": "Kadozai",
            "latitude": 31.52338,
            "longitude": 65.38021
        },
        {
            "name": "Kakaran",
            "latitude": 31.51769,
            "longitude": 65.36232
        },
        {
            "name": "Kalacha",
            "latitude": 31.56904,
            "longitude": 65.44603
        },
        {
            "name": "Kalizai",
            "latitude": 31.53278,
            "longitude": 65.38941
        },
        {
            "name": "Karkecha",
            "latitude": 31.50517,
            "longitude": 65.26907
        },
        {
            "name": "Kashta Sohbat",
            "latitude": 31.50718,
            "longitude": 65.24786
        },
        {
            "name": "Khan Mohammad Khan Kalay",
            "latitude": 31.50633,
            "longitude": 65.32659
        },
        {
            "name": "Khogyani",
            "latitude": 31.56083,
            "longitude": 65.42656
        },
        {
            "name": "Kota Zai",
            "latitude": 31.55008,
            "longitude": 65.43305
        },
        {
            "name": "Lahl Mohammad Khan",
            "latitude": 31.57003,
            "longitude": 65.40557
        },
        {
            "name": "Lowar Sohbat",
            "latitude": 31.52179,
            "longitude": 65.24574
        },
        {
            "name": "Mahajeren",
            "latitude": 31.53944,
            "longitude": 65.31515
        },
        {
            "name": "Mako",
            "latitude": 31.56921,
            "longitude": 65.43823
        },
        {
            "name": "Makwan",
            "latitude": 31.57846,
            "longitude": 65.46499
        },
        {
            "name": "Malangan",
            "latitude": 31.53722,
            "longitude": 65.33814
        },
        {
            "name": "Malik Ahmad Khan",
            "latitude": 31.5634,
            "longitude": 65.44704
        },
        {
            "name": "Manda",
            "latitude": 31.55376,
            "longitude": 65.45976
        },
        {
            "name": "Mani Zai Kalay",
            "latitude": 31.51518,
            "longitude": 65.3752
        },
        {
            "name": "Mardozai",
            "latitude": 31.53104,
            "longitude": 65.38386
        },
        {
            "name": "Markaz Woluswally",
            "latitude": 31.57867,
            "longitude": 65.42348
        },
        {
            "name": "Marsanzai",
            "latitude": 31.52544,
            "longitude": 65.39012
        },
        {
            "name": "Mir Hazar",
            "latitude": 31.67704,
            "longitude": 65.4389
        },
        {
            "name": "Mir Hotak",
            "latitude": 31.51275,
            "longitude": 65.26014
        },
        {
            "name": "Mir Waliyan",
            "latitude": 31.52055,
            "longitude": 65.33019
        },
        {
            "name": "Mullah Taj Mohammad",
            "latitude": 31.61849,
            "longitude": 65.50895
        },
        {
            "name": "Mullhyan",
            "latitude": 31.55557,
            "longitude": 65.3994
        },
        {
            "name": "Mussa Khan",
            "latitude": 31.52562,
            "longitude": 65.40854
        },
        {
            "name": "Nagharullah Kalay",
            "latitude": 31.53036,
            "longitude": 65.37167
        },
        {
            "name": "Nahr Karaiz",
            "latitude": 31.49566,
            "longitude": 65.28818
        },
        {
            "name": "Naik Mohammad Wa Haji Mohammad Hashemi",
            "latitude": 31.52909,
            "longitude": 65.39538
        },
        {
            "name": "Nalqam",
            "latitude": 31.49409,
            "longitude": 65.31143
        },
        {
            "name": "Nari",
            "latitude": 31.51167,
            "longitude": 65.26625
        },
        {
            "name": "Narow",
            "latitude": 31.50608,
            "longitude": 65.30979
        },
        {
            "name": "Noor Ali",
            "latitude": 31.55746,
            "longitude": 65.33555
        },
        {
            "name": "Noor Mohammad Khan Fazel Kalay",
            "latitude": 31.604,
            "longitude": 65.49296
        },
        {
            "name": "Noorulah Char Shakha",
            "latitude": 31.4925,
            "longitude": 65.27566
        },
        {
            "name": "Nooruldin Kalay",
            "latitude": 31.57277,
            "longitude": 65.45659
        },
        {
            "name": "Pas Ab",
            "latitude": 31.57092,
            "longitude": 65.42665
        },
        {
            "name": "Payan Dahi",
            "latitude": 31.54904,
            "longitude": 65.42786
        },
        {
            "name": "Rahmuldin Haji Wazer",
            "latitude": 31.53513,
            "longitude": 65.41139
        },
        {
            "name": "Sahdullah",
            "latitude": 31.52268,
            "longitude": 65.3525
        },
        {
            "name": "Salim Karaiz",
            "latitude": 31.66933,
            "longitude": 65.31411
        },
        {
            "name": "Salim Wa Azizullah",
            "latitude": 31.56804,
            "longitude": 65.45281
        },
        {
            "name": "Sanzari Aminullah",
            "latitude": 31.612,
            "longitude": 65.52909
        },
        {
            "name": "Sanzari Gharbi",
            "latitude": 31.60638,
            "longitude": 65.51604
        },
        {
            "name": "Sayyidan",
            "latitude": 31.50579,
            "longitude": 65.33475
        },
        {
            "name": "Shah Mohammad Khan Umar Khan Kalay",
            "latitude": 31.58995,
            "longitude": 65.48759
        },
        {
            "name": "Shahzada Abad",
            "latitude": 31.54053,
            "longitude": 65.26355
        },
        {
            "name": "Teer Yanan",
            "latitude": 31.55459,
            "longitude": 65.42565
        },
        {
            "name": "Wazer Kalay",
            "latitude": 31.56588,
            "longitude": 65.36753
        },
        {
            "name": "Zahedanan",
            "latitude": 31.56504,
            "longitude": 65.43525
        }
    ],
    # Add more districts and areas as needed
}


# Generate random data
num_records = 3000
data = []
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 1, 1)

for _ in range(num_records):
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    hour_of_day = random.randint(1, 24)
    
    district = random.choice(list(districts_data.keys()))
    area_info = random.choice(districts_data[district])
    
    location = area_info['name']
    latitude = area_info['latitude']
    longitude = area_info['longitude']
    
    victim_gender = random.choice(['Male', 'Female'])
    victim_age = random.randint(1, 100)
    perpetrator_gender = random.choice(['Male', 'Female'])
    perpetrator_age = random.randint(1, 100)
    weapon = random.choice(['Knife', 'Gun', 'None', 'Other'])
    injury = random.choice(['None', 'Minor', 'Severe', 'Fatal'])
    weather = random.choice(['Clear', 'Rainy', 'Snowy', 'Cloudy'])
    temperature = random.uniform(-10, 40)
    previous_activity = random.choice(['Walking', 'Driving', 'Shopping', 'Working'])
    economical_situation = random.choice(['Low', 'Medium', 'High'])
    education_level = random.choice(['None', 'Primary', 'Secondary', 'Tertiary'])
    crime_type = random.choice(['Theft','kill'])
    time_of_day = random.choice(['Morning', 'Afternoon', 'Evening', 'Night'])
    day_of_week = date.strftime("%A")
    month = date.strftime("%B")
    season = random.choice(['Winter', 'Spring', 'Summer', 'Fall'])
    victim_age_group = random.choice(['Child', 'Teen', 'Adult', 'Senior'])
    perpetrator_age_group = random.choice(['Child', 'Teen', 'Adult', 'Senior'])
    weather_condition = random.choice(['Dry', 'Wet'])
    economic_index = random.uniform(0, 100)
    education_index = random.uniform(0, 100)

    data.append([
        date, hour_of_day, location, district, area_info['name'], victim_gender, victim_age,
        perpetrator_gender, perpetrator_age, weapon, injury, weather, temperature, previous_activity,
        economical_situation, education_level, crime_type, latitude, longitude, time_of_day, day_of_week, 
        month, season, victim_age_group, perpetrator_age_group, weather_condition, economic_index, education_index
    ])

# Define column names
columns = [
    'date', 'hour_of_day', 'location', 'district', 'area_name', 'victim_gender', 'victim_age',
    'perpetrator_gender', 'perpetrator_age', 'weapon', 'injury', 'weather', 'temperature', 
    'previous_activity', 'economical_situation', 'education_level', 'crime_type', 'latitude', 'longitude',
    'time_of_day', 'day_of_week', 'month', 'season', 'victim_age_group', 'perpetrator_age_group', 
    'weather_condition', 'economic_index', 'education_index'
]

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('data.csv', index=False)

print("Data has been generated and saved to 'data.csv'.")










# import random
# import pandas as pd
# from datetime import datetime, timedelta
# # Sample data for districts and areas with latitude and longitude
# districts_data = {
#         "Center": [
#                 {"name": "Qalat", "latitude": 31.6116, "longitude": 65.7074},
#                 {"name": "Arghandab River", "latitude": 32.1091, "longitude": 66.9086},
#                 {"name": "Kandahar International Airport", "latitude": 31.5580, "longitude": 65.6625},
#                 {"name": "Kandahar Citadel (Arg-e-Kandahar)", "latitude": 31.5067, "longitude": 65.8472},
#                 {"name": "Mausoleum of Ahmad Shah Durrani", "latitude": 31.6283, "longitude": 65.7376},
#                 {"name": "Baba Wali Shrine", "latitude": 31.6122, "longitude": 65.7103},
#                 {"name": "Kandahar University", "latitude": 31.6539, "longitude": 65.6800},
#                 {"name": "Ziarat-e-Sakhi Baba", "latitude": 31.6231, "longitude": 65.6900},
#                 {"name": "Kandahar Central Mosque (Masjid-e-Kabir)", "latitude": 31.6383, "longitude": 65.6852},
#                 {"name": "Kandahar Museum", "latitude": 31.6100, "longitude": 65.7011},
#                 {"name": "Chahr Burjak", "latitude": 31.6180, "longitude": 65.7020},
#                 {"name": "Dahla Dam", "latitude": 31.5800, "longitude": 65.6150},
#                 {"name": "Spin Boldak (border town)", "latitude": 31.9500, "longitude": 65.5800},
#                 {"name": "Sarposa Prison", "latitude": 30.9000, "longitude": 66.2500},
#                 {"name": "Kandahar Stadium", "latitude": 31.6011, "longitude": 65.6967},
#                 {"name": "Aino Mina (residential area)", "latitude": 31.6100, "longitude": 65.6880},
#                 {"name": "Sarwar Khosti Mosque", "latitude": 31.5700, "longitude": 65.7090},
#                 {"name": "Haji Abdul Razziq Market", "latitude": 31.6250, "longitude": 65.7150},
#                 {"name": "Shahr-e Naw Park", "latitude": 31.6125, "longitude": 65.7070},
#                 {"name": "Mirwais Hospital", "latitude": 31.6120, "longitude": 65.7100},
#                 {"name": "Kandahar Public Library", "latitude": 31.6060, "longitude": 65.6980},
#                 {"name": "Shrine of Mirwais Hotak", "latitude": 31.6100, "longitude": 65.7010},
#                 {"name": "Mullah Omar's House", "latitude": 31.6120, "longitude": 65.7030},
#                 {"name": "Red Mosque (Masjid-e-Surkh)", "latitude": 31.6140, "longitude": 65.7075},
#                 {"name": "Provincial Governor's Office", "latitude": 31.6110, "longitude": 65.7050},
#                 {"name": "Shrine of Shah Agha", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Zarghona Ana High School", "latitude": 31.6150, "longitude": 65.7050},
#                 {"name": "Kandahar Agriculture Institute", "latitude": 31.6100, "longitude": 65.6980},
#                 {"name": "Kandahar City Center", "latitude": 31.6250, "longitude": 65.7150},
#                 {"name": "Old City (Shor Bazaar)", "latitude": 31.6160, "longitude": 65.7100},
#                 {"name": "Baba Sahib Shrine", "latitude": 31.6100, "longitude": 65.7080},
#                 {"name": "Shrine of Baba Jee", "latitude": 31.6300, "longitude": 65.6800},
#                 {"name": "Takht-e Safar (Hilltop park)", "latitude": 31.6350, "longitude": 65.6850},
#                 {"name": "Kandahar Industrial Park", "latitude": 31.6400, "longitude": 65.6750},
#                 {"name": "Tomb of Sher Ali Khan", "latitude": 31.5700, "longitude": 65.7450},
#                 {"name": "Shah Bazaar Mosque", "latitude": 31.6130, "longitude": 65.7040},
#                 {"name": "Baba Baba Shrine", "latitude": 31.6140, "longitude": 65.7060},
#                 {"name": "Juma Bazaar", "latitude": 31.6380, "longitude": 65.6820},
#                 {"name": "Shrine of Khoja Musafer", "latitude": 31.6130, "longitude": 65.7060},
#                 {"name": "Aino Mina Park", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Kandahar Central Park", "latitude": 31.5680, "longitude": 65.7120},
#                 {"name": "Malalai High School", "latitude": 31.6100, "longitude": 65.7010},
#                 {"name": "Kandahar Market Square", "latitude": 31.6140, "longitude": 65.7050},
#                 {"name": "Shrine of Sayyid Ali Akbar", "latitude": 31.6150, "longitude": 65.7070},
#                 {"name": "Mastoori High School", "latitude": 31.6150, "longitude": 65.7100},
#                 {"name": "Kandahar Red Crescent", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Kandahar Bank Headquarters", "latitude": 31.6180, "longitude": 65.7020},
#                 {"name": "Shahr-e Now Mosque", "latitude": 31.6160, "longitude": 65.7100},
#                 {"name": "Kandahar Fruit Market", "latitude": 31.6110, "longitude": 65.7100},
#                 {"name": "Kandahar Provincial Council", "latitude": 31.6130, "longitude": 65.7070},
#                 {"name": "Shrine of Pir Mohammad Jan", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Kandahar Police Headquarters", "latitude": 31.6150, "longitude": 65.7050},
#                 {"name": "Kandahar Radio Television (RTA)", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Kandahar Stadium (Sports Complex)", "latitude": 31.6180, "longitude": 65.7020},
#                 {"name": "Kandahar Women's Garden", "latitude": 31.6100, "longitude": 65.6880},
#                 {"name": "Shrine of Baba Sahib", "latitude": 31.6150, "longitude": 65.7050},
#                 {"name": "Kandahar School of Fine Arts", "latitude": 31.6300, "longitude": 65.6800},
#                 {"name": "Bibi Khadija Mosque", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Shrine of Mirwais Hotak", "latitude": 31.6100, "longitude": 65.7010},
#                 {"name": "Kandahar Institute of Modern Studies", "latitude": 31.6120, "longitude": 65.7030},
#                 {"name": "Shrine of Shah Agha", "latitude": 31.6250, "longitude": 65.7150},
#                 {"name": "Kandahar Public Health Directorate", "latitude": 31.6150, "longitude": 65.7050},
#                 {"name": "Kandahar Teacher Training College", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Regional Military Hospital", "latitude": 31.6200, "longitude": 65.7150},
#                 {"name": "Shrine of Baba Wali", "latitude": 31.6130, "longitude": 65.7040},
#                 {"name": "Kandahar Bagh-e Pul", "latitude": 31.6500, "longitude": 65.6900},
#                 {"name": "Kandahar Telecommunications Office", "latitude": 31.5800, "longitude": 65.7100},
#                 {"name": "Kandahar Vocational Training Center", "latitude": 31.6200, "longitude": 65.7150},
#                 {"name": "Kandahar Cultural Center", "latitude": 31.6230, "longitude": 65.7150},
#                 {"name": "Kandahar Agricultural Market", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Kandahar Technology Park", "latitude": 31.6100, "longitude": 65.7070},
#                 {"name": "Kandahar Railway Station", "latitude": 31.6300, "longitude": 65.6800},
#                 {"name": "Kandahar Post Office", "latitude": 31.6250, "longitude": 65.7000},
#                 {"name": "Kandahar Chamber of Commerce", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Fire Station", "latitude": 31.6200, "longitude": 65.7100},
#                 {"name": "Kandahar Electricity Department", "latitude": 31.6200, "longitude": 65.7150},
#                 {"name": "Kandahar Fish Market", "latitude": 31.6230, "longitude": 65.7150},
#                 {"name": "Kandahar Meat Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Dairy Market", "latitude": 31.6100, "longitude": 65.7070},
#                 {"name": "Kandahar Vegetable Market", "latitude": 31.6100, "longitude": 65.7070},
#                 {"name": "Kandahar Bakery Market", "latitude": 31.6130, "longitude": 65.7070},
#                 {"name": "Kandahar Carpet Market", "latitude": 31.6100, "longitude": 65.7070},
#                 {"name": "Kandahar Jewelry Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Textile Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Leather Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Handicrafts Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Furniture Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Electronics Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Auto Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Metal Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Construction Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Plastic Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Tools Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Pottery Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Book Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Flower Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Shoe Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Spice Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Kandahar Perfume Market", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Herat Gate (Herat Darwaza)", "latitude": 31.6100, "longitude": 65.7100},
#                 {"name": "Fruits Market Square (Meywa Mandi Chawk)", "latitude": 31.6100, "longitude": 65.6900},
#                 {"name": "Ghazi Square", "latitude": 31.6120, "longitude": 65.6940},
#                 {"name": "Shah Bazaar Square", "latitude": 31.6050, "longitude": 65.7050},
#                 {"name": "Khawja Bazaar Square", "latitude": 31.6090, "longitude": 65.6960},
#                 {"name": "Shorandam Square", "latitude": 31.6070, "longitude": 65.6990},
#                 {"name": "Chowk-e-Maidan", "latitude": 31.6200, "longitude": 65.6700},
#                 {"name": "Bazar-e-Khan Square", "latitude": 31.6080, "longitude": 65.7000},
#                 {"name": "Sarpoza Square", "latitude": 31.6110, "longitude": 65.6970},
#                 {"name": "Shaheedan Square", "latitude": 31.6130, "longitude": 65.7040},
#                 {"name": "Kandahar City Center Square", "latitude": 31.6050, "longitude": 65.7010},
#                 {"name": "Maiwand Gate Square", "latitude": 31.6100, "longitude": 65.7060},
#                 {"name": "Panjwayi Square", "latitude": 31.6140, "longitude": 65.7000},
#                 {"name": "Zhari Square", "latitude": 31.6000, "longitude": 65.7100},
#                 {"name": "Arghandab Square", "latitude": 31.6010, "longitude": 65.7110},
#                 {"name": "Daman Square", "latitude": 31.6120, "longitude": 65.6900},
#                 {"name": "Spin Boldak Square", "latitude": 31.6170, "longitude": 65.7020},
#                 {"name": "Nish Square", "latitude": 31.6050, "longitude": 65.6800},
#                 {"name": "Maroof Square", "latitude": 31.6100, "longitude": 65.6750},
#                 {"name": "Reg Square", "latitude": 31.6190, "longitude": 65.7070},
#                 {"name": "Ghorak Square", "latitude": 31.6220, "longitude": 65.7100},
#                 {"name": "Shurabak Square", "latitude": 31.6180, "longitude": 65.7120},
#                 {"name": "Miyan Nasheen Square", "latitude": 31.6250, "longitude": 65.7050},
#                 {"name": "Takht-e-Pol Square", "latitude": 31.6130, "longitude": 65.6950},
#                 {"name": "Maruf Square", "latitude": 31.6150, "longitude": 65.6980},
#                 {"name": "Mandisar Square", "latitude": 31.6200, "longitude": 65.6990},
#                 {"name": "Tiri Square", "latitude": 31.6160, "longitude": 65.7060},
#                 {"name": "Alokozai Square", "latitude": 31.6110, "longitude": 65.7020},
#                 {"name": "Mati Square", "latitude": 31.6090, "longitude": 65.6930},
#                 {"name": "Loy Wala Square", "latitude": 31.6070, "longitude": 65.7000},
#                 {"name": "Qalat Square", "latitude": 31.6140, "longitude": 65.6900},
#                 {"name": "Kash Square", "latitude": 31.6080, "longitude": 65.7050},
#                 {"name": "Salam Bazaar Square", "latitude": 31.6100, "longitude": 65.6960},
#                 {"name": "Janan Square", "latitude": 31.6130, "longitude": 65.6990},
#                 {"name": "Musa Square", "latitude": 31.6150, "longitude": 65.7000},
#                 {"name": "Barakzai Square", "latitude": 31.6070, "longitude": 65.7050},
#                 {"name": "Jalal Square", "latitude": 31.6080, "longitude": 65.6950},
#                 {"name": "Dand Square", "latitude": 31.6100, "longitude": 65.6980},
#                 {"name": "Shah Wali Kot Square", "latitude": 31.6140, "longitude": 65.6950},
#                 {"name": "Nawa Square", "latitude": 31.6050, "longitude": 65.6920},
#                 {"name": "Khakriz Square", "latitude": 31.6120, "longitude": 65.7040},
#                 {"name": "Gul Agha Square", "latitude": 31.6090, "longitude": 65.7030},
#                 {"name": "Mahmood Square", "latitude": 31.6170, "longitude": 65.6900},
#                 {"name": "Tariq Square", "latitude": 31.6180, "longitude": 65.6970},
#                 {"name": "Arbab Square", "latitude": 31.6100, "longitude": 65.7050},
#                 {"name": "Pach Square", "latitude": 31.6140, "longitude": 65.7000},
#                 {"name": "Farid Square", "latitude": 31.6110, "longitude": 65.6990},
#                 {"name": "Nasrat Square", "latitude": 31.6050, "longitude": 65.6900},
#                 {"name": "Latif Square", "latitude": 31.6090, "longitude": 65.7040},
#                 {"name": "Noor Square", "latitude": 31.6100, "longitude": 65.7020}
#         ],
#         "Kharkrez": [
                
#             {"name": "Alam", "latitude": 31.94474, "longitude": 65.55319},
#             {"name": "Aslam Kalay", "latitude": 31.96747, "longitude": 65.63512},
#             {"name": "Azmat Kalay", "latitude": 32.14261, "longitude": 65.52635},
#             {"name": "Baghak", "latitude": 32.0012, "longitude": 65.62588},
#             {"name": "Bagh Khalil", "latitude": 31.96108, "longitude": 65.47107},
#             {"name": "Baram Khail", "latitude": 32.01112, "longitude": 65.66342},
#             {"name": "Barikzo", "latitude": 32.20074, "longitude": 65.47645},
#             {"name": "Bay Himat", "latitude": 31.9138, "longitude": 65.47514},
#             {"name": "Burna Qara", "latitude": 32.06982, "longitude": 65.46315},
#             {"name": "Chahar Band", "latitude": 31.98742, "longitude": 65.63131},
#             {"name": "Chahar Sang Kalan", "latitude": 31.96611, "longitude": 65.51578},
#             {"name": "Chahar Sang Khurd", "latitude": 31.96442, "longitude": 65.52921},
#             {"name": "Chargh Ya Charagah", "latitude": 32.08058, "longitude": 65.48347},
#             {"name": "Chashma Ata", "latitude": 32.11539, "longitude": 65.50835},
#             {"name": "China", "latitude": 32.02968, "longitude": 65.56344},
#             {"name": "Chinar Baluch", "latitude": 31.97198, "longitude": 65.48169},
#             {"name": "Chingay", "latitude": 31.97224, "longitude": 65.46578},
#             {"name": "Chor Kalay", "latitude": 31.98681, "longitude": 65.64051},
#             {"name": "Darwishan", "latitude": 31.99469, "longitude": 65.47597},
#             {"name": "Din Mohammad Qanat", "latitude": 32.13842, "longitude": 65.52612},
#             {"name": "Dokhana", "latitude": 31.87389, "longitude": 65.38022},
#             {"name": "Faizullah Kalay", "latitude": 31.95067, "longitude": 65.66104},
#             {"name": "Fatih Khan Kalay", "latitude": 31.95709, "longitude": 65.64925},
#             {"name": "Ganda", "latitude": 31.96039, "longitude": 65.57424},
#             {"name": "Ghulaman", "latitude": 31.95611, "longitude": 65.52432},
#             {"name": "Ghulam Mohammad Kalay", "latitude": 31.96058, "longitude": 65.63709},
#             {"name": "Haji Abad", "latitude": 32.16194, "longitude": 65.52864},
#             {"name": "Haji Gul", "latitude": 31.96731, "longitude": 65.53151},
#             {"name": "Karaiz Usman", "latitude": 32.18836, "longitude": 65.56612},
#             {"name": "Karzalay", "latitude": 31.95919, "longitude": 65.53657},
#             {"name": "Khaki", "latitude": 32.00153, "longitude": 65.57336},
#             {"name": "Khosh Dar", "latitude": 31.91351, "longitude": 65.46674},
#             {"name": "Khoshi", "latitude": 31.9639, "longitude": 65.53782},
#             {"name": "Kido", "latitude": 31.94155, "longitude": 65.53856},
#             {"name": "Lalak", "latitude": 31.80778, "longitude": 65.30309},
#             {"name": "Landay", "latitude": 32.22094, "longitude": 65.54809},
#             {"name": "Liti", "latitude": 31.90982, "longitude": 65.48317},
#             {"name": "Loy Karaiz", "latitude": 32.19472, "longitude": 65.56704},
#             {"name": "Mir Abad", "latitude": 31.90782, "longitude": 65.49371},
#             {"name": "Musa Karaiz", "latitude": 31.79194, "longitude": 65.34895},
#             {"name": "Nasir Karaiz", "latitude": 31.9893, "longitude": 65.5977},
#             {"name": "Naw Abad", "latitude": 31.95156, "longitude": 65.56069},
#             {"name": "Qanad Umari", "latitude": 32.00531, "longitude": 65.65552},
#             {"name": "Sabzal Karaiz", "latitude": 31.85403, "longitude": 65.52051},
#             {"name": "Sad Kalay", "latitude": 32.09321, "longitude": 65.52157},
#             {"name": "Safid Khak", "latitude": 31.92918, "longitude": 65.42501},
#             {"name": "Sang Riz", "latitude": 31.93868, "longitude": 65.41296},
#             {"name": "Sanjid", "latitude": 32.17365, "longitude": 65.56415},
#             {"name": "Saraw Karaiz", "latitude": 32.21129, "longitude": 65.52224},
#             {"name": "Sar Gaw", "latitude": 31.91149, "longitude": 65.5037},
#             {"name": "Sar Khar", "latitude": 32.03317, "longitude": 65.4542},
#             {"name": "Sar Push", "latitude": 31.93655, "longitude": 65.46175},
#             {"name": "Sayyid Karaiz", "latitude": 31.90107, "longitude": 65.4853},
#             {"name": "Sayyidom", "latitude": 32.07123, "longitude": 65.46916},
#             {"name": "Shabi", "latitude": 32.15496, "longitude": 65.51019},
#             {"name": "Shairgha Hulya", "latitude": 31.95097, "longitude": 65.50544},
#             {"name": "Shairgha Sufla", "latitude": 31.94938, "longitude": 65.51316},
#             {"name": "Shams Kalay", "latitude": 31.96856, "longitude": 65.62621},
#             {"name": "Shokhan Kalay", "latitude": 31.90228, "longitude": 65.49107},
#             {"name": "Shutur Gardan", "latitude": 32.04817, "longitude": 65.49859},
#             {"name": "Tawagay", "latitude": 32.16906, "longitude": 65.57242},
#             {"name": "Tik", "latitude": 31.89078, "longitude": 65.46466},
#             {"name": "Tura Namak", "latitude": 32.16985, "longitude": 65.5319},
#             {"name": "Tur Kac", "latitude": 31.99158, "longitude": 65.64594},
#             {"name": "Zarak", "latitude": 31.78842, "longitude": 65.25643},
#             {"name": "Zil Abad", "latitude": 31.95598, "longitude": 65.51355},
#             {"name": "Ziyarat Shah Maqsud Agha Markaz Woluswally", "latitude": 31.98177, "longitude": 65.47083}
#     ],
#         "Ghorak": [
#             {"name": "Malmand", "latitude": 31.98997, "longitude": 64.98376},
#             {"name": "Malmona Ya Mehran", "latitude": 32.01042, "longitude": 64.98311},
#             {"name": "Shor Ab", "latitude": 32.00242, "longitude": 64.91901},
#             {"name": "Tootak Junobi", "latitude": 31.98191, "longitude": 64.94008},
#             {"name": "Tootak Shamaly", "latitude": 31.99964, "longitude": 64.93322}
#         ],
#         "Arghandab": [
#             {"name": "Baba Sahib", "latitude": 31.6556, "longitude": 65.65716},
#             {"name": "Baber", "latitude": 31.71417, "longitude": 65.67006},
#             {"name": "Bagh Sarkari", "latitude": 31.71023, "longitude": 65.70621},
#             {"name": "Barat Kalacha", "latitude": 31.68215, "longitude": 65.62052},
#             {"name": "Changal", "latitude": 31.68392, "longitude": 65.67784},
#             {"name": "Char Qoulba Hulya", "latitude": 31.69274, "longitude": 65.63969},
#             {"name": "Char Qoulba Sufla", "latitude": 31.68034, "longitude": 65.64595},
#             {"name": "Dahi Khushke", "latitude": 31.6685, "longitude": 65.67324},
#             {"name": "Dahi Sabzi", "latitude": 31.63333, "longitude": 65.58941},
#             {"name": "Dailawaran Kalacha", "latitude": 31.72848, "longitude": 65.71569},
#             {"name": "Dorahi", "latitude": 31.6963, "longitude": 65.62724},
#             {"name": "Faqeran Kalacha", "latitude": 31.62185, "longitude": 65.57887},
#             {"name": "Gul Kalacha", "latitude": 31.70335, "longitude": 65.69124},
#             {"name": "Haji Ali Mohammad Kalacha", "latitude": 31.62408, "longitude": 65.55323},
#             {"name": "Haji Fatta Mohammad Kalacha", "latitude": 31.6679, "longitude": 65.61188},
#             {"name": "Haji Malik Faiz Mohammad Kalacha", "latitude": 31.62594, "longitude": 65.56899},
#             {"name": "Haji Nazar Kalacha", "latitude": 31.62807, "longitude": 65.53581},
#             {"name": "Haji Noor Mohammad Kalacha", "latitude": 31.64427, "longitude": 65.61359},
#             {"name": "Haji Sameh Kalacha", "latitude": 31.68513, "longitude": 65.62557},
#             {"name": "Haji Satar Kalacha", "latitude": 31.71169, "longitude": 65.69652},
#             {"name": "Haji Toor Kalacha", "latitude": 31.71683, "longitude": 65.69315},
#             {"name": "Hajiyan Kala", "latitude": 31.64663, "longitude": 65.64577},
#             {"name": "Hazera", "latitude": 31.67867, "longitude": 65.6111},
#             {"name": "Jab Zar", "latitude": 31.68704, "longitude": 65.66904},
#             {"name": "Jaza", "latitude": 31.75508, "longitude": 65.71737},
#             {"name": "Jelawar", "latitude": 31.70137, "longitude": 65.6386},
#             {"name": "Jeledan", "latitude": 31.64844, "longitude": 65.64183},
#             {"name": "Khaleshak", "latitude": 31.65117, "longitude": 65.62467},
#             {"name": "Khana Gerdab", "latitude": 31.78028, "longitude": 65.74407},
#             {"name": "Khesrow Hulya", "latitude": 31.70335, "longitude": 65.66425},
#             {"name": "Khesrow Sufla", "latitude": 31.69558, "longitude": 65.65386},
#             {"name": "Khowja Malik Hulya", "latitude": 31.76676, "longitude": 65.75296},
#             {"name": "Khowja Malik Sufla", "latitude": 31.75891, "longitude": 65.74816},
#             {"name": "Kohak", "latitude": 31.64694, "longitude": 65.60743},
#             {"name": "Landa Taben", "latitude": 31.67433, "longitude": 65.65401},
#             {"name": "Langar", "latitude": 31.66075, "longitude": 65.66568},
#             {"name": "Loy Menara Hulya", "latitude": 31.66441, "longitude": 65.61536},
#             {"name": "Loy Menara Sufla", "latitude": 31.65905, "longitude": 65.60136},
#             {"name": "Maranjan", "latitude": 31.74243, "longitude": 65.7288},
#             {"name": "Mazreha", "latitude": 31.66496, "longitude": 65.67112},
#             {"name": "Mazreha Habas", "latitude": 31.69734, "longitude": 65.69127},
#             {"name": "Menara", "latitude": 31.66861, "longitude": 65.62871},
#             {"name": "Mir Abkhoran", "latitude": 31.6756, "longitude": 65.67591},
#             {"name": "Miyan Jowi", "latitude": 31.66274, "longitude": 65.65607},
#             {"name": "Mohammad Yaqoub Kalacha", "latitude": 31.73288, "longitude": 65.7216},
#             {"name": "Nagahan", "latitude": 31.64312, "longitude": 65.58211},
#             {"name": "Nar Rowza", "latitude": 31.65052, "longitude": 65.58087},
#             {"name": "Noor Mohammad Khan Kalacha", "latitude": 31.68594, "longitude": 65.63881},
#             {"name": "Noorzay Karaiz", "latitude": 31.75123, "longitude": 65.79419},
#             {"name": "Paitow", "latitude": 31.63077, "longitude": 65.54172},
#             {"name": "Sar Dahi Hulya", "latitude": 31.72003, "longitude": 65.70941},
#             {"name": "Sar Dahi Sufla", "latitude": 31.71033, "longitude": 65.68606},
#             {"name": "Sayidan", "latitude": 31.62707, "longitude": 65.58788},
#             {"name": "Sayidan Kalacha", "latitude": 31.720315, "longitude": 65.684435},
#             {"name": "Sediqe Kalacha", "latitude": 31.76929, "longitude": 65.77257},
#             {"name": "Shahtori", "latitude": 31.77378, "longitude": 65.73665},
#             {"name": "Shaikh Chala Hulya", "latitude": 31.69284, "longitude": 65.68839},
#             {"name": "Shaikh Chala Sufla", "latitude": 31.69213, "longitude": 65.66889},
#             {"name": "Shair Ahmad", "latitude": 31.63167, "longitude": 65.58224},
#             {"name": "Shewon Hulya", "latitude": 31.73886, "longitude": 65.70289},
#             {"name": "Shewon Sufla", "latitude": 31.72113, "longitude": 65.67626},
#             {"name": "Shewon Wasate", "latitude": 31.7294, "longitude": 65.68604},
#             {"name": "Taben", "latitude": 31.67525, "longitude": 65.64002},
#             {"name": "Taben Sufla", "latitude": 31.67098, "longitude": 65.63372},
#             {"name": "Yatemak Hulya", "latitude": 31.76832, "longitude": 65.74838},
#             {"name": "Yatemak Sufla", "latitude": 31.75975, "longitude": 65.74089}
#     ],
#         "Maruf": [
                
#             {"name": "Abdul Qadir Isahq Ghat Kalay", "latitude": 31.51428, "longitude": 67.46256},
#             {"name": "Khatni Zay", "latitude": 31.69846, "longitude": 67.22481},
#             {"name": "Mullah Khel Qala Rashid", "latitude": 31.5132, "longitude": 67.50817},
#             {"name": "Rab Kalay Akhund", "latitude": 31.50819, "longitude": 67.47925},
#             {"name": "Sayyid Wali Kalay", "latitude": 31.70387, "longitude": 67.3064},
#             {"name": "Warghar Kalay", "latitude": 31.58601, "longitude": 67.39402}

#         ],
#         "Spin Boldak": [
#                 {
#             "name": "Abdul Hakim Kalay Dad Mohammad Kalay",
#             "latitude": 31.09409,
#             "longitude": 66.62089
#         },
#         {
#             "name": "Abdul Karim",
#             "latitude": 31.06422,
#             "longitude": 66.41362
#         },
#         {
#             "name": "Abdullah Jan",
#             "latitude": 31.2949,
#             "longitude": 65.95549
#         },
#         {
#             "name": "Abdul Salam Kalay",
#             "latitude": 30.98127,
#             "longitude": 66.39733
#         },
#         {
#             "name": "Abdul Wahed Kalay",
#             "latitude": 30.99859,
#             "longitude": 66.36053
#         },
#         {
#             "name": "Abdul Wali Kalay",
#             "latitude": 30.97748,
#             "longitude": 66.51325
#         },
#         {
#             "name": "Abdul Zai Kalay",
#             "latitude": 31.22386,
#             "longitude": 65.96891
#         },
#         {
#             "name": "Aka Khail",
#             "latitude": 31.33647,
#             "longitude": 65.98369
#         },
#         {
#             "name": "Akhond Kaka Kalay",
#             "latitude": 31.18091,
#             "longitude": 66.49625
#         },
#         {
#             "name": "Akhond Zada Kalay",
#             "latitude": 31.31511,
#             "longitude": 65.94611
#         },
#         {
#             "name": "Akhtar Mohammad Kalay",
#             "latitude": 31.016725,
#             "longitude": 66.277505
#         },
#         {
#             "name": "Ali Jan",
#             "latitude": 30.99404,
#             "longitude": 66.16721
#         },
#         {
#             "name": "Alki Chena",
#             "latitude": 31.17538,
#             "longitude": 66.63021
#         },
#         {
#             "name": "Amir Mohammad Khan",
#             "latitude": 31.05513,
#             "longitude": 66.00858
#         },
#         {
#             "name": "Amir Tana Baidak",
#             "latitude": 31.22646,
#             "longitude": 66.26124
#         },
#         {
#             "name": "Anawi Kalay",
#             "latitude": 31.16309,
#             "longitude": 66.39033
#         },
#         {
#             "name": "Anzer Gay",
#             "latitude": 31.22137,
#             "longitude": 66.65192
#         },
#         {
#             "name": "Anzergay Kalay",
#             "latitude": 31.22685,
#             "longitude": 66.45107
#         },
#         {
#             "name": "Aqa Mohammad Jalal Jabar Kalay Qahraman",
#             "latitude": 30.86697,
#             "longitude": 66.25399
#         },
#         {
#             "name": "Azam Zai Kalay",
#             "latitude": 31.15864,
#             "longitude": 66.40648
#         },
#         {
#             "name": "Babek Sahib",
#             "latitude": 31.08772,
#             "longitude": 66.23055
#         },
#         {
#             "name": "Badam Kalay",
#             "latitude": 31.01442,
#             "longitude": 66.19531
#         },
#         {
#             "name": "Badeen Zai",
#             "latitude": 31.27532,
#             "longitude": 66.55164
#         },
#         {
#             "name": "Baesh Kalay",
#             "latitude": 31.1921,
#             "longitude": 66.63156
#         },
#         {
#             "name": "Bahader Zai",
#             "latitude": 31.07748,
#             "longitude": 66.16835
#         },
#         {
#             "name": "Bahder Zai",
#             "latitude": 31.1852,
#             "longitude": 66.33264
#         },
#         {
#             "name": "Baiz Anzergay",
#             "latitude": 31.20192,
#             "longitude": 66.67081
#         },
#         {
#             "name": "Bakari Kalay Khaday Rahim Kalay",
#             "latitude": 30.90784,
#             "longitude": 66.29385
#         },
#         {
#             "name": "Baqi Kalay",
#             "latitude": 30.991955,
#             "longitude": 66.37198
#         },
#         {
#             "name": "Barakat Kalay Mullah Dorani",
#             "latitude": 31.16358,
#             "longitude": 66.64855
#         },
#         {
#             "name": "Barjan Kalay",
#             "latitude": 31.2824,
#             "longitude": 65.94138
#         },
#         {
#             "name": "Beash Khala",
#             "latitude": 31.18864,
#             "longitude": 66.61099
#         },
#         {
#             "name": "Belal Abad",
#             "latitude": 30.97183,
#             "longitude": 66.4466
#         },
#         {
#             "name": "Burj Kalay",
#             "latitude": 31.08072,
#             "longitude": 66.45385
#         },
#         {
#             "name": "Chaghri Kalay",
#             "latitude": 31.33072,
#             "longitude": 65.88849
#         },
#         {
#             "name": "Chahel Gazi",
#             "latitude": 31.20743,
#             "longitude": 66.69027
#         },
#         {
#             "name": "Chawdaily Pote",
#             "latitude": 30.97383,
#             "longitude": 66.40704
#         },
#         {
#             "name": "Dabari",
#             "latitude": 31.12811,
#             "longitude": 66.24789
#         },
#         {
#             "name": "Dabari Burj Kala",
#             "latitude": 31.17881,
#             "longitude": 66.35438
#         },
#         {
#             "name": "Dadzai Kalay",
#             "latitude": 31.08392,
#             "longitude": 66.51004
#         },
#         {
#             "name": "Dahi Jalat Kalay",
#             "latitude": 31.07723,
#             "longitude": 66.53776
#         },
#         {
#             "name": "Dahi Wari Kalay",
#             "latitude": 31.179,
#             "longitude": 66.48504
#         },
#         {
#             "name": "Daman",
#             "latitude": 31.21097,
#             "longitude": 66.62586
#         },
#         {
#             "name": "Dokhuno Kalay Dost Mohammad",
#             "latitude": 31.22891,
#             "longitude": 66.11686
#         },
#         {
#             "name": "Fazel Karam Kalay",
#             "latitude": 31.09321,
#             "longitude": 66.53949
#         },
#         {
#             "name": "Galgari Matroka",
#             "latitude": 31.26813,
#             "longitude": 66.37005
#         },
#         {
#             "name": "Galgari Tawa",
#             "latitude": 31.26131,
#             "longitude": 66.37363
#         },
#         {
#             "name": "Garandi Kalay",
#             "latitude": 31.06545,
#             "longitude": 66.39038
#         },
#         {
#             "name": "Ghulam Nabi",
#             "latitude": 31.29748,
#             "longitude": 65.94621
#         },
#         {
#             "name": "Ghulam Sarwar",
#             "latitude": 31.13903,
#             "longitude": 65.97877
#         },
#         {
#             "name": "Goranda Kalay",
#             "latitude": 31.20211,
#             "longitude": 66.43732
#         },
#         {
#             "name": "Gul Kalay",
#             "latitude": 31.00739,
#             "longitude": 66.36702
#         },
#         {
#             "name": "Gul Mir Jan Darman",
#             "latitude": 31.05711,
#             "longitude": 66.14545
#         },
#         {
#             "name": "Gul Mohammad Ghulam Haidar Kalay",
#             "latitude": 31.1167,
#             "longitude": 66.59943
#         },
#         {
#             "name": "Gul Mohammad Ya Nazar Mohammad",
#             "latitude": 30.95714,
#             "longitude": 66.27658
#         },
#         {
#             "name": "Gulozai",
#             "latitude": 31.14012,
#             "longitude": 66.47721
#         },
#         {
#             "name": "Haji Abdul Razaq Kalay",
#             "latitude": 30.94238,
#             "longitude": 66.3956
#         },
#         {
#             "name": "Haji Abdul Wahed Kalay",
#             "latitude": 30.96001,
#             "longitude": 66.32956
#         },
#         {
#             "name": "Haji Ahmad Khan Kalay Zaren",
#             "latitude": 31.04864,
#             "longitude": 66.33775
#         },
#         {
#             "name": "Haji Fazil",
#             "latitude": 31.18528,
#             "longitude": 65.9473
#         },
#         {
#             "name": "Haji Ghulam Haidar Khan",
#             "latitude": 31.00289,
#             "longitude": 66.37157
#         },
#         {
#             "name": "Haji Habibullah Ghaows Mohammad",
#             "latitude": 31.04034,
#             "longitude": 66.38854
#         },
#         {
#             "name": "Haji Ibrahim Kalay",
#             "latitude": 31.1456,
#             "longitude": 66.27891
#         },
#         {
#             "name": "Haji Isahq Zai",
#             "latitude": 30.97391,
#             "longitude": 66.39847
#         },
#         {
#             "name": "Haji Jalal Kalay",
#             "latitude": 31.11472,
#             "longitude": 66.62921
#         },
#         {
#             "name": "Haji Jandu",
#             "latitude": 31.23532,
#             "longitude": 66.17175
#         },
#         {
#             "name": "Haji Khairo",
#             "latitude": 30.96154,
#             "longitude": 66.46219
#         },
#         {
#             "name": "Haji Kotan",
#             "latitude": 31.04333,
#             "longitude": 66.45161
#         },
#         {
#             "name": "Haji Mandi Kalay",
#             "latitude": 31.07865,
#             "longitude": 66.40423
#         },
#         {
#             "name": "Haji Mir Ahmad Khan",
#             "latitude": 31.14455,
#             "longitude": 65.95494
#         },
#         {
#             "name": "Haji Mir Wali Kalay",
#             "latitude": 31.02107,
#             "longitude": 66.43627
#         },
#         {
#             "name": "Haji Mir Zahe",
#             "latitude": 30.84708,
#             "longitude": 66.26198
#         },
#         {
#             "name": "Haji Mohammad Ekhlas Kalay",
#             "latitude": 30.83704,
#             "longitude": 66.30892
#         },
#         {
#             "name": "Haji Mohammad Fazel Mohammad Kalay",
#             "latitude": 31.06793,
#             "longitude": 66.41506
#         },
#         {
#             "name": "Haji Mohammad Khan",
#             "latitude": 31.11063,
#             "longitude": 66.04825
#         },
#         {
#             "name": "Haji Nasrula Kalay",
#             "latitude": 31.18278,
#             "longitude": 65.95872
#         },
#         {
#             "name": "Haji Nazar Mohammad Kalay",
#             "latitude": 31.24035,
#             "longitude": 65.97214
#         },
#         {
#             "name": "Haji Shah Mohammad Darman",
#             "latitude": 31.04877,
#             "longitude": 66.14394
#         },
#         {
#             "name": "Haji Shahtol Kalay",
#             "latitude": 31.13158,
#             "longitude": 66.34369
#         },
#         {
#             "name": "Haji Shair Jan Kalay",
#             "latitude": 30.86229,
#             "longitude": 66.28638
#         },
#         {
#             "name": "Haji Shir Kalay",
#             "latitude": 31.27481,
#             "longitude": 65.95602
#         },
#         {
#             "name": "Haji Wakil",
#             "latitude": 31.00968,
#             "longitude": 66.13851
#         },
#         {
#             "name": "Haji Wazer Kalay",
#             "latitude": 31.07272,
#             "longitude": 66.24693
#         },
#         {
#             "name": "Haji Yaqoub",
#             "latitude": 30.96241,
#             "longitude": 66.20556
#         },
#         {
#             "name": "Haji Zarif Bole",
#             "latitude": 31.11323,
#             "longitude": 66.28196
#         },
#         {
#             "name": "Halam Khan Zai",
#             "latitude": 31.17949,
#             "longitude": 66.46051
#         },
#         {
#             "name": "Hanefi Kalay Dawod Khan Kalay",
#             "latitude": 30.72177,
#             "longitude": 66.15612
#         },
#         {
#             "name": "Hanifya Kalay",
#             "latitude": 31.04237,
#             "longitude": 66.38145
#         },
#         {
#             "name": "Haq Dad Kalay",
#             "latitude": 31.21845,
#             "longitude": 65.97121
#         },
#         {
#             "name": "Hassan Zai Paro Karaiz",
#             "latitude": 31.17073,
#             "longitude": 66.34739
#         },
#         {
#             "name": "Hassan Zay",
#             "latitude": 31.18072,
#             "longitude": 65.97625
#         },
#         {
#             "name": "Hussain Zai",
#             "latitude": 31.29554,
#             "longitude": 66.4414
#         },
#         {
#             "name": "Hussain Zai Namaki Kalay",
#             "latitude": 31.09913,
#             "longitude": 66.3798
#         },
#             {"name": "Iqbal Khan Kalay", "latitude": 31.06462, "longitude": 66.4286},
#             {"name": "Isahq Zai", "latitude": 30.99704, "longitude": 66.13338},
#             {"name": "Jangal Sar Haji Shadi Zai", "latitude": 31.03125, "longitude": 66.13897},
#             {"name": "Jonobi Marsani Sangen", "latitude": 31.13068, "longitude": 66.65729},
#             {"name": "Kachi Kaku Zay", "latitude": 31.0363, "longitude": 66.03235},
#             {"name": "Kader Kalay", "latitude": 31.0331, "longitude": 66.23289},
#             {"name": "Kala Gay", "latitude": 31.15318, "longitude": 66.33902},
#             {"name": "Kamp Madena", "latitude": 30.9736, "longitude": 66.42778},
#             {"name": "Kamp Mahjeren Yaro", "latitude": 31.00269, "longitude": 66.38688},
#             {"name": "Kamp Nowi Hawame", "latitude": 30.99887, "longitude": 66.40164},
#             {"name": "Kamp Shalo Ya Alla Dukhtar", "latitude": 30.97672, "longitude": 66.41484},
#             {"name": "Kase Kalay", "latitude": 31.12503, "longitude": 66.5843},
#             {"name": "Khada Nazar", "latitude": 30.97337, "longitude": 66.37629},
#             {"name": "Khaday Rahem", "latitude": 30.9818, "longitude": 66.37278},
#             {"name": "Khairan", "latitude": 31.02967, "longitude": 66.17315},
#             {"name": "Khair Mohammad Kalay Loara Akhtar Zaye", "latitude": 31.26928, "longitude": 66.40117},
#             {"name": "Khal Gay", "latitude": 31.14613, "longitude": 66.31677},
#             {"name": "Khalifa Kalay", "latitude": 30.98677, "longitude": 66.50761},
#             {"name": "Khal Zai", "latitude": 31.25997, "longitude": 66.51419},
#             {"name": "Khan Sheren Kalay Mohammad Hawaz", "latitude": 30.89094, "longitude": 66.29415},
#             {"name": "Khar Bote", "latitude": 31.11016, "longitude": 66.58012},
#             {"name": "Khawaza Band Bala Kalay", "latitude": 31.18492, "longitude": 66.31868},
#             {"name": "Khowja Bakhtyar Choda", "latitude": 31.14268, "longitude": 66.40046},
#             {"name": "Khuday Dad", "latitude": 31.11282, "longitude": 66.02787},
#             {"name": "Khuday Rahm Wecha Kola", "latitude": 31.02328, "longitude": 66.60599},
#             {"name": "Kunje So Haji Ghafor", "latitude": 31.04005, "longitude": 66.57252},
#             {"name": "Kushta Kano Zai", "latitude": 31.24292, "longitude": 66.37268},
#             {"name": "Kushta Mil Haji Madad Kalay", "latitude": 31.08695, "longitude": 66.03967},
#             {"name": "Lakari", "latitude": 31.17444, "longitude": 66.59934},
#             {"name": "Landi Kalay", "latitude": 31.09204, "longitude": 66.56967},
#             {"name": "Landi Karaiz", "latitude": 31.18383, "longitude": 66.43686},
#             {"name": "Madeyan Kalay", "latitude": 31.12012, "longitude": 66.41196},
#             {"name": "Mahbob Khan Karaiz", "latitude": 31.15088, "longitude": 66.38957},
#             {"name": "Majlis Karaiz Kalay", "latitude": 31.23623, "longitude": 65.98787},
#             {"name": "Malik Mohammadulldin", "latitude": 31.02924, "longitude": 65.97752},
#             {"name": "Malik Zai", "latitude": 31.01695, "longitude": 66.3268},
#             {"name": "Markaz Loy Karaiz", "latitude": 31.17724, "longitude": 66.49005},
#             {"name": "Markaz Wolluswaly", "latitude": 31.31805, "longitude": 65.9628},
#             {"name": "Markaz Woluswally", "latitude": 31.00712, "longitude": 66.40204},
#             {"name": "Marsen Zai", "latitude": 31.10363, "longitude": 66.34362},
#             {"name": "Masala", "latitude": 31.18195, "longitude": 66.66638},
#             {"name": "Mashengazi", "latitude": 31.1128, "longitude": 66.50104},
#             {"name": "Masheng Zai", "latitude": 31.08837, "longitude": 66.38918},
#             {"name": "Mashi Kala", "latitude": 31.07045, "longitude": 66.32869},
#             {"name": "Matan Zai", "latitude": 31.08765, "longitude": 66.48719},
#             {"name": "Mawladad Kalay", "latitude": 31.03405, "longitude": 66.35722},
#             {"name": "Mawla Zay Pupal Zayi Kalay", "latitude": 31.19992, "longitude": 66.15376},
#             {"name": "Mese Zai Khuday Dad", "latitude": 31.02421, "longitude": 66.55551},
#             {"name": "Mikhanzai", "latitude": 30.98251, "longitude": 66.28367},
#             {"name": "Mil Karaiz", "latitude": 31.19463, "longitude": 66.06323},
#             {"name": "Mir Geyan", "latitude": 31.04802, "longitude": 66.27583},
#             {"name": "Mir Kalay", "latitude": 31.15151, "longitude": 66.36332},
#             {"name": "Mohammad Ahzam Wa Abdul Jabar Kalay", "latitude": 30.97862, "longitude": 66.4039},
#             {"name": "Mohammad Ayoub Kalay", "latitude": 30.98142, "longitude": 66.19782},
#             {"name": "Mohammad Azam Baqi Kalay", "latitude": 30.9792, "longitude": 66.5563},
#             {"name": "Mohammad Azam Kalay", "latitude": 31.03222, "longitude": 66.40838},
#             {"name": "Mohammad Mir Kalay", "latitude": 31.04429, "longitude": 66.42244},
#             {"name": "Mohammad Zahir Wa Gul Kalay", "latitude": 31.0095, "longitude": 66.161},
#             {"name": "Momin Khan Kalay", "latitude": 31.23057, "longitude": 65.98254},
#             {"name": "Mullah Abdul Razaq", "latitude": 31.03011, "longitude": 66.36376},
#             {"name": "Mullah Mohammad Umar Kalay", "latitude": 31.02096, "longitude": 66.36341},
#             {"name": "Mullah Nasruddin", "latitude": 31.28596, "longitude": 66.41046},
#             {"name": "Mullah Wali Waled", "latitude": 31.17788, "longitude": 66.57645},
#             {"name": "Mussa Khan", "latitude": 30.98597, "longitude": 66.36189},
#             {"name": "Mussa Khan Kalay Taj Mohammad", "latitude": 31.04407, "longitude": 66.38796},
#             {"name": "Nabi Dad Kalay", "latitude": 31.06839, "longitude": 66.37212},
#             {"name": "Nader Hamid Zai", "latitude": 30.98682, "longitude": 66.24069},
#             {"name": "Naido Kalay", "latitude": 31.11724, "longitude": 66.56772},
#             {"name": "Nasrat Afghan Kalay", "latitude": 30.99603, "longitude": 66.43984},

#     ],

#         "Daman": [
#             {"name": "Ahzam Kalay", "latitude": 31.64422, "longitude": 65.94175},
#             {"name": "Akhund Zada Kalay", "latitude": 31.71812, "longitude": 66.18801},
#             {"name": "Akhund Zada Sahib", "latitude": 31.7031, "longitude": 66.167},
#             {"name": "Ali Abad", "latitude": 31.7387, "longitude": 65.92142},
#             {"name": "Ali Zay", "latitude": 31.42325, "longitude": 65.92299},
#             {"name": "Anzirgay", "latitude": 31.77652, "longitude": 65.97012},
#             {"name": "Arhat Kalay", "latitude": 31.68236, "longitude": 66.01269},
#             {"name": "Awme", "latitude": 31.76115, "longitude": 65.93248},
#             {"name": "Bariki", "latitude": 31.69023, "longitude": 65.96822},
#             {"name": "Bashar Kalay", "latitude": 31.42243, "longitude": 65.95309},
#             {"name": "Bawary", "latitude": 31.69753, "longitude": 65.88339},
#             {"name": "Baz Mohammad Khan Kalay", "latitude": 31.64663, "longitude": 65.94916},
#             {"name": "Biyaban Dara", "latitude": 31.44774, "longitude": 65.92235},
#             {"name": "Biyabani Kalay", "latitude": 31.62404, "longitude": 66.15417},
#             {"name": "Burj", "latitude": 31.77743, "longitude": 66.03359},
#             {"name": "Bustan", "latitude": 31.66082, "longitude": 65.88018},
#             {"name": "Chahar Band", "latitude": 31.70889, "longitude": 65.9515},
#             {"name": "Daman Markaz Wolluswaly", "latitude": 31.61877, "longitude": 65.89522},
#             {"name": "Dayi Kalay", "latitude": 31.45528, "longitude": 65.92003},
#             {"name": "Gari Kalay", "latitude": 31.74175, "longitude": 66.00381},
#             {"name": "Ghaybi Qalacha", "latitude": 31.63002, "longitude": 65.85702},
#             {"name": "Haino Kalay", "latitude": 31.6356, "longitude": 65.84224},
#             {"name": "Haji Dahi", "latitude": 31.40741, "longitude": 65.88261},
#             {"name": "Haji Ghafar", "latitude": 31.62136, "longitude": 65.92718},
#             {"name": "Haji Lal Bik", "latitude": 31.72059, "longitude": 65.99262},
#             {"name": "Haji Shir Kalay", "latitude": 31.41146, "longitude": 65.93457},
#             {"name": "Hakim Kalay", "latitude": 31.4741, "longitude": 65.88325},
#             {"name": "Hijran Kalay", "latitude": 31.70905, "longitude": 65.88173},
#             {"name": "Hindo Karaiz", "latitude": 31.75218, "longitude": 66.23253},
#             {"name": "Hudud Kalacha", "latitude": 31.64268, "longitude": 65.96854},
#             {"name": "Kakaranu Kalacha", "latitude": 31.54164, "longitude": 65.90783},
#             {"name": "Khairati", "latitude": 31.77808, "longitude": 65.94938},
#             {"name": "Khaliq Dad", "latitude": 31.63602, "longitude": 65.89095},
#             {"name": "Khan Mohammad Wa Sher Mohammad Karaiz", "latitude": 31.64266, "longitude": 66.20167},
#             {"name": "Khwazhkay Kalay", "latitude": 31.63066, "longitude": 66.1333},
#             {"name": "Kuchni Karaiz", "latitude": 31.72753, "longitude": 66.05611},
#             {"name": "Kumana Karaiz", "latitude": 31.70117, "longitude": 66.01724},
#             {"name": "Kushta Mir Sanzai Kalacha", "latitude": 31.66442, "longitude": 66.12243},
#             {"name": "Kushta Mir Sanzai Kalay", "latitude": 31.62683, "longitude": 66.09825},
#             {"name": "Landi Kalay", "latitude": 31.46148, "longitude": 65.91794},
#             {"name": "Landi Karaiz", "latitude": 31.65167, "longitude": 65.91918},
#             {"name": "Maduzay Kalay", "latitude": 31.57442, "longitude": 66.04057},
#             {"name": "Makyan", "latitude": 31.41604, "longitude": 66.01852},
#             {"name": "Malakhi Ghundi", "latitude": 31.43873, "longitude": 65.95446},
#             {"name": "Malang Karaiz", "latitude": 31.64739, "longitude": 65.83752},
#             {"name": "Mandisyar", "latitude": 31.54531, "longitude": 65.8548},
#             {"name": "Mawlana Kalay", "latitude": 31.63437, "longitude": 66.15359},
#             {"name": "Mishi", "latitude": 31.75823, "longitude": 65.9604},
#             {"name": "Miyana Jakan", "latitude": 31.74163, "longitude": 66.13016},
#             {"name": "Miyanji Kalay", "latitude": 31.68413, "longitude": 66.09146},
#             {"name": "Mohammad Anwar Kalacha", "latitude": 31.57257, "longitude": 65.87464},
#             {"name": "Mohmand", "latitude": 31.59001, "longitude": 65.89965},
#             {"name": "Mullayan", "latitude": 31.6292, "longitude": 65.87842},
#             {"name": "Murghankicha", "latitude": 31.53345, "longitude": 65.96764},
#             {"name": "Najuyi", "latitude": 31.61007, "longitude": 65.9708},
#             {"name": "Nawi Dahi", "latitude": 31.513855, "longitude": 65.92016},
#             {"name": "Nazar Kalacha", "latitude": 31.68949, "longitude": 65.95133},
#             {"name": "Paiy Jakan", "latitude": 31.73592, "longitude": 66.11234},
#             {"name": "Pangay", "latitude": 31.60846, "longitude": 66.02677},
#             {"name": "Popal Zay Mohammad Rafiq Kalacha", "latitude": 31.5281, "longitude": 65.85497},
#             {"name": "Poul Tarank", "latitude": 31.55792, "longitude": 65.84438},
#             {"name": "Sahib Zada Kalacha", "latitude": 31.6099, "longitude": 65.87459},
#             {"name": "Salam Kalacha", "latitude": 31.66451, "longitude": 65.93479},
#             {"name": "Samul Zay", "latitude": 31.71295, "longitude": 66.21022},
#             {"name": "Sangar Ganj", "latitude": 31.67542, "longitude": 65.96808},
#             {"name": "Sara Kala", "latitude": 31.64963, "longitude": 66.17465},
#             {"name": "Sar Jakan", "latitude": 31.76176, "longitude": 66.1342},
#             {"name": "Sar Pali Kalay", "latitude": 31.73858, "longitude": 65.95276},
#             {"name": "Saydan Kalacha", "latitude": 31.62333, "longitude": 66.01452},
#             {"name": "Sayid Abad", "latitude": 31.68287, "longitude": 66.16897},
#             {"name": "Sayyid Akbar Shah", "latitude": 31.74483, "longitude": 66.2686},
#             {"name": "Sayyidan Kalay", "latitude": 31.45397, "longitude": 65.9332},
#             {"name": "Shah Dad Kalay", "latitude": 31.6763, "longitude": 65.94024},
#             {"name": "Shakur Kalay", "latitude": 31.69816, "longitude": 65.82682},
#             {"name": "Sher Ali Khan", "latitude": 31.73152, "longitude": 66.26586},
#             {"name": "Spin Waya", "latitude": 31.63265, "longitude": 66.0132},
#             {"name": "Sur Karaiz", "latitude": 31.72113, "longitude": 65.96306},
#             {"name": "Taryu", "latitude": 31.63319, "longitude": 65.89752},
#             {"name": "Yawari Hinayat", "latitude": 31.70244, "longitude": 65.93444},
#             {"name": "Zan Abad", "latitude": 31.74922, "longitude": 65.95967},
#             {"name": "Zangi", "latitude": 31.71516, "longitude": 66.22648}
#         ],
#         "Arghistan": [
#             {"name": "Akhtar Zai Noor Mohammad Kalay", "latitude": 31.32958, "longitude": 66.16542},
#             {"name": "Baba Ali", "latitude": 31.38975, "longitude": 66.2052},
#             {"name": "Bagh Kalay Amir Mohammad Landay Shadi Khan", "latitude": 31.40311, "longitude": 66.08506},
#             {"name": "Din Mohammad Kalay", "latitude": 31.31726, "longitude": 66.18218},
#             {"name": "Fazil Karam", "latitude": 31.32627, "longitude": 66.2009},
#             {"name": "Ghabarga", "latitude": 31.35377, "longitude": 66.19105},
#             {"name": "Haji Akhtar Zay", "latitude": 31.36806, "longitude": 66.19948},
#             {"name": "Loy Kalay", "latitude": 31.36665, "longitude": 66.28148},
#             {"name": "Makh Kalay", "latitude": 31.3732, "longitude": 66.27291},
#             {"name": "Patkay Hulya", "latitude": 31.38761, "longitude": 66.12366},
#             {"name": "Patkay Sufla", "latitude": 31.36703, "longitude": 66.08718},
#             {"name": "Payianda Kalay", "latitude": 31.78426, "longitude": 66.74429},
#             {"name": "Sapar Zay Kalay", "latitude": 31.36702, "longitude": 66.26151},
#             {"name": "Shah Kalay", "latitude": 31.3718, "longitude": 66.28518}
#     ],
#         "Panjwayi": [
#             {"name": "Abdul Rashid Kalacha", "latitude": 31.50075, "longitude": 65.54991},
#                 {"name": "Abdul Rauf Kalacha", "latitude": 31.4873, "longitude": 65.36791},
#                 {"name": "Achakzo Wa Biyabanak", "latitude": 31.46564, "longitude": 65.37633},
#                 {"name": "Achakzo Wa Kakaran", "latitude": 31.44784, "longitude": 65.34815},
#                 {"name": "Achk Zai", "latitude": 31.512, "longitude": 65.46006},
#                 {"name": "Adam Zai", "latitude": 31.48357, "longitude": 65.5318},
#                 {"name": "Aleko Zaye", "latitude": 31.46675, "longitude": 65.3636},
#                 {"name": "Alokuzay", "latitude": 31.52348, "longitude": 65.49636},
#                 {"name": "Armada", "latitude": 31.53514, "longitude": 65.46742},
#                 {"name": "Ashraf", "latitude": 31.43175, "longitude": 65.45047},
#                 {"name": "Askicha", "latitude": 31.51332, "longitude": 65.42899},
#                 {"name": "Badizu", "latitude": 31.53088, "longitude": 65.54624},
#                 {"name": "Badwan", "latitude": 31.57334, "longitude": 65.48446},
#                 {"name": "Bahadur", "latitude": 31.50263, "longitude": 65.49707},
#                 {"name": "Bala Dahi Bala", "latitude": 31.53542, "longitude": 65.59568},
#                 {"name": "Balambi", "latitude": 31.46132, "longitude": 65.36858},
#                 {"name": "Baluchan", "latitude": 31.54251, "longitude": 65.49311},
#                 {"name": "Baluchan Kalay", "latitude": 31.45829, "longitude": 65.32607},
#                 {"name": "Baluchan Mushan", "latitude": 31.46436, "longitude": 65.26369},
#                 {"name": "Bilandi", "latitude": 31.52895, "longitude": 65.60231},
#                 {"name": "Biyabanak Mushan", "latitude": 31.45823, "longitude": 65.27083},
#                 {"name": "Chaka Naw Masum Khan", "latitude": 31.47576, "longitude": 65.33035},
#                 {"name": "Chirgano Kor", "latitude": 31.49749, "longitude": 65.41122},
#                 {"name": "Dabak", "latitude": 31.51348, "longitude": 65.42082},
#                 {"name": "Dahimrasi", "latitude": 31.54115, "longitude": 65.49923},
#                 {"name": "Do Ab", "latitude": 31.47207, "longitude": 65.23797},
#                 {"name": "Faqir Zai", "latitude": 31.51614, "longitude": 65.59006},
#                 {"name": "Farsibanan", "latitude": 31.46835, "longitude": 65.32353},
#                 {"name": "Fattah Khan", "latitude": 31.45198, "longitude": 65.41383},
#                 {"name": "Fattihullah", "latitude": 31.52492, "longitude": 65.56879},
#                 {"name": "Garandi", "latitude": 31.45493, "longitude": 65.36528},
#                 {"name": "Haji Abdul", "latitude": 31.5156, "longitude": 65.46185},
#                 {"name": "Haji Abdulhaq Kalacha", "latitude": 31.43711, "longitude": 65.32585},
#                 {"name": "Haji Abdulrahman", "latitude": 31.50798, "longitude": 65.43433},
#                 {"name": "Haji Baluch Kalacha", "latitude": 31.45256, "longitude": 65.33103},
#                 {"name": "Haji Habibullah", "latitude": 31.52429, "longitude": 65.45166},
#                 {"name": "Haji Kakar", "latitude": 31.4676, "longitude": 65.332},
#                 {"name": "Haji Khiro", "latitude": 31.47405, "longitude": 65.33886},
#                 {"name": "Haji Mohammad Yusuf", "latitude": 31.47329, "longitude": 65.36594},
#                 {"name": "Haji Obidullah", "latitude": 31.51323, "longitude": 65.43535},
#                 {"name": "Haji Rahmatullah", "latitude": 31.48767, "longitude": 65.35248},
#                 {"name": "Haji Salam Khan", "latitude": 31.49794, "longitude": 65.42544},
#                 {"name": "Haji Wali Mohammad", "latitude": 31.51605, "longitude": 65.44003},
#                 {"name": "Kakaran", "latitude": 31.50702, "longitude": 65.431005},
#                 {"name": "Kalacha", "latitude": 31.52065, "longitude": 65.47456},
#                 {"name": "Kamp Mahajerin Mando Zai", "latitude": 31.4751, "longitude": 65.19804},
#                 {"name": "Kamp Mahjeren", "latitude": 31.47758, "longitude": 65.27564},
#                 {"name": "Kano Zai", "latitude": 31.46266, "longitude": 65.23075},
#                 {"name": "Kharot", "latitude": 31.58953, "longitude": 65.53806},
#                 {"name": "Khinjigak", "latitude": 31.46977, "longitude": 65.52331},
#                 {"name": "Khuganyan", "latitude": 31.47566, "longitude": 65.3727},
#                 {"name": "Kishkak", "latitude": 31.48022, "longitude": 65.35387},
#                 {"name": "Kochni Chalghor", "latitude": 31.54469, "longitude": 65.56493},
#                 {"name": "Kuchni Sayyidan", "latitude": 31.49396, "longitude": 65.37966},
#                 {"name": "Kundyanu Kalay", "latitude": 31.52355, "longitude": 65.44125},
#                 {"name": "Kunjak Wa Azim", "latitude": 31.45666, "longitude": 65.26203},
#                 {"name": "Lagari", "latitude": 31.47277, "longitude": 65.38608},
#                 {"name": "Lahl Khan Kalay", "latitude": 31.49664, "longitude": 65.5254},
#                 {"name": "Lolara", "latitude": 31.49787, "longitude": 65.39119},
#                 {"name": "Lor Salihan", "latitude": 31.57035, "longitude": 65.54611},
#                 {"name": "Loy Chalghor", "latitude": 31.53483, "longitude": 65.5577},
#                 {"name": "Loy Sayyidan", "latitude": 31.4826, "longitude": 65.38175},
#                 {"name": "Madrasa", "latitude": 31.55828, "longitude": 65.4783},
#                 {"name": "Mahajirin", "latitude": 31.53236, "longitude": 65.52299},
#                 {"name": "Markaz Panjwayi", "latitude": 31.54537, "longitude": 65.45305},
#                 {"name": "Mazangan", "latitude": 31.50518, "longitude": 65.54598},
#                 {"name": "Miral Zai", "latitude": 31.50585, "longitude": 65.53197},
#                 {"name": "Mobin Shah Agha", "latitude": 31.49121, "longitude": 65.37282},
#                 {"name": "Mohammad Akram Kalay", "latitude": 31.5312, "longitude": 65.46188},
#                 {"name": "Mohammad Gul Kakaran", "latitude": 31.46608, "longitude": 65.31615},
#                 {"name": "Mohammad Koh", "latitude": 31.489, "longitude": 65.36251},
#                 {"name": "Mohammad Sidiq", "latitude": 31.46403, "longitude": 65.27258},
#                 {"name": "Mullah Abdulghani", "latitude": 31.47205, "longitude": 65.31924},
#                 {"name": "Mullah Abdulrahman", "latitude": 31.51788, "longitude": 65.45094},
#                 {"name": "Mullah Abdulrahman Akhund", "latitude": 31.50732, "longitude": 65.42772},
#                 {"name": "Mullah Ahmad Kalay", "latitude": 31.45838, "longitude": 65.33044},
#                 {"name": "Mullah Dost", "latitude": 31.43123, "longitude": 65.49685},
#                 {"name": "Mullah Hassan Akhund Khushkyan", "latitude": 31.48231, "longitude": 65.34703},
#                 {"name": "Mushan (Sayyidan)", "latitude": 31.46042, "longitude": 65.26226},
#                 {"name": "Mussa Kalim", "latitude": 31.46837, "longitude": 65.49584},
#                 {"name": "Mussa Khan", "latitude": 31.49859, "longitude": 65.43533},
#                 {"name": "Nachar", "latitude": 31.52993, "longitude": 65.44313},
#                 {"name": "Nahan Zai", "latitude": 31.48925, "longitude": 65.39425},
#                 {"name": "Nahr Kalay", "latitude": 31.61023, "longitude": 65.55431},
#                 {"name": "Nakhuni", "latitude": 31.50739, "longitude": 65.56939},
#                 {"name": "Naw Ruz Kalay", "latitude": 31.4971, "longitude": 65.55156},
#                 {"name": "Nayib Kheil", "latitude": 31.46001, "longitude": 65.30387},
#                 {"name": "Nowrozi", "latitude": 31.59892, "longitude": 65.54846},
#                 {"name": "Pay Malluk", "latitude": 31.50575, "longitude": 65.41133},
#                 {"name": "Qasem Rabat", "latitude": 31.4751, "longitude": 65.4635},
#                 {"name": "Rigi", "latitude": 31.4839, "longitude": 65.43908},
#                 {"name": "Rigu Hulya", "latitude": 31.45161, "longitude": 65.5095},
#                 {"name": "Rigu Sufla", "latitude": 31.4422, "longitude": 65.51712},
#                 {"name": "Salawat Hulya", "latitude": 31.51798, "longitude": 65.54286},
#                 {"name": "Salawat Sufla", "latitude": 31.51755, "longitude": 65.52758},
#                 {"name": "Salihan", "latitude": 31.55392, "longitude": 65.53928},
#                 {"name": "Salu Aka Kalay", "latitude": 31.45166, "longitude": 65.27233},
#                 {"name": "Sami Zayi", "latitude": 31.48055, "longitude": 65.37535},
#                 {"name": "Sardaran", "latitude": 31.53047, "longitude": 65.45554},
#                 {"name": "Sayyida Khan", "latitude": 31.45367, "longitude": 65.38993},
#                 {"name": "Sayyid Kalacha", "latitude": 31.55192, "longitude": 65.56592},
#                 {"name": "Sayyid Rustam", "latitude": 31.47206, "longitude": 65.29315},
#                 {"name": "Shaikh Qalandar Baba", "latitude": 31.51823, "longitude": 65.42728},
#                 {"name": "Spin Midan", "latitude": 31.52044, "longitude": 65.4178},
#                 {"name": "Sultan Mohammad", "latitude": 31.49448, "longitude": 65.40254},
#                 {"name": "Tulukan", "latitude": 31.44277, "longitude": 65.31471},
#                 {"name": "Wakil Rustam Kalay", "latitude": 31.44698, "longitude": 65.30395},
#                 {"name": "Yaru Kalay", "latitude": 31.45183, "longitude": 65.52685},
#                 {"name": "Zala Dahi", "latitude": 31.60595, "longitude": 65.53949},
#                 {"name": "Zila Khan", "latitude": 31.52881, "longitude": 65.59026}
#         ],
#         "Maywand": [
#             {"name": "Abdullah Akhond Zada Kalay", "latitude": 31.53463, "longitude": 65.05457},
#             {"name": "Abdul Salam Kalay", "latitude": 31.52085, "longitude": 65.10004},
#             {"name": "Agha Khailo Kalay", "latitude": 31.57388, "longitude": 64.84946},
#             {"name": "Agha Mir Karaiz", "latitude": 31.61741, "longitude": 64.88323},
#             {"name": "Ahmad Jan Kalay", "latitude": 31.53054, "longitude": 64.99017},
#             {"name": "Airan", "latitude": 31.82735, "longitude": 65.067},
#             {"name": "Akbari Wala", "latitude": 31.49607, "longitude": 64.91044},
#             {"name": "Akhtari", "latitude": 31.62486, "longitude": 64.90694},
#             {"name": "Akhtar Khailo", "latitude": 31.53633, "longitude": 64.90314},
#             {"name": "Ali Abad", "latitude": 31.78318, "longitude": 65.04398},
#             {"name": "Amanat", "latitude": 31.76877, "longitude": 64.87837},
#             {"name": "Anjeran", "latitude": 31.89422, "longitude": 64.87621},
#             {"name": "Asoda Kalay", "latitude": 31.54704, "longitude": 65.0921},
#             {"name": "Atta Mohammad Karaiz", "latitude": 31.53128, "longitude": 65.16159},
#             {"name": "Azim Jan Karaiz", "latitude": 31.51811, "longitude": 65.23628},
#             {"name": "Aziz Abad", "latitude": 31.64652, "longitude": 65.0462},
#             {"name": "Babe Karaiz", "latitude": 31.5357, "longitude": 65.02913},
#             {"name": "Baberan", "latitude": 31.535605, "longitude": 65.019875},
#             {"name": "Bado Zai", "latitude": 31.53146, "longitude": 64.96974},
#             {"name": "Bahlol Zai", "latitude": 31.53074, "longitude": 64.94358},
#             {"name": "Balagh Kalay", "latitude": 31.80043, "longitude": 65.06644},
#             {"name": "Barang", "latitude": 31.7453, "longitude": 64.92106},
#             {"name": "Beyabanak", "latitude": 31.60501, "longitude": 64.95628},
#             {"name": "Chahel Gazi", "latitude": 31.60557, "longitude": 65.04756},
#             {"name": "Chashma", "latitude": 31.52784, "longitude": 65.01379},
#             {"name": "China", "latitude": 31.79904, "longitude": 65.08356},
#             {"name": "Choka Zai", "latitude": 31.52826, "longitude": 64.8964},
#             {"name": "Cholawak", "latitude": 31.62664, "longitude": 64.88514},
#             {"name": "Dab Karaiz", "latitude": 31.89854, "longitude": 64.81437},
#             {"name": "Dahi Qabad", "latitude": 31.49104, "longitude": 65.23667},
#             {"name": "Daka", "latitude": 31.81855, "longitude": 65.07006},
#             {"name": "Dar Weza", "latitude": 31.543, "longitude": 64.98845},
#             {"name": "Dewal Kala", "latitude": 31.54832, "longitude": 64.93301},
#             {"name": "Doli", "latitude": 31.60418, "longitude": 64.79004},
#             {"name": "Eashq Abad", "latitude": 31.64788, "longitude": 65.07148},
#             {"name": "Gach Karaiz", "latitude": 31.64263, "longitude": 64.97507},
#             {"name": "Gadiyan", "latitude": 31.60688, "longitude": 64.79954},
#             {"name": "Garmab", "latitude": 31.80517, "longitude": 64.90333},
#             {"name": "Garmabak Jonobi", "latitude": 31.76585, "longitude": 64.98494},
#             {"name": "Garmabak Shamaly", "latitude": 31.76474, "longitude": 64.95428},
#             {"name": "Ghona Che", "latitude": 31.65608, "longitude": 64.89673},
#             {"name": "Gondi Khail", "latitude": 31.59749, "longitude": 64.8021},
#             {"name": "Haji Habibullah Kalay", "latitude": 31.51705, "longitude": 65.07984},
#             {"name": "Haji Honar Kas", "latitude": 31.51077, "longitude": 65.12455},
#             {"name": "Haji Khail Karaiz", "latitude": 31.54848, "longitude": 64.9034},
#             {"name": "Haji Mir Afzal Kalay", "latitude": 31.88216, "longitude": 64.81183},
#             {"name": "Haji Mohammad Khan Kalay", "latitude": 31.5196, "longitude": 65.09464},
#             {"name": "Haji Mohammad Shah Kalay", "latitude": 31.51812, "longitude": 65.11724},
#             {"name": "Haji Taj Mohammad Karaiz", "latitude": 31.77092, "longitude": 64.90325},
#             {"name": "Hamid Karaiz", "latitude": 31.51789, "longitude": 65.14274},
#             {"name": "Hassan Abad", "latitude": 31.599, "longitude": 65.05895},
#             {"name": "Hotal", "latitude": 31.61726, "longitude": 65.05987},
#             {"name": "Jow Kari", "latitude": 31.51765, "longitude": 65.15115},
#             {"name": "Kafer Shagay", "latitude": 31.50604, "longitude": 64.8791},
#             {"name": "Kakaran", "latitude": 31.53089, "longitude": 64.95271},
#             {"name": "Kala Khan Kalay", "latitude": 31.77128, "longitude": 65.00455},
#             {"name": "Kalfak", "latitude": 31.7806, "longitude": 64.87943},
#             {"name": "Kamo Zai", "latitude": 31.53559, "longitude": 64.9098},
#             {"name": "Karaizak", "latitude": 31.63933, "longitude": 65.044907},
#             {"name": "Karaizak Mohammad Azim", "latitude": 31.76227, "longitude": 64.9103},
#             {"name": "Karaiz Wal", "latitude": 31.56462, "longitude": 64.85856},
#             {"name": "Kari Khail", "latitude": 31.63812, "longitude": 64.86772},
#             {"name": "Kazha Karaiz", "latitude": 31.70271, "longitude": 64.84218},
#             {"name": "Khaig Karaiz", "latitude": 31.72946, "longitude": 65.10166},
#             {"name": "Khak Chopan", "latitude": 31.67825, "longitude": 64.89637},
#             {"name": "Khaly Zar", "latitude": 31.7661, "longitude": 64.86206},
#             {"name": "Khano Khail", "latitude": 31.54444, "longitude": 64.87402},
#             {"name": "Khazan Kalay", "latitude": 31.63093, "longitude": 65.08066},
#             {"name": "Khogyani", "latitude": 31.64076, "longitude": 64.91801},
#             {"name": "Khosh Khaliq", "latitude": 31.60512, "longitude": 65.06274},
#             {"name": "Koriz Kalay", "latitude": 31.54684, "longitude": 64.97257},
#             {"name": "Koy Kak", "latitude": 31.58108, "longitude": 64.83406},
#             {"name": "Kushk Nakhod", "latitude": 31.62346, "longitude": 65.05192},
#             {"name": "Lahl Mohammad Kalay", "latitude": 31.63985, "longitude": 64.82769},
#             {"name": "Lala Zai", "latitude": 31.65383, "longitude": 64.85926},
#             {"name": "Landi", "latitude": 31.59755, "longitude": 65.04187},
#             {"name": "Landi Karaiz", "latitude": 31.60097, "longitude": 64.97707},
#             {"name": "Loy Kalay", "latitude": 31.51263, "longitude": 64.91791},
#             {"name": "Loy Karaiz", "latitude": 31.58014, "longitude": 65.04953},
#             {"name": "Magat", "latitude": 31.51808, "longitude": 65.22628},
#             {"name": "Mahmod Abad", "latitude": 31.71698, "longitude": 65.08803},
#             {"name": "Mahmod Khail", "latitude": 31.53871, "longitude": 64.91727},
#             {"name": "Mahsom Karaiz", "latitude": 31.8038, "longitude": 64.85774},
#             {"name": "Maiwand Chashma", "latitude": 31.74664, "longitude": 65.12872},
#             {"name": "Maiwand Karaiz", "latitude": 31.73147, "longitude": 65.12984},
#             {"name": "Mako Kalay", "latitude": 31.61072, "longitude": 64.966},
#             {"name": "Maly Khail", "latitude": 31.55863, "longitude": 64.84046},
#             {"name": "Mama Karaiz", "latitude": 31.53186, "longitude": 65.18432},
#             {"name": "Mando Zai", "latitude": 31.4981, "longitude": 65.20846},
#             {"name": "Mansor Kalay", "latitude": 31.53786, "longitude": 64.98543},
#             {"name": "Mazreha", "latitude": 31.62012, "longitude": 65.0378},
#             {"name": "Meya Karaiz", "latitude": 31.52355, "longitude": 65.19408},
#             {"name": "Mira Khor", "latitude": 31.50389, "longitude": 65.23208},
#             {"name": "Mohammad Ayoub Karaiz", "latitude": 31.87307, "longitude": 64.81066},
#             {"name": "Mohammad Halam Kalay", "latitude": 31.51552, "longitude": 65.15472},
#             {"name": "Mohammad Moseh Kalay", "latitude": 31.62857, "longitude": 65.0297},
#             {"name": "Mohsen Khan Kalay", "latitude": 31.63281, "longitude": 65.04142},
#             {"name": "Moshak", "latitude": 31.68162, "longitude": 65.05581},
#             {"name": "Murcha", "latitude": 31.61994, "longitude": 65.04399},
#             {"name": "Naik Karaiz", "latitude": 31.75935, "longitude": 64.79119},
#             {"name": "Naso Kalay", "latitude": 31.6413, "longitude": 65.02819},
#             {"name": "Nasrullah Khan Kalay", "latitude": 31.63874, "longitude": 64.92231},
#             {"name": "Nokar Khail", "latitude": 31.54026, "longitude": 64.89075},
#             {"name": "Noor Zai", "latitude": 31.55397, "longitude": 64.94129},
#             {"name": "Now Abad", "latitude": 31.692905, "longitude": 65.0192},
#             {"name": "Now Abad Lala Zai", "latitude": 31.67834, "longitude": 64.86934},
#             {"name": "Nowi Kas", "latitude": 31.51049, "longitude": 65.14467},
#             {"name": "Nowi Wialay", "latitude": 31.53091, "longitude": 64.93803},
#             {"name": "Pada", "latitude": 31.86694, "longitude": 64.86207},
#             {"name": "Pair Zada", "latitude": 31.60908, "longitude": 65.06707},
#             {"name": "Payen Kala", "latitude": 31.52014, "longitude": 65.13153},
#             {"name": "Qala Gay", "latitude": 31.64368, "longitude": 64.89665},
#             {"name": "Qala Khowja Mohammad Khan", "latitude": 31.53143, "longitude": 65.20372},
#             {"name": "Qazi Karaiz", "latitude": 31.67452, "longitude": 64.93486},
#             {"name": "Rangraizan", "latitude": 31.51132, "longitude": 65.18206},
#             {"name": "Sanger", "latitude": 31.7717, "longitude": 64.87007},
#             {"name": "Sar Boland", "latitude": 31.50946, "longitude": 65.04914},
#             {"name": "Sar Kari Kalay", "latitude": 31.6518, "longitude": 64.94305},
#             {"name": "Sarwar Karaiz", "latitude": 31.57328, "longitude": 65.0564},
#             {"name": "Sayban", "latitude": 31.63929, "longitude": 65.03091},
#             {"name": "Sayd Khan Kalay", "latitude": 31.86567, "longitude": 64.82609},
#             {"name": "Sayid Ahmad Jan Kalay", "latitude": 31.51516, "longitude": 65.16628},
#             {"name": "Shabaz", "latitude": 31.63796, "longitude": 65.05819},
#             {"name": "Shado Qalat", "latitude": 31.63664, "longitude": 65.01997},
#             {"name": "Shaghasi", "latitude": 31.51188, "longitude": 65.02523},
#             {"name": "Shakh Ghazay", "latitude": 31.62578, "longitude": 65.08037},
#             {"name": "Shakotay", "latitude": 31.63741, "longitude": 65.01008},
#             {"name": "Shamali Darya", "latitude": 31.62329, "longitude": 65.02991},
#             {"name": "Shari Kalay", "latitude": 31.58882, "longitude": 64.83822},
#             {"name": "Sher Ali", "latitude": 31.57532, "longitude": 65.05627},
#             {"name": "Sher Jan", "latitude": 31.54632, "longitude": 65.09325},
#             {"name": "Sher Mohammad Zai", "latitude": 31.6118, "longitude": 65.04454},
#             {"name": "Shna Ghazay", "latitude": 31.58623, "longitude": 64.96661},
#             {"name": "Shor Ab", "latitude": 31.53494, "longitude": 65.01238},
#             {"name": "Showa", "latitude": 31.63119, "longitude": 64.86703},
#             {"name": "Shurabak", "latitude": 31.60323, "longitude": 64.81422},
#             {"name": "Sia Khan", "latitude": 31.62067, "longitude": 64.93428},
#             {"name": "Siah Sang", "latitude": 31.76895, "longitude": 64.92761},
#             {"name": "Sir Sang", "latitude": 31.50454, "longitude": 65.17035},
#             {"name": "Sorkay", "latitude": 31.61686, "longitude": 65.03924},
#             {"name": "Sufla Chashma", "latitude": 31.57972, "longitude": 65.04203},
#             {"name": "Taghano", "latitude": 31.53445, "longitude": 65.16541},
#             {"name": "Tajaka", "latitude": 31.5708, "longitude": 64.89459},
#             {"name": "Takhta Pul", "latitude": 31.6426, "longitude": 64.98658},
#             {"name": "Tanai", "latitude": 31.53812, "longitude": 64.97066},
#             {"name": "Tara Khail", "latitude": 31.53874, "longitude": 64.97789},
#             {"name": "Taymur", "latitude": 31.5223, "longitude": 65.03232},
#             {"name": "Umar", "latitude": 31.52293, "longitude": 65.09164},
#             {"name": "Urak", "latitude": 31.5439, "longitude": 65.04366},
#             {"name": "Wadi-e-Khan", "latitude": 31.57395, "longitude": 65.01233},
#             {"name": "Wali Mohammad Ghazi", "latitude": 31.86955, "longitude": 64.82691},
#             {"name": "Wasimabad", "latitude": 31.5089, "longitude": 65.10491},
#             {"name": "Wosay Kalay", "latitude": 31.51283, "longitude": 65.10506},
#             {"name": "Yaqub Kalay", "latitude": 31.54269, "longitude": 64.95772},
#             {"name": "Yari", "latitude": 31.64505, "longitude": 65.05806},
#             {"name": "Yari Khan Kalay", "latitude": 31.53166, "longitude": 65.04891},
#             {"name": "Yosuf", "latitude": 31.53864, "longitude": 64.95512},
#             {"name": "Yusef Kalay", "latitude": 31.79805, "longitude": 65.01161},
#             {"name": "Zahida Kala", "latitude": 31.49368, "longitude": 65.04857},
#             {"name": "Zahir", "latitude": 31.64299, "longitude": 65.07838},
#             {"name": "Zarif", "latitude": 31.62366, "longitude": 65.0431},
#             {"name": "Zinay", "latitude": 31.5196, "longitude": 65.18431},
#             {"name": "Zowid Kala", "latitude": 31.48134, "longitude": 65.23974}
#         ],
#         "Shah Wali Kot": [
#                     {
#                 "name": "Ahzam Kalay",
#                 "latitude": 31.64422,
#                 "longitude": 65.94175
#             },
#             {
#                 "name": "Akhund Zada Kalay",
#                 "latitude": 31.71812,
#                 "longitude": 66.18801
#             },
#             {
#                 "name": "Akhund Zada Sahib",
#                 "latitude": 31.7031,
#                 "longitude": 66.167
#             },
#             {
#                 "name": "Ali Abad",
#                 "latitude": 31.7387,
#                 "longitude": 65.92142
#             },
#             {
#                 "name": "Ali Zay",
#                 "latitude": 31.42325,
#                 "longitude": 65.92299
#             },
#             {
#                 "name": "Anzirgay",
#                 "latitude": 31.77652,
#                 "longitude": 65.97012
#             },
#             {
#                 "name": "Arhat Kalay",
#                 "latitude": 31.68236,
#                 "longitude": 66.01269
#             },
#             {
#                 "name": "Awme",
#                 "latitude": 31.76115,
#                 "longitude": 65.93248
#             },
#             {
#                 "name": "Bariki",
#                 "latitude": 31.69023,
#                 "longitude": 65.96822
#             },
#             {
#                 "name": "Bashar Kalay",
#                 "latitude": 31.42243,
#                 "longitude": 65.95309
#             },
#             {
#                 "name": "Bawary",
#                 "latitude": 31.69753,
#                 "longitude": 65.88339
#             },
#             {
#                 "name": "Baz Mohammad Khan Kalay",
#                 "latitude": 31.64663,
#                 "longitude": 65.94916
#             },
#             {
#                 "name": "Biyaban Dara",
#                 "latitude": 31.44774,
#                 "longitude": 65.92235
#             },
#             {
#                 "name": "Biyabani Kalay",
#                 "latitude": 31.62404,
#                 "longitude": 66.15417
#             },
#             {
#                 "name": "Chakaw",
#                 "latitude": 31.93134,
#                 "longitude": 65.67861
#             },
#             {
#                 "name": "Haji Qayoum Kalacha",
#                 "latitude": 31.77513,
#                 "longitude": 65.81851
#             },
#             {
#                 "name": "Mansor Abad",
#                 "latitude": 31.77833,
#                 "longitude": 65.80112
#             }
#         ],
#         "Zhar": [
#                 {
#             "name": "Abdul Ghani Sanzari",
#             "latitude": 31.60789,
#             "longitude": 65.52299
#         },
#         {
#             "name": "Abdulhadi Sanzari",
#             "latitude": 31.59751,
#             "longitude": 65.52506
#         },
#         {
#             "name": "Abdul Hakim Kalacha",
#             "latitude": 31.61799,
#             "longitude": 65.53494
#         },
#         {
#             "name": "Abdul Mohammad Jatan",
#             "latitude": 31.58268,
#             "longitude": 65.43713
#         },
#         {
#             "name": "Abdul Rauof",
#             "latitude": 31.58513,
#             "longitude": 65.44816
#         },
#         {
#             "name": "Achekzai Gharbi",
#             "latitude": 31.54318,
#             "longitude": 65.29207
#         },
#         {
#             "name": "Achekzai Sharqi",
#             "latitude": 31.54991,
#             "longitude": 65.34757
#         },
#         {
#             "name": "Aghaygul",
#             "latitude": 31.52957,
#             "longitude": 65.40878
#         },
#         {
#             "name": "Akhtar Mohammad",
#             "latitude": 31.5647,
#             "longitude": 65.42827
#         },
#         {
#             "name": "Akhtar Mohammad Kalay",
#             "latitude": 31.54062,
#             "longitude": 65.30206
#         },
#         {
#             "name": "Ali Zai",
#             "latitude": 31.49672,
#             "longitude": 65.3251
#         },
#         {
#             "name": "Anezai",
#             "latitude": 31.53289,
#             "longitude": 65.38123
#         },
#         {
#             "name": "Ardozai",
#             "latitude": 31.53873,
#             "longitude": 65.34288
#         },
#         {
#             "name": "Asheqa",
#             "latitude": 31.59488,
#             "longitude": 65.5059
#         },
#         {
#             "name": "Ayoub Zai",
#             "latitude": 31.52768,
#             "longitude": 65.37167
#         },
#         {
#             "name": "Baberan",
#             "latitude": 31.57354,
#             "longitude": 65.44209
#         },
#         {
#             "name": "Baboghdi",
#             "latitude": 31.48022,
#             "longitude": 65.27627
#         },
#         {
#             "name": "Balochan Gharbi",
#             "latitude": 31.57861,
#             "longitude": 65.4157
#         },
#         {
#             "name": "Balosan",
#             "latitude": 31.549,
#             "longitude": 65.32183
#         },
#         {
#             "name": "Barik Zai",
#             "latitude": 31.531295,
#             "longitude": 65.349755
#         },
#         {
#             "name": "Barik Zai Jonobi",
#             "latitude": 31.50293,
#             "longitude": 65.27576
#         },
#         {
#             "name": "Barik Zai Wasate",
#             "latitude": 31.5076,
#             "longitude": 65.28225
#         },
#         {
#             "name": "Beyabanak",
#             "latitude": 31.51312,
#             "longitude": 65.29491
#         },
#         {
#             "name": "Bor Ahmad Umar Zai",
#             "latitude": 31.54113,
#             "longitude": 65.38797
#         },
#         {
#             "name": "Char Kocha Baberan",
#             "latitude": 31.55258,
#             "longitude": 65.43834
#         },
#         {
#             "name": "Char Shakha",
#             "latitude": 31.48142,
#             "longitude": 65.25999
#         },
#         {
#             "name": "Dagran",
#             "latitude": 31.55663,
#             "longitude": 65.41379
#         },
#         {
#             "name": "Dahi Dar",
#             "latitude": 31.54919,
#             "longitude": 65.37475
#         },
#         {
#             "name": "Dahi Ghaowjak",
#             "latitude": 31.5376,
#             "longitude": 65.36491
#         },
#         {
#             "name": "Dasht Balochan Gharbi",
#             "latitude": 31.57218,
#             "longitude": 65.32198
#         },
#         {
#             "name": "Deewar Shamaly",
#             "latitude": 31.53619,
#             "longitude": 65.32733
#         },
#         {
#             "name": "Faizullah Khan",
#             "latitude": 31.56389,
#             "longitude": 65.41143
#         },
#         {
#             "name": "Ghariban",
#             "latitude": 31.54808,
#             "longitude": 65.39866
#         },
#         {
#             "name": "Ghondi",
#             "latitude": 31.53129,
#             "longitude": 65.2993
#         },
#         {
#             "name": "Ghondi Kalay",
#             "latitude": 31.5323,
#             "longitude": 65.35742
#         },
#         {
#             "name": "Ghullam Hassan Khan",
#             "latitude": 31.54048,
#             "longitude": 65.30731
#         },
#         {
#             "name": "Habibullah",
#             "latitude": 31.49473,
#             "longitude": 65.33523
#         },
#         {
#             "name": "Haji Abdul Ahad",
#             "latitude": 31.52562,
#             "longitude": 65.33769
#         },

#         {
#             "name": "Haji Abdullah Khan",
#             "latitude": 31.50324,
#             "longitude": 65.33641
#         },

#         {
#             "name": "Haji Abdul Razaq",
#             "latitude": 31.512,
#             "longitude": 65.3883
#         },
#         {
#             "name": "Haji Besmillah",
#             "latitude": 31.55089,
#             "longitude": 65.42467
#         },
#         {
#             "name": "Haji Ghafar",
#             "latitude": 31.55933,
#             "longitude": 65.42978
#         },
#         {
#             "name": "Haji Haidar Khan",
#             "latitude": 31.52194,
#             "longitude": 65.40194
#         },
#         {
#             "name": "Haji Mahaiuldin",
#             "latitude": 31.56816,
#             "longitude": 65.41244
#         },
#         {
#             "name": "Haji Mohammad Hewaz Khawari",
#             "latitude": 31.54649,
#             "longitude": 65.40363
#         },
#         {
#             "name": "Haji Mohammad Hewaz Yasen Zai",
#             "latitude": 31.53885,
#             "longitude": 65.41609
#         },
#         {
#             "name": "Haji Mohammad Umar Wa Sayyidan",
#             "latitude": 31.59126,
#             "longitude": 65.49394
#         },
#         {
#             "name": "Haji Mussa Khan",
#             "latitude": 31.54166,
#             "longitude": 65.42243
#         },
#         {
#             "name": "Haji Nader Kalay",
#             "latitude": 31.50157,
#             "longitude": 65.33159
#         },
#         {
#             "name": "Haji Naserullah Khan",
#             "latitude": 31.53774,
#             "longitude": 65.37531
#         },
#         {
#             "name": "Haji Nehmatullah Kalay",
#             "latitude": 31.53487,
#             "longitude": 65.31069
#         },
#         {
#             "name": "Haji Pour Dail",
#             "latitude": 31.53634,
#             "longitude": 65.35911
#         },
#         {
#             "name": "Haji Shahabudin Kalacha",
#             "latitude": 31.61662,
#             "longitude": 65.54251
#         },
#         {
#             "name": "Haji Zarif Wa Haji Ibrahim",
#             "latitude": 31.54586,
#             "longitude": 65.33481
#         },
#         {
#             "name": "Kadhel",
#             "latitude": 31.50627,
#             "longitude": 65.36926
#         },
#         {
#             "name": "Kadi Zai",
#             "latitude": 31.53186,
#             "longitude": 65.35466
#         },
#         {
#             "name": "Kadozai",
#             "latitude": 31.52338,
#             "longitude": 65.38021
#         },
#         {
#             "name": "Kakaran",
#             "latitude": 31.51769,
#             "longitude": 65.36232
#         },
#         {
#             "name": "Kalacha",
#             "latitude": 31.56904,
#             "longitude": 65.44603
#         },
#         {
#             "name": "Kalizai",
#             "latitude": 31.53278,
#             "longitude": 65.38941
#         },
#         {
#             "name": "Karkecha",
#             "latitude": 31.50517,
#             "longitude": 65.26907
#         },
#         {
#             "name": "Kashta Sohbat",
#             "latitude": 31.50718,
#             "longitude": 65.24786
#         },
#         {
#             "name": "Khan Mohammad Khan Kalay",
#             "latitude": 31.50633,
#             "longitude": 65.32659
#         },
#         {
#             "name": "Khogyani",
#             "latitude": 31.56083,
#             "longitude": 65.42656
#         },
#         {
#             "name": "Kota Zai",
#             "latitude": 31.55008,
#             "longitude": 65.43305
#         },
#         {
#             "name": "Lahl Mohammad Khan",
#             "latitude": 31.57003,
#             "longitude": 65.40557
#         },
#         {
#             "name": "Lowar Sohbat",
#             "latitude": 31.52179,
#             "longitude": 65.24574
#         },
#         {
#             "name": "Mahajeren",
#             "latitude": 31.53944,
#             "longitude": 65.31515
#         },
#         {
#             "name": "Mako",
#             "latitude": 31.56921,
#             "longitude": 65.43823
#         },
#         {
#             "name": "Makwan",
#             "latitude": 31.57846,
#             "longitude": 65.46499
#         },
#         {
#             "name": "Malangan",
#             "latitude": 31.53722,
#             "longitude": 65.33814
#         },
#         {
#             "name": "Malik Ahmad Khan",
#             "latitude": 31.5634,
#             "longitude": 65.44704
#         },
#         {
#             "name": "Manda",
#             "latitude": 31.55376,
#             "longitude": 65.45976
#         },
#         {
#             "name": "Mani Zai Kalay",
#             "latitude": 31.51518,
#             "longitude": 65.3752
#         },
#         {
#             "name": "Mardozai",
#             "latitude": 31.53104,
#             "longitude": 65.38386
#         },
#         {
#             "name": "Markaz Woluswally",
#             "latitude": 31.57867,
#             "longitude": 65.42348
#         },
#         {
#             "name": "Marsanzai",
#             "latitude": 31.52544,
#             "longitude": 65.39012
#         },
#         {
#             "name": "Mir Hazar",
#             "latitude": 31.67704,
#             "longitude": 65.4389
#         },
#         {
#             "name": "Mir Hotak",
#             "latitude": 31.51275,
#             "longitude": 65.26014
#         },
#         {
#             "name": "Mir Waliyan",
#             "latitude": 31.52055,
#             "longitude": 65.33019
#         },
#         {
#             "name": "Mullah Taj Mohammad",
#             "latitude": 31.61849,
#             "longitude": 65.50895
#         },
#         {
#             "name": "Mullhyan",
#             "latitude": 31.55557,
#             "longitude": 65.3994
#         },
#         {
#             "name": "Mussa Khan",
#             "latitude": 31.52562,
#             "longitude": 65.40854
#         },
#         {
#             "name": "Nagharullah Kalay",
#             "latitude": 31.53036,
#             "longitude": 65.37167
#         },
#         {
#             "name": "Nahr Karaiz",
#             "latitude": 31.49566,
#             "longitude": 65.28818
#         },
#         {
#             "name": "Naik Mohammad Wa Haji Mohammad Hashemi",
#             "latitude": 31.52909,
#             "longitude": 65.39538
#         },
#         {
#             "name": "Nalqam",
#             "latitude": 31.49409,
#             "longitude": 65.31143
#         },
#         {
#             "name": "Nari",
#             "latitude": 31.51167,
#             "longitude": 65.26625
#         },
#         {
#             "name": "Narow",
#             "latitude": 31.50608,
#             "longitude": 65.30979
#         },
#         {
#             "name": "Noor Ali",
#             "latitude": 31.55746,
#             "longitude": 65.33555
#         },
#         {
#             "name": "Noor Mohammad Khan Fazel Kalay",
#             "latitude": 31.604,
#             "longitude": 65.49296
#         },
#         {
#             "name": "Noorulah Char Shakha",
#             "latitude": 31.4925,
#             "longitude": 65.27566
#         },
#         {
#             "name": "Nooruldin Kalay",
#             "latitude": 31.57277,
#             "longitude": 65.45659
#         },
#         {
#             "name": "Pas Ab",
#             "latitude": 31.57092,
#             "longitude": 65.42665
#         },
#         {
#             "name": "Payan Dahi",
#             "latitude": 31.54904,
#             "longitude": 65.42786
#         },
#         {
#             "name": "Rahmuldin Haji Wazer",
#             "latitude": 31.53513,
#             "longitude": 65.41139
#         },
#         {
#             "name": "Sahdullah",
#             "latitude": 31.52268,
#             "longitude": 65.3525
#         },
#         {
#             "name": "Salim Karaiz",
#             "latitude": 31.66933,
#             "longitude": 65.31411
#         },
#         {
#             "name": "Salim Wa Azizullah",
#             "latitude": 31.56804,
#             "longitude": 65.45281
#         },
#         {
#             "name": "Sanzari Aminullah",
#             "latitude": 31.612,
#             "longitude": 65.52909
#         },
#         {
#             "name": "Sanzari Gharbi",
#             "latitude": 31.60638,
#             "longitude": 65.51604
#         },
#         {
#             "name": "Sayyidan",
#             "latitude": 31.50579,
#             "longitude": 65.33475
#         },
#         {
#             "name": "Shah Mohammad Khan Umar Khan Kalay",
#             "latitude": 31.58995,
#             "longitude": 65.48759
#         },
#         {
#             "name": "Shahzada Abad",
#             "latitude": 31.54053,
#             "longitude": 65.26355
#         },
#         {
#             "name": "Teer Yanan",
#             "latitude": 31.55459,
#             "longitude": 65.42565
#         },
#         {
#             "name": "Wazer Kalay",
#             "latitude": 31.56588,
#             "longitude": 65.36753
#         },
#         {
#             "name": "Zahedanan",
#             "latitude": 31.56504,
#             "longitude": 65.43525
#         }
#     ],
#     # Add more districts and areas as needed
# }

# # Generate random data
# num_records = 6000
# data = []
# start_date = datetime(2020, 1, 1)
# end_date = datetime(2024, 1, 1)

# for _ in range(num_records):
#     date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
#     hour_of_day = random.randint(1, 24)
#     district = random.choice(list(districts_data.keys()))
#     area_info = random.choice(districts_data[district])
#     location = area_info['name']
#     latitude = area_info['latitude']
#     longitude = area_info['longitude']
#     victim_gender = random.choice(['Male', 'Female'])
#     victim_age = random.randint(1, 100)
#     perpetrator_gender = random.choice(['Male', 'Female'])
#     perpetrator_age = random.randint(1, 100)
#     weapon = random.choice(['Knife', 'Gun', 'None', 'Other'])
#     injury = random.choice(['None', 'Minor', 'Severe', 'Fatal'])
#     weather = random.choice(['Clear', 'Rainy', 'Snowy', 'Cloudy'])
#     temperature = random.uniform(-10, 40)
#     previous_activity = random.choice(['Walking', 'Driving', 'Shopping', 'Working'])
#     economical_situation = random.choice(['Low', 'Medium', 'High'])
#     education_level = random.choice(['None', 'Primary', 'Secondary', 'Tertiary'])
#     crime_type = random.choice(['Theft', 'Assault'])
#     time_of_day = random.choice(['Morning', 'Afternoon', 'Evening', 'Night'])
#     day_of_week = date.strftime("%A")
#     month = date.strftime("%B")
#     season = random.choice(['Winter', 'Spring', 'Summer', 'Fall'])
#     victim_age_group = random.choice(['Child', 'Teen', 'Adult', 'Senior'])
#     perpetrator_age_group = random.choice(['Child', 'Teen', 'Adult', 'Senior'])
#     weather_condition = random.choice(['Dry', 'Wet'])
#     economic_index = random.uniform(0, 100)
#     education_index = random.uniform(0, 100)

#     data.append([
#         date, hour_of_day, location, district, area_info['name'], victim_gender, victim_age,
#         perpetrator_gender, perpetrator_age, weapon, injury, weather, temperature, previous_activity,
#         economical_situation, education_level, crime_type, latitude, longitude, time_of_day, day_of_week, 
#         month, season, victim_age_group, perpetrator_age_group, weather_condition, economic_index, education_index
#     ])

# # Define column names
# columns = [
#     'date', 'hour_of_day', 'location', 'district', 'area_name', 'victim_gender', 'victim_age',
#     'perpetrator_gender', 'perpetrator_age', 'weapon', 'injury', 'weather', 'temperature', 
#     'previous_activity', 'economical_situation', 'education_level', 'crime_type', 'latitude', 'longitude',
#     'time_of_day', 'day_of_week', 'month', 'season', 'victim_age_group', 'perpetrator_age_group', 
#     'weather_condition', 'economic_index', 'education_index'
# ]

# # Create a DataFrame
# df = pd.DataFrame(data, columns=columns)

# # Save to CSV
# df.to_csv('data.csv', index=False)

# print("Data has been generated and saved to 'data.csv'.")


