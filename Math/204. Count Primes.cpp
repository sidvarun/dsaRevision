// We can start with the smallest prime number, 2, and mark all of its multiples up to "n" as non-primes. Then we repeat the same process for the next available number in the array that is not marked as composite 
// and so on.

// We have a nested-loop structure. Now the question is: What are the bounds on these two loops? The outer loop will start at 2 and go up to \sqrt{n} 
// n
// ​
//  . This is because by that point we will have considered all of the possible multiples of all the prime numbers below n. Let's look at the example where n is 30. Now the square-root of n is greater than 5.

// It is not necessary to consider any number greater than the square root of n. 

// 6 * 1 = 6 = 1 * 6
// 6 * 2 = 12 = 2 * 6
// 6 * 3 = 18 = 3 * 6
// 6 * 4 = 24 = 2 * 12
// 6 * 5 = 30 = 5 * 6
// 6 * 6 = 36 > 30

// Notice that every multiple of 6 was already addressed by some multiple of a prime number less than 6.
// Now that the outer loop's boundaries are defined, let's define the boundaries of the inner loop. We will invariantly pick the next available prime number (a number/index not yet marked in the array as a composite) before entering the inner loop. Say the index we picked from the outer loop is i, then the inner loop will start at i*i and increase by increments of i until it surpasses n. In short, we iterate over every multiple of i between i and n.

// The question now is why should we start at i*i. Why not start at 2*i to keep things simple? The reason is that all of the previous multiples would already have been covered by previous primes. In number theory, the fundamental theorem of arithmetic, also called the unique factorization theorem or the unique prime factorization theorem, states that every integer greater than 1 either is a prime number itself or can be represented as the product of prime numbers. So the prime numbers smaller than i would have already covered the multiples smaller than i*i. Let's look at the prime number 7 to see how all the multiples up to 7*7 are already covered by primes smaller than '7'.


// Let's assume that n is 50 (a value greater than 7*7) to demonstrate this claim. 

// 7 * 2 = 14 = 2 * 7
// 7 * 3 = 21 = 3 * 7
// 7 * 4 = 28 = 2 * 2 * 7 = 2 * 14
// 7 * 5 = 35 = 5 * 7
// 7 * 6 = 42 = 2 * 3 * 7 = 2 * 21


// Algorithm

// Wikipedia provides a great approach for this algorithm. So we will follow their method step by step to find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

// Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
// Let p be the variable we use in the outer loop that iterates from 2 to \sqrt{n} 
// n. Initially, let p equal 2, the smallest prime number.
// Enumerate the multiples of p by counting in increments of p from p*p to n, and mark them in the list (these will be p*p, p*p + p, p*p + 2*p, ...; p itself should be prime).
// Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
// When the algorithm terminates, all of the remaining numbers that are not marked are prime.
// A key observation is that p will always be prime because every composite value less than p*p has already been marked as a multiple of some smaller prime. Note that some of the numbers may be marked more than once (e.g., 15 will be marked by both 3 and 5).

class Solution {
public:
	int countPrimes(int n) {
		//prime no. generation using sieve of eratothons
		vector<bool> prime(n + 1, true);
		prime[0] = false;
		prime[1] = false;
		for (int i = 2; i * i <= n; i++) {
			if (prime[i]) {
				for (int j = i * i; j <= n; j += i) {
					prime[j] = false;
				}
			}
		}
		//counting prime numbers
		int primeCount = 0;
		for (int i = 2; i < n; i++) {
			if (prime[i]) {
				primeCount++;
			}
		}
		return primeCount;
	}
};