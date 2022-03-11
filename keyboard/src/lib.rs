extern crate cpython;

use cpython::{Python, py_module_initializer, py_fn , PyResult, PyObject, PyDict, PyString, PyTuple};
use rustyline::error::ReadlineError;
use rustyline::Editor;

py_module_initializer!(keyboard, |py, m| {
    m.add(py, "__doc__", "This module is implemented in Rust.")?;
    m.add(py, "run", py_fn!(py, is_pressed(key: &str)))?;
    Ok(())
});

fn is_pressed(py: Python, key: &str) -> PyResult<bool> {
    let mut rl = Editor::<()>::new();
    let mut keys = vec![];
    loop {
        let readline = rl.readline("");
        match readline {
            Ok(line) => {
                rl.add_history_entry(&line);
                keys.push(line);
            },
            Err(ReadlineError::Interrupted) => {
                println!("CTRL-C");
                break Ok(false);
            },
            Err(ReadlineError::Eof) => {
                println!("CTRL-D");
                break Ok(false);
            },
            Err(err) => {
                println!("Error: {:?}", err);
                break Ok(false);
            }
        }
        // check if &key is = to the last key in keys return py<bool>
        if keys.last().unwrap() == key {
            return Ok(true);
        }
        else {
            return Ok(false);
        }


    }
}