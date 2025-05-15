# Input list of tags
tags = ["ai", "ml", "python", "ml", "dl", "ai"]

# Dictionary to count occurrences
tag_count = {}

# Loop through each tag and count them
for tag in tags:
    if tag in tag_count:
        tag_count[tag] += 1
    else:
        tag_count[tag] = 1

# Extract duplicates (those with count > 1)
duplicates = [tag for tag, count in tag_count.items() if count > 1]

# Output the duplicates
print("Duplicate Tags:", duplicates)