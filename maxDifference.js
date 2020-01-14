function maxDifference(nums) {
    if (!nums) {
      throw new Error('You must enter a series of numbers');
    }

    let firstNumber = nums[0];
    let diff = -1;
    
    for (let i = 1; i < nums.length; ++i) {
      if(nums[i] > firstNumber) {
        diff = Math.max(nums[i] - firstNumber, diff);
      }
      min = Math.min(firstNumber, arr[i]);
    }
    console.log(`The maximum difference is ${diff}`);
}

// Runner
// e.g You can run this script by doing node maxDifference.js 12345 in the terminal
const arr = process.argv[2].split('');
maxDifference(arr);