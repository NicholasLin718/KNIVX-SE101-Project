import json

def clear():
    path = './templates/data.json'
    with open(path, 'r') as f:
        data = json.load(f)
    data["input"] = ""
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)        

def main():
    value = clear()
    print(value)

if __name__ == "__main__":
    main()
