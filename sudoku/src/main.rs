fn main() {
    println!("Hello Stuff and Things");

    let digits = vec!['1', '2', '3', '4', '5', '6', '7', '8', '9'];
    let rows = vec!['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'];
    let cols = digits.clone();

    let squares = cross(&rows, &cols);
    //println!("{:?}", squares);

    let mut unit_list = Vec::new();
    for d in digits.iter() {
        let mut v = Vec::new();
        let s = d.to_string();
        match s.chars().next() {
            Some(i) => v.push(i),
            _ => (),
        }
        unit_list.push(cross(&rows, &v));
    }

    for r in rows.iter() {
        let mut v = Vec::new();
        let s = r.to_string();
        match s.chars().next() {
            Some(i) => v.push(i),
            _ => (),
        }
        unit_list.push(cross(&v, &cols));
    }


    /*
     *  NEED TO CREATE BLOCK
     *
     */


}

fn cross(a: &Vec<char>, b: &Vec<char>) -> Vec<String> {
    let mut v = Vec::new();

    for a in a.iter() {
        for b in b.iter() {
            let prefix = a.to_string();
            let suffix = b.to_string();
            let mut cell = String::new();
            cell.push_str(&prefix);
            cell.push_str(&suffix);
            v.push(cell);
        }
    }
    v
}
