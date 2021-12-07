from string import ascii_letters, ascii_lowercase, digits
import threading

password_contains = ascii_letters + digits
most_common = ascii_lowercase + " .,-"

# Get the contents of the output
outputFile = open("output", "rb")
content = outputFile.read().decode()
outputFile.close()

def findPotentialKey(keylength):
    potentialKey = []
    for _ in range(keylength):
        potentialKey.append({char: 0 for char in password_contains})

    for i in range(len(content)):
        for char in password_contains:
            tmp = chr(ord(char) ^ ord(content[i]))
            if tmp in most_common:
                potentialKey[i % keylength][char] += 1

    potentialKeyStr = ""
    for passChr in potentialKey:
        potentialKeyStr += max(passChr, key=lambda index: passChr[index])

    print(f'Potential password for length: {keylength} - {potentialKeyStr}')
    
if __name__ == "__main__":
    threads = {}
    for i in range(0, 6):
        threads[i] = threading.Thread(target=findPotentialKey, args=(i + 10, ))
    for i in range(0, 6):
        threads[i].start()
    for i in range(0, 6):
        threads[i].join()
    print("THREADS: Done, threads are terminated.")