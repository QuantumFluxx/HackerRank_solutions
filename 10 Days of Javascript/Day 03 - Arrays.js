// ========================
//       Information
// ========================

// Direct Link: https://www.hackerrank.com/challenges/js10-arrays/problem
// Difficulty: Easy
// Max Score: 15
// Language: JavaScript (Node.js)

// ========================
//         Solution
// ========================

// Return the second largest number in the array.
// @param {Number[]} nums - An array of numbers.
// @return {Number} The second largest number in the array.

function getSecondLargest(nums) {
    // Complete the function
   let first = nums[0]; 
   let second = -1;
    for (let i = 0; i < nums.length; i++) {
    if (nums[i] > first) {
        second = first;
        first = nums[i]
    }

    if (nums[i] > second && nums[i] < first) {
        second = nums[i];
    }
}


return second;
}