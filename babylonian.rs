fn is_square(n: usize) -> bool {
	if n == 0 {
		return true
	}
	
	let mut x = n / 2;
	let mut y = HashSet::<usize>::new();
	//The type HashMap<K, V> stores a mapping of keys of type K to values of type V. It does this via a hashing function, which determines how it places these keys and values into memory.
	while x*x != n {
		x = (x + (n / x)) / 2;
		if y.contains(&x) {
			return false
		}
		y.insert(x);
	}
	
	return true
}
