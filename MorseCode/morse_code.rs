use std::collections::HashMap;
use std::io;


//sets up the hash table
fn setup_morse(morse:&mut HashMap<String, String>){
    morse.insert(String::from(".-"), String::from("a"));
    morse.insert(String::from("-..."), String::from("b"));
    morse.insert(String::from("-.-."), String::from("c"));
    morse.insert(String::from("-.."), String::from("d"));
    morse.insert(String::from("."), String::from("e"));
    morse.insert(String::from("..-."), String::from("f"));
    morse.insert(String::from("--."), String::from("g"));
    morse.insert(String::from("...."), String::from("h"));
    morse.insert(String::from(".."), String::from("i"));
    morse.insert(String::from(".---"), String::from("j"));
    morse.insert(String::from("-.-"), String::from("k"));
    morse.insert(String::from(".-.."), String::from("l"));
    morse.insert(String::from("--"), String::from("m"));
    morse.insert(String::from("-."), String::from("n"));
    morse.insert(String::from("---"), String::from("o"));
    morse.insert(String::from(".--."), String::from("p"));
    morse.insert(String::from("--.-"), String::from("q"));
    morse.insert(String::from(".-."), String::from("r"));
    morse.insert(String::from("..."), String::from("s"));
    morse.insert(String::from("-"), String::from("t"));
    morse.insert(String::from("..-"), String::from("u"));
    morse.insert(String::from("...-"), String::from("v"));
    morse.insert(String::from(".--"), String::from("w"));
    morse.insert(String::from("-..-"), String::from("x"));
    morse.insert(String::from("-.--"), String::from("y"));
    morse.insert(String::from("--.."), String::from("z"));
    morse.insert(String::from(".-.-.-"), String::from("."));
    morse.insert(String::from("..--.."), String::from("?"));
    morse.insert(String::from("..-.."), String::from(","));
}


//converts letters to morse code
fn eng_to_morse(line:String, morse:HashMap<String, String>){
    let mut result = String::new();
    
    for i in line.chars(){
        for (key, val) in morse.iter(){
            if i == val.chars().next().unwrap(){
                for j in key.chars(){
                    result.push(j);
                }
                result.push(' ');
            }
        }
    }
    println!("{}", result);
}


//converts morse code to letters
fn morse_to_eng(line:String, morse:HashMap<String, String>){
    let mut result = String::new();
    let mut temp = String::new();
    for i in line.chars(){
        if i != ' '{
            temp.push(i);
        }
        else{
            
            result.push(morse[&temp].chars().next().unwrap());
            temp = String::new();
            
        }
    }
    println!("{}", result);
}



fn main() {
    let mut morse = HashMap::new();
    setup_morse(&mut morse);

    //determine which way to translate
    let mut eng_morse = String::new();
    println!("Are you translating from english to morse code (1) or morse code to english(2)?");
    io::stdin().read_line(&mut eng_morse).expect("Error reading input");
    
    //get user input of what to translate
    let mut line = String::new();
    println!("please enter what you want translated: ");
    io::stdin().read_line(&mut line).expect("Error reading input");
    
    if eng_morse.trim() == "1"{
        eng_to_morse(line, morse);
    }
    else if eng_morse.trim() == "2"{
        morse_to_eng(line, morse);        
    }
    else{
        println!("Bad Input!");
    }

}
