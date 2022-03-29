extern crate cpython;
// catch space for shooting implement while loop here instead of in main.py because its not moving the player if the player is not pressing up down or space every frame
use cpython::{Python, py_module_initializer, py_fn , PyResult};
use crossterm::{
    event::{self, Event, KeyCode, KeyEvent, KeyModifiers},
    terminal,
};
use std::time::{Duration, Instant};

py_module_initializer!(keyboard, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "is_pressed", py_fn!(py, is_pressed()))?;
    println!("keyboard module initialized");
    Ok(())
});


fn read_key(timeout: Duration) -> Option<KeyEvent> {
    struct RawModeGuard;
    impl Drop for RawModeGuard {
        fn drop(&mut self) {
            terminal::disable_raw_mode().unwrap();
        }
    }
    
    terminal::enable_raw_mode().unwrap();
    let _guard = RawModeGuard;
    let start = Instant::now();
    let mut offset = Duration::ZERO;
    while offset <= timeout && event::poll(timeout - offset).unwrap() {
        if let Event::Key(event) = event::read().unwrap() {
            return Some(event);
        }
        offset = start.elapsed();
    }
    return None;
}
fn is_pressed(py: Python) -> PyResult<String> {
    match read_key(Duration::from_secs_f64(0.3333)) {
        Some(KeyEvent {
            code: KeyCode::Char('q'),
            modifiers: KeyModifiers::NONE,
        }) => {
            return Ok("q".to_string());
        },
        Some(KeyEvent {
            code: KeyCode::Up,
            modifiers: KeyModifiers::NONE,
        }) => {
            return Ok("up".to_string());
        },
        Some(KeyEvent {
            code: KeyCode::Down,
            modifiers: KeyModifiers::NONE,
        }) => {
            return Ok("down".to_string());
        },
        Some(KeyEvent {
            code: KeyCode::Enter,
            modifiers: KeyModifiers::NONE,
        }) => {
            return Ok("enter".to_string());
        },
        Some(KeyEvent {
            code: KeyCode::Char(' '),
            modifiers: KeyModifiers::NONE,
        }) => {
            return Ok("space".to_string());
        },
        Some(KeyEvent {
            code: KeyCode::Char('l'),
            modifiers: KeyModifiers::NONE,
        }) => {
            return Ok("l".to_string());
        },
        Some(KeyEvent {
            code: KeyCode::Char('n'),
            modifiers: KeyModifiers::NONE,
        }) => {
            return Ok("n".to_string());
        },
        _ => {
            return Ok("".to_string());
        }
        
    }
    

}