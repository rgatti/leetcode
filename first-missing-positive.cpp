/*
https://leetcode.com/problems/first-missing-positive/description/
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
*/
#include <iostream>
#include <vector>
#include <cmath>

using std::cout;
using std::endl;
using std::vector;

int firstMissingPositive(vector<int>& nums)
{
	// Number of bits each vector item can hold.
	const int WIDTH = 8 * sizeof(int);
	// Max integer value we care about.
	const int MAX = nums.size();
	// Number of buckets needed for the total bitmask.
	const int BUCKETS = (int)std::ceil(MAX / (double)WIDTH);

	// Given value v return bucket to use for the bitmask.
	auto getBucket = [WIDTH](int v) { return (int)std::ceil(v / (double)WIDTH) - 1; };

	// Clean & organize the vector
	//
	// * Any value outside the valid integer range set to 0
	// * Make sure the values in positions used for bitmask can be set immediately
	for (auto& value : nums) {
		if (value < 1 || value > MAX)
			value = 0;
		else {
			const int bucket = getBucket(value);
			const int temp = value;
			value = nums[bucket];
			nums[bucket] = temp;
		}
	}

	// Set bitmask for each value
	//
	// For each value in nums determine which bucket to use for the bitmask and
	// set appropriately. The values in bucket positions are already known to be
	// assignable immediately from the 'clean & organize' step above.
	for (auto& value : nums) {
		if (value == 0) continue;
		const int temp = value;
		const int bucket = getBucket(value);
		value = 0;
		nums[bucket] = nums[bucket] | 0x1 << (temp - WIDTH * bucket - 1);
	}

	// Find first 0 bit
	//
	// Even though this double loop has a potential search space of
	// 32 * ceil(nums.size / 32) the actual searched bits will never be more than
	// the size of nums + 1 (if all bits are set), therefore the complexity is O(n).
	for (int bucket = 0; bucket < BUCKETS; ++bucket)
		for (int shift = 0; shift < WIDTH; ++shift) {
			const unsigned mask = 1 << shift;
			if ((nums[bucket] & mask) == 0) {
				return bucket * WIDTH + shift + 1;
			}
		}

	return 0; // to remove compiler warning
}

int main()
{
	// 1-bucket
	//
	vector<int> vec1{ 1, 2, 0 }; // 3
	vector<int> vec2{ 3, 4, -1, 1 }; // 2

	// 2-buckets
	//
	// This array will use the first two integers as bitmasks. The first mask
	// will be full. Position 2 in the second mask will be 0.
	vector<int> vec3{
		1,   2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
		17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
		33, 35, 36 }; // 34 .. (line 68 = bucket 1 * width 32 + shift 2 + 1)


	cout << firstMissingPositive(vec1) << endl;
	cout << firstMissingPositive(vec2) << endl;
	cout << firstMissingPositive(vec3) << endl;
}
