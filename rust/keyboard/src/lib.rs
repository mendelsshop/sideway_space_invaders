extern crate cpython;
// catch space for shooting implement while loop here instead of in main.py because its not moving the player if the player is not pressing up down or space every frame
use cpython::{Python, py_module_initializer, py_fn , PyResult, PyObject, PyDict, PyString, PyTuple};
use crossterm::{
    event::{self, Event, KeyCode, KeyEvent, KeyModifiers},
    terminal,
    ExecutableCommand, execute, Result,
    cursor::{EnableBlinking}
};
use std::time::{Duration, Instant};

py_module_initializer!(keyboard, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "is_pressed", py_fn!(py, is_pressed(key: &str)))?;
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
    // EnableBlinking;
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
fn is_pressed(py: Python, key: &str) -> PyResult<bool> {
    print!(">");
    match read_key(Duration::from_secs_f32(1.0)) {
        Some(KeyEvent {
            code: KeyCode::Char('q'),
            modifiers: KeyModifiers::NONE,
        }) => {
            if key == "q" {
                return Ok(true);
            } else {
                return Ok(false);
            }
        },
        Some(KeyEvent {
            code: KeyCode::Up,
            modifiers: KeyModifiers::NONE,
        }) => {
            if key == "up" {
                return Ok(true);
            } else {
                return Ok(false);
            }
        },
        Some(KeyEvent {
            code: KeyCode::Down,
            modifiers: KeyModifiers::NONE,
        }) => {
            if key == "down" {
                return Ok(true);
            } else {
                return Ok(false);
            }
        },
        Some(KeyEvent {
            code: KeyCode::Enter,
            modifiers: KeyModifiers::NONE,
        }) => {
            if key == "enter" {
                return Ok(true);
            } else {
                return Ok(false);
            }
        },
        Some(KeyEvent {
            code: KeyCode::Char(' '),
            modifiers: KeyModifiers::NONE,
        }) => {
            if key == "space" {
                return Ok(true);
            } else {
                return Ok(false);
            }
        },
        _ => {
            return Ok(false);
        }
        
    }
    

}