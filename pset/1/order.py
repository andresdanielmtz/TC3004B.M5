class Order:
    def __init__(self, order):
        self.name = order["id"]
        self.items = order["items"]

    def printTotal(self):
        print(sum(item["price"] for item in self.items))


def main():
    print("Initiated")


if __name__ == "__main__":
    main()
