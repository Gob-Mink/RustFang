use std::env;
fn main() {
    let args: Vec<String> = env::args().collect();
    match args.get(1).map(|s| s.as_str()) {
        Some("play") => println!("Sequencer started."),
        Some("stop") => println!("Sequencer stopped."),
        Some("tempo") => println!("Tempo adjusted."),
        Some(other) => eprintln!("Unknown command: {}", other),
        None => {
            eprintln!("Usage: rust_cli_poc <command>");
            eprintln!("Commands: play | stop | tempo");
        }
    }
}