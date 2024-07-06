### 2. Two Pointers Or Iterators (sorting, linked list , searching - usually pointer at opposite directions until they met)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/38bc1e2c-c178-42c6-b5f5-243b031ea4cb/9585428c-8975-4e19-bc9f-97618b68588b/Untitled.png)

this is a pattern where two pointers iterate through the DS in tandem until one or two of them find the answer.
![alt text](image.png)

### **Identify**

- problems where we deal with sorted array or linked list, and need to find a set of elements that **fulfil a certain purpose.**
- set of element are **pair, triplet or even subarray**.

### **LeetCode questions**

- squaring a sorted array - easy
- triplet that sum to zero - medium

  Code example : binary search C#

  ```csharp
  // complexity of o(log n) assuming the array is sorted
  public static object BinarySearchDisplay(int[] arr, int key) {
     int minNum = 0;
     int maxNum = arr.Length - 1;

     while (minNum <=maxNum) {
        int mid = (minNum + maxNum) / 2;
        if (key == arr[mid]) {
           return ++mid;
        } else if (key < arr[mid]) {
           max = mid - 1;
        }else {
           min = mid + 1;
        }
     }
     return "None";
  }
  ```

  ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/38bc1e2c-c178-42c6-b5f5-243b031ea4cb/74f9b4d1-ac03-4b48-bfb9-965b5888de10/Untitled.png)

  ![alt text](image-1.png)
