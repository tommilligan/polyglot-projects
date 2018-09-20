use std::collections::HashMap;

/// Given a vector of string refs, return a vector of vector pairs of string refs
fn cartesian<'a>(tokens: &Vec<&'a str>) -> Vec<Vec<&'a str>> {
    let mut pairs = Vec::new();
    for (i, prim) in tokens.iter().enumerate() {
        for sec in tokens[i + 1..].iter() {
            // Implicitly copy &str
            pairs.push(vec![*prim, *sec])
        }
    }
    pairs
}

/// Given a vector of string slices, generates a sorted key for id
fn key_from(mut tokens: Vec<&str>) -> String {
    tokens.sort();
    tokens.join("/")
}

/// Process lines of data and hold token cooccurrence counts
pub struct Cooccurrence {
    lookup: HashMap<String, u64>,
}

impl Cooccurrence {
    /// Read in a set of lines and get cooccurrence data
    pub fn from(lines: Vec<String>) -> Cooccurrence {
        let mut lookup = HashMap::new();
        for line in lines.iter() {
            let tokens: Vec<&str> = line.split(" ").collect();
            for pair in cartesian(&tokens) {
                let k = key_from(pair);
                let count = lookup.entry(k).or_insert(0);
                *count += 1;
            }
        }
        Cooccurrence { lookup: lookup }
    }

    /// Get cooccurrence counts for two tokens
    pub fn get(&self, a: &str, b: &str) -> u64 {
        *self.lookup.get(&key_from(vec![a, b])).unwrap_or(&0)
    }
}

#[cfg(test)]
mod tests {
    use super::{cartesian, key_from, Cooccurrence};

    #[test]
    fn test_key_from_sorting() {
        assert_eq!(key_from(vec!["foo", "bar"]), key_from(vec!["bar", "foo"]))
    }

    #[test]
    fn test_cartesian_pairs() {
        assert_eq!(
            cartesian(&vec!["foo", "bar", "spam"]),
            vec![vec!["foo", "bar"], vec!["foo", "spam"], vec!["bar", "spam"]]
        );
    }

    #[test]
    fn simple_case() {
        let cooc = Cooccurrence::from(vec![
            "Alice Bob".to_string(),
            "Charlie Alice Eve".to_string(),
        ]);
        assert_eq!(cooc.get("Alice", "Bob"), 1);
        assert_eq!(cooc.get("Eve", "Bob"), 0);
    }
}
