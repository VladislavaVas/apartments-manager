class Apartment:
    def __init__(self, street='', house_no='', apt_no='', rooms='', floor=''):
        self.street = street
        self.house_no = house_no
        self.apt_no = apt_no
        self.rooms = rooms
        self.floor = floor
   
    def getApartment_forTable(self):
        return [
            self.street,
            self.house_no,
            self.apt_no,
            self.rooms,
            self.floor
        ]

    def equval_Apartment(self, other):
        return self.street == other.street and \
               self.house_no == other.house_no and \
               self.apt_no == other.apt_no and \
               self.rooms == other.rooms and \
               self.floor == other.floor

class HouseManager:
    def __init__(self):
        self.apartments = {}
        self.count = 0

    def __str__(self):
        s = ''
        for x in self.apartments:
            s += f'Apartment {x+1}:\n'
            s += str(self.apartments[x])
            s += '\n'
        return s

    def appendApartment(self, data_list):
        new_apt = Apartment(*data_list)
        self.apartments[self.count] = new_apt
        self.count += 1

    def editApartment(self, index, data_list):
        apt = Apartment(*data_list)
        self.apartments[index] = apt

    def read_data_from_file(self, filename):
        self.apartments = {}
        self.count = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("&")
                    self.apartments[self.count] = Apartment(*parts)
                    self.count += 1

    def find_keyApartment(self, data_list):
        apt = Apartment(*data_list)
        for x in self.apartments:
            if self.apartments[x].equval_Apartment(apt):
                return x
        return -1

    def delApartment(self, data_list):
        apt = Apartment(*data_list)
        for x in self.apartments:
            if self.apartments[x].equval_Apartment(apt):
                del self.apartments[x]
                self.count -= 1
                break

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for x in self.apartments:
                apt = self.apartments[x]
                file.write("&".join([
                    apt.street,
                    apt.house_no,
                    apt.apt_no,
                    apt.rooms,
                    apt.floor
                ]) + "\n")
