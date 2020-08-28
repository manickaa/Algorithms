# Algorithms
Contains various sorting algorithms in Python

1.  Insertion Sort:

For each element in the array from 0 to len(array), the element is stored as key. The predecessor of the key are compared to it. If it is greater than key, the elements are swapped, until the key moves to a position where its predecessor is less than it. 

Time complexity :  O(N^2)

2.  Selection Sort:

The array is divided into two parts, the sorted part and the unsorted part. Intially there is no sorted part, only the unsorted part.
Compare each element in the array to find the smallest of the array and swap it with the first element. So that, now, the first element becomes a part of the sorted array. Likewise continuously take the smallest element from the unsorted part and swap it with the element after the end of the sorted part of the array.

Time complexity :  O(N^2)

3. Bubble sort:

Each element is the array is compared sequentially, until the largest element reaches the end of the array. This step is repeated until the smallest element reaches to the first position in the array.

Time complexity : O(N^2)

4. Merge Sort:

This algorithm uses 'Divide and Conquer' technique, the array is divided into small parts, until the small parts is nothing but the sorted array itself using recursion. When the array is completed divided into smaller parts, which cannot be divided further, the smaller parts are merged. During merge, parts of the array are compared and sorted in the right order and then returned. 

Time Complexity : O(N logN)
Explanation: The array is divided logN times (N -> N/2 -> N/4 -> N/8 -> .... -> 1).
             The number of merges happen : N
             So, the time complexity is O(N log N)
             
 5. Quick Sort:
 
 The last index of the array is chosen as the pivot and all the elements before the pivot are compared to it. If the element is greater than pivot, it is left as it is. If the element is less than pivot, the elements are swapped sequentically. Finally, the 
