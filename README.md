# mergesort-nonrecursive
Non recursive mergesort in python

Sorting
O(n^2) methods
  - Bubble sort(in place)
  - Insertion Sort(in place)
  - Selection Sort(in place)

  These methods consist of sorting the array begining from one end, making a full pass of the
  array up to the sorted point each time

  in bullble sort two successive elements are comared to push the largest element to the end
  in insertion sort the largest element is picked in a scan and swapped to the last position each time
  in selection sort we being with sorting 1,2,...n elements each time by inserting the nth element into the
  right position each time


O(n long(n))
   - Merge Sort

Between O(n^2) and O(n log n)
   - Quick Sort (in place)
   We pick a pivot, usially the right most element of the partition. We then scan right to left from the pivot.
   If a element is larger than the pivot, a triple swap takes place. The larger element is pulledout, the number right to the left of the pivot is moved in there and the pivot moves to its left and the larger element to its right.   - IF THE list is already sorted and we start at the wrong end we have O(n^2)

   - Heap Sort ( Selection Sort with using a heap to pick the
     	       	  next lowest key O(log(n)))

Merge Sort is generally out of place and requires extra storage
