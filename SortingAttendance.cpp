#include<iostream>
#include <bits/stdc++.h>
using namespace std;
void removeDuplicates(int arr[], int n)
{
  
    int i;
  
    // Initialise a set
    // to store the array values
    set<int> s;
  
    // Insert the array elements
    // into the set
    for (i = 0; i < n; i++) {
  
        // insert into set
        s.insert(arr[i]);
    }
  
    set<int>::iterator it;
  
    // Print the array with duplicates removed
    cout << "\nAfter removing duplicates:\n";
    for (it = s.begin(); it != s.end(); ++it)
        cout << *it << ", ";
    cout << '\n';
}
  
// Driver code
int main()
{
    //Replace the elements in array with the output you got from python
    int arr[] = {1,50,92,18,39,52,107,24,30,33,6,84,89,53,60,83,03,22,50,113,47,57,15,38,23,120,77,9,74,111,57,86,24,37,95,88,77,118,43,14,84,44,19,111,93,71,25,58,55};
  
    int n = sizeof(arr) / sizeof(arr[0]);
  
    // call removeDuplicates()
    removeDuplicates(arr, n);
  
    return 0;
}