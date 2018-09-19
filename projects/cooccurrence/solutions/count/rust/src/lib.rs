use std::collections::HashMap;

fn cartesian<'a>(tokens: &Vec<&'a str>) -> Vec<Vec<&'a str>> {
    let mut pairs = Vec::new();
    for (i, prim) in tokens.iter().enumerate() {
        for sec in tokens[i + 1..].iter() {
            pairs.push(vec![*prim, *sec])
        }
    }
    pairs
}

fn key_from(mut tokens: Vec<&str>) -> String {
    tokens.sort();
    tokens.join("/")
}

pub struct Cooccurrence {
    lookup: HashMap<String, u64>,
}

impl Cooccurrence {
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

    pub fn get(&self, a: &str, b: &str) -> u64 {
        *self.lookup.get(&key_from(vec![a, b])).unwrap_or(&0)
    }
}

#[cfg(test)]
mod tests {
    use super::Cooccurrence;
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
