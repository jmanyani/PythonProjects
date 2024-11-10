import json

# Load the following data from JSON file
with open(r'C:\Users\manya\Downloads\instagram-manyani_jatin-2024-11-05-T7s9JBZO\connections\followers_and_following\following.json', 'r') as file:
    following_data = json.load(file)

# Extract usernames from the 'relationships_following' data
following_usernames = [
    entry['string_list_data'][0]['value']
    for entry in following_data['relationships_following']
    if entry['string_list_data']
]

# Load the followers data from JSON file
with open(r'C:\Users\manya\Downloads\instagram-manyani_jatin-2024-11-05-T7s9JBZO\connections\followers_and_following\followers_1.json', 'r') as file:
    followers_data = json.load(file)

# Extract usernames from the followers data
followers_usernames = [
    entry['string_list_data'][0]['value']
    for entry in followers_data
    if entry['string_list_data']
]

# Identify usernames that you're following but who aren't following you back
not_following_back = [username for username in following_usernames if username not in followers_usernames]

# Print the usernames that aren't following you back
print("Usernames you are following but who aren't following you back:")
count = 0
for username in not_following_back:
    print(username)
    count += 1

print(f'Count: Number of users you follow who don’t follow you back: {count}')

# Specify the location to save the text file
output_path = r'C:\Users\manya\Downloads\not_following_back.txt'
with open(output_path, "w") as file:
    file.write("Usernames you are following but who aren't following you back:\n")
    for username in not_following_back:
        file.write(f"{username}\n")
    file.write(f"\nCount: Number of users you follow who don’t follow you back: {count}\n")

print(f"Usernames saved to '{output_path}'")
