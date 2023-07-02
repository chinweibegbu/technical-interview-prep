import utils
import sorts

def by_title_ascending(book_a, book_b):
  return book_a["title_lower"] > book_b["title_lower"]

def by_author_ascending(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]

def by_total_length(book_a, book_b):
  total_length_a = len(book_a["title"]) + len(book_a["author"])
  total_length_b = len(book_b["title"]) + len(book_b["author"])
  return total_length_a > total_length_b

## Sort files in books_large.csv
# 1. Load books_small.csv
bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

# 2. Print out all books in books_small.csv
print("\n>> Printing all books without sorting:")
for book in bookshelf:
  print(book["title"])

# 3. Sort books by title (in ascending order) using bubble sort
print("\n>> Printing books sorted by title in ascending order using BUBBLE SORT:")
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for s_1 in sort_1:
  print(s_1["title"])

# 4. Sort books by author (in ascending order) using bubble sort
print("\n>> Printing books sorted by author in ascending order using BUBBLE SORT:")
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for s_2 in sort_2:
  print(s_2["author"])

# 5. Sort books  author (in ascending order) using quick sort
print("\n>> Printing books sorted by author in ascending order using QUICK SORT:")
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
for book_v2 in bookshelf_v2:
  print(book_v2["author"])

## Sort files in books_large.csv
# 1. Load books_large.csv
long_bookshelf = utils.load_books('books_large.csv')
long_bookshelf_v2 = long_bookshelf.copy()

# 2. Sort books by total length using bubble sort
print("\n>> Printing books (long) sorted by total length in ascending order using BUBBLE SORT:")
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
for s_3 in sort_3:
  print(s_3["title"])

# 3. Sort books by total length using quick sort
print("\n>> Printing books sorted by total length in ascending order using QUICK SORT:")
sorts.quicksort(long_bookshelf_v2, 0, len(long_bookshelf_v2)-1, by_total_length)
for long_book_v2 in long_bookshelf_v2:
  print(long_book_v2["title"])
