import json

cache_name = lambda num: "cache"+str(num)+".csv"
json_data_path = "queue_init.json"

class BMQueue:
    def __init__(self):
        self.data = None
        with open(json_data_path) as f:
            self.data = json.load(f)
            f.close()
        
    def __next(self, index) -> int:
        return (index+1) % self.data["capacity"]

    def __is_full(self) -> bool:
        if self.data["capacity"] == 0:
            return True
        if self.data["front"] == -1 or self.__next(self.data["back"]) != self.data["front"]:
            return False
        return True

    def __is_empty(self) -> bool:
        return self.data["front"] == -1

    def __write_queue_state(self):
        with open(json_data_path, "w") as f:
            json.dump(self.data, f)
            f.close()

    def __resize(self):
        capacity = self.data["capacity"]
        if capacity == 0:
            self.data["capacity"] = 1
        else:
            self.data["capacity"] *= 2
        for i in range(capacity, self.data["capacity"]):
            with open(cache_name(i), "x") as f:
                f.close()

    def enqueue(self, data:str):
        if self.__is_full():
            self.__resize()

        if not self.__is_empty():
            self.data["back"] = self.__next(self.data["back"])
        else:
            self.data["back"] = self.data["front"] = 0
        
        with open(cache_name(self.data["back"]), "w") as f:
            f.write(data)
            f.close()

        self.__write_queue_state()

    def dequeue(self) -> str:
        if self.__is_empty():
            return ""
        
        t_front = self.data["front"]
        if t_front == self.data["back"]:
            self.data["front"] = self.data["back"] = -1
        else:
            self.data["front"] = self.__next(self.data["front"])
        
        result = None
        with open(cache_name(t_front), "r") as f:
            result = f.read()
            f.close()
        
        self.__write_queue_state()

        return result

# test = BMQueue()
# test.enqueue("NASHE")
# # print(test.dequeue())