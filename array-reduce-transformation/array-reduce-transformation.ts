type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    return nums.length === 0
        ? init
        : reduce(nums.slice(1), fn, fn(init, nums[0]));
};