import json

def update():
    val = input("enter character: \n")
    path = 'data.json'
    with open(path, 'r') as f:
        data = json.load(f)
    data["input"] += val
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)        

def main():
    value = update()
    print(value)

if __name__ == "__main__":
    main()
