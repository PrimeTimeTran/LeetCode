// var reduce = function(nums, fn, init) {
//   let acc = init;
//   for (let i = 0; i < nums.length; i++) {
//     acc = fn(acc, nums[i]);
//   }
//   return acc;
// };

var reduce = function(nums, fn, init) {
  let acc = init
  for (let n of nums) {
    acc = fn(acc, n)
  }
  return acc
};