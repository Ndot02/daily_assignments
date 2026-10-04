

s1 = input("Sentence 1: ").lower()
s2 = input("Sentence 2: ").lower()

words1 = set(s1.split())
words2 = set(s2.split())

common = words1 & words2
print("Common words:", sorted(common))

# Your job:
all_words = words1 | words2
print(f"all words {all_words}")
counts = (len(common), len(all_words))
# 3. unpack counts into two names and print them
common_count, all_count = counts
print(f"the no of common words are {common_count}")
print(f"The no of words are {(all_count)}")
# 4. words in only one sentence (^)
only_one = words1 ^ words2
print("Words in only one sentence:", sorted(only_one))