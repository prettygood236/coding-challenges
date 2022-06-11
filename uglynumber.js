function upperBound(a , low , high , element) {
		while (low < high) {
			var middle = low + parseInt((high - low) / 2);
			if (a[middle] > element)
				high = middle;
			else
				low = middle + 1;
		}
		return low;
}

	// Print nth Ugly number
	function nthUglyNumber(n) {

		var pow = Array(40).fill(1);
	

		// stored powers of 2 from
		// Math.pow(2,0) to Math.pow(2,30)
		for (i = 1; i <= 30; ++i)
			pow[i] = pow[i - 1] * 2;

		// Initialized low and high
		var l = 1, r = 2147483647;

		var ans = -1;

		// Applying Binary Search
		while (l <= r) {

			// Found mid
			var mid = l + parseInt((r - l) / 2);

			// cnt stores total numbers of ugly
			// number less than mid
			var cnt = 0;

			// Iterate from 1 to mid
			for (i = 1; i <= mid; i *= 5)

			{
				// Possible powers of i less than mid is i
				for (j = 1; j * i <= mid; j *= 3)

				{
					// possible powers of 3 and 5 such that
					// their product is less than mid

					// using the power array of 2 (pow) we are
					// trying to find the max power of 2 such
					// that i*J*power of 2 is less than mid

					cnt += upperBound(pow, 0, 31, parseInt( (mid / (i * j))));
				}
			}

			// If total numbers of ugly number
			// less than equal
			// to mid is less than n we update l
			if (cnt < n)
				l = mid + 1;

			// If total numbers of ugly number
			// less than equal to
			// mid is greater than n we update
			// r and ans simultaneously.
			else {
				r = mid - 1;
				ans = mid;
			}
		}

		return ans;
	}

