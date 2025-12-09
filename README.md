---
title: Binary Search Implementation
sdk: gradio
app_file: app.py
pinned: false
license: apache-2.0
emoji: 🚀
---
# Algorithm Name
I am choosing Binary Search as my algorithm because it is efficient, clean and easy to visualize because you can show the low, mid and high and how it searches through those and how the space shrinks each and every step of the way. The worst case for binary search is O(log n) which is way better than linear search’s O(n) time complexity.

## Demo video/gif/screenshot of test
https://imgur.com/a/Y7HS5QE
This imgur contains 7 test cases I screenshotted from if needed I have the actual PNGS I will include in the dropbox

## Problem Breakdown & Computational Thinking (You can add a flowchart and write the
four pillars of computational thinking briefly in bullets)
Decomposition: 
Start with two pointers: low=0 and high=n-1 
While low<=high you can compute the middle index and add low and high together and divide it by two splitting the search
If the target is either below the mid search either right or left half and keep doing this until target is found
Return the target in the end
Pattern Recognition: 
With every iteration of this search you must compute the mid value check the mid value and based on the mid value search right or left half
The list always shrinks but the first step is crucial to nail because you need to know if its the right or left half so it cuts the time in half
The shrinking part is why the time complexity of this search is log n
Abstraction:
Only show the current portion of the list being searched
The values of low, mid and high
The comparison happening between [mid] vs target
Whether the left or right side is being searched at that very moment
Algorithm Design:
Input - a sorted list and a targeted value
Run the binary search function and track each step in the list with screenshots and highlighting 
Output - Found the index value or a ‘Not found’ output if the targeted value could not be found. Step by step visual with low, mid and high and the current part of the list being searched and the direction we have to go for the next search.
Flowchart: https://imgur.com/a/f8SyBlL
For the GUI elements I will be showing the steps in which it took to get to the target number and the each indexed low and high integer for each step. 
And with that I can show the mid of each step and which side it will be taking.


## Steps to Run
Open Hugging Face link below
Enter a sorted list with commas inbetween the numbers
Enter the targetted number you would want to find
Click the submit button
View the result and you can see the steps it took to find your number by each indexed number.

## Hugging Face Link
https://huggingface.co/spaces/prsee/binary-search-ikjot

## Author & Acknowledgment
Author: Ikjot Bakshi
Student Number: 20480595
I acknowledge I used Gradio was the only interface tool I used for this assignment. I used some AI not for the coding portion of the assignment but for the Hugging Face deployment because I have never used this site and needed a bit of guidance on where to click and how to upload my project.